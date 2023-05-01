import dash
import dash_table
import pandas as pd
import folium
import fiona
import geopandas as gpd
from folium.features import DivIcon

df = pd.read_csv('congress_sessions_details.csv')

place_list = pd.unique(df['Place']).tolist()
lat_list = pd.unique(df['Lat']).tolist()
lon_list = pd.unique(df['Lon']).tolist()

output_df = pd.DataFrame(columns=['Place','Snippet'])

for place in place_list:
    df_place = df[df["Place"]==place]
    del df_place["Lat"]
    del df_place["Lon"]
    del df_place["Place"]
    snippet = df_place.to_html(index=False)
    df_row = pd.DataFrame({'Place':[place], 'Snippet':[snippet]})
    output_df = output_df.append(df_row)

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

data = output_df

# gdf['Popups'] = output_df['Snippet'].tolist()
# gdf['Tooltip'] = [state_name+": "+str(count) for state_name, count in zip(output_df['State'].tolist(), output_df['Count'].tolist())]

for item in place_list:
    lat = lat_list[place_list.index(item)]
    lon = lon_list[place_list.index(item)]
    snippet = output_df['Snippet'].tolist()[place_list.index(item)]

    # resolution, width, height = 10, 50, 25
    iframe = folium.IFrame(snippet, width=250, height=120)
    popup = folium.Popup(iframe, max_width=1000)
    icon = folium.Icon(color="blue", icon="flag", prefix='glyphicon')
    marker = folium.Marker(location=[lat, lon], tooltip=item, popup=popup, icon=icon, style='overflow: scroll; height: 200px; font-size:8px')
    marker.add_to(m)

# choropleth = folium.Choropleth(
#     geo_data=gdf,
#     name='choropleth',
#     data=data,
#     columns=['State', 'Count'],
#     key_on='feature.properties.st_nm',
#     # popup='feature.properties.st_nm',
#     # tooltip=folium.features.GeoJsonTooltip(['st_nm']),
#     # fill_color=color_scheme,
#     # fill_opacity=0.4,
#     line_opacity=0.8,
#     # legend_name=f'{parameter.capitalize()} Cases',
#     highlight=True,
#     line_color='green',
#     # background_color= 'none'
# ).add_to(m)

# choropleth.geojson.add_child(
#         folium.features.GeoJsonTooltip(['Tooltip'], ['']),
#         )

# choropleth.geojson.add_child(
#         folium.features.GeoJsonPopup(['Popups'], [''], style='overflow: scroll; height: 200px'),
#         )

m.save('map_congress_sessions.html')
