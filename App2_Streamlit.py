"""
# AI_Talk_Streamlit APP Class 2nd app
Here's our second attempt at using data to create a table:
"""
import streamlit as st
import pandas as pd
import numpy as np
st.title('資料展示的不同方式')
# 生成隨機數據 30x20 的表格
df = pd.DataFrame(np.random.randn(30, 20), columns=("col %d" % i for i in range(20))) 
tab1, tab2 ,tab3, tab4 = st.tabs(["1. Dataframe", "2. Table","3. Dataframe with highlight","4. Data editor"])
with tab1:
  st.dataframe(df) # 與 st.write(df) 類似，顯示強大的表格
with tab2:
  st.table(df)     # 顯示靜態表格
with tab3:
  st.dataframe(df.style.highlight_max(axis=0)) # 顯示高亮最大值的表格
with tab4:
  edited_df = st.data_editor(df) # 顯示可編輯的表格  
  favorite_command = edited_df.loc[edited_df["col 1"].idxmax()]["col 1"]   # 取得編輯後名為"Col 1"的最大值
  st.markdown(f"Your favorite command is **{favorite_command}** 🎈") # 顯示最大值

