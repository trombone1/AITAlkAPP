import streamlit as st
import numpy as np
import pandas as pd
st.title('展示的不同資料繪圖方式')
data = pd.DataFrame(
     np.random.randn(30, 4),
     columns=['A', 'B', 'C','D'])
tab1, tab2 ,tab3, tab4 , tab5 = st.tabs(["1. Data", "2. Line_chart","3. Bar_chart","4. Pyplot","5. Area Chart"])
with tab1:
  data   # 顯示資料內容
with tab2:
  st.line_chart(data, width=0, height=0, use_container_width=True) # 折線圖
with tab3:
  st.bar_chart(data)  # 長條圖

import matplotlib.pyplot as plt
with tab4:
  fig, ax = plt.subplots()
  ax.hist(data, bins=20)

  fig  # 👈 Draw a Matplotlib chart
with tab5:
    st.area_chart(data, x="A", y=["B", "C"], color=["#FF0000", "#0000FF"] ) # 顯示面積圖


