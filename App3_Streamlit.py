"""
# AI_Talk_Streamlit APP Class 3th app
Here's to using data to create a map data:
"""
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    # 生成隨機數據 500x2 的表格元素都被除以 20，再加上 [24.24, 121.2]
    np.random.randn(500, 2) / [20, 20] + [24.24, 121.2], 
    columns=['lat', 'lon'])

st.map(map_data,zoom=7, use_container_width=True,color='#0033ff') # 顯示地圖