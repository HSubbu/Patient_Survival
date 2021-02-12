# mainpage.py
import streamlit as st
import pandas as pd 
import seaborn as sns
import joblib
import numpy as np
import cv2
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

def app():
    #personalise home page
    #display thayer school logo
    #imagee = cv2.imread('images/new_logo.png')
    #cv2.imshow('Image', imagee)
    #st.image(imagee, caption='Thayer School of Engineering at Dartmouth')http
    st.markdown("![Thayer School of Engineering at Dartmouth](http://smt.iconnect007.com/files/5815/0593/2065/ThayerLogo.jpg)")

    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">PATIENT SURVIVAL PREDICTION APP</h1> 
    </div> 
    """      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 



    #create containers
    header = st.beta_container()
    #dataset = st.beta_container()
    #features = st.beta_container()
    #model_training = st.beta_container()

    #write in header section
    with header:
        st.title("PCADS- CAPSTONE PROJECT")
        st.text('Developed by ....Subramanian Hariharan ')
        st.text('Date ...........February 2021')
        st.markdown("> “You can have data without information, but you cannot have information without data.” \n\n—Daniel Keys Moran")
        st.header('Problem Statement')
        st.markdown("""The dataset is sourced from open domain and is about data related to a hospital in Greenland. It is the responsibility of Hospital Administration to provide efficient and timely patient care to ensure that the individual concerned recovers from the illness completely. The Hospital admistration is seeking answers for improving the standard 
                of medical care by addressing related factors. The data is related to a particular department in the Hospital where mortality rate is beyond acceptable levels. Accordingly, it is understood that towards this, the data related to patient has been obtained from multiple SQL tables in the database and collated. The historical data collates information 
                regarding demographics of the patient as well as treatment and medical condition and includes a binary variable which indicates whether the patient survived at the end of 12 months of care. The attributes  which affect the patient survival in a significant way can also be flagged.
                """)
        st.markdown("""**The **Objective** of the Project is to analyse the factors given in the dataset and predict chance of survival of patient at the end of 12 months of treatment. 
                with dataset**""")
        st.header('PATIENT DATASET')
        st.text('This Dataset is available in open domain...https://dphi.tech/')
    data = pd.read_csv('dataset/patient_survival.csv')#read the csv file into df
    #function to show first five rows of trg dataset
    def view_dataset(data):
        st.text('A glance at top 5 rows of Training dataset')
        s = data.head().style.background_gradient(cmap='viridis')
        st.dataframe(s) # output first 5 lines of dataset
        return None 
    view_dataset(data) #call function
    


