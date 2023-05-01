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
    data_frame = pd.read_csv('biosphere_reserves_details.csv')

    name_list = data_frame['Name'].tolist()
    lat_list = data_frame['Lat'].tolist()
    lon_list = data_frame['Lon'].tolist()
    key_fauna_list = data_frame['Key fauna'].tolist()
    type_list = data_frame['Type'].tolist()
    location_list = data_frame['Location'].tolist()

    fi = fiona.open(state_geo)

    top = fi.bounds[3]
    bottom = fi.bounds[1]
    left = fi.bounds[0]
    right = fi.bounds[2]

    m = folium.Map(
        location=[(top+bottom)/2,((left+right)/2)],
        zoom_start=zoom,
        minZoom=zoom-2,
        maxZoom=zoom+2,
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
        key_fauna = key_fauna_list[name_list.index(item)]
        type = type_list[name_list.index(item)]
        location = location_list[name_list.index(item)]

        Filename ='test_image.png'
        # encoded = base64.b64encode(open(Filename, 'rb').read())
        html="<div style=\"@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');font-family: 'Roboto Condensed', sans-serif;\">"+"<h5>"+item+"</h5>"+"<h6>Location: "+location+"</h6>"+"<h6>Classification: "+type+"</h6>"+"<h6>Key Fauna: "+key_fauna+"</h6>"+"</div>"
        # resolution, width, height = 10, 50, 25
        iframe = IFrame(html, width=200, height=200)
        popup = folium.Popup(iframe, max_width=1000)
        icon = folium.Icon(color='blue', icon_color='white', icon='leaf')
        marker = folium.Marker(location=[lat, lon], popup=popup, icon=icon)
        marker.add_to(m)

        m.save(f'map_with_text.html')

if __name__=='__main__':
    generate_map()
