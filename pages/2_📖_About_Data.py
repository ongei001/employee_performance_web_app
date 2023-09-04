import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings

#Ignore Warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Our Data",
    page_icon="📖",
)
st.write("# Our Data✍️")
st.sidebar.success("Data Facts")

#App title
st.title('Understanding our data')
#Describing data
st.markdown(""" This data was provided by Mr. Brain, a CEO at INX Future Inc. The data has several features which are going to be described below""")
#Loading data
data = pd.read_csv("Employee_performance.csv")

#Getting user input on how many rows to display
rows = st.slider('Slide along to view more parts of the data',0,15,5)
#Display data as a dataframe
st.dataframe(data.head(rows))

st.markdown("""* **Columns:** The data has 29 columns
* **Rows:** There are a total of 1200 columns
* **DataTypes:**  There are 2 data types: int64(19) and object(9)                     
* **Duplicates:** There are no duplicates            
* **Missing Values:** There are no missing values            
            
            """)