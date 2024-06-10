import streamlit as st
from multiapp import MultiApp
from apps import home, data, eda, model # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App

This my multi-page app :)
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("EDA", eda.app)
app.add_app("Model", model.app)
# The main app
app.run()
