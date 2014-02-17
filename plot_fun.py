#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math

def plot_fun(func,begin = 0.,end = 1., width=20, height=10, only_return = False):
    x_chr = np.arange(width)
    y_chr = np.arange(height)
    x = begin + (end - begin) * np.hstack([x_chr,[width]]) / float(width)
    y = np.array(map(func,x))

    y_min = np.min(y)
    y_max = np.max(y)

    # initialize char grid
    grid=[]
    for i in range(height):
        grid.append([' ']*width)

    # plot function into char grid
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

    ### string auxiliary functions

    # align two texts in a given length of string
    def align_left_and_right(left,right,width,padding=1):
        if width-len(left)-len(right)+padding > 0:
            return left+' ' * (width-len(left)-len(right)+padding) + right
        else:

            width_minus_padding = width-padding
            width_for_left = int(width_minus_padding/2) 
            width_for_right = width_minus_padding - width_for_left
            return left[:width_for_left] + ' ' * padding + right[:width_for_right]

    # string representation of a point given by tuple
    def str_point(point):
        return ';'.join(map(str,list(point)))


    # build resulting string
    lines = []
    lines.append(align_left_and_right(str_point((begin,y_max)),str_point((end,y_max)),width))
    lines.extend( map(lambda arr: "".join(arr),grid) )
    lines.append(align_left_and_right(str_point((begin,y_min)),str_point((end,y_min)),width))

    # convert to string
    string = "\n".join(lines)

    # print 
    if not only_return:
        print string

    return string

if __name__ == '__main__':
    plot_fun(lambda x: math.sin(x),begin=0,end=1*1*math.pi,width=80,height=10)
