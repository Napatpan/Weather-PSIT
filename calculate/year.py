import pandas as pd
import pygal
from pygal.style import RedBlueStyle
def chart():
    """ years """
    data = pd.read_csv("2504_2533n.csv")
    line_chart = pygal.Bar(fill=True, interpolate='cubic', style=RedBlueStyle)
    line_chart.title = 'Average weather in a year 2504-2533'
    line_chart.x_labels = map('Month', [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec])
    line_chart.add('Maxtemp', [32, 32.7, 33.7, 34.9, 34, 33.1, 32.7, 32.5, 32.3, 32, 31.6, 31.3])
    line_chart.add('Mintemp', [21, 23.3, 24.9, 26.1, 25.6, 25.4, 25, 24.9, 24.6, 24.3, 23.1, 20.8])
    line_chart.add('Water', [9.1, 29.9, 28.6, 64.7, 220.4, 149.3, 154.5, 196.7, 344.2, 241.6, 48.1, 9.7])
    line_chart.add('rainday', [1, 3, 3, 6, 16, 16, 18, 20, 21, 17, 6, 1])
    line_chart.value_formatter = lambda x: '%.2f%%' % x if x is not None else '∅'
    line_chart.render_table(style=True, total=True, transpose=True)
    line_chart.render_to_file("T2504-2533.svg")
chart()
