"""The Night Console for manim: the folio's inks, type and math, so a video looks like its PDF.

In a scene file:   from klmanim import *      then subclass KLScene.
Render with:       python engine/kl.py anim <file.py> [--draft]
"""
from pathlib import Path

import manimpango
import numpy as np
from manim import *

ENGINE = Path(__file__).resolve().parent
FONTS = (ENGINE / 'fonts').as_posix()

PAGE, INK, HI, DIM, LOW, FAINT, SEAL = '#121212', '#C5BCAB', '#E6E0D4', '#8A8376', '#4C4741', '#1B1A18', '#8E2B22'
BODY, FELL, PIX, GOTH = 'EB Garamond', 'IM FELL English', 'Silkscreen', 'UnifrakturMaguntia'

for f in ['EBGaramond-Medium.otf', 'EBGaramond-MediumItalic.otf', 'IMFellEnglish.ttf', 'IMFellEnglish-Italic.ttf',
          'Silkscreen.ttf', 'UnifrakturMaguntia-Book.ttf']:
    manimpango.register_font(f'{FONTS}/{f}')

# MathTex and Tex set in Garamond, through XeLaTeX like the folios
config.tex_template = TexTemplate(tex_compiler='xelatex', output_format='.xdv', preamble=rf"""
\usepackage{{amsmath}}
\usepackage{{fontspec}}
\usepackage{{unicode-math}}
\setmainfont{{EBGaramond}}[Path={FONTS}/,Extension=.otf,UprightFont=*-Medium,ItalicFont=*-MediumItalic]
\setmathfont{{Garamond-Math.otf}}[Path={FONTS}/,StylisticSet={{7,9}}]
""")
config.background_color = PAGE
Text.set_default(font=BODY, weight=MEDIUM, color=INK)
for cls in (MathTex, Tex, Line, DashedLine, Arrow, Circle, Rectangle, Polygon, ParametricFunction):
    cls.set_default(color=INK)
Dot.set_default(color=HI)


def label(s, size=16):
    """Pixel label, like the title strips."""
    return Text(s.upper(), font=PIX, font_size=size, color=DIM)


def caption(s, size=26):
    """Fell italic, for what to notice."""
    return Text(s, font=FELL, slant=ITALIC, font_size=size, color=DIM)


def leds(mob, buff=0.25, color=DIM):
    """The dotted LED frame around a mobject."""
    r = SurroundingRectangle(mob, buff=buff, color=color, stroke_width=4, corner_radius=0)
    return DashedVMobject(r, num_dashes=int(r.get_arc_length() / 0.12), dashed_ratio=0.25)


def kl_axes(x_range, y_range, x_length=10, y_length=5, **kw):
    """Axes in the console's inks: dim lines, no tips."""
    return Axes(x_range=x_range, y_range=y_range, x_length=x_length, y_length=y_length, tips=False,
                axis_config={'color': DIM, 'stroke_width': 2, 'tick_size': 0.06, 'font_size': 22}, **kw)


def kl_axes3d(x_range, y_range, z_range, x_length=7, y_length=7, z_length=3.5, **kw):
    """3D axes in the console's inks, without ticks."""
    return ThreeDAxes(x_range=x_range, y_range=y_range, z_range=z_range, x_length=x_length, y_length=y_length,
                      z_length=z_length, tips=False, axis_config={'color': DIM, 'stroke_width': 2, 'include_ticks': False},
                      **kw)


def kl_surface(ax, f, x_range, y_range, res=28, opacity=0.8):
    """The graph of a height f(x, y) over 3D axes, shaded from LOW (low) to HI (high)."""
    xs, ys = np.meshgrid(np.linspace(*x_range, 40), np.linspace(*y_range, 40))
    z = np.vectorize(f)(xs, ys)
    s = Surface(lambda u, v: ax.c2p(u, v, f(u, v)), u_range=x_range, v_range=y_range, resolution=(res, res),
                fill_opacity=opacity, stroke_color=LOW, stroke_width=0.4, checkerboard_colors=False)
    return s.set_fill_by_value(axes=ax, colorscale=[(LOW, z.min()), (HI, z.max())], axis=2)


class _Cards:
    """Title, question and idea cards and the caption line, shared by 2D and 3D scenes."""
    line = None

    def pin(self, *mobs):
        """Keep overlays flat on the screen. Only 3D scenes need it."""

    def title_card(self, title, sub=None, pose='reading'):
        """Opening: Fraktur title, one line of Fell, Kael'thos in the corner. About 3 s."""
        t = Text(title, font=GOTH, font_size=72, color=HI)
        g = VGroup(t, caption(sub, 30).next_to(t, DOWN, buff=0.35)) if sub else VGroup(t)
        cat = ImageMobject(str(ENGINE / 'art' / f'{pose}.png')).set_height(2.2).to_corner(DR, buff=0.5)
        self.pin(g, cat)
        self.play(FadeIn(g, shift=0.2 * UP), FadeIn(cat), run_time=1.2)
        self.wait(1.6)
        self.play(FadeOut(g), FadeOut(cat), run_time=0.8)

    def card(self, head, tex, hold):
        body = Tex(tex, font_size=38, color=HI)
        if body.width > 11.5:
            body.scale_to_fit_width(11.5)
        g = VGroup(label(head).next_to(body, UP, buff=0.45).align_to(body, LEFT), body).move_to(ORIGIN)
        frame = leds(g, buff=0.45)
        self.pin(g, frame)
        self.play(FadeIn(g), Create(frame), run_time=1.2)
        self.wait(hold)
        return VGroup(g, frame)

    def question_card(self, tex, hold=5):
        """Right after the title: the question the video answers, in full, so it stands alone."""
        self.play(FadeOut(self.card('The question', tex, hold)), run_time=0.8)

    def idea_card(self, tex, hold=5):
        """Closing: the answer in one or two sentences. Hold it long enough to read twice."""
        self.card('The idea', tex, hold)

    def say(self, tex):
        """The caption line at the top. Clears the old line, returns the animation that writes the new one."""
        new = Tex(tex, font_size=32)
        if new.width > 13:
            new.scale_to_fit_width(13)
        new.to_edge(UP, buff=0.45)
        if self.line is not None:  # out first, then in: overlapping lines read as ghosts
            self.play(FadeOut(self.line), run_time=0.4)
        self.pin(new)  # not a Transform: in 3D, Transform leaves new letters unpinned
        self.line = new
        return FadeIn(new)


class KLScene(_Cards, Scene):
    pass


class KLScene3D(_Cards, ThreeDScene):
    def pin(self, *mobs):
        self.add_fixed_in_frame_mobjects(*mobs)

    def orbit(self, degrees, run_time=6, *anims):
        """Swing the camera around the vertical axis, easing in and out. Use this, never ambient
        rotation: that starts and stops with a jerk."""
        self.move_camera(theta=self.camera.get_theta() + degrees * DEGREES, run_time=run_time,
                         rate_func=smooth, added_anims=list(anims))


