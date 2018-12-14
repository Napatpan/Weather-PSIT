import pandas as pd
import pygal
from pygal.style import RedBlueStyle

def tabless():
    """ years """
    data = pd.read_csv("csvmn.csv")
    line_chart = pygal.Bar(fill=True, interpolate='cubic', style=RedBlueStyle)
    line_chart.title = 'Average weather in a years'
    line_chart.x_labels = data.month
    line_chart.y_labels = map(int, range(0, 611, 25))
    line_chart.add('2504 - 2524', data.year1)
    line_chart.add('2524 - 2553', data.year2)
    line_chart.add('2552', data.year3)
    line_chart.add('2553', data.year4)
    line_chart.add('2554', data.year5)
    line_chart.add('2555', data.year6)
    line_chart.add('2556', data.year7)
    line_chart.add('2557', data.year8)
    line_chart.add('2558', data.year9)
    line_chart.add('2559', data.year10)
    line_chart.add('2560', data.year11)
    line_chart.render_to_file("years.svg")

tabless()
