import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import time
import altair as alt
import warnings

alt.data_transformers.disable_max_rows()
#Ignore Warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="Plottings", page_icon="📊")

st.markdown("# Visualizations and insights 📊")
st.sidebar.success("Visualizations")

data = pd.read_csv("Employee_performance.csv")
#drop EmpNumber
data.drop('EmpNumber',axis=1,inplace=True)

st.subheader('Performance Rating Distribution')
perfomance_dist=pd.DataFrame(data['PerformanceRating'].value_counts())
st.bar_chart(perfomance_dist)
st.markdown("""***From the Rating Distribution above, it can be concluded that:***
* There are more employees that performed excellently(3) leading both Good(2) and Outstanding(4) combined
* Outstanding performers were less than 200 and Good performers were almost 200            
              
            
            """)

#Exploring the perfomance rating totals per department
st.subheader('Peformance Rating Distribution per Department')
plt.figure(figsize = (15,10))
sns.countplot(data = data, x ='EmpDepartment', hue ='PerformanceRating',hatch='//')
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
st.pyplot()
st.markdown('''***From the Performance Rating Distribution above, it can be concluded that:***
* Development department had the highest number of both Outstanding and Excellent performers which is a very positive indicator. However, the department should focus on reducing the excellent performers and increase the outstanding performers number
* The sales department had the highest number of good perfomers. The department should focus on reducing that number and increasing the number of outstanding performers
* Human resources, Data science and Finance departments should focus on reducing the number of reducing the good and excellent and increase the the number of outstanding performers given their manageable number of employees
* Finaly, the Research & Development has the secong largest number of employees who were rated good. The department should also give focus to reducing that number and feed the outstanding rating.
''')
st.write('')


#performance percentage per department
st.subheader('Departmental average performance rating')
data.groupby('EmpDepartment')['PerformanceRating'].mean().sort_values(ascending=False).plot(kind='pie',figsize=(9,4),colors=['#05fc0d','#20f7da',"#d0f5f4","#9a959c","#9eb07d",'#f72020'],
                                                           explode=[0.1,0.05,0.0,0.0,0.0,0.0],autopct="%1.2f%%",shadow = True,                       
                                                           )
plt.xticks(rotation=90)
st.pyplot()
st.markdown('''***From the departmental average percentage performance rating above, it can be concluded that:***
* Development department tops all the other departments followed closely by the Data Science departement. The Finance departement had the lowest average
* It is also important as well to note that the margin/difference between Development and Data Science is 0.20 percent
* The Human Resources and Research & development departments have a very close range of 0.03 percent
* This visualization indicates a possible bias in resource alloction, talent acquision and rewards among the departments. The company needs to make a balance and maintain equity
''')
st.write('')
#average performance rating per department
st.subheader('Average performance rating per department')
average = data.groupby('EmpDepartment')['PerformanceRating'].mean()
st.bar_chart(average)
st.markdown('''***This is a boost visualization to the departmental average percentage performance rating***''')
st.write('')
st.write('')
#Visualizing the performance average of categorical columns per department
st.subheader('Average performance rating per department')
for i in data.drop(['EmpDepartment','EmpJobRole'],axis=1).select_dtypes(include='object'):
    plt.figure(figsize=(7,4))
    data.groupby(['EmpDepartment',i])['PerformanceRating'].mean().unstack(level=1).plot(kind='bar',hatch='*')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.title(f"Performance average in {i} per department")
    plt.xlabel(f' Department and \n{i}',fontsize=12)
    plt.ylabel('Perfomance rating average')
    plt.legend(loc='lower right')
    st.pyplot()
st.markdown('''
***Gender***
* The trend shows a relatively balanced performance for both genders across the departments. It should however be noted only two departments (Data Science and Development) had the average performance for both genders at 3(excellent) and above. The company should therefore focus on empowering both male and females with perfoance enhancement trainings and investigate possible gender based recruitment process that may be taking place silently in the deparments
            
***Education Background***
* Different education backgrounds performed diffrently across the different departments. The company should therefore seek to recruit employees in the departments based on the outstanding performing education background per department.
            
***Marital Status***            
* It can be noted that different marital statuses perform differently across the diffrent departments. There is no unique trend across the departmsnts. The company should therefore recruit employees depending on the outstanding performance in a pasticular department. For example, married employees in the Data Science department had the best average (above 3.5) hence the talent acquisition team should always consider married employees in that department
            
***Business Travel Frequency***
* As seen from the visualization travel frequency affected the perfomance differently and there was no linear correlation across all departments. The company should therefore balance all the departments with frequncy needed to avoid misuse of funds injected into business travels that do not yield a positive performance.
            
***Overtime***
* There is no linear correlation as well. It seems overtime affected some departments positively and otheres negatively. The company should therefore seek to a common overtime rate across all departments. The company needs to allow overtime on departments that are positively impacted

***Education Background***                                                           
* The chart shows different trends again across the departments. The company needs to balance the sizes of their departments according to their needs to maximize the performance per department

''')
st.write('')
st.write('')

#Selecting columns that need analysis cohortwise
coh = data.loc[:,['EmpDepartment','Age','DistanceFromHome','EmpHourlyRate','EmpLastSalaryHikePercent','TotalWorkExperienceInYears',
       'ExperienceYearsAtThisCompany','ExperienceYearsInCurrentRole',
       'YearsSinceLastPromotion','YearsWithCurrManager','PerformanceRating']]

#Creating cohorts per required columns with long ranges of data
coh = coh.assign(AgeCohorts=pd.cut(coh['Age'], bins=[15,20,25,30,35,40,45,50,55,60,65], 
                           right=False, labels=['15-19','20-24','25-29', '30-34', '35-39',
                                                '40-44','45-49','50-54','55-59','60+']))
coh = coh.assign(DistanceCohorts=pd.cut(coh['DistanceFromHome'], bins=[1,5,10,15,20,25,30], 
                           right=False, labels=['1-5','6-10','11-15','16-20', '21-24','25+']))
coh = coh.assign(HourlyRateCohorts=pd.cut(coh['EmpHourlyRate'], bins=[30,40,50,60,70,80,90,100], 
                           right=False, labels=['30-39','40-49','50-59','60-69','70-79','80-89','90+']))
coh = coh.assign(SalaryHikeCohorts=pd.cut(coh['EmpLastSalaryHikePercent'], bins=[10,15,20,25], 
                           right=False, labels=['10-14','15-19','20+']))
coh = coh.assign(WorkExperienceCohorts=pd.cut(coh['TotalWorkExperienceInYears'], bins=[0,5,10,15,20,25,30,35,40], 
                           right=False, labels=['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35+']))
coh = coh.assign(WrkExperCompanyCohorts=pd.cut(coh['ExperienceYearsAtThisCompany'], bins=[0,5,10,15,20,25,30,35,40], 
                           right=False, labels=['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35+']))
coh = coh.assign(RoleExperCohorts=pd.cut(coh['ExperienceYearsInCurrentRole'], bins=[0,2,4,6,8,10,12,14,16,18], 
                           right=False, labels=['0-1','2-3','4-5','6-7','8-9','10-11','12-13','14-15','16+']))
coh = coh.assign(LastPromoCohorts=pd.cut(coh['YearsSinceLastPromotion'], bins=[0,4,8,12,16], 
                           right=False, labels=['0-3','4-7','8-11','12+']))
coh = coh.assign(CurrManYrsCohorts=pd.cut(coh['YearsWithCurrManager'], bins=[0,5,10,15,20], 
                           right=False, labels=['0-4','5-9','10-14','15+']))

#Performance average per department on other metrics
st.subheader('Bar chart visualizations on performance average per department for selected cohorts')
plt.figure(figsize=(8,4))
for i in coh.select_dtypes(include='category'):
    coh.groupby(['EmpDepartment',i])['PerformanceRating'].mean().unstack(level=1).plot(kind='bar',hatch='')
    plt.title(f"Performance average in {i} per department")
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.6)
    plt.xlabel(f' Departmentwise performance rating average for {i}',fontsize=9)
    plt.ylabel('Perfomance rating average')
    plt.legend(loc='lower right')
    st.pyplot()
st.markdown('''
##### Departmentwise performance rating average per cohort
* Different ages performed differently in different departments. For example the 25-34 age group performed outstandingly in the Data Science compared to all other departments. The age between 15-24 performed well in Development. The age 55+ performed poorly in Finance. The company needs to structure its departments with the correct employee age groups
* Distance is also affecting the perfomance differently. This could be because of the nature of work done by the employees.The company needs to advise their employees on living within the distance that does not incovenience their acess to work
* The hourly rate also has different effects on dirrent departments. The hourly rate of 60-74 seem to have a better balance across all the departments. The company therefore needs to compensate their employees fairly to cultivate a positive mindset among towards better performances
* The salary hike percentage is clearly affecting the employee performance across all the departments. Employees with a salary hike of 20+ percent performed better than all other employees with a lower hike. The issue of undercompensation should be investigated in this company. The company therefore needs to have a standard salary hike percentage that is applied to all employees
* Employees in each department are affected differently according to their work experience. Therefore, it is recommended that each department recruits employees with with the work experience that produces an outstanding performance
* Work Experience in this company shows that employees with 0-9 years experience in the company have a balanced performance. Employees with an experience between 20-29 years in this company had a weak performance across all the departments. It should also be noted that employees with 30+ years experience in the company performed well in Research & Development. The company should therefore address the employee overstay issue in different departments. 
* Research and Sales departments prove a linear relationship between the performance and the 12+ years experience in the roles they are holding. Other departments different results across. Therefore, there are departments whose employees depict job monotony and others are comfortable. The company needs to structure every job role with the time limit the employee can hold the position
* Years since last promotion does not show a clear picture on the performance rating. It keeps changing in every department. Hence the company has to structure the promotion timeline per department
* Data Science, Development and Finance departments clearly indicate that staying with the same manager longer affected their performance negatively. The company should consider constant managr rotation in these departments. On the other hand, Human Resources and Sales departments indicates that the longer an employee stays with the manager the better the performance. Therefore manager rotation should be minimized.

''')
st.write('')
st.write('')

#Selecting remaining rated columns for analysis.
rated_cols=data.loc[:,['EmpEducationLevel','EmpEnvironmentSatisfaction','EmpJobInvolvement',
                       'EmpJobSatisfaction','EmpRelationshipSatisfaction','TrainingTimesLastYear',
                       'EmpWorkLifeBalance','PerformanceRating'
                      ]]
rated_cols.head()

#Visualizing educaion level effect on performance
st.subheader('Education Level vs performance rating')
label1=['Bellow College','College','Bachelor','Master','Doctor']
rated_cols.groupby('EmpEducationLevel')['PerformanceRating'].mean().plot(
    kind='pie',autopct="%1.2f%%",labels=label1,shadow=True,explode=[0.0,0.05,0.12,0.01,0.00],
colors=['#f72020','#20f7da','#05fc0d','#024504','#a35c46'],figsize=(3,3))
plt.xticks(rotation=90)
st.pyplot()
st.markdown('''
* The performance on education level (20.42%), College(20.17%), Master(20.09%),Doctor(19.7%) and Below College was poor at (19.63%). The Bachelor level performeed better than the other because they are in a transition stage to better their careers while below College might have performed poorly because of the lower compensation. Doctor level would have been expected to perfom better but it did not in this case and this could mean such employees are more focused on other projects than work.
* It is therefore recommended that the company focus on hiring Bachelor, College and Masters employees who are more focused to performing better at work. This would in return reduce the escalations and improve the company's Net Promoter Score
''')
st.write('')
st.write('')

#Visualizing environment satisfaction effect on performance
st.subheader('Environment Satisfaction vs performance rating')
label=['Low','Medium','High','Very High']
rated_cols.groupby('EmpEnvironmentSatisfaction')['PerformanceRating'].mean().plot(
    kind='pie',autopct="%1.2f%%",labels=label,shadow=True,explode=[0.0,0.0,0.1,0.02],
colors=['#a35c46','#f72020','#05fc0d','#20f7da'],figsize=(3,3))
plt.xticks(rotation=90)
st.pyplot()
st.markdown('''
* Employees who had a high or very high environment satisfaction performed better.
* The company should therefore do a more analysis on the factors contributing to a high or or very high satisfaction and evaluate whether any changes are necessary to make sure that employees either have a high or very high environment satisfaction.
* Understanding why some employees had a low or medium satifaction could lead to a refined knowledge on how to better the environment
''')
st.write('')
st.write('')

#Visualizing work-life effect on performance
st.subheader('Work-Life Balance vs performance rating')
label2=['Bad','Good','Better','Best']
rated_cols.groupby('EmpWorkLifeBalance')['PerformanceRating'].mean().plot(
    kind='pie',autopct="%1.2f%%",labels=label2,shadow=True,explode=[0.0,0.0,0.02,0.07],
colors=['#f72020','#a35c46','#20f7da','#05fc0d'],figsize=(3,3))
plt.xticks(rotation=90)
st.pyplot()
st.markdown('''
* Employees with the best work-life balance performed better while employees with a Bad work-life balance performed poorly. The company may need to do a more analysis on factors that lead to employees not having a better work-life balance so that during the hiring process such factors can be detected. The company may also need to organize work-life training seminars for its employees
''')
st.write('')
st.write('')

#Visualizing job involvement effect on performance
st.subheader('Job Involvement vs performance rating')
label3=['Low','Medium','High','Very High']
rated_cols.groupby('EmpJobInvolvement')['PerformanceRating'].mean().plot(
    kind='pie',autopct="%1.2f%%",labels=label2,shadow=True,explode=[0.0,0.0,0.02,0.07],
colors=['#f72020','#a35c46','#20f7da','#05fc0d'],figsize=(3,3))
plt.xticks(rotation=90)
st.pyplot()
st.markdown('''
* Those with a Low job involvement performed better. However, it should also noted that the difference between low and very high involvement is only 0.13%. Not such a significant difference.
''')
st.write('')
st.write('')

#Visualizing job satisfaction effect on performance
st.subheader('Job Satisfaction vs performance rating')
label4=['Low','Medium','High','Very High']
rated_cols.groupby('EmpJobSatisfaction')['PerformanceRating'].mean().plot(
    kind='pie',autopct="%1.2f%%",labels=label4,shadow=True,explode=[0.0,0.0,0.0,0.1],
colors=['#20f7da','#a35c46','#f72020','#05fc0d'],figsize=(3,3))
plt.xticks(rotation=90)
st.pyplot()
st.markdown('''
* It should be noted that employees with a very high and low job satisfaction performed better than medium and high job satisfaction. Given that a very high job satisfaction had the best rating, the company should analyze deeper on factors that may be hindering employees job satisfaction from being high.
''')
st.write('')
st.write('')

#Visualizing relationship satisfaction effect on performance
st.subheader('Relationship Satisfaction vs performance rating')
label5=['Low','Medium','High','Very High']
rated_cols.groupby('EmpRelationshipSatisfaction')['PerformanceRating'].mean().plot(
    kind='pie',autopct="%1.2f%%",labels=label5,shadow=True,explode=[0.0,0.02,0.07,0.0],
colors=['#a35c46','#20f7da','#05fc0d','#f72020'],figsize=(3,3))
plt.xticks(rotation=90)
st.pyplot()
st.markdown('''
* There was not significant correlation between performance and relationship satisfaction. The performance was distributed equally
''')
st.write('')
st.write('')

#Visualizing last year training times effect on performance
st.subheader('Last Year Training times vs performance rating')
plt.figure(figsize=(3,3))
rated_cols.groupby('TrainingTimesLastYear')['PerformanceRating'].mean().plot(
    kind='pie',autopct="%1.2f%%",shadow=True,explode=[0.0,0.0,0.04,0.09,0.0,0.02,0.0],
colors=['#f72020','#a35c46','#20f7da','#05fc0d','#5f87a3','#c898d6','#94094e'])
plt.xticks(rotation=90)
st.pyplot()
st.markdown('''
* As noted, employees trained 3 times last year had a better performance
* Employees with 0 training times last year least performed.
* It should however be noted that employees that were trained once or twice has a peformance that was almost the same with a difference of 0.01 percent. 
            Therefore the company should take not of this and avoid using so much funds training employees up to 6 times. The funds should be channelled 
            to training employees who had zero(0) training times to improve their performance
''')

#Hiding the Streamlit rerun menu from the user
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
