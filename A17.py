from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
import numpy as np

output_notebook()

x = np.random.random(100)
y = np.random.random(100)
sizes = np.random.randint(10, 30, 100)
colors = np.random.choice(['blue', 'red', 'green', 'yellow'], 100)

source = ColumnDataSource(data=dict(x=x, y=y, sizes=sizes, colors=colors))

p = figure(title='Scatter Plot')
p.scatter('x', 'y', size='sizes', color='colors', source=source)

show(p)
