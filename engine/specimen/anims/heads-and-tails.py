# The reference animation: one idea, moving. Specimen, copy the shape, not the content.
from klmanim import *

A = 2.0
SEQ = [5.4, -0.6, 4.3, 0.4, 3.6, 1.1] + [A + 0.95 * (-1) ** n * 7 / n for n in range(7, 21)]


def first_n(eps):
    # the first index after which every term stays within eps of a
    return next(n for n in range(1, 21) if all(abs(x - A) < eps for x in SEQ[n - 1:]))


class HeadsAndTails(KLScene):
    def construct(self):
        self.title_card('Heads and Tails', 'why a convergent sequence is bounded')

        ax = kl_axes([0, 21, 5], [-1.5, 6.5, 2], x_length=11, y_length=5).shift(0.6 * DOWN)
        dots = VGroup(*[Dot(ax.c2p(n, x), radius=0.06) for n, x in enumerate(SEQ, 1)])
        a_line = DashedLine(ax.c2p(0, A), ax.c2p(21, A), color=DIM, dash_length=0.08)
        a_lab = MathTex('a', color=DIM).next_to(a_line, RIGHT, buff=0.15)
        say = Tex(r'$a_n \to a$: the terms settle near $a$.', font_size=34).to_edge(UP, buff=0.5)
        self.play(Create(ax), FadeIn(say), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.12), run_time=2.5)
        self.add(dots.set_z_index(1))  # the group itself must be in the scene for its updater to run
        self.play(Create(a_line), FadeIn(a_lab))
        self.wait(1)

        eps = ValueTracker(1.0)

        def band():
            n, e = first_n(eps.get_value()), eps.get_value()
            r = Polygon(ax.c2p(n - 0.5, A - e), ax.c2p(21, A - e), ax.c2p(21, A + e), ax.c2p(n - 0.5, A + e),
                        stroke_width=0, fill_color=INK, fill_opacity=0.12)
            v = DashedLine(ax.c2p(n - 0.5, -1.5), ax.c2p(n - 0.5, 6.5), color=DIM, dash_length=0.08)
            return VGroup(r, v, MathTex('N', color=DIM, font_size=30).next_to(v, DOWN, buff=0.1))

        def recolor(g):
            n = first_n(eps.get_value())
            for i, d in enumerate(g, 1):
                d.set_color(HI if i >= n else DIM)

        b = always_redraw(band)
        self.play(Transform(say, Tex(r'Choose $\varepsilon = 1$. Past $N$, every term is within $1$ of $a$.',
                                     font_size=34).to_edge(UP, buff=0.5)), FadeIn(b))
        dots.add_updater(recolor)
        self.wait(2)

        m_line = DashedLine(ax.c2p(0, 5.4), ax.c2p(21, 5.4), color=DIM, dash_length=0.08)
        m_lab = MathTex('M', color=DIM).next_to(m_line, RIGHT, buff=0.15)
        head = SurroundingRectangle(VGroup(*dots[:6]), color=LOW, buff=0.15)
        self.play(Transform(say, Tex(r'Before $N$: finitely many terms. A finite set has a maximum.',
                                     font_size=34).to_edge(UP, buff=0.5)), Create(head))
        self.play(Create(m_line), FadeIn(m_lab))
        self.wait(2)

        self.play(FadeOut(head), Transform(say, Tex(r'Shrink $\varepsilon$: $N$ moves right, the head grows, '
                                                    r'and it stays finite.', font_size=34).to_edge(UP, buff=0.5)))
        self.play(eps.animate.set_value(0.4), run_time=4, rate_func=smooth)
        self.wait(2)

        dots.clear_updaters()
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.idea_card('Convergence tames the tail with one fixed ε.\nThe head is finite, so it has a maximum.')
