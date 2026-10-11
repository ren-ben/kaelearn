# The 3D reference: one layer at a time. The surface, then the map seen from straight above,
# then back to the side. Specimen: copy the shape, not the content.
from klmanim import *

LEVELS = (0.3, 0.7, 1.1, 1.5, 1.9)  # equal steps in height, so crowded rings mean steep ground
SIDE = dict(phi=64 * DEGREES, theta=-50 * DEGREES, zoom=0.9)


def f(x, y):
    return 2.2 * np.exp(-(x ** 2 + y ** 2) / 4)


def grad(x, y):
    return -f(x, y) / 2 * np.array([x, y])


def ascent(x, y, h=0.05, steps=400):
    # follow the gradient uphill until it is nearly flat
    pts = [(x, y)]
    for _ in range(steps):
        g = grad(*pts[-1])
        if np.linalg.norm(g) < 0.02:
            break
        pts.append(tuple(np.array(pts[-1]) + h * g / max(np.linalg.norm(g), 0.25)))
    return pts


class Uphill(KLScene3D):
    def construct(self):
        self.title_card('Uphill', 'what the gradient points at')
        self.question_card(r'A height $f(x,y)$ above every point of the plane.\\'
                           r'Where does $\nabla f$ point, and what does its length tell you?')

        self.set_camera_orientation(**SIDE)
        ax = kl_axes3d([-3, 3], [-3, 3], [0, 2.5], z_length=3)
        surf = kl_surface(ax, f, [-3, 3], [-3, 3])
        self.play(self.say(r'The surface is the graph of $f$: its height above each point $(x,y)$.'),
                  Create(surf), run_time=2.5)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        # from straight above, the surface becomes a map
        self.play(self.say(r'Look down from above. Each ring joins the points where $f$ has the same height.'))
        self.move_camera(phi=0, theta=-90 * DEGREES, zoom=0.78, run_time=3)
        unit = ax.x_axis.get_unit_size()
        rings = VGroup(*[Circle(radius=np.sqrt(-4 * np.log(c / 2.2)) * unit, color=DIM, stroke_width=2)
                         .move_to(ax.c2p(0, 0, 2.4)) for c in LEVELS])
        self.play(Create(rings), surf.animate.set_fill(opacity=0.3).set_stroke(opacity=0.1), run_time=2)
        self.wait(2)

        arrows = VGroup()
        for x in np.linspace(-2.5, 2.5, 6):
            for y in np.linspace(-2.5, 2.5, 6):
                g = grad(x, y)
                if np.linalg.norm(g) > 0.15:
                    arrows.add(Arrow(ax.c2p(x, y, 2.4), ax.c2p(x + 0.8 * g[0], y + 0.8 * g[1], 2.4), buff=0,
                                     color=HI, stroke_width=3, max_tip_length_to_length_ratio=0.3))
        self.play(self.say(r'Now $\nabla f$ at each point: it crosses the rings at right angles, pointing uphill.'),
                  LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.04), run_time=3)
        self.wait(2.5)
        self.play(self.say(r'Its length is the steepness: long where the rings crowd together, short near the top.'))
        self.wait(3)

        pts = ascent(2.7, -1.2)
        path = VMobject(color=HI, stroke_width=5).set_points_smoothly([ax.c2p(x, y, f(x, y) + 0.04) for x, y in pts])
        dot = Dot3D(path.get_start(), radius=0.09, color=HI)
        self.play(self.say(r'Start anywhere and follow the arrows: they lead to the top.'),
                  Create(path), MoveAlongPath(dot, path), run_time=4, rate_func=smooth)
        self.wait(1.5)

        # back to the side: the same path, now as a climb
        self.play(FadeOut(rings), FadeOut(arrows), surf.animate.set_fill(opacity=0.85).set_stroke(opacity=1),
                  self.say(r'From the side, that path is the steepest way up the hill. At the top, $\nabla f = 0$.'),
                  run_time=1.5)
        self.move_camera(**SIDE, run_time=3)
        dot.move_to(path.get_start())
        self.play(MoveAlongPath(dot, path), run_time=4, rate_func=smooth)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.idea_card(r'$\nabla f$ points where $f$ grows fastest, and its length is how fast.\\'
                       r'Where $f$ is flat, $\nabla f = 0$.')
