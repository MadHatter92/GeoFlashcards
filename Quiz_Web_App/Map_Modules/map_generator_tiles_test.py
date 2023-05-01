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
    data_frame = pd.read_csv('national_geological_monuments_details.csv')

    name_list = data_frame['Geo-Heritage site'].tolist()
    district_list = data_frame['District'].tolist()
    location_list = data_frame['Location'].tolist()
    category_list = data_frame['Geotourism Category'].tolist()
    
    lat_list = data_frame['Lat'].tolist()
    lon_list = data_frame['Lon'].tolist()

    fi = fiona.open(state_geo)

    top = fi.bounds[3]
    bottom = fi.bounds[1]
    left = fi.bounds[0]
    right = fi.bounds[2]

    f = folium.Figure(width=1000, height=500)

    m = folium.Map(
        location=[(top+bottom)/2,((left+right)/2)],
        zoom_start=zoom,
        minZoom=zoom,
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
        ).add_to(f)

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

        district = str(district_list[name_list.index(item)])
        location = str(location_list[name_list.index(item)])
        category = str(category_list[name_list.index(item)])

        district_html = '' if (district=='nan') else "<p style=\"font-size:12px\">District: "+district+"</p>"
        location_html = '' if (location=='nan') else "<p style=\"font-size:12px\">Location: "+location+"</p>"
        category_html = '' if (category=='nan') else "<p style=\"font-size:12px\">Geotourism Category: "+category+"</p>"

        html="<div style=\"@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');font-family: 'Roboto Condensed', sans-serif;\">"+"<h5>"+item+"</h5>"+district_html+location_html+category_html

        # resolution, width, height = 10, 50, 25
        iframe = IFrame(html, width=200, height=200)
        popup = folium.Popup(iframe, max_width=1000)
        icon = folium.Icon(color="darkblue", icon="image", prefix='fa')
        marker = folium.Marker(location=[lat, lon], popup=popup, icon=icon)
        marker.add_to(m)

    f.save('map_national_geological_monuments.html')

if __name__=='__main__':
    generate_map()
