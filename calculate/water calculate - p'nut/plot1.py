import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot, plot

# read
df = pd.read_csv('./csvmn.csv')
cols = df.columns
summary = pd.DataFrame(df.mean()).T

# image 1
data = [
    go.Table(
        header = dict(
            values=list(cols),
            fill = dict(color='#C2D4FF'),
            align = ['left'] * 5
        ),
        cells=dict(
            values=[df[col] for col in cols],
            fill = dict(color='#F5F8FF'),
            align = ['left'] * 5
        )
    )
]
layout = go.Layout(title='Table')
fig = go.Figure(data, layout=layout)
plot(data, filename='fig1.html')

# image 2
data = [
    go.Table(
        header = dict(
            values=list(summary.columns),
            fill = dict(color='#C2D4FF'),
            align = ['left'] * 5
        ),
        cells=dict(
            values=[summary[col] for col in summary.columns],
            fill = dict(color='#F5F8FF'),
            align = ['left'] * 5
        )
    )
]
layout = go.Layout(title='Summary')
fig = go.Figure(data, layout=layout)
plot(data, filename='fig2.html')

