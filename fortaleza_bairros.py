# Link de onde tirei os exemplos
# https://stackoverflow.com/questions/40226189/bokeh-is-not-rendering-properly-multipolygon-islands-from-geojson
# http://bokeh.pydata.org/en/0.11.1/docs/user_guide/geo.html

from bokeh.io import show, output_notebook, output_file
from bokeh.models import (GeoJSONDataSource,HoverTool,LinearColorMapper)
from bokeh.plotting import figure
from bokeh.palettes import Viridis6

with open(r'fortaleza_bairros.json', 'r') as f:
    geo_source = GeoJSONDataSource(geojson=f.read())

color_mapper = LinearColorMapper(palette=Viridis6)

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="Fortaleza Bairros", tools=TOOLS, x_axis_location=None, y_axis_location=None, width=800, height=800)
p.grid.grid_line_color = None

p.patches('xs', 'ys', fill_alpha=0.7, line_color='white', fill_color={'field': 'REGIONAL', 'transform': color_mapper}, line_width=0.5, source=geo_source)

hover = p.select_one(HoverTool)
hover.tooltips = [("Bairro:", "@NOME"),("Regional:", "@REGIONAL")]

output_file("fortaleza_bairros.html")
show(p)