#! /usr/bin/env python3
"""
Create grid of Anscombe's quarter of scatter plots.
Use LaTeX to show equation in legend.
Label figure, axes.
Title figure, axes.
"""

from pathlib import Path
from typing import Tuple

from numpy.polynomial import polynomial as nppoly
import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd


def main():
    axes_title = ["Data set 1", "Data set 2", "Data set 3", "Data set 4"]
    left, right, top, bottom = 2, 20, 14, 2
    output_url = "anscombes_quartet.html"
    x_axis_label = "X axis label (units)"
    y_axis_label = "Y axis label (units)"
    header_title = "Anscombe’s Quartet"
    fig_title = "Anscombe’s Quartet"
    header_id = "anscombes-quartet"
    colour_blue = "#0077bb"
    colour_cyan = "#33bbee"
    figsize = (12, 9)
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    ds.style_graph()
    df1, df2, df3, df4 = create_dataframe()
    fig = plt.figure(figsize=figsize)
    fig.suptitle(t=fig_title)
    for index in range(1, 5):
        df = eval(f"df{index}")
        ax = fig.add_subplot(2, 2, index)
        ax.plot(df["x"], df["y"], linestyle="", color=colour_blue)
        b, m = nppoly.polyfit(df["x"], df["y"], 1)
        equation = f"$y = {b:.1f} + {m:.1f}x$"
        ax.plot(
            df["x"], m * df["x"] + b, marker="",
            color=colour_cyan, label=equation
        )
        ax.set_ylim(bottom=bottom, top=top)
        ax.set_xlim(left=left, right=right)
        ax.set_title(label=f"{axes_title[index-1]}")
        ax.set_ylabel(ylabel=y_axis_label)
        ax.set_xlabel(xlabel=x_axis_label)
        ax.legend(frameon=False)
        ds.despine(ax=ax)
    plt.tight_layout(pad=3)
    fig.savefig(fname="anscombes_quartet.svg", format="svg")
    ds.html_figure(file_name="anscombes_quartet.svg")
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


def create_dataframe() -> Tuple[pd.DataFrame]:
    """
    Load data into separate dataframes.

    Returns
    -------
    df1, df2, fd3, df4 : Tuple[pd.DataFrame]
    """
    data_aq1 = {
        "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        "y": [
            8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68
        ],
    }
    data_aq2 = {
        "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        "y": [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74],
    }
    data_aq3 = {
        "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        "y": [
            7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73
        ],
    }
    data_aq4 = {
        "x": [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
        "y": [
            6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89
        ],
    }
    df1 = pd.DataFrame(data=data_aq1)
    df2 = pd.DataFrame(data=data_aq2)
    df3 = pd.DataFrame(data=data_aq3)
    df4 = pd.DataFrame(data=data_aq4)
    return (df1, df2, df3, df4)


if __name__ == "__main__":
    main()
