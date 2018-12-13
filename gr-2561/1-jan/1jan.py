import pandas as pd
import pygal
from pygal.style import RedBlueStyle

def chart():
    """ Jan """
    data = pd.read_csv("1-january.csv")
    line_chart = pygal.Bar(fill=True, interpolate='cubic', style=RedBlueStyle)
    line_chart.title = 'January 2018'
    line_chart.x_labels = data.day
    line_chart.y_labels = map(int, range(0, 50, 1))
    line_chart.add('Maxtemp', data.Max)
    line_chart.add('Mintemp', data.Min)
    line_chart.render_to_file("1jan.svg")
chart()
