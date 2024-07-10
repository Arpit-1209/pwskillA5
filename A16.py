import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()

x = np.linspace(0, 10, 100)
y = np.sin(x)

p = figure(title='Sine Wave')
p.line(x, y, line_width=2)

show(p)
