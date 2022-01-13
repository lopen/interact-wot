from flask import Flask, render_template
import folium, json
from folium.plugins import MousePosition

app = Flask(__name__)

min_lat = -150
max_lat = 180
min_lot = -180
max_lot = 180

markers = json.load(open('markers.json'))

@app.route('/')
def render_the_map():
    folium_map = folium.Map(
        tiles='None',
        attr='Wheel of Time Map, drawn by Dimension Door 2021, site by @trgyve',
        height='80%',
        width='100%',
        max_bounds=True,
        min_zoom=3,
        max_zoom=5,
        zoom_control=False)

    folium.raster_layers.ImageOverlay(
        image='./wot.jpeg',
        bounds=[[min_lat, min_lot], [max_lat, max_lot]]).add_to(folium_map)

    for marker in markers['poi']:
        iframe = folium.IFrame(marker['info'])                     # | to get bigger info box
        popup = folium.Popup(iframe, min_width=500, max_width=500) # |
        folium.Marker(marker['location'], popup=popup, tooltip=marker['name']).add_to(folium_map)

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter
    ).add_to(folium_map)

    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(host="0.0.0.0")