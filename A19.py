from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
import numpy as np

output_notebook()

data_hist = np.random.randn(1000)
hist, edges = np.histogram(data_hist, bins=30)

p = figure(title="Histogram")
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="navy", line_color="white", alpha=0.5)

show(p)
