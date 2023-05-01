import folium
import fiona
import pandas as pd
import geopandas as gpd
from folium.features import DivIcon
from folium import IFrame
import base64

def generate_map():

    zoom = 2

    state_geo = f'world.geojson'

    gdf = gpd.read_file(state_geo)
    data_frame = pd.read_csv('World_Geo_Markers/world_lakes.csv')

    name_list = data_frame['Name'].tolist()
    lat_list = data_frame['Lat'].tolist()
    lon_list = data_frame['Lon'].tolist()

    fi = fiona.open(state_geo)

    top = fi.bounds[3]
    bottom = fi.bounds[1]
    left = fi.bounds[0]
    right = fi.bounds[2]

    m = folium.Map(
        location=[(top+bottom)/2,((left+right)/2)],
        zoom_start=zoom,
        minZoom=zoom-2,
        maxZoom=zoom+2.5,
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
        tiles='',
        # maxBoundsViscosity= 1.0,
        # interactive= False,
        # tap=False
        )

    choropleth = folium.Choropleth(
        geo_data=gdf,
        name='choropleth',
        fill_color='white',
        fill_opacity=0.4,
        line_opacity=0.8,
        highlight=True,
        line_color='black',
    ).add_to(m)

    # tooltip = 'Which National Park?'

    for item in name_list:

        lat = lat_list[name_list.index(item)]
        lon = lon_list[name_list.index(item)]

        Filename ='test_image.png'
        # encoded = base64.b64encode(open(Filename, 'rb').read())
        html="<div style=\"@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');font-family: 'Roboto Condensed', sans-serif;\">"+"<h5>"+item+"</h5>"
        # resolution, width, height = 10, 50, 25
        # iframe = IFrame(html, width=200, height=200)
        tooltip = folium.Tooltip(html)
        icon = folium.Icon(color='green', icon_color='white', icon='compass', prefix='fa')
        marker = folium.Marker(location=[lat, lon], tooltip=tooltip, icon=icon)
        marker.add_to(m)
        print('Added '+ item)

        m.save(f'../map_world_lakes.html')

if __name__=='__main__':
    generate_map()