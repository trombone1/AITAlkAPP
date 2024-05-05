"""
# AI_Talk_Streamlit APP Class 4th app
Here's to using data to create a map:
"""
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

map_data = pd.DataFrame(
    np.random.randn(500, 2) / [10, 10] + [24.24, 121.2],
    columns=['lat', 'lon'])

st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state={
                "latitude": 24.24,
                "longitude":  121.2,
                "zoom": 7,
                "pitch": 50,
            },
            layers= [pdk.Layer(
                "ScatterplotLayer",
                data=map_data,
                get_position=['lon','lat'],
                auto_highlight=True,
                get_color=[200, 0, 000, 140],
                get_radius=500,
            
                )] 
        )
    )