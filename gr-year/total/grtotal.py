import pandas as pd
import pygal
from pygal.style import RedBlueStyle

def chart():
    """ Total """
    data = pd.read_csv("total.csv")
    line_chart = pygal.Bar(fill=True, interpolate='cubic', style=RedBlueStyle)
    line_chart.title = 'Total'
    line_chart.x_labels = data.years
    line_chart.y_labels = map(int, range(0, 2601, 500))
    line_chart.add('Maxtemp', data.maxtemp)
    line_chart.add('Mintemp', data.mintemp)
    line_chart.add('Water', data.water)
    line_chart.add('Rainday', data.rainday)
    line_chart.render_to_file("total.svg")
chart()
