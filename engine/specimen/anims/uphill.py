# The 3D reference: a surface, a field on the floor below it, a path that ties them together.
# Specimen: copy the shape, not the content.
from klmanim import *

FLOOR = -2.6


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

        self.set_camera_orientation(phi=64 * DEGREES, theta=-50 * DEGREES, zoom=0.85)
        ax = kl_axes3d([-3, 3], [-3, 3], [FLOOR, 2.5], z_length=5.1)
        surf = kl_surface(ax, f, [-3, 3], [-3, 3])
        rings = VGroup(*[Circle(radius=np.sqrt(-4 * np.log(c / 2.2)) * ax.x_axis.get_unit_size(), color=DIM,
                                stroke_width=1.5).move_to(ax.c2p(0, 0, FLOOR)) for c in (0.3, 0.7, 1.1, 1.5, 1.9)])
        self.play(self.say(r'The surface is the graph of $f$: its height above each point $(x,y)$.'),
                  Create(surf), run_time=2.5)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.wait(2)
        self.play(self.say(r'Below it, the map: each ring joins the points where $f$ has the same height.'),
                  Create(rings), surf.animate.set_fill(opacity=0.25).set_stroke(opacity=0.3), run_time=2)
        self.wait(2)

        arrows = VGroup()
        for x in np.linspace(-2.6, 2.6, 7):
            for y in np.linspace(-2.6, 2.6, 7):
                g = grad(x, y)
                if np.linalg.norm(g) > 0.15:
                    arrows.add(Arrow(ax.c2p(x, y, FLOOR), ax.c2p(x + 0.7 * g[0], y + 0.7 * g[1], FLOOR), buff=0,
                                     color=HI, stroke_width=3, max_tip_length_to_length_ratio=0.35))
        self.play(self.say(r'On the map, $\nabla f$ at each point: it crosses the rings at right angles, '
                           r'pointing uphill.'), LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.03),
                  run_time=3)
        self.wait(2.5)
        self.play(self.say(r'Its length is the steepness: long on the slopes, short near the flat top.'))
        self.wait(3)

        pts = ascent(2.7, -1.2)
        top = VMobject(color=HI, stroke_width=4).set_points_smoothly([ax.c2p(x, y, f(x, y)) for x, y in pts])
        low = VMobject(color=INK, stroke_width=3).set_points_smoothly([ax.c2p(x, y, FLOOR) for x, y in pts])
        climber, shadow = Dot(top.get_start(), color=HI, radius=0.08), Dot(low.get_start(), color=INK, radius=0.06)
        self.add(climber, shadow)
        self.play(surf.animate.set_fill(opacity=0.8).set_stroke(opacity=1), run_time=1)
        self.play(self.say(r'Follow the arrows and you climb the steepest way up. At the top, $\nabla f = 0$.'),
                  Create(top), Create(low), MoveAlongPath(climber, top), MoveAlongPath(shadow, low),
                  run_time=5, rate_func=smooth)
        self.wait(2)

        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.idea_card(r'$\nabla f$ points where $f$ grows fastest, and its length is how fast.\\'
                       r'Where $f$ is flat, $\nabla f = 0$.')
