import streamlit as st

# 從本地載入圖片
st.image('test.webp.svg', caption='本地圖片', use_column_width=True)

# 從 URL 載入圖片
st.image('https://hips.hearstapps.com/hmg-prod/images/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2-2-661f7a46107a4.png', caption='網絡圖片', use_column_width=True)