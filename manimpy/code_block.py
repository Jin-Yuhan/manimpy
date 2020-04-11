"""
表示一个代码块
"""

from manimlib.imports import *


class CodeBlock(Text):
    """
    表示一个代码块
    """

    CONFIG = {
        'font': 'Consolas',
        'size': 0.5,
        'color': WHITE,
        'stroke_color': WHITE,
        'stroke_weight': 0,
        'line_number_color': GRAY,
        "t2c": {}
    }

    def __init__(self, *lines: str, **config):
        digest_config(self, config)

        text = ''
        i = 1

        for line in lines:
            lines1 = line.split('\n')
            text += CodeBlock.get_lines_text(i, lines1)
            i += len(lines1)

        super().__init__(text, **config)
        self.set_stroke(self.stroke_color, self.stroke_weight)

    @staticmethod
    def get_lines_text(i, lines):
        text = ''
        for line in lines:
            line_no = str(i)
            text += ''.join([' ' for _ in range(4 - len(line_no))]) + line_no + ' ' + line + '\n'
            i += 1
        return text

    def set_color_by_t2c(self, t2c=None):
        super().set_color_by_t2c(t2c)

        if len(self) > 5:
            self[0:5].set_color(self.line_number_color)
            for _, end in self.find_indexes('\n'):
                self[end:end+5].set_color(self.line_number_color)


class WriteCodeBlock(ShowIncreasingSubsets):
    def __init__(self, code_block: CodeBlock, **kwargs):
        new_group = Group(*code_block)
        super().__init__(new_group, **kwargs)

    def update_submobject_list(self, index):
        self.mobject.submobjects = self.all_submobs[:index]

