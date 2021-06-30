import streamlit as st

color = st.color_picker("Background color hex: ", "#eee", key="main")
st.write("color", color)
