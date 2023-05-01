import dash
import dash_table
import pandas as pd
import folium
import fiona
import geopandas as gpd
from folium.features import DivIcon

df = pd.read_csv('india_ancient_cities_details.csv')

name_list = df['Capital'].tolist()
founder_list = df['Dynasty/King'].tolist()
image_link_list = df['Image Link'].tolist()

lat_list = df['Lat'].tolist()
lon_list = df['Lon'].tolist()

zoom = 4.4

state_geo = 'india_states_with_ladakh.geojson'

gdf = gpd.read_file(state_geo)

fi = fiona.open(state_geo)

top = fi.bounds[3]
bottom = fi.bounds[1]
left = fi.bounds[0]
right = fi.bounds[2]

m = folium.Map(
    location=[(top+bottom)/2,((left+right)/2)],
    zoom_start=zoom,
    minZoom=zoom-2,
    maxZoom=zoom+3,
    # resize=False,
    # zoomControl= False,
    # zoomAnimation= False,
    # trackResize= True, 
    # touchZoom=False,
    # boxZoom=False,
    # doubleClickZoom=False,
    scrollWheelZoom= 'center',
    # singleClickZoom=False,
    dragging=True,
    tiles='Stamen Toner',
    # maxBoundsViscosity= 1.0,
    # interactive= False,
    # tap=False
    )

choropleth = folium.Choropleth(
    geo_data=gdf,
    name='choropleth',
    fill_color='white',
    fill_opacity=0,
    line_opacity=0.8,
    highlight=False,
    line_color='black',
).add_to(m)


for item in name_list:

    lat = lat_list[name_list.index(item)]
    lon = lon_list[name_list.index(item)]

    founder = str(founder_list[name_list.index(item)])
    image_link = str(image_link_list[name_list.index(item)])

    name_html = "<p style=\"font-size:12px\">City: "+item+"</p>"
    founder_html = "<p style=\"font-size:12px\">Founded by: "+founder+"</p>"
    image_html = "<img src=\""+image_link+"\">"
    
    html="<div style=\"@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');font-family: 'Roboto Condensed', sans-serif;\">"+name_html+founder_html+image_html+"</div>"

    # resolution, width, height = 10, 50, 25
    iframe = folium.IFrame(html, width=220, height=250)
    popup = folium.Popup(iframe, max_width=1000)
    icon = folium.Icon(color='darkgreen', icon="hospital-o", prefix='fa')
    marker = folium.Marker(location=[lat, lon], tooltip=item, popup=popup, icon=icon)
    marker.add_to(m)

m.save(f'../map_ancient_indian_cities.html')