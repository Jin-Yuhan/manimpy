from manimpy import *


class Scene1(Scene):
    CONFIG = {
        "radius": 3,
        "red_color": "#E83015",
        "font": "思源黑体",
        "times": 0,
        "vector_scale": 0.025,
        "should_new_dir": True,
        "camera_config": {
            "background_color": WHITE
        },
        "texts": [
            "manim向MK表白~",
            "I",
            "MK",
            "Manim Kindergarten"
        ],
        "t2c": {
            "M": BLUE,
            "K": "#97694F"
        },
    }

    def construct(self):
        title = Text(self.texts[0], color=BLACK, font=self.font, t2c=self.t2c).scale(0.7).set_stroke(width=0.5)
        self.play(WriteRandom(title), run_time=2)
        self.wait(2)
        self.play(UnWriteRandom(title), run_time=2)
        self.wait(1)

        circle = Circle(radius=self.radius, color=DARK_BLUE, plot_depth=3).flip().rotate(-PI / 2)
        self.play(ShowCreation(circle), run_time=2)

        point_a = Dot(vec(0, self.radius, 0), plot_depth=4, color=PURPLE)
        self.play(ShowCreation(point_a))

        alpha = ValueTracker(0.0001)
        point_b = Dot(color=BLUE, radius=0.07, plot_depth=4)
        point_b.add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())))

        alpha.set_value(0.125)
        self.play(ShowCreation(point_b))
        self.play(alpha.increment_value, 0.6, run_time=1.5)
        self.play(alpha.increment_value, -0.6, run_time=1.6)

        point_c = Dot(color=BLUE, radius=0.07, plot_depth=4)
        point_c.add_updater(lambda m: self.update_dot(m, point_b))

        line1 = Line(point_a.get_center(), point_c.get_center(), color=RED)
        line1.add_updater(lambda m: m.put_start_and_end_on(vec(0.001, self.radius, 0), point_c.get_center()))

        line2 = Line(point_b.get_center(), point_c.get_center(), color=RED)
        line2.add_updater(lambda m: m.put_start_and_end_on(point_b.get_center(), point_c.get_center()))

        ra = RightAngle(corner=point_c.get_center(), on_the_right=False, stroke_color=BLUE)
        ra.add_updater(lambda m: m.move_corner_to(point_c.get_center()))
        ra.add_updater(lambda m: m.change_angle_to(line1.get_angle() + PI/2))

        self.play(ShowCreation(point_c), ShowCreation(line1), ShowCreation(line2))
        self.wait()
        self.play(ShowCreation(ra))
        self.wait(2)
        self.play(FadeOut(ra))
        self.play(alpha.increment_value, 0.6, run_time=1.5)
        self.play(alpha.increment_value, -0.725, run_time=2, rate_func=linear)
        self.wait()

        trace = VGroup()
        vertices = []

        def update_trace(m):
            m.add(line1.copy().clear_updaters(), line2.copy().clear_updaters())
            vertices.append(point_c.get_center())

        self.add(trace)
        line1.set_stroke(width=2)
        line2.set_stroke(width=2)
        self.wait(2)

        trace.add_updater(update_trace)

        for _ in range(2):
            vertices.clear()
            alpha.set_value(0)
            self.play(ApplyMethod(alpha.increment_value, 1, run_time=8, rate_func=linear))
            self.wait()

        heart = Polygon(*vertices, color=self.red_color)
        self.play(ShowCreation(heart), run_time=5)
        self.play(heart.set_fill, self.red_color, 1, run_time=2)
        self.wait()

        self.remove(*[obj.clear_updaters() for obj in [point_a, point_b, point_c, circle, line1, line2, trace]])

        self.play(heart.scale, 0.1)
        self.wait(2)

        text1 = Text(self.texts[1], font=self.font, color=BLACK).scale(0.8).next_to(heart, LEFT, aligned_edge=ORIGIN, buff=0.25)\
            .set_stroke(width=0.5)
        text2 = Text(self.texts[2], font=self.font, t2c=self.t2c).scale(0.8).next_to(heart, RIGHT, aligned_edge=ORIGIN, buff=0.25)\
            .set_stroke(width=0.5)

        self.play(
            FadeInFrom(text1, RIGHT),
            FadeInFrom(text2, LEFT),
            run_time=2
        )
        self.wait(3.5)

        coin = SVGMobject(BILIBILI_COIN_SVG, color=BLUE).scale(0.35).next_to(heart, RIGHT, aligned_edge=ORIGIN, buff=0.25)
        favo = SVGMobject(BILIBILI_FAVO_SVG, color=LIGHT_PINK).scale(0.35)
        good = SVGMobject(BILIBILI_GOOD_SVG, color=GREEN).scale(0.35)
        self.add(coin.rotate(-TAU * 1.25).shift(vec(TAU * 1.25, 0, 0)))

        self.text2_rotation = 0

        def update_text2(m):
            m.rotate(PI / 10, about_point=m.get_center())
            self.text2_rotation += PI / 10

        text2.add_updater(lambda m: update_text2(m))

        velocity = 0.15
        for i in range(int(5 / velocity)):
            text2.shift(vec(UR * velocity))
            self.wait(1 / self.camera.frame_rate)
        text2.clear_updaters()
        self.remove(text2)
        self.wait()

        velocity = PI / 20
        for i in range(int(TAU * 1.25 / velocity)):
            coin.rotate(velocity, about_point=coin.get_center())
            coin.shift(vec(-velocity, 0, 0))
            self.wait(1 / self.camera.frame_rate)
        self.wait(3)

        self.play(
            FadeIn(good.move_to(coin.get_center())),
            coin.shift, vec(1, 0, 0),
            FadeInFrom(favo.move_to(coin.get_center() + vec(2, 0, 0)), LEFT),
            run_time=2.5
        )
        self.wait(1)

        surrounding = SurroundingRectangle(VGroup(text1, heart, good, coin, favo), color=BLUE)
        self.play(ShowCreationThenDestruction(surrounding), run_time=4)
        self.wait(2)

        text2.next_to(heart, LEFT, aligned_edge=ORIGIN, buff=0.25).rotate(-self.text2_rotation)
        self.play(ReplacementTransform(text1, text2), run_time=1.5)
        self.wait(2)

        surrounding = SurroundingRectangle(VGroup(text2, heart, good, coin, favo), color="#97694F")
        self.play(ShowCreationThenDestruction(surrounding), run_time=4)
        self.wait(2)

        line = Line(heart.get_corner(UP) + vec(0, -0.07, 0), heart.get_corner(UP) + vec(0, 0.25, 0), color="#97694F")
        ellipse = Ellipse(width=0.1 * np.sqrt(5), height=0.1, color=GREEN).set_fill(GREEN, 1)\
            .move_to(line.point_from_proportion(0.75) + vec(0.05 * np.sqrt(5), 0, 0))
        text3 = Text(self.texts[3], color=BLACK, font=self.font, t2c=self.t2c).scale(0.7).set_stroke(width=0.5)\
            .to_edge(DOWN)

        self.play(ShowCreation(ellipse), ShowCreation(line), run_time=1.5)
        self.wait(2)
        self.play(
            FadeOutAndShift(text2, LEFT),
            FadeInFromDown(text3),
            run_time=1.5
        )
        self.wait(1)

        apple = VGroup(heart, line, ellipse)
        velocity = 0.001
        final_pos = text3.get_corner(UP) + vec(0, (apple.get_height() / 2), 0)
        for i in range(1000):
            if apple.get_center()[1] <= final_pos[1]:
                break
            apple.shift(vec(0, -velocity, 0))
            velocity += 0.0098
            self.wait(1 / self.camera.frame_rate)

        velocity = TAU / 300
        vertical_velocity = 0.002
        for i in range(int(PI / 18 / velocity)):
            apple.rotate(-velocity, about_point=apple.get_center())
            apple.shift(vec(0.01, -vertical_velocity, 0))
            vertical_velocity += 0.00005
            self.wait(1 / self.camera.frame_rate)
        self.wait(2)

        self.play(VGroup(good, coin, favo).move_to, ORIGIN)
        self.wait()
        self.play(
            good.shift, LEFT,
            favo.shift, RIGHT,
        )
        self.wait()
        self.play(
            good.set_height, 1,
            coin.set_height, 1,
            favo.set_height, 1,
        )
        self.wait()

        circle_coin = Circle().scale(0.7).move_to(coin).set_stroke(BLUE, 8).rotate(PI / 2).flip(UP)
        circle_favo = Circle().scale(0.7).move_to(favo).set_stroke(BLUE, 8).rotate(PI / 2).flip(UP)

        good.add_updater(self.update_good)

        self.play(
            ShowCreation(circle_coin),
            ShowCreation(circle_favo),
            run_time=1.5
        )

        self.play(
            FadeOut(circle_coin),
            FadeOut(circle_favo),
            good.rotate, PI / 8,
            coin.scale, 1.2,
            favo.scale, 1.2,
            run_time=0.3
        )

        self.play(
            good.rotate, -PI / 8,
            coin.scale, 5 / 6,
            favo.scale, 5 / 6,
            run_time=0.1
        )

        self.play(
            FadeToColor(good, BLUE),
            FadeToColor(coin, BLUE),
            FadeToColor(favo, BLUE),
            Flash(coin.get_center(), color=BLUE, line_length=0.4, flash_radius=1.5),
            Flash(favo.get_center(), color=BLUE, line_length=0.4, flash_radius=1.5),
            Flash(good.get_center(), color=BLUE, line_length=0.4, flash_radius=1.5),
            run_time=0.3
        )

        self.wait(2)

        self.play(
            FadeOut(good),
            FadeOut(coin),
            FadeOut(favo),
            run_time=0.8
        )
        self.wait(5)

    def update_dot(self, m, point_b):
        tangent = vertical_vec(point_b.get_center())  # ->(a, b), point_b: (c, d)
        a = x_of(tangent)
        b = y_of(tangent)
        c = x_of(point_b.get_center())
        d = y_of(point_b.get_center())
        x = (self.radius * a * b - a * b * d + b * b * c) / (a * a + b * b)  # that's good
        y = -a / b * x + self.radius
        m.move_to(vec(x, y, 0))

    def update_good(self, good, dt):
        self.times += dt

        if self.times < 1.5:
            if self.should_new_dir:
                self.next_shift_dir = random_direction(scale=self.vector_scale)
            else:
                self.next_shift_dir = -self.next_shift_dir

            self.should_new_dir = not self.should_new_dir
            good.shift(self.next_shift_dir)

