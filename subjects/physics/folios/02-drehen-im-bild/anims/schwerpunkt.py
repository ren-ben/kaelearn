# Der Schwerpunkt: der eine Punkt einer geworfenen Hantel, der eine saubere Parabel fliegt, und warum.
# Folio physics 02 (Drehen, im Bild), Teil II.
from klmanim import *

A, B = 1.2, 0.4   # distances of the light end (m) and the heavy end (3m) from the centre of mass: m*A = 3m*B
TURNS = 3


def cm(s):
    """Parabola: uniform in x, quadratic in y (constant horizontal velocity, constant g)."""
    return np.array([-5.6 + 11.2 * s, -2.0 + 13.6 * s * (1 - s), 0])


def unit(s):
    a = 20 * DEGREES + TURNS * TAU * s   # free rotation: gravity has no torque about the centre of mass
    return np.array([np.cos(a), np.sin(a), 0])


def light(s):
    return cm(s) + A * unit(s)


def heavy(s):
    return cm(s) - B * unit(s)


def middle(s):
    return cm(s) + (A - B) / 2 * unit(s)


class Schwerpunkt(KLScene):
    def construct(self):
        self.title_card('Der Schwerpunkt', 'der eine Punkt, der sich benimmt')
        q = self.card('Die Frage', r'Eine Hantel mit den Massen $m$ und $3m$ wird geworfen und dreht sich im Flug.\\'
                                   r'Welcher ihrer Punkte fliegt eine saubere Parabel?\\'
                                   r'Und warum gerade dieser?', 6)
        self.play(FadeOut(q), run_time=0.8)

        def flight(tracked):
            """A fresh dumbbell at the start, its traces, and the tracker that throws it."""
            s = ValueTracker(0)

            def body():
                v = s.get_value()
                return VGroup(Line(light(v), heavy(v), color=INK, stroke_width=4),
                              Dot(light(v), radius=0.09, color=INK), Dot(heavy(v), radius=0.17, color=HI)).set_z_index(2)

            b = always_redraw(body)
            traces = [TracedPath(lambda f=f: f(s.get_value()), stroke_color=c, stroke_width=w) for f, c, w in tracked]
            return s, b, traces

        # flight 1: the two ends
        s, b, tr = flight([(light, DIM, 2.5), (heavy, INK, 2.5)])
        lab = VGroup(MathTex('m', font_size=32, color=INK).next_to(light(0), UP, buff=0.15),
                     MathTex('3m', font_size=32, color=HI).next_to(heavy(0), DOWN, buff=0.2))
        self.play(FadeIn(b), FadeIn(lab), self.say(r'Leichtes Ende $m$, schweres Ende $3m$, ein Stab dazwischen.'), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(lab), run_time=0.6)
        self.add(*tr)
        self.play(self.say(r'Geworfen. Die beiden Enden fliegen wilde Schleifen.'),
                  s.animate.set_value(1), run_time=7, rate_func=smooth)
        self.wait(2)
        for t in tr:
            t.clear_updaters()
        b.clear_updaters()
        self.play(FadeOut(b), *[FadeOut(t) for t in tr], run_time=1)

        # flight 2: the middle of the rod, and the centre of mass
        s, b, tr = flight([(middle, DIM, 2.5), (cm, HI, 5)])
        self.play(self.say(r'Noch einmal. Grau: die Mitte des Stabs. Hell: ein Punkt n\"aher am schweren Ende.'), run_time=1.2)
        self.play(FadeIn(b), run_time=1.2)
        self.wait(1)
        self.add(*tr)
        self.play(s.animate.set_value(1), run_time=7, rate_func=smooth)
        self.play(self.say(r'Die Mitte schlingert. Nur ein Punkt fliegt eine glatte Parabel: der Schwerpunkt.'), run_time=1)
        self.wait(3)
        for t in tr:
            t.clear_updaters()
        b.clear_updaters()
        self.play(FadeOut(b), *[FadeOut(t) for t in tr], run_time=1)

        # the seesaw: where it balances
        y, d = -0.4, 0.9
        L, H, S = np.array([-3 * d, y, 0]), np.array([d, y, 0]), np.array([0, y, 0])
        rod = Line(L, H, color=INK, stroke_width=5)
        ml = Dot(L, radius=0.12, color=INK)
        mh = Dot(H, radius=0.24, color=HI)
        knife = Polygon([0, y - 0.1, 0], [-0.35, y - 0.75, 0], [0.35, y - 0.75, 0], color=DIM, stroke_width=2,
                        fill_color=INK, fill_opacity=0.12)
        names = VGroup(MathTex('m', font_size=34, color=INK).next_to(ml, UP, buff=0.2),
                       MathTex('3m', font_size=34, color=HI).next_to(mh, UP, buff=0.2))
        arms = VGroup(DashedLine(L + 0.55 * DOWN, S + 0.55 * DOWN + 0.4 * LEFT, color=DIM, dash_length=0.08),
                      DashedLine(S + 0.55 * DOWN + 0.4 * RIGHT, H + 0.55 * DOWN, color=DIM, dash_length=0.08))
        armlab = VGroup(MathTex('3d', font_size=32, color=DIM).next_to(arms[0], DOWN, buff=0.12),
                        MathTex('d', font_size=32, color=DIM).next_to(arms[1], DOWN, buff=0.12))
        self.play(self.say(r'Wo liegt dieser Punkt? Leg die Hantel auf eine Schneide.'),
                  Create(rod), FadeIn(ml), FadeIn(mh), FadeIn(names), FadeIn(knife), run_time=2.5)
        self.wait(1)
        self.play(self.say(r'Sie balanciert, wenn sich die Drehmomente der Gewichte aufheben: $m\cdot 3d = 3m\cdot d$.'),
                  Create(arms), FadeIn(armlab), run_time=3)
        self.wait(2.5)
        eq = MathTex(r'm\cdot(-3d) \;+\; 3m\cdot(+d) \;=\; 0', font_size=44, color=HI).move_to([0, -2.6, 0])
        self.play(self.say(r'Mit Vorzeichen, vom Balancierpunkt aus gemessen: Die gewichteten Abst\"ande heben sich auf.'),
                  FadeIn(eq), run_time=3)
        self.wait(2)
        eq2 = MathTex(r'\sum_i m_i\,\vec r_{si} = 0', font_size=48, color=HI).move_to([0, -2.6, 0])
        self.play(self.say(r'Das ist $\sum m_i\vec r_{si} = 0$: Der Schwerpunkt ist der Balancierpunkt.'),
                  FadeOut(eq), run_time=2.5)
        self.play(FadeIn(eq2), run_time=1.2)
        self.wait(2.5)

        # why this point flies the parabola: Newton, summed
        self.play(FadeOut(VGroup(rod, ml, mh, knife, names, arms, armlab, eq2)),
                  self.say(r'Und warum fliegt gerade er die Parabel? Newton f\"ur beide Enden:'), run_time=2)
        lines = VGroup(
            MathTex(r'm\,\ddot{\vec r}_1 = m\vec g + \vec F', font_size=42),
            MathTex(r'3m\,\ddot{\vec r}_2 = 3m\vec g - \vec F', font_size=42),
            MathTex(r'm\,\ddot{\vec r}_1 + 3m\,\ddot{\vec r}_2 = 4m\,\vec g', font_size=42, color=HI),
            MathTex(r'\ddot{\vec R}_s = \vec g,\qquad \vec R_s = \frac{m\,\vec r_1 + 3m\,\vec r_2}{4m}', font_size=44, color=HI),
        ).arrange(DOWN, buff=0.45).move_to([0, -0.4, 0])
        self.play(FadeIn(lines[0]), FadeIn(lines[1]), run_time=2)
        self.wait(1.5)
        self.play(self.say(r'Der Stab zieht an beiden Enden mit $\vec F$ und $-\vec F$. Addiert f\"allt er heraus.'),
                  FadeIn(lines[2]), run_time=3)
        self.wait(2)
        self.play(self.say(r'Der massengewichtete Mittelwert f\"allt wie ein Stein: $\ddot{\vec R}_s = \vec g$, eine Parabel.'),
                  FadeIn(lines[3]), run_time=3)
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.card('Die Idee', r'Der Schwerpunkt ist der massengewichtete Mittelwert der Orte.\\'
                              r'Nur f\"ur diese Gewichte fallen die inneren Kr\"afte heraus,\\'
                              r'darum fliegt er wie ein Massenpunkt. Und $\sum m_i\vec r_{si} = 0$ hei\ss t: Dort balanciert er.', 6)
