#! /usr/bin/env python3


'''
Anscombe's quartet

- Create Anscombe's quartet of four graphs as four axes in one figure.
- Create Anscombe's quartet of four graphs as four separate figures.

./anscombes_quartet.py
'''


import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as nppoly
import matplotlib.cm as cm
import matplotlib.axes as axes
from matplotlib.gridspec import GridSpec


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    Used to enforce standard and *correct* style. There is only one x,
    and one y axis, left and bottom, therefore there should only be
    these axes.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


