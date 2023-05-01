import dash
import dash_table
import pandas as pd
import folium
import fiona
import pandas as pd
import geopandas as gpd
from folium.features import DivIcon

df = pd.read_csv('wildlife_sanctuaries_details.csv')

states_list = ['Punjab', 'Haryana', 'Chhattisgarh', 'Karnataka', 'Maharashtra', 'Assam', 'Telangana', 'Kerala', 'Andaman & Nicobar Islands', 'Uttarakhand', 'Delhi', 'Odisha', 'Meghalaya', 'Uttar Pradesh', 'Gujarat', 'West Bengal', 'Jammu & Kashmir', 'Rajasthan', 'Madhya Pradesh', 'Himachal Pradesh', 'Bihar', 'Sikkim', 'Goa', 'Mizoram', 'Tamil Nadu', 'Ladakh', 'Chandigarh', 'Andhra Pradesh', 'Arunachal Pradesh', 'Dadra & Nagar Haveli', 'Jharkhand', 'Nagaland', 'Daman & Diu', 'Tripura', 'Manipur', 'Puducherry', 'Lakshadweep']

output_df = pd.DataFrame(columns=['State','Count','Snippet',])

for state in states_list:
    df_state = df[df["State Name"]==state]
    del df_state["State Name"]
    del df_state["S. No."]
    rows = df_state.shape[0]
    snippet = df_state.to_html()
    df_row = pd.DataFrame({'State':[state], 'Count':[rows], 'Snippet':[snippet]})
    output_df = output_df.append(df_row)

print(output_df)
