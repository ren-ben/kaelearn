"""The Night Console for manim: the folio's inks, type and math, so a video looks like its PDF.

In a scene file:   from klmanim import *      then subclass KLScene.
Render with:       python engine/kl.py anim <file.py> [--draft]
"""
from pathlib import Path

import manimpango
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


class KLScene(Scene):
    def title_card(self, title, sub=None, pose='reading'):
        """Opening: Fraktur title, one line of Fell, Kael'thos in the corner. About 3 s."""
        t = Text(title, font=GOTH, font_size=72, color=HI)
        g = VGroup(t, caption(sub, 30).next_to(t, DOWN, buff=0.35)) if sub else VGroup(t)
        cat = ImageMobject(str(ENGINE / 'art' / f'{pose}.png')).set_height(2.2).to_corner(DR, buff=0.5)
        self.play(FadeIn(g, shift=0.2 * UP), FadeIn(cat), run_time=1.2)
        self.wait(1.6)
        self.play(FadeOut(g), FadeOut(cat), run_time=0.8)

    def idea_card(self, text, hold=4):
        """Closing: the one idea, framed. Hold it long enough to read twice."""
        body = Text(text, font_size=34, color=HI, line_spacing=1.2)
        if body.width > 11:
            body.scale_to_fit_width(11)
        top = label('The idea').next_to(body, UP, buff=0.45).align_to(body, LEFT)
        g = VGroup(top, body).move_to(ORIGIN)
        self.play(FadeIn(g), Create(leds(g, buff=0.45)), run_time=1.2)
        self.wait(hold)
