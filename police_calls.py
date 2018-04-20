import os
import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool, BoxZoomTool
from bokeh.plotting import gmap

output_file("police_calls.html")

map_options = GMapOptions(lat=-3.7318616, lng=-38.5266704, map_type="roadmap", zoom=11)

p = gmap("AIzaSyDwd7ijPklG7RTlJh3WPTNXe6K6sbTHGiA", map_options, title="")

def load_csv():
    crimes = pd.read_csv('policecalls.csv')
    return crimes

local_crimes = load_csv()
local_crimes.head()

source = ColumnDataSource(
    data=dict(
        lat=local_crimes.lat.tolist(),
        lon=local_crimes.lng.tolist(),
        type=local_crimes.type.tolist()
    )
)

hover = HoverTool(tooltips = [('Tipo crime:', '@type')])

p.add_tools(hover)
p.circle(x="lon", y="lat", size=10, fill_color="blue", fill_alpha=0.8, source=source)

show(p)