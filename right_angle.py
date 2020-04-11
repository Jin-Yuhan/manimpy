# from @cigar666
# cgnb!!!!

from manimlib.imports import *


class RightAngle(VGroup):
    CONFIG = {
        'size': 0.25,
        'stroke_color': WHITE,
        'stroke_width': 3.2,
        'fill_color': BLUE,
        'fill_opacity': 0.5,
        'on_the_right': True,
    }

    def __init__(self, corner=ORIGIN, angle=0, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.corner = ORIGIN
        self.angle = 0
        r = UR if self.on_the_right else UL
        self.add(
                Polygon(ORIGIN, RIGHT * self.size * r, UR * self.size * r, UP * self.size * r, stroke_width=0,
                        fill_color=self.fill_color, fill_opacity=self.fill_opacity),

                Line(RIGHT * self.size * r, UR * self.size * r + UP * self.stroke_width / 100 / 2 * 0.8,
                     stroke_width=self.stroke_width, stroke_color=self.stroke_color),

                Line(UR * self.size * r + RIGHT * self.stroke_width / 100 / 2 * r * 0.8, UP * self.size * r,
                     stroke_width=self.stroke_width, stroke_color=self.stroke_color),
                 )
        self.move_corner_to(corner)
        self.change_angle_to(angle)

    def move_corner_to(self, new_corner):
        self.shift(new_corner - self.corner)
        self.corner = new_corner
        return self

    def change_angle_to(self, new_angle):
        self.rotate(new_angle - self.angle, about_point=self.corner)
        self.angle = new_angle
        return self

