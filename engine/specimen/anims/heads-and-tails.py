# The reference animation: one idea, moving, understandable without the PDF.
# Specimen: copy the shape, not the content.
from klmanim import *

A = 2.0
SEQ = [5.4, -0.6, 4.3, 0.4, 3.6, 1.1] + [A + 0.95 * (-1) ** n * 7 / n for n in range(7, 21)]


def first_n(eps):
    # the first index after which every term stays within eps of a
    return next(n for n in range(1, 21) if all(abs(x - A) < eps for x in SEQ[n - 1:]))


class HeadsAndTails(KLScene):
    def construct(self):
        self.title_card('Heads and Tails', 'why a convergent sequence is bounded')
        self.question_card(r'If $a_n \to a$, is the sequence bounded?\\'
                           r'Is there one number $M$ with $|a_n| \le M$ for every $n$?')

        ax = kl_axes([0, 21, 5], [-1.5, 6.5, 2], x_length=11, y_length=5).shift(0.7 * DOWN)
        dots = VGroup(*[Dot(ax.c2p(n, x), radius=0.06) for n, x in enumerate(SEQ, 1)]).set_z_index(1)
        a_line = DashedLine(ax.c2p(0, A), ax.c2p(21, A), color=DIM, dash_length=0.08)
        a_lab = MathTex('a', color=DIM).next_to(a_line, RIGHT, buff=0.15)
        self.play(Create(ax), self.say(r'A convergent sequence: the terms $a_n$ settle near the limit $a$.'))
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.12), run_time=2.5)
        self.add(dots)  # the group itself must be in the scene for its updater to run
        self.play(Create(a_line), FadeIn(a_lab))
        self.wait(1)
        self.play(self.say(r'Convergence promises: for every $\varepsilon > 0$ there is an $N$ with '
                           r'$|a_n - a| < \varepsilon$ for all $n \ge N$.'))
        self.wait(3)

        # eps shrinks in steps; N glides to each new whole number at the same time
        eps, nx = ValueTracker(1.0), ValueTracker(first_n(1.0))

        def band():
            e, x = eps.get_value(), nx.get_value() - 0.5
            r = Polygon(ax.c2p(x, A - e), ax.c2p(21, A - e), ax.c2p(21, A + e), ax.c2p(x, A + e),
                        stroke_width=0, fill_color=INK, fill_opacity=0.12)
            v = DashedLine(ax.c2p(x, -1.5), ax.c2p(x, 6.5), color=DIM, dash_length=0.08)
            return VGroup(r, v, MathTex('N', color=DIM, font_size=30).next_to(v, DOWN, buff=0.1))

        def recolor(g):
            for i, d in enumerate(g, 1):
                d.set_color(HI if i >= nx.get_value() - 1e-6 else DIM)

        eps_lab = always_redraw(lambda: MathTex(rf'\varepsilon = {eps.get_value():.2f}', color=DIM, font_size=30)
                                .next_to(ax.c2p(21, 6.5), RIGHT, buff=0.15))
        self.play(self.say(r'You choose $\varepsilon$. Take $\varepsilon = 1$: from $N$ on, every term '
                           r'sits in the band around $a$.'), FadeIn(always_redraw(band)), FadeIn(eps_lab))
        dots.add_updater(recolor)
        self.wait(3)

        head = SurroundingRectangle(VGroup(*dots[:6]), color=LOW, buff=0.15)
        self.play(self.say(r'The tail is bounded by $|a| + 1$. Before $N$: only finitely many terms.'), Create(head))
        self.wait(2.5)
        m_line = DashedLine(ax.c2p(0, 5.4), ax.c2p(21, 5.4), color=DIM, dash_length=0.08)
        m_lab = MathTex('M', color=DIM).next_to(m_line, RIGHT, buff=0.15)
        self.play(self.say(r'Finitely many numbers have a largest one. That, or $|a|+1$ if it is '
                           r'bigger, is $M$.'), Create(m_line), FadeIn(m_lab))
        self.wait(3)

        self.play(FadeOut(head), self.say(r'Any $\varepsilon$ works. Smaller $\varepsilon$ pushes $N$ '
                                          r'right: the head grows, but it stays finite.'))
        for e in (0.6, 0.45):
            self.play(eps.animate.set_value(e), nx.animate.set_value(first_n(e)), run_time=2.5, rate_func=smooth)
            self.wait(1.5)

        dots.clear_updaters()
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.idea_card(r'Convergence tames the tail with one fixed $\varepsilon$.\\'
                       r'The head is finite, so it has a maximum.')
