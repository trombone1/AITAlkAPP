import streamlit as st
import pandas as pd
from io import BytesIO

st.title("專案管理：問題清單")

# 側邊欄上傳 Excel 文件
uploaded_file = st.sidebar.file_uploader("上傳問題清單 Excel", type=["xlsx"])
if uploaded_file:
    st.session_state['issues_df'] = pd.read_excel(uploaded_file,)
else:
    # 初始化數據框
    if 'issues_df' not in st.session_state:
        st.session_state['issues_df'] = pd.DataFrame(columns=['問題描述','執行狀態', '負責人', '優先級', '截止日期', '預計修復時間', '時間標記'])

# 側邊欄互動元件
with st.sidebar:
    # 問題描述
    issue_description = st.text_area('輸入問題描述',value='描述問題')

    # 執行狀態
    issue_Status = st.text_area('輸入目前執行狀態',value='執行狀態說明')
    
    # 負責人
    issue_owner = st.multiselect('選擇負責人', ['Alice', 'Bob', 'Charlie', 'Diana'], default=[])

    # 優先級
    issue_priority = st.select_slider('選擇問題優先級', options=['低', '中', '高'], value='低')

    # 截止日期
    due_date = st.date_input('選擇截止日期')
    type(due_date)
    # 預計修復時間
    fix_time = st.slider('選擇預計修復時間 (小時)', 0, 48, 8)

    # 時間標記
    timestamp = st.time_input('選擇時間標記', pd.Timestamp.now().time())
    type(timestamp)
    # 提交按鈕
    if st.button('提交問題'):
        num_records = len(st.session_state.issues_df)
        st.session_state.issues_df.loc[num_records]=[issue_description, issue_Status, ', '.join(issue_owner), issue_priority, due_date, f"{fix_time} 小時", timestamp]
        
# 顯示可編輯的數據框
edited_df = st.data_editor(st.session_state['issues_df'], key='editor')

# Excel 檔案下載
def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Issues')
    return output.getvalue()

excel_data = convert_df_to_excel(edited_df)
st.download_button('下載問題清單 Excel', data=excel_data, file_name='issues.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

