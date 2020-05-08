'''
@Author       : Jin Yuhan
@Date         : 2020-05-02 22:01:34
@LastEditors  : Jin Yuhan
@LastEditTime : 2020-05-02 23:12:38
@Description  : 字幕
'''

class Captions:
    """ 用于保存字幕 """
    
    def __init__(self, *captions):
        self.captions = captions
        self.index = -1
        
    def get(self, count=1, move_index=True, single_value_if_possible=True):
        """ 获取接下来的count个字幕 """
        
        if count <= 0:
            raise IndexError('count必须是正整数')
        
        if self.index + count >= len(self.captions):
            raise IndexError('字幕已经到达尽头o(╥﹏╥)o')
        
        self.index += count
        result = self.captions[self.index] if count ==1 and single_value_if_possible \
                else self.captions[self.index - count + 1 : self.index + 1]
        # 这里懒得改了，后加的
        if not move_index:
            self.index -= count
        return result
    
    def get_remaining_count(self) -> int:
        return len(self.captions) - self.index - 1
    
    def reset(self):
        self.index = -1
        
    def __len__(self):
        return len(self.captions)
        
    def __getitem__(self, index):
        return self.captions[index]
    
    def __setitem__(self, index, value):
        self.captions[index] = value