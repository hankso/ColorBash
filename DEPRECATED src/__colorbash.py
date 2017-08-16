#!/usr/bin/python
#-*- coding: utf-8 -*-


'''
ColorBash is a class for colorful output in bash.
Use ColorBash.c(text, color) function to generate string containing colorful info
See details in ColorBash.colorize.__doc__()

Copyright 2017 Hankso
This module is distributed under the term of GNU General Public License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


'''
\33[0m 关闭所有属性 
1 设置高亮度 
2 设置低亮度
3 斜体
4 下划线 
5 闪烁
7 反显
8 消隐

设置前景色 
30:黑 
31:红 
32:绿 
33:黄 
34:蓝色 
35:紫色 
36:深绿 
37:白色 

设置背景色 
40:黑 
41:深红 
42:绿 
43:黄色 
44:蓝色 
45:紫色 
46:深绿 
47:白色 

黑底彩色 
90:黑 
91:深红 
92:绿 
93:黄色 
94:蓝色 
95:紫色 
96:深绿 
97:白色 

nA 光标上移n行 
nB 光标下移n行 
nC 光标右移n行 
nD 光标左移n行 
y;xH设置光标位置 
2J 清屏 
K 清除从光标到行尾的内容 
s 保存光标位置 
u 恢复光标位置 
?25l 隐藏光标 
?25h 显示光标
'''



_colorshead = '\33[{}{}m'
_colorslist = ['black', 'red', 'green', 'brown', 'blue', 'purple', 'cyan', 'white']

_effecthead = '\33[{}'
_effectdict = {'default':'0m', 'bold':'1m',      'higherlight':'2m', 'lowerlight':'2m',
               'italic':'3m',  'underline':'4m', 'inverse':'7m',     'syncolor':'8m',
               'up':'1A',      'down':'1B',      'left':'1D',        'right':'1C',
               'clear':'2J',   'clr2end':'K'}

def colorize(text = None,
             color = None,
             bg = False,
             effects = [],
             blackback = True):
    '''
    Make your output in bash colorful
    
    Parameters
    ----------
    text   :str or number or anything
            Message to output
            
    color  :str, color name in lowercase, lowercase, lowercase!
            black, red, green, brown, blue, purple, cyan, white
            
    bg     :boolean, default False
            True  :specialized color is for background color
            False :specialized color is for font color
            
    effects:list of str, special effects on text and curser. Different effects may mix toghter, and command to move curser may be repeated.
            underline
            italic
            bold
            higherlight
            lowerlight
            inverse (inverse color)
            up (move curser 1 line up)
            down
            left (move curser 1 character left)
            right
            clear (clear the screen)
            clr2end (clear screen from curser to the end of the line)
            syncolor (output will has same color with background,only activited when bg = True)
            
    blackback:False if your bash background color is white (e.g. MacOS shell)
            default black, like Ubuntu bash or Windows cmd
            
    Examples
    --------
    In [1]: print(colorize(effects = ['underline']) +
                  colorize(text = '~'*17) +
                  colorize(text = 'ColorBash', effects = ['left']*14+['bold']) +
                  colorize(effects = ['right']*3+['clr2end']))
                  
    Out[1]: ~~~ColorBash~~~
    '''

    try:
        effect_part = ''
        if effects.__len__():
            for effect in effects:
                if _effectdict.has_key(effect):
                    effect_part += _effecthead.format(_effectdict[effect])                    
    except BaseException, e:
        print e
        print('Effects must be a list of str, see help(colorize)')
    
    try:
        if color:
            temp = 3
            if bg:
                temp = 4
            if blackback:
                temp = 9
            if _colorslist.count(color):
                color_part = _colorshead.format(temp, _colorslist.index(color))
        else:
            color_part = ''
    except BaseException, e:
        print e
        print('Color must be lowercase str of color name, see help(colorize)')
        
    return effect_part + color_part + (str(text) if text else '')
