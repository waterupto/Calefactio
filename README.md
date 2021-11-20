<p align="center"><img src="assets/logo.png" height="200px"><br>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourGitHubName/yourRepo/yourApp/)
[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
</p>
We plan to create an Exploratory Data Analytics Web Application that will help us explore and perform operations on the various elements affecting global warming.

## Objective🤔
Having a comprehensive view of various factors effecting the climate with the ability of performing operations will be really helpful. With our clean UI and nifty features like uploading your own database, the application is sure to be helpful.

## Dataset Used📚
For the intial working and reference of data field we are using the [GISS Surface Temperature Analysis (GISTEMP v4)](https://data.giss.nasa.gov/gistemp/) dataset by NASA.<br>

<img src="assets/annual.gif" height=450px><br>

The GISS Surface Temperature Analysis (GISTEMP v4) is an estimate of global surface temperature change. Graphs and tables are updated around the middle of every month using current data files from NOAA GHCN v4 (meteorological stations) and ERSST v5 (ocean areas), combined as described in our publications Hansen et al. (2010) and Lenssen et al. (2019). These updated files incorporate reports for the previous month and also late reports and corrections for earlier months.

## Pipeline of the Project🛣
- [x] Data Acquisition
- [x] Data Pre-Processing
- [x] UI/UX Design
- [x] EDA Backend
- [X] EDA Frontend

## Features⚙
We are thinking of providing the following features through our project:
- Univariate Analysis: Histogram and Bar Chart help to visualize the distribution and variance of each variable

- Correlation Analysis: Heatmap facilitates the identification of highly correlated explanatory variables and reduces collinearity.

- Bivariate Analysis: Box plot and Grouped bar chart help to spot the dependency and relationship between explanatory variables and response variable.


We are hoping to provide outputs in the line of our reference and all the while trying to incorporate better features.

## Using the deployed version of the web application

- Cloning the Repository: 

        git clone https://github.com/waterupto/Calefactio
- Setting up the Python Environment with dependencies 

        pip install -r requirements.txt

- Running the web application:

        streamlit run app.py

- Stopping the web application from the terminal

        Ctrl+C

## Steps to Run

1. Run the Streamlit App
<img src="assets/1.png">

2. Select the Sub-Data to Explore
<img src="assets/2.png">

3. Start Analyzing the Data
<img src="assets/3.png">

4. Get a category wise study of the dataset
<img src="assets/4.png">

5. Get a category correlation graph to study relations
<img src="assets/5.png">

## License⚖

This project is under the MIT License. See [LICENSE](LICENSE) for Details.

## Contributors🤝 

<table>
<tr align="center">
<td>

Aryan Kargwal

<p align="center">
<img src = "https://media-exp1.licdn.com/dms/image/C4E03AQF-jQx69fbYiw/profile-displayphoto-shrink_400_400/0/1610317317984?e=1638403200&v=beta&t=aFEY07dTsSqTmm_BpbsAiaQTuHHU_o6Wk552nJ8RXoQ"  height="120" alt="Aryan Kargwal">
</p>
<p align="center">
<a href = "https://github.com/aryankargwal"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/aryan-kargwal-2550561a2/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Nitish Chaturvedi

<p align="center">
<img src = "https://media-exp1.licdn.com/dms/image/C4E03AQHfb4nZEZKXhQ/profile-displayphoto-shrink_400_400/0/1615868393779?e=1638403200&v=beta&t=BU8HkWr2Bxq0OVXqaQcHSDHKnZ6l9n9ttL4O5oSHy2w"  height="120" alt="Nitish Chaturvedi">
</p>
<p align="center">
<a href = "https://github.com/waterupto"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/waterupto/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
</table>
