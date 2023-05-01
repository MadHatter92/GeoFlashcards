import folium
import fiona
import pandas as pd
import geopandas as gpd
from folium.features import DivIcon
from folium import IFrame
import base64

def generate_map():

    zoom = 4.4

    state_geo = f'india_states_with_ladakh.geojson'

    gdf = gpd.read_file(state_geo)
    data_frame = pd.read_csv('national_parks_details.csv')

    name_list = data_frame['Name'].tolist()
    states_list = data_frame['State'].tolist()
    notability_list = data_frame['Notability'].tolist()
    area_list = data_frame['Area (in km2)'].tolist()
    water_list = data_frame['Rivers and lakes inside the national park'].tolist()
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
        tiles='OpenStreetMap',
        # maxBoundsViscosity= 1.0,
        # interactive= False,
        # tap=False
        )

    choropleth = folium.Choropleth(
        geo_data=gdf,
        name='choropleth',
        fill_color='white',
        fill_opacity=0.8,
        line_opacity=0.8,
        highlight=False,
        line_color='black',
    ).add_to(m)

    # tooltip = 'Which National Park?'

    for item in name_list:

        lat = lat_list[name_list.index(item)]
        lon = lon_list[name_list.index(item)]
        states = states_list[name_list.index(item)]
        notability = str(notability_list[name_list.index(item)])
        area = str(area_list[name_list.index(item)])
        water = str(water_list[name_list.index(item)])

        notability_html = '' if (notability=='nan') else "<p style=\"font-size:12px\">Known For: "+notability+"</p>"
        area_html = '' if (area=='nan') else "<p style=\"font-size:12px\">Area (sq km): "+area+"</p>"
        water_html = '' if (water=='nan') else "<p style=\"font-size:12px\">Water Bodies: "+water+"</p>"

        html="<div style=\"@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');font-family: 'Roboto Condensed', sans-serif;\">"+"<h5>"+item+"</h5>"+"<p style=\"font-size:12px\">State(s): "+states+"</p>"+notability_html+area_html+water_html

        # resolution, width, height = 10, 50, 25
        iframe = IFrame(html, width=200, height=200)
        popup = folium.Popup(iframe, max_width=1000)
        icon = folium.Icon(color="red", icon="paw", prefix='fa')
        marker = folium.Marker(location=[lat, lon], popup=popup, icon=icon)
        marker.add_to(m)

    m.save(f'../map_national_parks.html')

if __name__=='__main__':
    generate_map()
