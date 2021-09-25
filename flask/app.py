from bokeh.embed import components
from bokeh.models import (FactorRange, LinearAxis, Grid,
                          Range1d)
from bokeh.models.glyphs import VBar
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure
from flask import Flask, render_template

from utils.json_utils import read_from_json

app = Flask(__name__)


@app.route("/graph")
def chart():

    current = read_from_json("access_points.json")["access_points"]

    data = {"ssid": [], "snr": [], "channel": []}
    for i in range(0, len(current)):
        data['ssid'].append(current[i]["ssid"])
        data['snr'].append(current[i]["snr"])
        data['channel'].append(current[i]["channel"])

    plot = create_bar_chart(data, "WirelessAPs Bar Chart", "ssid", "snr")
    script, div = components(plot)

    return render_template("chart.html", the_div=div, the_script=script)


def create_bar_chart(data, title, x_name, y_name, width=1200, height=300):
    source = ColumnDataSource(data)
    xdr = FactorRange(factors=data[x_name])
    ydr = Range1d(start=0, end=max(data[y_name])*1.5)

    tools = []
    plot = figure(title=title, x_range=xdr, y_range=ydr, plot_width=width,
                  plot_height=height, h_symmetry=False, v_symmetry=False,
                  min_border=0, toolbar_location="above", tools=tools,
                  responsive=True, outline_line_color="#666666")

    glyph = VBar(x=x_name, top=y_name, bottom=0, width=.8,
                 fill_color="#77CC66")
    plot.add_glyph(source, glyph)

    x_axis = LinearAxis()
    y_axis = LinearAxis()

    plot.add_layout(Grid(dimension=0, ticker=x_axis.ticker))
    plot.add_layout(Grid(dimension=1, ticker=y_axis.ticker))
    plot.toolbar.logo = None
    plot.min_border_top = 0
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = "#999999"
    plot.yaxis.axis_label = "SNR"
    plot.ygrid.grid_line_alpha = 0.1
    plot.xaxis.axis_label = "CHANNEL"
    plot.xaxis.major_label_orientation = 1
    return plot


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
