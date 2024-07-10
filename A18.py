from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource, FactorRange

output_notebook()

fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

p = figure(x_range=fruits, title="Fruit Counts", toolbar_location=None, tools="")
p.vbar(x='fruits', top='counts', width=0.9, source=source, legend_field="fruits",
       line_color='white', fill_color=factor_cmap('fruits', palette=['#718dbf', '#e84d60', '#ddb7b1', '#c9d9d3'], factors=fruits))

p.y_range.start = 0
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)
