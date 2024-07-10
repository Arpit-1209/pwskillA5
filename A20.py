from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import LinearColorMapper, ColorBar
from bokeh.transform import transform
import numpy as np

output_notebook()

data_heatmap = np.random.rand(10, 10)
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
xx, yy = np.meshgrid(x, y)

mapper = LinearColorMapper(palette='Viridis256', low=data_heatmap.min(), high=data_heatmap.max())

p = figure(title="Heatmap")
p.image(image=[data_heatmap], x=0, y=0, dw=1, dh=1, color_mapper=mapper)

color_bar = ColorBar(color_mapper=mapper, location=(0, 0))
p.add_layout(color_bar, 'right')

show(p)
