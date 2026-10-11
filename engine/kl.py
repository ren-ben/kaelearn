"""Kaelearn engine. One entry point, run from the repo root:

  python engine/kl.py build <file.tex>        compile to <file>.pdf beside the source
  python engine/kl.py look <file.pdf> [-p 1-3] [--dpi 80]
                                              render pages to PNG (and a contact sheet) to check them
  python engine/kl.py plate <scene> <out.png> [--seed N]
                                              a dithered plate; scenes: nave horizon orrery field lattice
  python engine/kl.py anim <scene.py> [--draft] [--poster 0.66]
                                              render a manim scene (engine/klmanim.py) to <scene>.mp4 + poster,
                                              and a contact sheet of frames to check it
  python engine/kl.py publish <file>          copy a PDF or MP4 into the vault, then mirror the md files
  python engine/kl.py mirror                  copy ATLAS.md and GRIMOIRE.md into the vault
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / 'engine'
CACHE = ROOT / '.kl-cache'
VAULT = Path(json.loads((ROOT / 'kaelearn.json').read_text(encoding='utf8'))['vault'])
MIRRORS = {'ATLAS.md': 'Atlas.md', 'GRIMOIRE.md': 'Grimoire.md'}


def clean_env():
    # Claude Code puts its own .exe on PATH; MiKTeX dies on PATH entries that are files.
    env = dict(os.environ)
    env['PATH'] = os.pathsep.join(p for p in env.get('PATH', '').split(os.pathsep) if p and os.path.isdir(p))
    env['TEXINPUTS'] = str(ENGINE) + os.pathsep
    return env


def build(tex: Path):
    tex = tex.resolve()
    out = CACHE / 'build' / tex.stem
    out.mkdir(parents=True, exist_ok=True)
    env = clean_env()
    miktex = 'MiKTeX' in subprocess.run(['xelatex', '--version'], capture_output=True, text=True, env=env).stdout
    cmd = ['xelatex', '-interaction=nonstopmode', '-halt-on-error', f'-output-directory={out}', f'-jobname={tex.stem}']
    if miktex:
        cmd.append(f'-include-directory={ENGINE}')
    cmd.append(r'\def\KLROOT{%s/}\def\KLVAULT{%s}\input{%s}' % (ENGINE.as_posix(), obsidian_url(vault_path(tex).parent), tex.name))
    for _ in range(2):  # twice: the page meter and the cover need the page count
        r = subprocess.run(cmd, cwd=tex.parent, capture_output=True, text=True, env=env, encoding='utf8', errors='replace')
        if r.returncode:
            log = (out / f'{tex.stem}.log').read_text(encoding='utf8', errors='replace').splitlines()
            errs = [ln for i, ln in enumerate(log) if ln.startswith('!') or re.match(r'l\.\d+', ln)]
            sys.exit('build failed:\n' + '\n'.join(errs[:20]))
    log = (out / f'{tex.stem}.log').read_text(encoding='utf8', errors='replace')
    for m in sorted(set(re.findall(r'Missing character: There is no (.+?) in font (\S+)', log)))[:10]:
        print(f'warning: no glyph {m[0]} in {m[1]}')
    for pt, lines in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\) in (?:paragraph|alignment) at lines (\d+--\d+)', log):
        if float(pt) > 4:
            print(f'warning: {pt}pt too wide at lines {lines}')
    pdf = tex.with_suffix('.pdf')
    shutil.copyfile(out / f'{tex.stem}.pdf', pdf)
    print(pdf.relative_to(ROOT).as_posix())


def look(pdf: Path, pages: str | None, dpi: int):
    d = CACHE / 'look' / pdf.stem
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    cmd = ['pdftoppm', '-r', str(dpi), '-png']
    if pages:
        a, _, b = pages.partition('-')
        cmd += ['-f', a, '-l', b or a]
    subprocess.run(cmd + [str(pdf), str(d / 'p')], check=True, env=clean_env(), capture_output=True)
    ims = sorted(d.glob('p-*.png'))
    for p in ims:
        print(p.relative_to(ROOT).as_posix())
    if len(ims) > 1:
        tiles = [Image.open(p) for p in ims]
        g, cols = 12, min(6, len(tiles))
        tw, th = max(t.width for t in tiles), max(t.height for t in tiles)
        rows = -(-len(tiles) // cols)
        sheet = Image.new('RGB', (cols * (tw + g) + g, rows * (th + g) + g), (64, 62, 58))
        for i, t in enumerate(tiles):
            sheet.paste(t, (g + (i % cols) * (tw + g), g + (i // cols) * (th + g)))
        sheet.save(d / 'sheet.png')
        print((d / 'sheet.png').relative_to(ROOT).as_posix())


def vault_path(f: Path) -> Path:
    parts = f.resolve().relative_to(ROOT).parts
    if parts[0] == 'subjects':      # subjects/<s>/<kind>/.../x -> Folios|Debriefs|Exams|Anims/<s>/x
        return VAULT / parts[2].capitalize() / parts[1] / f.name
    if parts[0] == 'review':
        return VAULT / 'Reviews' / f.name
    return VAULT / f.name           # codex and anything else at the top


def obsidian_url(folder: Path) -> str:
    # obsidian://open?vault=...&file=... for a folder in the vault, escaped for TeX
    root = next((p for p in [VAULT, *VAULT.parents] if (p / '.obsidian').is_dir()), VAULT.parent)
    url = f'obsidian://open?vault={quote(root.name)}&file={quote(folder.relative_to(root).as_posix() + "/", safe="")}'
    return url.replace('%', r'\%')


def publish(f: Path):
    """Copy a PDF or MP4 into the vault (it lands where vault_path says), then mirror the md files."""
    dest = vault_path(f)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(f, dest)
    print(dest)
    mirror()


def anim(py: Path, draft: bool, poster: float):
    """Render a manim scene file; final renders land beside it as <stem>.mp4 and a <stem>.png poster."""
    py = py.resolve()
    out = CACHE / 'anim' / py.stem
    env = clean_env()
    env['PYTHONPATH'] = str(ENGINE)
    t0 = time.time()
    q = ['-ql'] if draft else ['-qh', '--fps', '30']
    r = subprocess.run([sys.executable, '-m', 'manim', 'render', *q, '-a', '--media_dir', str(out), str(py)],
                       cwd=py.parent, env=env, capture_output=True, text=True, encoding='utf8', errors='replace')
    if r.returncode:
        sys.exit('render failed:\n' + (r.stderr or r.stdout)[-4000:])
    vids = [v for v in (out / 'videos').rglob('*.mp4') if 'partial_movie_files' not in v.parts and v.stat().st_mtime >= t0]
    for v in vids:
        stem = py.stem if len(vids) == 1 else f'{py.stem}-{v.stem}'
        frames = contact_sheet(v, out / f'{stem}-sheet.png', poster)
        if not draft:
            shutil.copyfile(v, py.with_name(stem + '.mp4'))
            frames[1].save(py.with_name(stem + '.png'))
            v = py.with_name(stem + '.mp4')
        print(f'{v.relative_to(ROOT).as_posix()}  {frames[0]:.0f} s  {v.stat().st_size / 1e6:.1f} MB')
        print((out / f'{stem}-sheet.png').relative_to(ROOT).as_posix())


def contact_sheet(mp4: Path, out: Path, poster: float, n: int = 12):
    # n evenly spaced frames in a 4-column grid, to check a render without watching it
    import av
    with av.open(str(mp4)) as c:
        s = c.streams.video[0]
        total = s.frames
        want = {round(i * (total - 1) / (n - 1)) for i in range(n)}
        pick = round(poster * (total - 1))
        tiles, still = [], None
        for i, fr in enumerate(c.decode(s)):
            if i in want:
                tiles.append(fr.to_image().resize((480, 270)))
            if i == pick:
                still = fr.to_image()
        dur = float(s.duration * s.time_base) if s.duration else total / float(s.average_rate)
    g, cols = 8, 4
    rows = -(-len(tiles) // cols)
    sheet = Image.new('RGB', (cols * (480 + g) + g, rows * (270 + g) + g), (64, 62, 58))
    for i, t in enumerate(tiles):
        sheet.paste(t, (g + (i % cols) * (480 + g), g + (i // cols) * (270 + g)))
    sheet.save(out)
    return dur, still


def mirror():
    for src, name in MIRRORS.items():
        if (ROOT / src).exists():
            shutil.copyfile(ROOT / src, VAULT / name)
            print(VAULT / name)


# ---- plates: a scene in grey, thresholded to the two inks -------------------
INK, PHOS = (0x12, 0x12, 0x12), (0xC5, 0xBC, 0xAB)
BAYER = (1 / 64) * np.array([[0, 32, 8, 40, 2, 34, 10, 42], [48, 16, 56, 24, 50, 18, 58, 26],
                              [12, 44, 4, 36, 14, 46, 6, 38], [60, 28, 52, 20, 62, 30, 54, 22],
                              [3, 35, 11, 43, 1, 33, 9, 41], [51, 19, 59, 27, 49, 17, 57, 25],
                              [15, 47, 7, 39, 13, 45, 5, 37], [63, 31, 55, 23, 61, 29, 53, 21]]) + 1 / 128


def grid(w, h):
    ys, xs = np.mgrid[0:h, 0:w].astype(float)
    return (xs - w / 2) / h, (ys - h / 2) / h      # y grows downward, unit = plate height


def stars(rng, shape, density=0.004):
    return (rng.random(shape) > 1 - density) * 0.95


def lancet(x, y, s):
    a, yb, ysp = 0.46 * s, 0.70 * s, -0.12 * s
    rect = (np.abs(x) <= a) & (y >= ysp) & (y <= yb)
    arc = (y < ysp) & (np.hypot(x - a, y - ysp) <= 2 * a) & (np.hypot(x + a, y - ysp) <= 2 * a)
    return rect | arc


def nave(w, h, rng):
    """Arches receding at a geometric rate toward a black hole: a limit."""
    x, y = grid(w, h)
    r = np.hypot(x, y)
    grain = rng.random((h, w))
    v = 0.012 * grain + stars(rng, (h, w))
    q, K = 0.80, 13
    for k in range(K):
        s, t = 1.05 * q ** k, k / K
        face = lancet(x, y, s) & ~lancet(x, y, s * 0.93)
        v = np.where(face, 0.10 + 0.30 * t ** 1.3 + 0.08 * grain, v)
        reveal = lancet(x, y, s * 0.93) & ~lancet(x, y, s * 0.86)
        v = np.where(reveal, np.clip(0.35 + 0.55 * t + 0.25 * np.clip(-x / s, -1, 1), 0, 1), v)
        floor = lancet(x, y, s * 0.86) & (y > 0.70 * s * q)
        v = np.where(floor, 0.18 + 0.4 * t + 0.1 * ((np.floor(x / (0.05 * s)) + np.floor(y / (0.03 * s))) % 2), v)
        if k < K - 1:
            v = np.where(lancet(x, y, s * 0.86) & ~lancet(x, y, s * q) & ~floor, 0.12 + 0.35 * t + 0.06 * grain, v)
    beyond = lancet(x, y, 1.05 * q ** (K - 1) * 0.86)
    v = np.where(beyond, 0.25 + 0.75 * np.exp(-(r / 0.07) ** 2), v)
    v = np.maximum(v, np.exp(-(((r - 0.032) / 0.005) ** 2)) * (r < 0.06))
    return np.where(r < 0.027, 0.02, v)


def horizon(w, h, rng):
    """His address: a black hole, its tilted disk brighter on the side that comes at you."""
    x, y = grid(w, h)
    r = np.hypot(x, y)
    v = stars(rng, (h, w), 0.005) * (r > 0.2)
    rho = np.hypot(x, y / 0.24)
    disk = (rho > 0.13) & (rho < 0.62)
    lum = np.clip((0.62 - rho) / 0.49, 0, 1) ** 0.8 * (1 + 0.55 * (-x / (rho + 1e-9)))
    lum *= 0.75 + 0.25 * np.sin(rho * 90 + rng.random() * 6)        # rings in the disk
    back = disk & (y < 0)
    v = np.where(back, np.clip(0.6 * lum, 0, 1), v)
    arc = np.hypot(x, (y + 0.015) / 0.95)                             # the far side, lensed over the top
    v = np.maximum(v, np.clip(0.9 - np.abs(arc - 0.135) / 0.02, 0, 1) * (y < 0.02) * 0.9)
    v = np.where(r < 0.105, 0.0, v)                                   # the shadow
    v = np.maximum(v, np.exp(-(((r - 0.112) / 0.006) ** 2)))          # photon ring
    front = disk & (y >= 0)
    v = np.where(front, np.clip(0.75 * lum + 0.1, 0, 1), v)
    return np.clip(v + 0.25 * np.exp(-(r / 0.5) ** 2) * (v < 0.05) * rng.random((h, w)) ** 3, 0, 1)


def orrery(w, h, rng):
    """Orbits around a hot centre: mechanics, conic sections, the solar system."""
    x, y = grid(w, h)
    x = x + 0.35
    v = stars(rng, (h, w), 0.003) + 0.9 * np.exp(-(np.hypot(x, y) / 0.06) ** 2)
    for i, (a, e) in enumerate([(0.18, 0.05), (0.32, 0.12), (0.5, 0.2), (0.74, 0.32), (1.05, 0.45)]):
        c = a * e
        rr = np.hypot((x + c) / a, y / (a * np.sqrt(1 - e * e) * 0.55))
        v = np.maximum(v, np.clip(1 - np.abs(rr - 1) * a / 0.0035, 0, 1) * (0.35 + 0.1 * i))
        th = rng.random() * 2 * np.pi
        px, py = a * np.cos(th) - c, a * np.sqrt(1 - e * e) * 0.55 * np.sin(th)
        d = np.hypot(x - px, y - py)
        body = d < 0.012 + 0.006 * i
        lit = np.clip(0.5 - ((x - px) * px + (y - py) * py) / (d + 1e-9) / (np.hypot(px, py) + 1e-9) * 0.5, 0, 1)
        v = np.where(body, 0.15 + 0.85 * lit, v)
    return np.clip(v, 0, 1)


def field(w, h, rng):
    """Streamlines of a spiral sink: flows, differential equations, fields."""
    x, y = grid(w, h)
    r = np.hypot(x, y) + 1e-6
    th = np.arctan2(y, x)
    psi = th - 2.2 * np.log(r) + 0.6 * np.sin(3 * th) * r
    lines = np.clip(1 - np.abs(np.sin(psi * 4)) / 0.18, 0, 1)
    v = lines * (0.25 + 0.75 * np.exp(-(r / 0.55) ** 2)) + 0.08 * rng.random((h, w))
    v = np.maximum(v, np.exp(-(r / 0.035) ** 2))
    return np.clip(v, 0, 1)


def lattice(w, h, rng):
    """A floor grid under a linear map, the images of the basis vectors standing out: linear algebra."""
    x, y = grid(w, h)
    y0 = -0.12
    below = y > y0 + 0.004
    Z = 0.4 / np.where(below, y - y0, 1)
    X = x * Z
    u, wv = 4 * (X + 0.45 * (Z - 1.6)), 4 * (-0.3 * X + 0.95 * (Z - 1.6))   # sheared and rotated
    fade = np.clip(2.2 / Z, 0, 1) ** 1.5
    line = lambda t: np.clip(1 - np.abs(t - np.round(t)) / 0.05, 0, 1)
    v = np.where(below, np.maximum(line(u), line(wv)) * (0.15 + 0.7 * fade) + 0.05 * fade * rng.random((h, w)),
                 stars(rng, (h, w), 0.004))
    e1 = below & (np.abs(wv) < 0.09) & (u > 0) & (u < 1)
    e2 = below & (np.abs(u) < 0.09) & (wv > 0) & (wv < 1)
    v = np.where(e1 | e2, 1.0, v)
    v = np.maximum(v, 0.9 * np.exp(-(np.hypot(u, wv) / 0.15) ** 2) * below)  # the origin
    v = np.maximum(v, 0.45 * np.exp(-((y - y0) / 0.01) ** 2))               # the horizon line
    return np.clip(v, 0, 1)


SCENES = {f.__name__: f for f in (nave, horizon, orrery, field, lattice)}


def plate(scene: str, out: Path, seed: int, cells: int = 400, cell: int = 4):
    rng = np.random.default_rng(seed)
    v = SCENES[scene](cells, int(cells * 0.62), rng)
    t = np.tile(BAYER, (v.shape[0] // 8 + 1, v.shape[1] // 8 + 1))[:v.shape[0], :v.shape[1]]
    pal = np.array([INK, PHOS], np.uint8)
    img = Image.fromarray(pal[(v > t).astype(int)])
    img.resize((v.shape[1] * cell, v.shape[0] * cell), Image.NEAREST).save(out, optimize=True)
    print(out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('build').add_argument('tex', type=Path)
    lk = sub.add_parser('look')
    lk.add_argument('pdf', type=Path)
    lk.add_argument('-p', '--pages')
    lk.add_argument('--dpi', type=int, default=80)
    pl = sub.add_parser('plate')
    pl.add_argument('scene', choices=SCENES)
    pl.add_argument('out', type=Path)
    pl.add_argument('--seed', type=int, default=7)
    an = sub.add_parser('anim')
    an.add_argument('py', type=Path)
    an.add_argument('--draft', action='store_true')
    an.add_argument('--poster', type=float, default=0.66)
    sub.add_parser('publish').add_argument('file', type=Path)
    sub.add_parser('mirror')
    a = ap.parse_args()
    if a.cmd == 'build':
        build(a.tex)
    elif a.cmd == 'look':
        look(a.pdf, a.pages, a.dpi)
    elif a.cmd == 'plate':
        plate(a.scene, a.out, a.seed)
    elif a.cmd == 'anim':
        anim(a.py, a.draft, a.poster)
    elif a.cmd == 'publish':
        publish(a.file)
    else:
        mirror()
