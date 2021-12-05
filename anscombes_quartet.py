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
figsize = [8, 6]
colour1 = '#0077bb'
colour2 = '#33bbee'


def main():
    output_url = 'anscombes_quartet.html'
    header_title = 'anscombes_quartet'
    header_id = 'anscombes-quarter'
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    aq1, aq2, aq3, aq4 = load_data()
    df = [(aq1, aq2), (aq3, aq4)]
    plot_four_in_one(df)
    plot_one_in_four(df)
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


def plot_scatter(dfx, dfy, i, j):
    '''
    Plot each Anscombe Quartet graph in a figure by itself.
    '''
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    fig.suptitle(
        t=fig_title,
        fontweight='bold'
    )
    ax.scatter(dfx, dfy,
               color=colour1, linewidth=0,
               linestyle="-", s=10, label="I")
    b, m = nppoly.polyfit(dfx, dfy, 1)
    ax.plot(dfx, m*dfx + b, '-', color=colour2)
    ax.set_ylim(
        bottom=2,
        top=14
    )
    ax.set_xlim(
        left=2,
        right=20
    )
    ax.set_title(label=ax_title[i][j])
    ax.set_ylabel(ylabel=yaxislabel)
    ax.set_xlabel(xlabel=xaxislabel)
    ds.despine(ax)
    return ax


def load_data():
    '''
    Load the Anscombe Quartet data into separate dataframes.
    '''
    data_aq1 = {
        'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'y': [
            8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68
        ]
    }
    data_aq2 = {
        'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'y': [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]
    }
    data_aq3 = {
        'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'y': [
            7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73
        ]
    }
    data_aq4 = {
        'x': [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
        'y': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]
    }
    aq1 = pd.DataFrame(data=data_aq1)
    aq2 = pd.DataFrame(data=data_aq2)
    aq3 = pd.DataFrame(data=data_aq3)
    aq4 = pd.DataFrame(data=data_aq4)
    return aq1, aq2, aq3, aq4


def plot_one_in_four(df):
    '''
    Plot each Anscombe Quartet graph in a figure by itself.
    '''
    for i in range(2):
        for j in range(2):
            plot_scatter(df[i][j]['x'], df[i][j]['y'], i, j)
            plt.savefig(fname=f'aq{i}{j}.svg')
            ds.html_figure(file_name=f'aq{i}{j}.svg')


def plot_four_in_one(df):
    '''
    Plot each Anscombe Quartet graph in an axes within a figure.
    '''
    fig = plt.figure(figsize=(figsize))
    fig.suptitle(
        t=fig_title,
        fontweight="bold"
    )
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
            ax.set_ylim(
                bottom=2,
                top=14
            )
            ax.set_xlim(
                left=2,
                right=20
            )
            ax.set_title(label=ax_title[i][j])
            ax.set_ylabel(ylabel=yaxislabel)
            ax.set_xlabel(xlabel=xaxislabel)
            ds.despine(ax)
    plt.tight_layout(pad=3)
    plt.savefig(fname='aq.svg')
    ds.html_figure(file_name='aq.svg')


if __name__ == '__main__':
    main()
