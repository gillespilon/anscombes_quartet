#! /usr/bin/env python3
"""
Anscombe's quartet

- Create Anscombe's quartet of four graphs as four axes in one figure.
- Create Anscombe's quartet of four graphs as four separate figures.

./anscombes_quartet.py
"""

from numpy.polynomial import polynomial as nppoly
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import datasense as ds
import pandas as pd

fig_title = "Anscombe's Quartet"
ax_title = [('Data set I', 'Data set II'), ('Data set III', 'Dataset IV')]
yaxislabel = 'Y'
xaxislabel = 'X'
xlim = [2, 20]
ylim = [2, 14]
figsize = [8, 6]
colour1 = '#0077bb'
colour2 = '#33bbee'


def main():
    aq1, aq2, aq3, aq4 = read_files()
    df = [(aq1, aq2), (aq3, aq4)]
    plot_four_in_one(df)
    plot_one_in_four(df)


def plot_scatter(dfx, dfy, i, j):
    '''
    Plot each Anscombe Quartet graph in a figure by itself.
    '''
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    fig.suptitle(fig_title, fontweight='bold')
    ax.scatter(dfx, dfy,
               color=colour1, linewidth=0,
               linestyle="-", s=10, label="I")
    b, m = nppoly.polyfit(dfx, dfy, 1)
    ax.plot(dfx, m*dfx + b, '-', color=colour2)
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
    ax.set_title(ax_title[i][j])
    ax.set_ylabel(yaxislabel)
    ax.set_xlabel(xaxislabel)
    ds.despine(ax)
    return ax


def read_files():
    '''
    Read each of the Anscombe Quartet data files into a separate dataframe.
    '''
    aq1 = pd.read_csv('aq1.csv')
    aq2 = pd.read_csv('aq2.csv')
    aq3 = pd.read_csv('aq3.csv')
    aq4 = pd.read_csv('aq4.csv')
    return aq1, aq2, aq3, aq4


def plot_one_in_four(df):
    '''
    Plot each Anscombe Quartet graph in a figure by itself.
    '''
    for i in range(2):
        for j in range(2):
            plot_scatter(df[i][j]['x'], df[i][j]['y'], i, j)
            plt.savefig(fname=f'aq{i}{j}.svg')


def plot_four_in_one(df):
    '''
    Plot each Anscombe Quartet graph in an axes within a figure.
    '''
    fig = plt.figure(figsize=(figsize))
    fig.suptitle(fig_title, fontweight="bold")
    gs = GridSpec(2, 2, figure=fig)
    for i in range(2):
        for j in range(2):
            ax = fig.add_subplot(gs[i, j])
            ax.scatter(
                df[i][j]['x'],
                df[i][j]['y'],
                color=colour1,
                linewidth=0,
                linestyle="-",
                s=10,
                label="I"
            )
            b, m = nppoly.polyfit(df[i][j]['x'], df[i][j]['y'], 1)
            ax.plot(df[i][j]['x'], m*df[i][j]['x'] + b, '-', color=colour2)
            ax.set_ylim(ylim)
            ax.set_xlim(xlim)
            ax.set_title(ax_title[i][j])
            ax.set_ylabel(yaxislabel)
            ax.set_xlabel(xaxislabel)
            ds.despine(ax)
    plt.tight_layout(pad=3)
    plt.savefig(fname='aq.svg')


if __name__ == '__main__':
    main()
