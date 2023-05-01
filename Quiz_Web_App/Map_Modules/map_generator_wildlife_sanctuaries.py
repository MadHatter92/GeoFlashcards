import dash
import dash_table
import pandas as pd
import folium
import fiona
import pandas as pd
import geopandas as gpd
from folium.features import DivIcon

df = pd.read_csv('wildlife_sanctuaries_details.csv')

states_list = ['Mizoram', 'Tamil Nadu', 'Madhya Pradesh', 'Maharashtra', 'Chhattisgarh', 'Gujarat', 'Odisha', 'Andhra Pradesh', 'Karnataka', 'Goa', 'Kerala', 'Telangana', 'West Bengal', 'Dadra and Nagar Haveli and Daman and Diu', 'Puducherry', 'Lakshadweep', 'Arunachal Pradesh', 'Assam', 'Nagaland', 'Meghalaya', 'Manipur', 'Tripura', 'Andaman and Nicobar Islands', 'Uttar Pradesh', 'Rajasthan', 'Delhi', 'Haryana', 'Sikkim', 'Bihar', 'Jharkhand', 'Ladakh', 'Jammu and Kashmir', 'Himachal Pradesh', 'Punjab', 'Uttarakhand', 'Chandigarh']

output_df = pd.DataFrame(columns=['State','Count','Snippet',])

for state in states_list:
    df_state = df[df["State Name"]==state]
    del df_state["State Name"]
    del df_state["S. No."]
    rows = df_state.shape[0]
    snippet = df_state.to_html(index=False)
    df_row = pd.DataFrame({'State':[state], 'Count':[rows], 'Snippet':[snippet]})
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
    tiles='OpenStreetMap',
    # maxBoundsViscosity= 1.0,
    # interactive= False,
    # tap=False
    )

data = output_df

gdf['Popups'] = output_df['Snippet'].tolist()
gdf['Tooltip'] = [state_name+": "+str(count) for state_name, count in zip(output_df['State'].tolist(), output_df['Count'].tolist())]

choropleth = folium.Choropleth(
    geo_data=gdf,
    name='choropleth',
    data=data,
    columns=['State', 'Count'],
    key_on='feature.properties.st_nm',
    # popup='feature.properties.st_nm',
    # tooltip=folium.features.GeoJsonTooltip(['st_nm']),
    # fill_color=color_scheme,
    # fill_opacity=0.4,
    line_opacity=0.8,
    # legend_name=f'{parameter.capitalize()} Cases',
    highlight=True,
    line_color='green',
    # background_color= 'none'
).add_to(m)

choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['Tooltip'], ['']),
        )

choropleth.geojson.add_child(
        folium.features.GeoJsonPopup(['Popups'], [''], style='overflow: scroll; height: 200px'),
        )

m.save('map_wildlife_sanctuaries.html')
