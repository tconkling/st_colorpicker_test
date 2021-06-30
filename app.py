import streamlit as st

st.color_picker("Background color hex: ", "#eee", key="main")
st.sidebar.color_picker("Background color hex: ", "#eee", key="sidebar")
