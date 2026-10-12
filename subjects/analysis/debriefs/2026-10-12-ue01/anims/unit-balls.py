# ANA UE01, Problem 03: the unit balls of the p-norms grow with p, from diamond to disc to square.
from klmanim import *

R = 1.35  # half-width of the plotted window


def p_of(s):
    # s in [0, 1) runs p from 1 (s = 0) through 2 (s = 1/2) towards infinity
    return 1 / (1 - s)


def ball_points(ax, p, n=480):
    # |x|^p + |y|^p = 1, parametrised so that |x|^p = cos^2 t and |y|^p = sin^2 t
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    c, s = np.cos(t), np.sin(t)
    x = np.sign(c) * np.abs(c) ** (2 / p)
    y = np.sign(s) * np.abs(s) ** (2 / p)
    return [ax.c2p(a, b) for a, b in zip(x, y)]


class UnitBalls(KLScene):
    def construct(self):
        self.title_card('Diamond, Disc, Square', 'the unit balls of the p-norms')
        self.question_card(r'$A_p=\{(x,y): |x|^p+|y|^p\le 1\}$, and $A_\infty=\{(x,y): \max(|x|,|y|)\le 1\}$.\\'
                           r'Why is $A_1\subset A_2\subset A_\infty$?', hold=6)

        ax = kl_axes([-R, R, 1], [-R, R, 1], x_length=5.6, y_length=5.6).shift(0.45 * DOWN)
        self.play(Create(ax), self.say(r'$p=1$: the set $|x|+|y|\le 1$ is a diamond.'), run_time=1.5)

        s = ValueTracker(0.0)

        def ball():
            return Polygon(*ball_points(ax, p_of(s.get_value())), color=HI, stroke_width=3,
                           fill_color=INK, fill_opacity=0.12)

        def p_label():
            p = p_of(s.get_value())
            return MathTex(rf'p = {p:.2f}' if p < 10 else rf'p = {p:.1f}', color=DIM, font_size=34) \
                .next_to(ax, RIGHT, buff=0.6).shift(1.6 * UP)

        live, plab = always_redraw(ball), always_redraw(p_label)
        self.play(FadeIn(live), FadeIn(plab), run_time=1.5)
        self.wait(2)

        def ghost(p, name, corner, side):
            g = DashedVMobject(Polygon(*ball_points(ax, p, 240), color=DIM, stroke_width=2), num_dashes=90)
            lab = MathTex(name, color=DIM, font_size=34).next_to(ax.c2p(*corner), side, buff=0.1)
            return g, lab

        g1, l1 = ghost(1, 'A_1', (-0.5, 0.5), UL)
        self.play(FadeIn(g1), FadeIn(l1), run_time=1)
        self.play(s.animate.set_value(0.5), run_time=4.5, rate_func=smooth,
                  added_anims=[self.say(r'Raise $p$. For $0\le t\le 1$, $t^p$ shrinks as $p$ grows: '
                                        r'the condition gets easier, the set grows.')])
        self.wait(1.5)

        g2, l2 = ghost(2, 'A_2', (-0.71, -0.71), DL)
        self.play(FadeIn(g2), FadeIn(l2), self.say(r'$p=2$: $x^2+y^2\le 1$, the disc. The diamond is still inside.'),
                  run_time=1.2)
        self.wait(2.5)

        self.play(s.animate.set_value(0.975), run_time=5, rate_func=smooth,
                  added_anims=[self.say(r'$p\to\infty$: the largest of $|x|,|y|$ takes over. '
                                        r'The ball fills out towards the square.')])
        self.wait(1)

        square = Polygon(ax.c2p(1, 1), ax.c2p(-1, 1), ax.c2p(-1, -1), ax.c2p(1, -1), color=HI, stroke_width=3,
                         fill_color=INK, fill_opacity=0.12)
        inf_lab = MathTex(r'p = \infty', color=DIM, font_size=34).move_to(plab)
        live.clear_updaters()
        plab.clear_updaters()
        # morph, never crossfade: two large translucent fills fading against each other flicker
        self.play(Transform(live, square), FadeOut(plab), FadeIn(inf_lab), run_time=1.5)
        l3 = MathTex(r'A_\infty', color=DIM, font_size=34).next_to(ax.c2p(1, -1), DR, buff=0.1)
        self.play(FadeIn(l3), self.say(r'$p=\infty$: $\max(|x|,|y|)\le 1$, the square: $|x|\le1$ and $|y|\le1$, '
                                       r'one condition per coordinate.'), run_time=1)
        self.wait(2.5)

        w = 1 / np.sqrt(2)
        d1 = Dot(ax.c2p(w, w), radius=0.07).set_z_index(2)
        d2 = Dot(ax.c2p(1, 1), radius=0.07).set_z_index(2)
        t1 = MathTex(r'(\tfrac{1}{\sqrt2},\tfrac{1}{\sqrt2})', font_size=28, color=HI) \
            .next_to(ax.c2p(0.45, 1), UP, buff=0.15)
        lead = DashedLine(d1.get_center(), t1.get_bottom(), color=DIM, dash_length=0.05, stroke_width=1.5)
        t2 = MathTex(r'(1,1)', font_size=28, color=HI).next_to(d2, UR, buff=0.1)
        self.play(FadeIn(d1, scale=0.5), FadeIn(t1), FadeIn(lead),
                  self.say(r'Strict: $(\tfrac{1}{\sqrt2},\tfrac{1}{\sqrt2})$ is in the disc, not the diamond '
                           r'($|x|+|y|=\sqrt2$).'), run_time=1.2)
        self.wait(2.5)
        self.play(FadeIn(d2, scale=0.5), FadeIn(t2),
                  self.say(r'And $(1,1)$ is in the square, not the disc ($x^2+y^2=2$).'), run_time=1.2)
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1)
        self.idea_card(r'If $|x|,|y|\le 1$, higher powers are smaller: $t^q\le t^p$ for $p\le q$.\\'
                       r'So $A_p\subseteq A_q$: the ball grows with $p$, from diamond to square.', hold=6)
