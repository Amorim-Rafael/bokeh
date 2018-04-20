# from bokeh.io import output_notebook, show
# from bokeh.plotting import figure

# output_notebook()

from bokeh.io import output_file, show
from bokeh.plotting import figure

fg = figure(x_axis_label='x_axis', y_axis_label='y_axis')

x=[1,2,3,4]
y=[1,2,3,4]

fg.circle(x,y)
output_file('basic.html')
show(fg)