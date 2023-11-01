import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import time
import warnings

#Ignore Warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="Predictions", page_icon="🧠")

st.markdown("# Machine Learning 🧠")
st.sidebar.success("Make Predictions")

data = pd.read_csv("Employee_performance.csv")

#Machine Learning
st.header('Machine Learning')
#importing all required libraries for machine learning modeling
from sklearn.preprocessing import LabelEncoder, StandardScaler,OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


#drop EmpNumber
data.drop('EmpNumber',axis=1,inplace=True)
#encode categorical variables using LabelEncoder

for col in data.select_dtypes(include='object').columns:
    LE = LabelEncoder()
    LE.fit(data[col].unique())
    data[col]=LE.transform(data[col])

#create features and target variables (target=type)
X = data.drop(['PerformanceRating','NumCompaniesWorked','TrainingTimesLastYear','EmpEducationLevel','EmpJobSatisfaction','EmpRelationshipSatisfaction',
               'EducationBackground','EmpJobLevel','EmpJobInvolvement','MaritalStatus','BusinessTravelFrequency','OverTime','Gender','Attrition'],axis=1)
y = data['PerformanceRating']

#Split data into train and test sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=42)

# instantiate my model
rf = RandomForestClassifier()
# fit the model
rf.fit(X, y)

# show progress bar for model training
import time
with st.spinner('Finding a match...'):
    time.sleep(5)# wait for 5 seconds
    st.success('Model Training complete',icon="✅")
   # st.balloons()

# print model accuracy
st.subheader('Model Accuracy')
st.write(f'The model Accuracy is : {rf.score(X, y)*100}%')

# get user input
st.subheader('User Inputs')
Age=st.number_input('Employee age')
EmpDepartment = st.selectbox('Employee Department: Data Science-0  Development-1  Finance-2  Human Resources-3  Research & Development-4  Sales-5',('0','1','2','3','4','5'))
EmpJobRole = st.selectbox('Employee Role:Business Analyst-0 Data Scientist-1 Delivery Manager-2  Developer-3 Finance Manager-4 Healthcare Representative-5 Human Resources-6 Laboratory Technician-7 Manager-8 Manager R&D-9 Manufacturing Director-10 Research Director-11 Research Scientist-12 Sales Executive-13 Sales Representative-14 Senior Developer-15 Senior Manager R&D-16  Technical Architect-17 Technical Lead-18',(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18))
DistanceFromHome=st.number_input('Distance from home in miles')
EmpEnvironmentSatisfaction = st.selectbox('Environment Satisfaction: 1-Low, 2-Medium, 3-High, 4-Very High',(1,2,3,4))
EmpHourlyRate=st.number_input('Hourly Rate in Dollars')
EmpLastSalaryHikePercent=st.number_input('Salary Hike Percentage')
TotalWorkExperienceInYears=st.number_input('Work Experience')
EmpWorkLifeBalance = st.selectbox('Work-Life Balance: 1-Low, 2-Medium, 3-High, 4-Very High',(1,2,3,4))
ExperienceYearsAtThisCompany=st.number_input('Experience in this Company: Years')
ExperienceYearsInCurrentRole=st.number_input('Experience in this Role: Years')
YearsSinceLastPromotion= st.number_input('Time since last promotion: Years')
YearsWithCurrManager=st.number_input('Years with current manager')

# create a new dataframe to display selected input
pred1 = pd.DataFrame({'Age':Age,'EmpDepartment':EmpDepartment,'EmpJobRole' : EmpJobRole,
                      'DistanceFromHome' : DistanceFromHome,'EmpEnvironmentSatisfaction': EmpEnvironmentSatisfaction,
                       'EmpHourlyRate' : EmpHourlyRate,'EmpLastSalaryHikePercent': EmpLastSalaryHikePercent,'TotalWorkExperienceInYears': TotalWorkExperienceInYears,
                       'EmpWorkLifeBalance': EmpWorkLifeBalance,'ExperienceYearsAtThisCompany': ExperienceYearsAtThisCompany,
                       'ExperienceYearsInCurrentRole': ExperienceYearsInCurrentRole,'YearsSinceLastPromotion': YearsSinceLastPromotion,
                       'YearsWithCurrManager': YearsWithCurrManager},index=[0])


# print the user input
st.subheader('User input values')
st.dataframe(pred1)

# making predictions and print them 
prediction = rf.predict(pred1)
st.subheader('The Prediction')
st.write('Employee rating: 1-Low  2-Good  3-Excellent  4-Outstanding')
st.write(f'The Employee rating is: {prediction}')

#Hiding the Streamlit rerun menu from the user
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
