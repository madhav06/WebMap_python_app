# we are importing folium first
import folium
# importing pandas
import pandas

# create object to read file
#data = pandas.read_csv("volcanoes.txt")
data = pandas.read_csv("corona.txt")
lat = list(data["LAT"])   # adding lat
lon = list(data["LON"])   # adding lon
nam = list(data["NAME"]) # adding NAME
age = list(data["CAP"])

# reading file corona_cured.txt
data = pandas.read_csv("corona_cured.txt")
lat1 = list(data["LATA"])  #adding LATA
lon1 = list(data["LONA"])   # adding LONA
nama = list(data["NAMEA"])   # adding NAME
cap = list(data["CAPA"])     # adding age

#adding html to beautify popup
html = """<h4> Corona Information: </h4>
Height: %s m
"""

# adding color points
def color_producer(agebar):
    if agebar < 30:
        return 'orange'
    elif 30 <= agebar < 60:
        return 'red'
    else:
        return 'darkred'

# creating map object
map = folium.Map(location=[26.052525,85.721238], zoom_start = 6, tiles = "Stamen Terrain")

# add feature group variable
fg = folium.FeatureGroup(name="My Map")

# for loop that iterating over corona_cured
for lit, lin, nm, es in zip(lat1, lon1, nama, cap):
    fg.add_child(folium.Marker(location=[lit, lin], popup = "patient: "+nm+" ; "+"age: "+str(es), icon=folium.Icon(color="lightgreen")))

# for loop that iterates over corona
for lt, ln, el, ep in zip(lat, lon, nam, age):
# adding marker on map
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup = "patient: "+el+" ; " +"age: "+str(ep), icon=folium.Icon(color=color_producer(ep))))


# fg.add_child(folium.GeoJson(data=open('kalounjar.json', 'r', encoding='utf-8-sig').read(),
# style_function=lambda x: {'fillColor:'green' if x['properties']['POP2020'] < 8500
# else 'orange' if 8300 <= x['properties']['POP2020'] < 10000 else 'red' }))
#
# #

fg.add_child(folium.GeoJson(data =open("kalounjar.json", 'r', encoding= 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green'}))

# calling method
map.add_child(fg)
map.save("Map_html_popup.html")     # save it
