from bokeh.io import show, output_notebook, output_file
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper
)
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
# hover.point_policy = "follow_mouse"
hover.tooltips = [("Bairro:", "@NOME"),("Regional:", "@REGIONAL")]

output_file("fortaleza_bairros.html")
show(p)

# map_options = GMapOptions(lat=-3.7318616, lng=-38.5266704, map_type="roadmap", zoom=11)

# p = gmap("AIzaSyDwd7ijPklG7RTlJh3WPTNXe6K6sbTHGiA", map_options, title="")

# p.grid.grid_line_color = None
# color_mapper = LogColorMapper(palette=palette)

# p.patches('x', 'y', source=geo_source,
#           fill_color={'field': 'rate', 'transform': color_mapper},
#           fill_alpha=0.7, line_color="white", line_width=0.5)

# show(p)