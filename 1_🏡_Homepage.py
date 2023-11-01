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
    page_title="Hello",
    page_icon="🏡",
)
st.write("# Welcome to the employee hiring App 👋")
#App title
st.title('Employee Hiring App')
st.sidebar.success("Select a demo above.")

st.markdown(
    """Many companies regard employee performance highly. For a company to succeed in service delivery to its customers, employees should ready their 
    morale and avoid distractions that affect their performance negatively. In return for this, the company will keep its performance index high and 
    attract more customers and potential highr performing employees

This is the exact reason why Mr. Brain, a CEO at INX Future Inc , (referred as INX ); one of the leading data analytics and automation solutions provider 
with over 15 years of global business presence is concerned about the performnace index of the employees in the company. The employee performance dip has 
resulted in the increased customer escalations and the worst part of it customer satisfaction levels came down by 8% points.

The CEO therefore, says there is need to scale up employee performance rating for which a detailed analysis of the factors which are responsible for 
the poor employee performance are to be analyzed. There are so many attributes that influence the employee performance such as environment satisfaction, 
salary hike percentage in the previous one year, overtime,employee work-life balance and many more which will be revealed in the course of this deep 
analysis. Proper analysis of the employee performance will provide useful insights regarding the causes of the dip in performance and how it affects the 
company's share in the market. It is also good to predict the employee's performance prior to hiring in order to counter issues.

Predictive analytics is one of the techniques that will be used in this project and a Machine Learning model which is an artificial intelligence 
technique/algorithm will also be used. The model will be created using the past data which has been provided. Once the model is created, whenever a new set of 
data if provided it can provide approximate or exact values. In this machine learning project, I will be able to use Random Forest to get a more accurate 
forecasting. Therefore, this will help Mr. Brain take the right course of action.
"""
)
#Hiding the Streamlit rerun menu from the user
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
