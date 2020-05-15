'''
@Author       : Jin Yuhan
@Date         : 2020-05-15 12:45:33
@LastEditors  : Jin Yuhan
@LastEditTime : 2020-05-15 18:01:34
@Description  : 视频开头动画
'''

from manimpy import *

class Start(Scene):
    def construct(self):
        self.wait(0.5)
        
        text = TextMobject('Made With Manim', color=BLACK).scale(0.65).shift(LEFT)
        rect = SurroundingRectangle(text, stroke_width=0)
        rect.set_fill(WHITE, 1).next_to(text.get_corner(LEFT), aligned_edge=LEFT, buff=0)
        rect.set_width(rect.get_width() * 0.9, stretch=True, about_point=rect.get_corner(LEFT))
        side_line = Line(vec(FRAME_WIDTH / 2, FRAME_HEIGHT / 2, 0), vec(FRAME_WIDTH / 2, FRAME_HEIGHT / 2 + 0.05, 0), stroke_width=16)
        
        three = VGroup(
            SVGMobject(BILIBILI_GOOD_SVG).set_color(BLUE).set_opacity(0.4),
            SVGMobject(BILIBILI_COIN_SVG).set_color(BLUE).set_opacity(0.4),
            SVGMobject(BILIBILI_FAVO_SVG).set_color(BLUE).set_opacity(0.4)
        ).set_height(0.6).arrange(RIGHT).to_corner(UL)
        
        rect.add_updater(lambda m, dt: m.set_width(m.get_width() + 0.5 * dt, stretch=True, about_point=rect.get_corner(LEFT)))
        text.add_updater(lambda m, dt: m.shift(RIGHT * 0.2 * dt))
        side_line.add_updater(lambda m, dt: m.put_start_and_end_on(m.get_start(), m.get_end() + DOWN * dt * 1.5))
        
        self.add(side_line)
        self.play(
            FadeIn(rect),
            FadeInFrom(text, LEFT),
            *[FadeInFrom(m, LEFT, run_time=t) for m, t in zip(three, [0.5, 1, 1.5])]
        )
        
        link = TextMobject('Manim: ', 'https://github.com/3b1b/manim').scale(0.4).to_edge(DOWN)
        link_1 = TextMobject('Source Code: ', 'https://github.com/Jin-Yuhan/manimpy').scale(0.4).to_edge(DOWN)
        link_2 = TextMobject('bilibili only').scale(0.4).to_edge(DOWN).set_color(BLUE)
        kwargs =  {'axis': X_AXIS, 'about_point': link.get_center() + IN * 0.09}
        
        link.rotate(-PI / 2, **kwargs)
        link_1.rotate(-PI / 2, **kwargs)
        link_2.rotate(-PI / 2, **kwargs)
        
        link[1].set_color(BLUE)
        link_1[1].set_color(BLUE)
        
        self.add(link, link_1, link_2)
        
        self.play(link.rotate, PI / 2, kwargs)
        self.play(
            link.rotate, PI / 2, kwargs,
            link_1.rotate, PI / 2, kwargs
        )
        self.play(
            link_1.rotate, PI / 2, kwargs,
            link_2.rotate, PI / 2, kwargs
        )
        
        self.wait(0.5)
        
        self.play(
            FadeOutAndShift(text, RIGHT), 
            FadeOut(rect, RIGHT), 
            FadeOutAndShiftDown(side_line),
            link_2.rotate, PI / 2, kwargs,
            *[FadeOutAndShift(m, RIGHT, run_time=t) for m, t in zip(three, [1.5, 1, 0.5])],
            rate_func=smooth
        )
        self.wait(1)