#! /usr/bin/env python3
"""
Anscombe's quartet

- Create Anscombe's quartet of four graphs as four axes in one figure.
- Create Anscombe's quartet of four graphs as four separate figures.
"""

from typing import List, NoReturn, Tuple

from numpy.polynomial import polynomial as nppoly
import matplotlib.pyplot as plt
import matplotlib.axes as axes
from itertools import chain
import datasense as ds
import pandas as pd


def main():
    # define parameters
    ax_title = [('Data set I', 'Data set II'), ('Data set III', 'Data set IV')]
    axs = (('ax1', 'ax2'), ('ax3', 'ax4'))
    output_url = 'anscombes_quartet.html'
    header_title = "Anscombe's Quartet"
    fig_title = "Anscombe's Quartet"
    header_id = 'anscombes-quartet'
    colour1 = '#0077bb'
    colour2 = '#33bbee'
    figsize = [8, 6]
    xlabel = 'X'
    ylabel = 'Y'
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    aq1, aq2, aq3, aq4 = load_data()
    dfs = ((aq1, aq2), (aq3, aq4))
    combinations = tuple(zip(chain(*axs), chain(*dfs), chain(*ax_title)))
    plot_many_in_one(
        df=dfs,
        axs=axs,
        fig_title=fig_title,
        xlabel=xlabel,
        ylabel=ylabel,
        figsize=figsize,
        colour1=colour1,
        colour2=colour2
    )
    # plot each data set as a separate graph
    for ax, df, ax_title in combinations:
        fig, ax = ds.plot_scatter_x_y(
            X=df['x'],
            y=df['y'],
            colour=colour1
        )
        fig.suptitle(
            t=fig_title,
            fontweight='bold'
        )
        b, m = nppoly.polyfit(df['x'], df['y'], 1)
        ax.plot(
            df['x'],
            m*df['x'] + b,
            '-',
            color=colour2
        )
        ax.set_ylim(
            bottom=2,
            top=13
        )
        ax.set_xlim(
            left=3,
            right=15
        )
        ax.set_title(label=ax_title)
        ax.set_ylabel(ylabel=ylabel)
        ax.set_xlabel(xlabel=xlabel)
        ds.despine(ax=ax)
        fig.savefig(fname=f'{"_".join(ax_title.split()).lower()}.svg')
        ds.html_figure(file_name=f'{"_".join(ax_title.split()).lower()}.svg')
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


def load_data() -> Tuple[pd.DataFrame]:
    '''
    Load data into separate dataframes.
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
    return (aq1, aq2, aq3, aq4)


def plot_many_in_one(
    *,
    df: pd.DataFrame,
    axs: axes.Axes,
    fig_title: str,
    xlabel: str,
    ylabel: str,
    figsize: List[float],
    colour1: str,
    colour2: str
) -> NoReturn:
    '''
    Plot each graph in an axes within a figure.
    '''
    fig = plt.figure(figsize=(figsize))
    fig, axs = plt.subplots(
        nrows=2,
        ncols=2,
        sharex=True,
        sharey=True
    )
    fig.suptitle(
        t=fig_title,
        fontweight="bold"
    )
    # axs = ((ax1, ax2), (ax3, ax4))
    combinations = tuple(zip(chain(*axs), chain(*df)))
    for axx, dff in combinations:
        axx.scatter(
            dff['x'],
            dff['y'],
            color=colour1,
            linewidth=0,
            linestyle="-",
            s=10,
            label="I"
        )
        b, m = nppoly.polyfit(dff['x'], dff['y'], 1)
        axx.plot(dff['x'], m*dff['x'] + b, '-', color=colour2)
        axx.set_ylim(
            bottom=2,
            top=13
        )
        axx.set_xlim(
            left=3,
            right=15
        )
        # axx.set_title(label=ax_title[i][j])
        axx.set_xlabel(xlabel=xlabel)
        axx.set_ylabel(ylabel=ylabel)
        ds.despine(ax=axx)
    fig.savefig(fname='aq.svg')
    ds.html_figure(file_name='aq.svg')


if __name__ == '__main__':
    main()
