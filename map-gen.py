import folium, json
from folium.plugins import MousePosition, Fullscreen

min_lat = -150
max_lat = 180
min_lot = -180
max_lot = 180

folium_map = folium.Map(
    tiles='None',
    attr='Wheel of Time Map, drawn by <a href="https://linktr.ee/dimensiondoormaps" target="_blank">Dimension Door</a>, site by <a href="https://github.com/lopen/interact-wot" target="_blank">@trgyve</a>',
    height='50%',
    width='50%',
    max_bounds=True,
    min_zoom=3,
    max_zoom=5,
    zoom_control=False)

def main():
    # adds the overlay of the wot map ontop of the old map
    add_map_overlay()
    # adds markers from markers.json
    add_makers()
    # adds coordinates of mouse location in top right
    add_coordinates()
    # adds a fullscreen option in top left
    add_fullscreen()
    # adds more html/css elements to complete page
    add_htmlcss()
    # saves map to html file html/map
    folium_map.save('html/index')

def add_map_overlay():
    folium.raster_layers.ImageOverlay(
        image='resources/wot.jpeg',
        bounds=[[min_lat, min_lot], [max_lat, max_lot]]).add_to(folium_map)


def add_makers():
    markers = json.load(open('json/markers.json'))

    for marker in markers['poi']:
        iframe = folium.IFrame(marker['info'])                     # | to get bigger info box
        popup = folium.Popup(iframe, min_width=500, max_width=500) # |
        folium.Marker(
            marker['location'], 
            popup=popup, 
            tooltip=marker['name'],
            #icon=folium.DivIcon(html=f"{marker['size']}")
        ).add_to(folium_map)

def add_coordinates():
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

def add_fullscreen():
    Fullscreen(
        position="topleft",
        title="Full Screen",
        title_cancel="Exit Full Screen",
        force_separate_button=True
    ).add_to(folium_map)

def add_htmlcss():
    title = '<title>interact-wot</title>'
    folium_map.get_root().header.add_child(folium.Element(title))

    heading = '<h2>interact-wot</h2>'
    folium_map.get_root().html.add_child(folium.Element(heading))

main()