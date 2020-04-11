"""
bilibili三连动画
"""

from manimlib.imports import *
from vectors import random_direction
from assets import *


class BilibiliScene(Scene):
    """
    修改自翔鸽的代码，
    xgnb!
    """

    CONFIG = {
        "good": SVGMobject(BILIBILI_GOOD_SVG, color=LIGHT_PINK).set_height(1).move_to(LEFT * 2.5 + DOWN * 2.7),
        "coin": SVGMobject(BILIBILI_COIN_SVG, color=LIGHT_PINK).set_height(1).move_to(DOWN * 2.7),
        "favo": SVGMobject(BILIBILI_FAVO_SVG, color=LIGHT_PINK).set_height(1).move_to(RIGHT * 2.5 + DOWN * 2.7),
        "times": 0,
        "vector_scale": 0.025,
        "should_new_dir": True
    }

    def construct(self):
        good = self.good
        coin = self.coin
        favo = self.favo

        self.play(
            FadeInFromPoint(good, good.get_center()),
            FadeInFromPoint(coin, coin.get_center()),
            FadeInFromPoint(favo, favo.get_center())
        )

        self.wait(0.4)

        circle_coin = Circle().scale(0.7).move_to(coin).set_stroke(BLUE, 8).rotate(PI/2).flip(UP)
        circle_favo = Circle().scale(0.7).move_to(favo).set_stroke(BLUE, 8).rotate(PI/2).flip(UP)

        good.add_updater(self.update_good)

        self.play(
            ShowCreation(circle_coin),
            ShowCreation(circle_favo),
            run_time=1.5
        )

        self.play(
            FadeOut(circle_coin),
            FadeOut(circle_favo),
            good.rotate, PI/8,
            coin.scale, 1.2,
            favo.scale, 1.2,
            run_time=0.3
        )

        self.play(
            good.rotate, -PI/8,
            coin.scale, 5/6,
            favo.scale, 5/6,
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
        self.wait()

    def update_good(self, good, dt):
        self.times += dt

        if self.times < 1.5:
            if self.should_new_dir:
                self.next_shift_dir = random_direction(scale=self.vector_scale)
            else:
                self.next_shift_dir = -self.next_shift_dir

            self.should_new_dir = not self.should_new_dir
            good.shift(self.next_shift_dir)


class BilibiliWhiteScene(BilibiliScene):
    """
    白色背景
    """
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }

