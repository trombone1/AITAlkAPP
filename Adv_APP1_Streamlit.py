"""
# Advance app
Here's Advanced Streamlit App: 專案管理: 任務分配
"""
import streamlit as st
import pandas as pd
from io import BytesIO

st.title("專案管理: 任務分配")

# 初始數據框架
if 'tasks_df' not in st.session_state:
    st.session_state['tasks_df'] = pd.DataFrame(columns=['任務名稱', '負責人', '優先級', '預計日期', '任務提出日期', '執行狀態', '完成狀態'])
#st.session_state.tasks_df
# 任務名稱
task_name = st.text_input('輸入任務名稱')
# 負責人
team_member = st.selectbox('選擇負責人', ['Alice', 'Bob', 'Charlie', 'Diana'])
# 優先級
priority = st.radio('選擇任務優先級', ['高', '中', '低'])
# 預計完成日期
due_date = st.date_input('選擇預計完成日期')
# 任務提出日期
issue_day = pd.Timestamp.today().date()
# 執行狀態
Exec_status = st.text_input('輸入執行狀態')
# 完成狀態
is_completed = st.checkbox('任務已完成')
# 提交按鈕
if st.button('提交任務'):     
    num_records = len(st.session_state.tasks_df)
    st.session_state.tasks_df.loc[num_records]=[task_name, team_member, priority, due_date, issue_day, Exec_status, '已完成' if is_completed else '未完成']
# 顯示可編輯的數據框架
edited_df = st.data_editor(st.session_state.tasks_df, key='editor')

# Excel 檔案下載
def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Tasks')
    return output.getvalue()

excel_data = convert_df_to_excel(edited_df)
st.download_button('下載 Excel', data=excel_data, file_name='tasks.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


