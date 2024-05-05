"""
# This Session State Basics exmaple 

"""
import streamlit as st

st.title("Session State Basics")
#callback functions to convert lbs to kgs and vice versa
def lbs_to_kgs():
    st.session_state.kg=st.session_state.lbs*0.45359237
#callback functions to convert kgs to lbs and vice versa
def kgs_to_lbs():
    st.session_state.lbs=st.session_state.kg/0.45359237

tab1, tab2 = st.tabs(["1. With Session State", "2. Without Session State"])
#using session state to store the values of lbs and kgs
with tab1:
    "st.session_state objects.", st.session_state
    # setup columns for input objects
    col1,buff,col2=st.columns([2,1,2])
    with col1:
        #initializing the session state variables lbs 
        pounds=st.number_input("Pounds",key="lbs",on_change=lbs_to_kgs)
    with col2:
        #initializing the session state variables kg
        kilograms=st.number_input("Kilograms",key="kg",on_change=kgs_to_lbs)
#without session state
with tab2:
    pounds2=0
    kilograms2=0
    # setup columns for input objects
    col3,buff2,col4=st.columns([2,1,2])
    with col3:
        pounds2=st.number_input("Pounds2",value=pounds2)
        kilograms2=pounds2*0.45359237
        'kilograms2 : ',kilograms2
    with col4:
        kilograms2=st.number_input("Kilograms2",value=kilograms2)
        pounds2=kilograms2/0.45359237
        'pounds2 : ',pounds2