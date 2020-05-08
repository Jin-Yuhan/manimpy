'''
@Author       : Jin Yuhan
@Date         : 2020-04-30 19:50:04
@LastEditors  : Jin Yuhan
@LastEditTime : 2020-05-08 12:07:04
@Description  : 等差数列求和
'''
from manimpy import *

# 证明
class Scene2(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 6,
        "y_min": 0,
        "y_max": 6,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "graph_origin": vec(-5, -3, 0),
        "axes_color": WHITE,
        "rainbow_colors": [RED, ORANGE, YELLOW, GREEN, BLUE]
    }
    
    def setup_axes(self):
        x_num_range = float(self.x_max - self.x_min)
        self.space_unit_to_x = self.x_axis_width / x_num_range
        if self.x_labeled_nums is None:
            self.x_labeled_nums = []
        if self.x_leftmost_tick is None:
            self.x_leftmost_tick = self.x_min
        x_axis = NumberLine(
            x_min=self.x_min,
            x_max=self.x_max,
            unit_size=self.space_unit_to_x,
            tick_frequency=self.x_tick_frequency,
            leftmost_tick=self.x_leftmost_tick,
            numbers_with_elongated_ticks=self.x_labeled_nums,
            color=self.axes_color
        )
        x_axis.shift(self.graph_origin - x_axis.number_to_point(0))
        if len(self.x_labeled_nums) > 0:
            if self.exclude_zero_label:
                self.x_labeled_nums = [x for x in self.x_labeled_nums if x != 0]
            x_axis.add_numbers(*self.x_labeled_nums)
        if self.x_axis_label:
            x_label = TextMobject(self.x_axis_label)
            x_label.next_to(
                x_axis.get_tick_marks(), UP + RIGHT,
                buff=SMALL_BUFF
            )
            x_label.shift_onto_screen()
            x_axis.add(x_label)
            self.x_axis_label_mob = x_label

        y_num_range = float(self.y_max - self.y_min)
        self.space_unit_to_y = self.y_axis_height / y_num_range

        if self.y_labeled_nums is None:
            self.y_labeled_nums = []
        if self.y_bottom_tick is None:
            self.y_bottom_tick = self.y_min
        y_axis = NumberLine(
            x_min=self.y_min,
            x_max=self.y_max,
            unit_size=self.space_unit_to_y,
            tick_frequency=self.y_tick_frequency,
            leftmost_tick=self.y_bottom_tick,
            numbers_with_elongated_ticks=self.y_labeled_nums,
            color=self.axes_color,
            line_to_number_vect=LEFT,
            label_direction=LEFT,
        )
        y_axis.shift(self.graph_origin - y_axis.number_to_point(0))
        y_axis.rotate(np.pi / 2, about_point=y_axis.number_to_point(0))
        if len(self.y_labeled_nums) > 0:
            if self.exclude_zero_label:
                self.y_labeled_nums = [y for y in self.y_labeled_nums if y != 0]
            y_axis.add_numbers(*self.y_labeled_nums)
        if self.y_axis_label:
            y_label = TextMobject(self.y_axis_label)
            y_label.next_to(
                y_axis.get_corner(UP + RIGHT), UP + RIGHT,
                buff=SMALL_BUFF
            )
            y_label.shift_onto_screen()
            y_axis.add(y_label)
            self.y_axis_label_mob = y_label

        self.x_axis, self.y_axis = self.axes = VGroup(x_axis, y_axis)
        self.default_graph_colors = it.cycle(self.default_graph_colors)
        
    def draw_x_axis(self):
        self.play(Write(self.x_axis))
        
    def draw_y_axis(self):
        self.play(Write(self.y_axis))
    
    def construct(self):
        unit = self.x_axis_width / (self.x_max - self.x_min) #* 图像单位
        half_unit = unit * 0.5 #* 图像 0.5单位
        
        captions = Captions(
            "f(x)=x+1",
            "a_{%d}",
            "在一个", "等差数列", "中", "$S_n$", "即前", "$n$", "项的和 要如何计算呢？",
            "不妨先在", "$a_1=2$", ", ", "$d=1$", "的条件下研究", "$S_5$", "的值",
            "f(%d)",
            "S_5",
            r"\Leftrightarrow {", "5", r" \cdot (", "f(0.5)", "+", "f(5.5)", r") \over 2}",
            r"={", "5", r" \cdot (", "1.5", " + ", "6.5", r") \over 2}",
            r"= 20"
        )
        
        self.setup_axes()
        _graph = self.get_graph(lambda x: x + 1, '#2EA9DF')
        graph = VGroup(_graph, TexMobject(captions.get(), color='#2EA9DF').next_to(_graph, UP, buff=-1))
        #-----------------------------------------------------------------------------------
        
        self.draw_x_axis()
        self.wait()
        
        points = VGroup(*[
            Dot(vec(self.graph_origin[0] + x * unit, self.graph_origin[1], 0), color=self.rainbow_colors[x - 1]) 
            for x in range(1, 6)
        ])
        seq_values = VGroup(*[
            TexMobject(captions.get(move_index=i == 5) % i).next_to(p, direction=UP, buff=0.25)
            for i, p in zip(range(1, 6), points)
        ])
        
        trails = [Trail(p, width=15).enable() for p in points]
        self.add(*trails)

        self.play(
            ShowCreation(points),
            ShowCreation(seq_values),
            run_time=2
        )
        self.wait(2)
        
        text_1 = TextMobject(*captions.get(7)).scale(0.75).to_edge(UP).set_color_by_tex_to_color_map({
            "等差数列": PINK,
            "S_n": PINK,
            "n": PINK
        })
        text_2 = TextMobject(*captions.get(7)).scale(0.75).to_edge(UP).set_color_by_tex_to_color_map({
            "a_1=2": BLUE, 
            "d=1": BLUE,
            "S_5": BLUE
        })
        
        self.play(Write(text_1), run_time=1.8)
        self.wait(3)
        self.play(ReplacementTransform(text_1, text_2), run_time=1.8)
        self.wait(3)
        self.play(Uncreate(text_2))
        self.wait()
        
        numbers = VGroup(*[TexMobject(str(i)) for i in range(1, 6)])
        self.play(*[Write(numbers[i].next_to(points[i], DOWN)) for i in range(len(numbers))], run_time=1.5)
        self.wait()
        
        seq_values[0].add_updater(lambda m: m.next_to(points[0], direction=UP, buff=0.25))
        seq_values[1].add_updater(lambda m: m.next_to(points[1], direction=UP, buff=0.25))
        seq_values[2].add_updater(lambda m: m.next_to(points[2], direction=UP, buff=0.25))
        seq_values[3].add_updater(lambda m: m.next_to(points[3], direction=UP, buff=0.25))
        seq_values[4].add_updater(lambda m: m.next_to(points[4], direction=UP, buff=0.25))
        #-----------------------------------------------------------------------------------
        
        self.draw_y_axis()
        self.wait()
        self.play(*[
            ApplyMethod(points[i].move_to, self.input_to_graph_point(i + 1, graph[0]), run_time=2) 
            for i in range(len(points))
        ])
        self.wait()
        
        for fv in seq_values:
            fv.clear_updaters()
            
        func_values = VGroup(*[
            TexMobject(captions.get(move_index=i == 5) % i).next_to(points[i - 1], direction=UP, buff=0.25)
            for i in range(1, 6)
        ])
        
        self.add(graph)
        self.remove(*points).add(*points)
        self.play(ShowCreation(graph), run_time=1.5)
        self.wait(1.5)
        
        self.play(ReplacementTransform(seq_values, func_values), run_time=2)
        self.wait(1.5)
        
        for t in trails:
            t.disable()
        #-----------------------------------------------------------------------------------
        
        lines = self.get_vertical_lines_to_graph(graph[0], 1, 5, 5)
        self.play(
            *[ShowCreation(lines[i].rotate(PI).set_color(self.rainbow_colors[i])) for i in range(len(lines))], 
            run_time=1.5
        )
        self.wait(1)

        value_traker = ValueTracker(0)
        temp_rects = VGroup(*[
            Polygon(
                line.get_corner(UP),
                line.get_corner(UP),
                line.get_corner(DOWN),
                line.get_corner(DOWN),
                stroke_color = line.get_stroke_color(),
            ).add_updater(lambda m: m.become(
                Polygon(
                    m.get_corner(UP) + LEFT * value_traker.get_value(),
                    m.get_corner(UP) + RIGHT * value_traker.get_value(),
                    m.get_corner(DOWN) + RIGHT * value_traker.get_value(),
                    m.get_corner(DOWN) + LEFT * value_traker.get_value(),
                    stroke_color = m.get_stroke_color()
                )
            ))
            for line in lines
        ])
        self.add(temp_rects)
        self.remove(*lines)
        self.play(FadeOut(points))
        self.play(value_traker.set_value, half_unit, run_time=2)
        self.wait(1.5)
        
        rects = VGroup()
        self.add(rects)
        
        for i in range(len(func_values)):
            x = i + 1
            pos_x = self.graph_origin[0] + x * unit
            color = self.rainbow_colors[i]
            rects.add(VGroup(
                Polygon(
                    vec(pos_x - half_unit, self.input_to_graph_point(x - 0.5, graph[0])[1], 0),
                    vec(pos_x - half_unit, self.input_to_graph_point(x, graph[0])[1], 0),
                    vec(pos_x, self.input_to_graph_point(x, graph[0])[1], 0),
                    stroke_color=color,
                    fill_color=color,
                    fill_opacity=0.2
                ),
                Polygon(
                    vec(pos_x - half_unit, self.graph_origin[1], 0),
                    vec(pos_x + half_unit, self.graph_origin[1], 0),
                    vec(pos_x + half_unit, self.input_to_graph_point(x, graph[0])[1], 0),
                    vec(pos_x, self.input_to_graph_point(x, graph[0])[1], 0),
                    vec(pos_x - half_unit, self.input_to_graph_point(x - 0.5, graph[0])[1], 0),
                    stroke_color=color,
                    fill_color=color,
                    fill_opacity=0.2
                )
            ))
            self.remove(func_values[i])
            self.add(func_values[i])
            self.play(
                FadeIn(rects[-1]),
                ApplyMethod(
                    func_values[i].move_to, 
                    vec(self.graph_origin[0] + (i + 1) * unit, 0.5 * (self.input_to_graph_point(i + 1, graph[0])[1] - 3), 0)
                )
            )
        self.wait()
        self.remove(temp_rects)
        self.wait(2)
        
        for i in range(len(rects)):
            self.play(Rotating(
                rects[i][0], radians=-PI, run_time=1, axis=OUT, about_point=self.input_to_graph_point(i + 1, graph[0])
            ), run_time=0.5)
        self.wait(1.5)
        # !前半段动画结束
        #-----------------------------------------------------------------------------------
        
        area_shape = Polygon(
            vec(self.graph_origin[0] + half_unit, self.graph_origin[1], 0),
            vec(self.graph_origin[0] + half_unit, self.input_to_graph_point(0.5, graph[0])[1], 0),
            vec(self.graph_origin[0] + 5.5 * unit, self.input_to_graph_point(5.5, graph[0])[1], 0),
            vec(self.graph_origin[0] + 5.5 * unit, self.graph_origin[1], 0),
            stroke_color=self.rainbow_colors,
            fill_color=self.rainbow_colors,
            fill_opacity=0.35
        )
        area_shape.set_sheen_direction(RIGHT)
        all_shapes = VGroup(func_values, numbers, self.axes, *graph, rects)
        
        area_shape.scale(0.6).shift(UP + DR * 0.05)
        self.play(all_shapes.scale, 0.6)
        self.wait()
        self.play(all_shapes.shift, UP)
        self.wait(1.5)
        
        s_5 = TexMobject(captions.get()).scale(0.8).set_color(self.rainbow_colors).set_sheen_direction(RIGHT)
        proofs = VGroup(
            TexMobject(*captions.get(7)),
            TexMobject(*captions.get(7)),
            TexMobject(captions.get())
        ).scale(0.8).next_to(all_shapes, DOWN).arrange(DOWN, False, aligned_edge=LEFT)
        
        s_5.next_to(proofs[0], LEFT)
        proofs[1].set_color_by_tex_to_color_map({"5": PINK, "1.5": PINK, "6.5": PINK})
        area_shape_copy = area_shape.copy()
        
        self.play(ShowCreation(area_shape_copy))  
        self.wait()  
        self.play(ReplacementTransform(area_shape_copy, s_5))
        self.wait()
        
        self.play(Write(proofs[0][0]))
        
        line_1 = Line(area_shape.point_from_proportion(0), area_shape.point_from_proportion(0.7508852), color=PINK, stroke_width=8)
        self.play(ShowCreation(line_1), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(line_1, proofs[0][1].set_color(PINK)))
        
        self.play(Write(proofs[0][2]))
        
        line_2 = Line(area_shape.point_from_proportion(0), area_shape.point_from_proportion(0.245), color=PINK, stroke_width=8)
        self.play(ShowCreation(line_2), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(line_2, proofs[0][3].set_color(PINK)))
        
        self.play(Write(proofs[0][4]))
        
        line_3 = Line(area_shape.point_from_proportion(0.7508852), area_shape.point_from_proportion(0.5), color=PINK, stroke_width=8)
        self.play(ShowCreation(line_3), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(line_3, proofs[0][5].set_color(PINK)))
        
        self.play(Write(proofs[0][6]))
        
        for i in range(1, 3):
            self.play(Write(proofs[i]), run_time=1.2)
        self.wait(5)
        
    def func(self, x):
        return x + 1
    
    
class Scene3(Scene):
    def construct(self):
        captions = Captions(
            "根据上面的结果，易知：",
            "若将", "等差数列", r"$\{a_n\}$", "的通项公式看成是函数", "f(x)",
            "那么", "$f(x)=a_1 + (x-1)d_0$", "，", "$d_0$", "是公差",
            "S_n",
            r"={n(f(0.5) + f(n + 0.5)) \over 2}",
            r"={n(2a_1 + nd_0 - d_0) \over 2}",
            r"=na_1 + {n(n-1)\over 2}d_0",
            
            "如果觉得刚才的方法过于简单，也可以使用微积分",
            "S_n",
            r"=\int_{0.5}^{n+0.5}{a_1+(x-1)d_0 \, dx}",
            r"=a_1x+d_0(\frac{1}{2}x^2-x) \, \Big\vert_{0.5}^{n+0.5}",
            r"=na_1 + {n(n-1)\over 2}d_0"
        )
        
        desc = VGroup(
            TextMobject(captions.get()),
            TextMobject(*captions.get(5)),
            TextMobject(*captions.get(5))
        ).scale(0.75).arrange(DOWN, False, aligned_edge=LEFT).to_edge(UL)
        desc[1][1].set_color(BLUE)
        desc[1][2].set_color(BLUE)
        desc[1][4].set_color(BLUE)
        desc[2][1].set_color(BLUE)
        desc[2][3].set_color(BLUE)
        
        s_n = TexMobject(captions.get()).scale(0.75)
        proofs = VGroup(*[TexMobject(t) for t in captions.get(3)]).scale(0.75).arrange(DOWN, False, aligned_edge=LEFT)
        s_n.next_to(proofs[0], LEFT)
        
        for d in desc:
            self.play(Write(d), run_time=1.5)
            self.wait()
        self.wait(2.5)
        self.play(Write(s_n))
        self.wait()
        
        for p in proofs:
            self.play(Write(p))
        self.wait(5)
        
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))
        self.wait()
        
        desc_1 = TextMobject(captions.get()).scale(0.75).to_edge(UL)
        s_n = TexMobject(captions.get()).scale(0.75)
        proofs = VGroup(*[TexMobject(t) for t in captions.get(3)]).scale(0.75).arrange(DOWN, False, aligned_edge=LEFT)
        s_n.next_to(proofs[0], LEFT)
        
        self.play(Write(desc_1), run_time=1.5)
        self.wait(1.5)
        self.play(Write(s_n))
        self.wait()
        for p in proofs:
            self.play(Write(p))
        self.wait(5)