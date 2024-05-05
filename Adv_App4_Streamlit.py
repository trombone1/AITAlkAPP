import streamlit as st
import pandas as pd
import time

@st.cache_data
def fetch_and_clean_data(url):
    data = pd.read_csv(url)
    return data

start_time = time.time()
d1 = fetch_and_clean_data("https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv")
# 實際執行函式，因為這是第一次遇到它。
end_time = time.time()
st.write(f"d1 fetch data: {end_time - start_time:.2f} seconds")

start_time = time.time()
d2 = fetch_and_clean_data("https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv")
# 不執行函式。相反地，返回先前計算的值。這表示現在 d1 中的資料與 d2 中的相同。
end_time = time.time()
st.write(f"d2 fetch data: {end_time - start_time:.2f} seconds")

start_time = time.time()
d3 = fetch_and_clean_data("https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv")
# 這是不同的 URL，因此函式會執行。
end_time = time.time()
st.write(f"d3 fetch data: {end_time - start_time:.2f} seconds")

