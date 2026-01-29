import kagglehub
import streamlit as st
import plotly.express as px
import pandas as pd
import os

# Get ACNH catalog dataset
dataset_path = kagglehub.dataset_download("jessicali9530/animal-crossing-new-horizons-nookplaza-dataset")
file_path = ("//Users/joshuaizquierdo/.cache/kagglehub/datasets/"
        "jessicali9530/animal-crossing-new-horizons-nookplaza-dataset/versions/3/")
file_list = []

for file in os.listdir(file_path):
    file_list.append(file)

st.title("Animal Crossing New Horizons Catalog")

# Let user choose which file to view
category = st.selectbox(
    "Choose a file containing the catalog of items.",
    file_list
)

acnh_df = pd.read_csv(file_path + category) # Create Dataframe

tab1, tab2 = st.tabs(["Table", "Bar Chart"])

with tab1:
    # Lets users select what .csv file to view
    options = st.multiselect(
        "Select what items you want to hide",
        acnh_df.keys()
    )

    # Display .csv file as a table
    st.dataframe(acnh_df, hide_index=True, column_order=options)
    st.info("This table displays all the information from the selected CSV file. "
            "The columns shown can be filtered using the multiselect box above the table.")

with tab2:
    col1, col2 = st.columns(2)

    with col1: # Determines the x-axis of the bar graph
        x_axis = st.selectbox(
            "Choose the x-axis",
            acnh_df.keys()
        )

    with col2: # Determines the y-axis of the bar graph
        y_axis = st.selectbox(
            "Choose the y-axis",
            acnh_df.keys()
        )

    fig1 = px.bar(
        data_frame=acnh_df,
        x=x_axis,
        y=y_axis
    )

    st.plotly_chart(fig1) # Display bar graph
    st.info("This bar chart is used to display the correlation between certain columns. For example, having 'Name'"
            "on the x-axis and 'Buy' on the y-axis will properly display the the price of each item in-game.")
