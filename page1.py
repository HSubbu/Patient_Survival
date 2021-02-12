# app1.py
import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

def app():
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">PATIENT SURVIVAL PREDICTION APP</h1> 
    </div> 
    """   
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 


    #display some plots
    def plot_graphs(data):
        st.header('Some Visualisation of Training Data...')
        sns.set(rc={'figure.figsize':(11.7,8.27),"font.size":20,"axes.titlesize":20,"axes.labelsize":20},style="whitegrid")
        st.subheader('Count plot of Survived Column in Dataset')
        sns.countplot(x=data['Survived_1_year'],color='g',palette='Set1')
        st.pyplot()
    
        numeric_columns=['Patient_Age','Patient_Body_Mass_Index','Diagnosed_Condition','Number_of_prev_cond']
        st.markdown("**Histogram of Numeric Attributes**")
        f=plt.figure(figsize=(20,10))
        i=1
        for col in numeric_columns:
            f.add_subplot(2,2,i)
            sns.histplot(data=data,x=col,hue='Survived_1_year',kde=True,palette='Set1')
            i+=1
        st.pyplot()

    # box plot of numeric variables
        st.markdown('**Box Plots of Numeric Attributes with Survived column as hue**')
        f=plt.figure(figsize=(20,10))
        i=1
        for col in numeric_columns:
            f.add_subplot(2,2,i)
            sns.boxplot(y=col,data=data,x='Survived_1_year',showmeans=True,palette='Set1')
            i+=1
        st.pyplot()
        #countplots of categorical attributes
        st.markdown('**Count plot of Smokers and Rural/Urban with Survived as hue**')
        f=plt.figure(figsize=(20,10))
        f.add_subplot(1,2,1)
        sns.countplot(data['Patient_Smoker'],hue=data['Survived_1_year'],palette='Set1')
        f.add_subplot(1,2,2)
        sns.countplot(data['Patient_Rural_Urban'],hue=data['Survived_1_year'],palette='Set1')
        st.pyplot(f)
        return None
    
    data = pd.read_csv('dataset/patient_survival.csv')#read the csv file into df
    plot_graphs(data) # call the function
