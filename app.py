# Imports
import pandas as pd
import pandas_profiling
import streamlit as st
import numpy as np
from streamlit_pandas_profiling import st_profile_report


# Sidebar Menu
st.sidebar.image("assets/logo.png", width=300)
st.sidebar.markdown(
    "Calefactio is an undergraduate team's effort to shine a brigher light onto various factors that affect Global Warming through an elaborate exploratory data analysis of the GISS Surface Temperature Analysis (GISTEMP v4) dataset by NASA"
)
st.sidebar.markdown("Check out the code at:")
st.sidebar.markdown("[Github Repository](!https://github.com/waterupto/Calefactio)")

# Data Profiling
def profiling():
    st.header("Calfactio")
    st.subheader(
        "Having a comprehensive view of various factors effecting the climate with the ability of performing operations will be really helpful. With our clean UI and nifty features like uploading your own database, the application is sure to be helpful."
    )
    st.subheader(
        "The GISS Surface Temperature Analysis (GISTEMP v4) is an estimate of global surface temperature change. Graphs and tables are updated around the middle of every month using current data files from NOAA GHCN v4 (meteorological stations) and ERSST v5 (ocean areas), combined as described in our publications Hansen et al. (2010) and Lenssen et al. (2019). These updated files incorporate reports for the previous month and also late reports and corrections for earlier months."
    )
    st.subheader("Let us start!")

    df1 = pd.read_csv("data/GLB.Ts+dSST.csv")
    pr1 = df1.profile_report()

    st_profile_report(pr1)


if __name__ == "__main__":
    profiling()
