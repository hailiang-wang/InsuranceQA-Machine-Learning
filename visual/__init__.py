#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/InsuranceQA-Machine-Learning/deep_qa_1/visual.py
# Author: Hai Liang Wang
# Date: 2017-08-09:21:56:58
#
#===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-08-09:21:56:58"


import os
import sys
import numpy as np
from scipy.interpolate import spline
from scipy.interpolate import interp1d
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(curdir))

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# style.use('fivethirtyeight')
style.use(["ggplot", os.path.join(curdir, "tensorflowvisu.mplstyle")])
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('loss')
ax1.set_ylabel('steps')

graph_data_f = os.path.join(curdir, '..', 'tmp', 'example1.txt')

def init_graph_data():
    with open(graph_data_f, "w") as f:
        f.write('')

def append_graph_data(line):
    with open(graph_data_f, "a") as f:
        f.write('%s\n' % line)

def animate(i):
    xs = []
    ys = []
    graph_data = open(graph_data_f,'r').read()
    lines = graph_data.split('\n')
    for line in lines:
        o = line.split()
        if len(line) > 1 and len(o) == 2:
            xs.append(o[0])
            ys.append(o[1])
    # https://stackoverflow.com/questions/25825946/generating-smooth-line-graph-using-matplotlib
    # x_sm = np.array(xs).astype(np.float)
    # y_sm = np.array(ys).astype(np.float)
    # f = interp1d(x_sm, y_sm)
    # x_smooth = np.linspace(x_sm.min(), x_sm.max(), 600)
    # y_smooth = spline(xs, ys, x_smooth)
    # ax1.plot(x_smooth, y_smooth, linewidth=1)
    ax1.clear()
    ax1.plot(xs, ys, linewidth=1)

def test_draw():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

if __name__ == '__main__':
    test_draw()
