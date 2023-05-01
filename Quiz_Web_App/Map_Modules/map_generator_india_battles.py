import folium
import fiona
import pandas as pd
import geopandas as gpd
from folium.features import DivIcon
from folium import IFrame
import base64

zoom = 4.4

state_geo = f'india_states_with_ladakh.geojson'

gdf = gpd.read_file(state_geo)

data_frame = pd.read_csv('historical_india_battle_sites_details.csv')

name_list = data_frame['Battle'].tolist()
year_list = data_frame['Year'].tolist()
place_list = data_frame['Place'].tolist()
campaign_list = data_frame['Part of'].tolist()
winner_list = data_frame['Winner'].tolist()
loser_list = data_frame['Loser'].tolist()

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
    maxZoom=zoom+4,
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
    fill_opacity=0,
    line_opacity=0.8,
    highlight=False,
    line_color='black',
).add_to(m)


for item in name_list:

    lat = lat_list[name_list.index(item)]
    lon = lon_list[name_list.index(item)]

    year = str(year_list[name_list.index(item)])
    place = str(place_list[name_list.index(item)])
    campaign = str(campaign_list[name_list.index(item)])
    winner = str(winner_list[name_list.index(item)])
    loser = str(loser_list[name_list.index(item)])

    year_html = '' if (year=='nan') else "<p style=\"font-size:12px\">Year: "+year+"</p>"
    place_html = '' if (place=='nan') else "<p style=\"font-size:12px\">Place: "+place+"</p>"
    campaign_html = '' if (campaign=='nan') else "<p style=\"font-size:12px\">Campaign: "+campaign+"</p>"
    winner_html = '' if (winner=='nan') else "<p style=\"font-size:12px\">Winner: "+winner+"</p>"
    loser_html = '' if (loser=='nan') else "<p style=\"font-size:12px\">Loser: "+loser+"</p>"

    html="<div style=\"@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');font-family: 'Roboto Condensed', sans-serif;\">"+"<h5>"+item+"</h5>"+year_html+place_html+campaign_html+winner_html+loser_html

    # resolution, width, height = 10, 50, 25
    iframe = IFrame(html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=1000)
    icon = folium.Icon(color="black", icon="bomb", prefix='fa')
    marker = folium.Marker(location=[lat, lon], popup=popup, icon=icon)
    marker.add_to(m)

m.save(f'map_india_battles.html')