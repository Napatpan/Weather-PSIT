import pandas as pd
import pygal
from pygal.style import RedBlueStyle

def chart():
    """ 2559 """
    data = pd.read_csv("2559.csv")
    line_chart = pygal.Bar(fill=True, interpolate='cubic', style=RedBlueStyle)
    line_chart.title = '2559'
    line_chart.x_labels = data.month
    line_chart.y_labels = map(int, range(0, 501, 25))
    line_chart.add('Maxtemp', data.maxtemp)
    line_chart.add('Mintemp', data.mintemp)
    line_chart.add('Water', data.water)
    line_chart.add('Rainday', data.rainday)
    line_chart.render_to_file("G2559.svg")
chart()
