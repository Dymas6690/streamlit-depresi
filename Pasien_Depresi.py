import pickle
import streamlit as st

depresi_model = pickle.load(open('depresi_model.sav', 'rb'))

st.logo('depresi.png')
st.title('Data Mining Prediksi Depresi')
st.caption('Input angka 1-10')
col1, col2 = st.columns(2)
with col1 :
    Age = st.number_input ('Input nilai Age/Umur')
with col2 :
    WorkPressure = st.slider ('Input nilai Work Pressure/Tekanan Kerja')
with col1 :
    JobSatisfaction = st.text_slider ('Input nilai Job Satisfaction/Kepuasan Kerja')
with col2 :
    Haveyoueverhadsuicidalthoughts = st.text_selectbox ('Input nilai Have you ever had suicidal thoughts?/Pernahkah Anda memiliki pikiran untuk bunuh diri?',['0','1'])
with col1 :
    WorkHours = st.number_input ('Input nilai Work Hours/Jam Kerja')
with col2 :
    FinancialStress = st.slider ('Input nilai Financial Stress/Tekanan Keuangan')

dep_diagnosis = ''

if st.button('Test Prediksi Depresi'):
    prediction = depresi_model.predict([[Age, WorkPressure, JobSatisfaction, Haveyoueverhadsuicidalthoughts, WorkHours, FinancialStress]])

    if(prediction[0] == 0):
        dep_diagnosis = 'Pasien tidak Depresi'
    else :
        dep_diagnosis = 'Pasien Depresi'

    st.success(dep_diagnosis)
