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


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    Used to enforce standard and *correct* style. There is only one x,
    and one y axis, left and bottom, therefore there should only be
    these axes.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def plot_scatter(dfx, dfy, i, j):
    fig, ax = plt.subplots(figsize=(fighw))
    fig.suptitle(fig_title, fontweight="bold")
    ax.scatter(dfx, dfy, color=c[0], lw=0, ls="-", s=10, label="I")
    b, m = nppoly.polyfit(dfx, dfy, 1)
    ax.plot(dfx, m*dfx + b, '-', color=c[1])
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
    ax.set_title(ax_title[i][j])
    ax.set_ylabel(yaxislabel)
    ax.set_xlabel(xaxislabel)
    despine(ax)
    return ax


def read_files():
    aq1 = pd.read_csv('aq1.csv')
    aq2 = pd.read_csv('aq2.csv')
    aq3 = pd.read_csv('aq3.csv')
    aq4 = pd.read_csv('aq4.csv')
    return aq1, aq2, aq3, aq4


def plot_one_in_four(df):
    for i in range(2):
        for j in range(2):
            plot_scatter(df[i][j]['x'], df[i][j]['y'], i, j)
            plt.savefig(f'aq{i}{j}.svg')


def plot_four_in_one(df):
    fig = plt.figure(figsize=(fighw))
    fig.suptitle(fig_title, fontweight="bold")
    gs = GridSpec(2, 2, figure=fig)
    for i in range(2):
        for j in range(2):
            ax = fig.add_subplot(gs[i, j])
            ax.scatter(df[i][j]['x'], df[i][j]['y'], color=c[0], linewidth=0,
                       linestyle="-", s=10, label="I")
            b, m = nppoly.polyfit(df[i][j]['x'], df[i][j]['y'], 1)
            ax.plot(df[i][j]['x'], m*df[i][j]['x'] + b, '-', color=c[1])
            ax.set_ylim(ylim)
            ax.set_xlim(xlim)
            ax.set_title(ax_title[i][j])
            ax.set_ylabel(yaxislabel)
            ax.set_xlabel(xaxislabel)
            despine(ax)
    plt.tight_layout(pad=3)
    plt.savefig('aq.svg')


if __name__ == '__main__':
    fig_title = "Anscombe's Quartet"
    ax_title = [('Data set I', 'Data set II'), ('Data set III', 'Dataset IV')]
    yaxislabel = 'Y'
    xaxislabel = 'X'
    xlim = [2, 20]
    ylim = [2, 14]
    fighw = [8, 6]
    c = cm.Paired.colors
    aq1, aq2, aq3, aq4 = read_files()
    df = [(aq1, aq2), (aq3, aq4)]
    plot_four_in_one(df)
    plot_one_in_four(df)
