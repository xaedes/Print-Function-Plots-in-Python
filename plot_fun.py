#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math



# sparks = ['▁','▂','▃','▄','▅','▆','▇','█']


# def getSparks( numbers ):
#     maximum = max(numbers)
#     minimum = min(numbers)

#     div = float(maximum - minimum)
#     if div == 0:
#         div = 1
#     return ''.join( sparks[int((n - minimum)/div * 7)] for n in numbers)


# def stringToNumberList( string ):
#     numbers = []
#     for n in string:
#         try:
#             numbers.append(float(n))
#         except ValueError:
#             pass
#     return numbers

def plot_fun(func,begin = 0.,end = 1., width=20, height=10, only_return = False):
    x_chr = np.arange(width)
    y_chr = np.arange(height)
    x = begin + (end - begin) * np.hstack([x_chr,[width]]) / float(width)
    y = np.array(map(func,x))
    # print getSparks(list(y))
    # print "foo"

    y_min = np.min(y)
    y_max = np.max(y)

    grid=[]
    for i in range(height):
        grid.append([' ']*width)
    # print y_min
    # print y_max
    for i in range(width):
        y_norm = (y[i]-y_min) / (y_max-y_min)
        y_chr_idx = int(math.floor((1-y_norm) * (height-1)))

        diff = y[i+1] - y[i]
        # print y_norm
        char='*'
        diff_norm = diff/((y_max-y_min)/height)
        if abs(diff_norm)<0.5:
            char = '-'
        elif diff>0:
            char = '/'
        elif diff<0:
            char = '\\'
        grid[y_chr_idx][i] = char

    # xs, ys = meshgrid(x_chr, y)
    # bounds = map(lambda grid_line: map(lambda grid_cell,grid_line),grid)

    def align_left_and_right(left,right,width,padding=1):
        if width-len(left)-len(right)+padding > 0:
            return left+' ' * (width-len(left)-len(right)+padding) + right
        else:

            width_minus_padding = width-padding
            width_for_left = int(width_minus_padding/2) 
            width_for_right = width_minus_padding - width_for_left
            return left[:width_for_left] + ' ' * padding + right[:width_for_right]

    def str_point(point):
        return ';'.join(map(str,list(point)))

    lines = []
    lines.append(align_left_and_right(str_point((begin,y_max)),str_point((end,y_max)),width))
    lines.extend( map(lambda arr: "".join(arr),grid) )
    lines.append(align_left_and_right(str_point((begin,y_min)),str_point((end,y_min)),width))

    string = "\n".join(lines)

    if not only_return:
        print string

    return string

if __name__ == '__main__':
    fun = lambda dt_now, self_dt: pow(1./2000.,abs(dt_now - self_dt))
    fun2 = lambda x: fun(dt_now=x+0.0,self_dt=0.0)


    plot_fun(lambda x: math.sin(x),begin=0,end=1*1*math.pi,width=80,height=10)
    # plot_fun(math.sin,end=0.5,width=80,height=30)
    # plot_fun(fun2,end=0.5,width=40,height=10)