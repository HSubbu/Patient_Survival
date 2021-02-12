# app2.py
import streamlit as st
import joblib
import pandas as pd 
def app():
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">PATIENT SURVIVAL PREDICTION APP</h1> 
    </div> 
    """   
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 


    st.header('Model Prediction')
    st.subheader('Model Predicts whether a patient will survive at the end of one year of treatment based on user input of features')
    st.write('Please Enter Patient Attributes for Model Prediction')
    
    #patient previous condition
    A = st.selectbox('What is Patient Previous Condiion "A" ?',(0.0,1.0))#drop down
    B = st.selectbox('What is Patient Previous Condiion "B" ?',(0.0,1.0))#drop down
    C = st.selectbox('What is Patient Previous Condiion "C" ?',(0.0,1.0))#drop down
    D = st.selectbox('What is Patient Previous Condiion "D" ?',(0.0,1.0))#drop down
    E = st.selectbox('What is Patient Previous Condiion "E" ?',(0.0,1.0))#drop down
    
    
    #patient treatment drug
    DX1 = st.selectbox('What is Patient Treated Drug "DX1" ?',(0.0,1.0))#drop down
    DX2 = st.selectbox('What is Patient Treated Drug "DX2" ?',(0.0,1.0))#drop down
    DX3 = st.selectbox('What is Patient Treated Drug "DX3" ?',(0.0,1.0))#drop down
    DX4 = st.selectbox('What is Patient Treated Drug "DX4" ?',(0.0,1.0))#drop down
    DX5 = st.selectbox('What is Patient Treated Drug "DX5" ?',(0.0,1.0))#drop down
    DX6 = st.selectbox('What is Patient Treated Drug "DX6" ?',(0.0,1.0))#drop down
    

    #patient smoker or no
    smoker = st.selectbox('What is Smoking Habit "Yes/No/Cannot Say" ?',('Yes','No','Cannot_Say'))#drop down
    
    if smoker == 'Yes':
        Patient_Smoker_YES =1.0
        Patient_Smoker_NO =0.0
    elif smoker == 'Cannot_Say':
        Patient_Smoker_YES =0.0
        Patient_Smoker_NO =1.0
    else:
        Patient_Smoker_YES =0.0
        Patient_Smoker_NO =1.0

    #patient rural or urban
    geog = st.selectbox('Where does patient stay "Rural/Urban" ?',('Rural','Urban'))#drop down
    if geog == 'Rural':
        Patient_Rural_Urban_RURAL =1.0
        Patient_Rural_Urban_URBAN =0.0
    else:
        Patient_Rural_Urban_RURAL =0.0
        Patient_Rural_Urban_URBAN =1.0

    
    # Number_of_prev_cond
    Number_of_prev_cond= st.number_input("Enter Number of prev condition")
    Number_of_prev_cond = float(Number_of_prev_cond)

    # patient Age
    Patient_Age = st.number_input("Enter Patient Age")
    Patient_Age = float(Patient_Age)
    

    # Diagnosed_Condition
    Diagnosed_Condition = st.number_input("Enter Patient Diagnosed_Condition")
    Diagnosed_Condition = float(Diagnosed_Condition)
    

    #Patient_Body_Mass_Index
    Patient_Body_Mass_Index = st.number_input('Input BMI of Patient', value=1.0)
    Patient_Body_Mass_Index = float(Patient_Body_Mass_Index)
    

    # No_of_treatment_drugs
    No_of_treatment_drugs = DX1+DX2+DX3+DX4+DX5+DX6
    No_of_treatment_drugs = float(No_of_treatment_drugs)

        

    # Load the model from the file 
    XGB_from_joblib = joblib.load('patient_survival.pkl')

    st.write('A dataframe constructed with User Input Attributes is ...')   

    X_test = pd.DataFrame({'Diagnosed_Condition':Diagnosed_Condition,
                        'Patient_Age':Patient_Age,
                        'Patient_Body_Mass_Index':Patient_Body_Mass_Index,
                         'A':A, 'B':B, 'C':C, 'D':D, 'E':E,
                        'Number_of_prev_cond':Number_of_prev_cond, 
                        'DX1':DX1, 'DX2':DX2, 'DX3':DX3, 'DX4':DX4, 'DX5':DX5, 'DX6':DX6,
                        'Patient_Smoker_NO':Patient_Smoker_NO,
                        'Patient_Smoker_YES':Patient_Smoker_YES,
                        'Patient_Rural_Urban_RURAL':Patient_Rural_Urban_RURAL,
                        'Patient_Rural_Urban_URBAN':Patient_Rural_Urban_URBAN, 
                        'No_of_treatment_drugs':No_of_treatment_drugs},index=[1])
    st.write(X_test)

               
    # Use the loaded model to make predictions 
    @st.cache
    def authenticate(username, password):#saved username and password
        return username == "admin" and password == "admin"

    username = st.text_input('username',value='admin') #user input of UN
    password = st.text_input("Password:", value="", type="password")#user input pwd

    st.cache()
    def load_authorize(username,password):
        import time
        time.sleep(5)
        return username,password

    st.cache()
    def predict_model(X):
        result = XGB_from_joblib.predict(X)
        if result == 0:
            answer = 'Not_Survived_1_year'
        else:
            answer = 'Survived_1_year'

        st.subheader('The Model prediction for the given patient....')
        if result==1:
            st.success(answer)
        else:
            st.error(answer)
        prob = pd.DataFrame(XGB_from_joblib.predict_proba(X_test),columns=['Not_Survived','Survived'])
        st.success('Probability for Survived_1_year')
        st.write(prob)
        return None 

    if st.button("Predict"):
        data = load_authorize(username,password)

    if authenticate(username, password):
        st.success('You are authenticated!')
        predict_model(X_test)    
    else:
        st.error('The username or password you have entered is invalid.')
