# Imports
import pandas as pd
import pandas_profiling
import streamlit as st
import numpy as np
from streamlit_pandas_profiling import st_profile_report


# Sidebar Menu
st.sidebar.image("assets/logo.png")
st.sidebar.markdown(
    "MediaPedia is our attempt to make an interactive and user friendly media recommender web application with added utilities and features."
)
st.sidebar.markdown("Check out the code at:")
st.sidebar.markdown("[Github Repository](!https://github.com/aryankargwal/mediapedia)")
