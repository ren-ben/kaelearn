# Rollen: Schieben plus Drehen ist in jedem Moment eine Drehung um den Auflagepunkt.
# Folio physics 01 (Starrer Körper), Teil VII.
from klmanim import *

R = 1.7                        # wheel radius
GY = -2.75                     # ground height
C = np.array([-1.0, GY + R, 0])  # centre for the still part
V = 1.3                        # v_s, drawn as this length (so omega = V / R)
VR = 0.75                      # v_s while rolling, shorter so the arrow stays in frame


def arrow(a, b, color=HI, w=5):
    return Arrow(a, b, buff=0, color=color, stroke_width=w, max_tip_length_to_length_ratio=0.22,
                 max_stroke_width_to_length_ratio=8)


class Rollen(KLScene):
    def construct(self):
        self.title_card('Rollen', 'warum der oberste Punkt doppelt so schnell ist')
        q = self.card('Die Frage', r'Ein Rad rollt ohne zu rutschen mit $v_s$ nach rechts.\\'
                                   r'Wie schnell bewegt sich jeder seiner Punkte?\\'
                                   r'Und warum steht der unterste Punkt still?', 6)
        self.play(FadeOut(q), run_time=0.8)

        ground = Line([-7.2, GY, 0], [7.2, GY, 0], color=DIM, stroke_width=3)
        wheel = Circle(radius=R, color=INK, stroke_width=4).move_to(C)
        top, right, left, P = C + R * UP, C + R * RIGHT, C + R * LEFT, C + R * DOWN
        pts = [C, top, right, left, P]
        dots = VGroup(*[Dot(p, radius=0.07) for p in pts]).set_z_index(3)
        p_lab = MathTex('P', color=DIM, font_size=34).next_to(P, DL, buff=0.12)
        self.play(Create(ground), Create(wheel), FadeIn(dots), FadeIn(p_lab),
                  self.say(r'Ein Rad auf der Stra\ss e. Zerlegt in zwei Teile: Schieben und Drehen.'), run_time=2)
        self.wait(1.5)

        # 1: Schieben, every point gets v_s
        trans = [arrow(p, p + V * RIGHT, DIM) for p in pts]
        vs_lab = MathTex('v_s', color=DIM, font_size=30).next_to(trans[0], UP, buff=0.08)
        self.play(self.say(r'Schieben: Jeder Punkt bekommt dieselbe Geschwindigkeit $v_s$ wie die Mitte.'),
                  LaggedStart(*[GrowArrow(a) for a in trans], lag_ratio=0.15), FadeIn(vs_lab), run_time=3)
        self.wait(2)

        # 2: Drehen about the centre (clockwise): omega x r, tangential, length omega R = v_s
        dirs = [None, RIGHT, DOWN, UP, LEFT]
        rot = {i: arrow(pts[i], pts[i] + V * dirs[i], INK) for i in (1, 2, 3, 4)}
        arc = Arc(radius=0.55, start_angle=225 * DEGREES, angle=-90 * DEGREES, color=INK, stroke_width=3).move_arc_center_to(C)
        arc.add_tip(tip_length=0.15)
        om = MathTex(r'\omega', color=INK, font_size=30).move_to(C + 0.3 * LEFT)
        self.play(self.say(r'Drehen um die Mitte: $\vec\omega\times\vec r$ steht tangential, Betrag $\omega R$.'),
                  Create(arc), FadeIn(om), LaggedStart(*[GrowArrow(rot[i]) for i in rot], lag_ratio=0.15), run_time=3.5)
        self.wait(2)
        self.play(self.say(r'Kein Rutschen hei\ss t: $\omega R = v_s$. Beide Pfeile sind gleich lang.'),
                  *[Indicate(rot[i], color=HI, scale_factor=1.08) for i in rot], run_time=2.5)
        self.wait(1.5)

        # 3: add them, head to tail
        self.play(self.say(r'Addieren: den Drehpfeil an die Spitze des Schiebepfeils setzen.'),
                  *[rot[i].animate.shift(V * RIGHT) for i in rot], FadeOut(vs_lab), run_time=3.5)
        self.wait(1.5)
        res = {0: arrow(C, C + V * RIGHT), 1: arrow(top, top + 2 * V * RIGHT),
               2: arrow(right, right + V * (RIGHT + DOWN)), 3: arrow(left, left + V * (RIGHT + UP))}
        labs = VGroup(MathTex('v_s', font_size=30, color=HI).next_to(res[0].get_end(), UP, buff=0.12),
                      MathTex('2v_s', font_size=30, color=HI).next_to(res[1].get_end(), RIGHT, buff=0.12),
                      MathTex(r'\sqrt2\,v_s', font_size=30, color=HI).next_to(res[2].get_end(), RIGHT, buff=0.12),
                      MathTex(r'\sqrt2\,v_s', font_size=30, color=HI).next_to(res[3].get_center(), UL, buff=0.08),
                      MathTex('0', font_size=30, color=HI).next_to(P, DR, buff=0.12))
        self.play(self.say(r'Oben $2v_s$, Mitte $v_s$, unten $0$: Der Auflagepunkt steht still.'),
                  *[GrowArrow(res[i]) for i in res], *[FadeOut(trans[i]) for i in range(5)],
                  *[FadeOut(rot[i]) for i in rot], FadeIn(labs), run_time=3.5)
        self.play(Flash(P, color=HI, line_length=0.25, flash_radius=0.3), run_time=1.2)
        self.wait(2)

        # 4: pure rotation about P
        rays = VGroup(*[DashedLine(P, p, color=DIM, dash_length=0.08, stroke_width=2) for p in (C, top, right, left)])
        self.play(self.say(r'Jeder Pfeil steht senkrecht auf seiner Linie zu $P$.'),
                  LaggedStart(*[Create(r) for r in rays], lag_ratio=0.2), run_time=3)
        self.wait(2)
        prof = DashedLine(P, top + 2 * V * RIGHT, color=HI, dash_length=0.1, stroke_width=2)
        self.play(self.say(r'Und seine L\"ange w\"achst mit dem Abstand zu $P$: eine reine Drehung um $P$.'),
                  Create(prof), run_time=3)
        self.wait(3)

        # 5: roll it, a rim point traces a cycloid
        still = VGroup(wheel, dots, p_lab, arc, om, labs, rays, prof, *res.values())
        self.play(FadeOut(still), self.say(r'Jetzt rollt das Rad. Ein Punkt am Rand, oben gestartet:'), run_time=1.5)
        x0 = -5.4
        phi = ValueTracker(0)

        def centre():
            return np.array([x0 + R * phi.get_value(), GY + R, 0])

        def rim():
            a = PI / 2 - phi.get_value()
            return centre() + R * np.array([np.cos(a), np.sin(a), 0])

        def rolling_wheel():
            c, f = centre(), phi.get_value()
            spokes = VGroup(*[Line(c, c + R * np.array([np.cos(PI / 2 - f + k * PI / 2), np.sin(PI / 2 - f + k * PI / 2), 0]),
                                   color=LOW, stroke_width=2) for k in range(4)])
            return VGroup(Circle(radius=R, color=INK, stroke_width=4).move_to(c), spokes)

        def vel():
            p, c = rim(), centre()
            d = p - (c + R * DOWN)
            v = (VR / R) * np.array([d[1], -d[0], 0])
            if np.linalg.norm(v) < 0.06:  # at the cusp: no arrow (a VGroup, so become() never empties an Arrow)
                return VGroup()
            return VGroup(arrow(p, p + v, HI, 4))

        w = always_redraw(rolling_wheel)
        mark = always_redraw(lambda: Dot(rim(), radius=0.09, color=HI).set_z_index(3))
        varr = always_redraw(vel)
        self.play(FadeIn(w), FadeIn(mark), FadeIn(varr), run_time=1.2)
        trace = TracedPath(rim, stroke_color=HI, stroke_width=3)
        self.add(trace)
        self.play(self.say(r'Er zeichnet eine Zykloide. Sein Pfeil: immer senkrecht zur Linie nach unten.'),
                  phi.animate.set_value(PI), run_time=6, rate_func=smooth)
        self.play(self.say(r'Unten steht er f\"ur einen Augenblick still: die Spitze der Kurve.'), run_time=1)
        self.wait(2.5)
        self.play(phi.animate.set_value(2 * PI), run_time=6, rate_func=smooth)
        self.wait(1.5)

        trace.clear_updaters()
        for m in (w, mark, varr):
            m.clear_updaters()
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.card('Die Idee', r'Rollen ist Schieben plus Drehen, und das ist in jedem Moment\\'
                              r'eine reine Drehung um den Auflagepunkt.\\'
                              r'Geschwindigkeit $= \omega\cdot$ Abstand zu $P$: unten $0$, Mitte $v_s$, oben $2v_s$.', 6)
