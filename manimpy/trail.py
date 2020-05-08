'''
@Author       : Jin Yuhan
@Date         : 2020-04-22 17:09:23
@LastEditors  : Jin Yuhan
@LastEditTime : 2020-05-08 12:07:37
@Description  : 拖尾特效
'''
from manimlib.imports import *
from manimpy.vectors import *

class Trail(VGroup):
    class Position:
        def __init__(self, pos, life_time):
            super().__init__()
            self.pos = pos
            self.time = life_time
            self.life_time = life_time
            
        def update_life_time(self, dt):
            self.time -= dt
            
        def get_opacity(self):
            return self.time / self.life_time
            
        @property
        def should_remove(self):
            return self.life_time <= 0
    
    CONFIG = {
        'life_time': 1,  #* 拖尾的生命周期，以秒为单位
        'min_width': 5,  #* 最小的宽度
        'trail_color': None,  #* 默认使用目标对象的颜色
        'width': None,  #* 默认目标对象的宽度，如果它大于min_width
        'rate_func': linear
    }
    
    def __init__(self, obj: Mobject, **kwargs):
        super().__init__(obj, VGroup(), **kwargs)
        self.all_pos = []
        self.last_pos = obj.get_center()
        
        if self.trail_color is None:
            self.trail_color = obj.color
        
        if not self.width:
            self.width = obj.get_width() if obj.get_width() > self.min_width else self.min_width
    
    def update_point_list(self, dt, pos=None):
        for i in range(len(self.all_pos)):
            self.all_pos[i].update_life_time(dt)
        
        while len(self.all_pos) > 0 and self.all_pos[0].should_remove:
            self.all_pos.pop(0)
            
        if not (pos is None):
            self.all_pos.append(Trail.Position(pos, self.life_time))

        return self
    
    def get_path(self):
        return VGroup(*[
                Line(
                    self.all_pos[i].pos, self.all_pos[i + 1].pos, 
                    stroke_color=self.trail_color,
                    stroke_opacity=self.rate_func(self.all_pos[i].get_opacity()), 
                    plot_depth=self.rate_func(self.all_pos[i].get_opacity()),
                    stroke_width=self.width * self.rate_func(self.all_pos[i].get_opacity())
                )
                for i in range(len(self.all_pos) - 1)
            ]) if len(self.all_pos) > 1 else VGroup()

    def update_trail(self, trail, dt):
        pos = self[0].get_center()
        self.update_point_list(dt, pos if sqr_distance(pos, self.last_pos) > 0 else None)
        
        self.last_pos = pos
        trail.become(self.get_path())
    
    def enable(self):
        self[1].add_updater(self.update_trail)
        return self
    
    def disable(self):
        self[1].remove_updater(self.update_trail)
        return self
