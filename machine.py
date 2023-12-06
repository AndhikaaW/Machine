import pickle
import streamlit as st
import pandas as pd
import numpy as np
from playsound import playsound

page = st.sidebar.selectbox('Select Page',['Home','Grafik','Prediction','About'])
st.sidebar.caption('Andhika Wahyu Agustian')
st.sidebar.caption('223307090')
st.sidebar.caption('Betrant Wiprazzia Mezaluna')
st.sidebar.caption('223307091')
st.sidebar.caption('Bintang Teja Permana')
st.sidebar.caption('223307092')

model = pickle.load(open('model_prediksi_type_mesin.sav', 'rb'))

if page=='Home':
    st.title('Prediksi torsi Mesin')
    st.image('mesin.jpg',width=400)
    st.header('Dataset')
    df1 = pd.read_csv('PrediksiMesin.csv')
    st.dataframe(df1)

elif page=='Grafik':
    df1 = pd.read_csv('PrediksiMesin.csv')
    chart_air_temperature = pd.DataFrame(df1, columns=["Air_temperature"])
    chart_process_temperature = pd.DataFrame(df1, columns=["Process_temperature"])
    chart_rpm = pd.DataFrame(df1, columns=["Rotational_speed"])

    grafik = st.selectbox('Pilih Grafik', ['Air temperature', 'Process temperature', 'Rotational speed'])
    if grafik=='Air temperature':
        chart = st.selectbox('Silahkan pilih :' , ['line chart' , 'area chart', 'bar chart'])
        if chart=='line chart':
            st.write('Grafik line Air Temperature')
            st.line_chart(chart_air_temperature)
        elif chart=='area chart':
            st.write('Grafik area Air Temperature')
            st.area_chart(chart_air_temperature)
        elif chart=='bar chart':
            st.write('Grafik bar Air Temperature')
            st.bar_chart(chart_air_temperature)
    if grafik=='Process temperature':
        chart = st.selectbox('Silahkan pilih :' , ['line chart' , 'area chart', 'bar chart'])
        if chart=='line chart':
            st.write('Grafik line Process Temperature')
            st.line_chart(chart_process_temperature)
        elif chart=='area chart':
            st.write('Grafik area Process Temperature')
            st.area_chart(chart_process_temperature)
        elif chart=='bar chart':
            st.write('Grafik bar Process Temperature')
            st.bar_chart(chart_process_temperature)
    if grafik=='Rotational speed':
        chart = st.selectbox('Silahkan pilih :' , ['line chart' , 'area chart', 'bar chart'])
        if chart=='line chart':
            st.write('Grafik line RPM')
            st.line_chart(chart_rpm)
        elif chart=='area chart':
            st.write('Grafik area RPM')
            st.area_chart(chart_rpm)
        elif chart=='bar chart':
            st.write('Grafik bar RPM')
            st.bar_chart(chart_rpm)
    
elif page=='Prediction':
    df1 = pd.read_csv('PrediksiMesin.csv')
    air_temperature = st.number_input("Air temperature ", 0,10000)
    process_temperature = st.number_input("Process temperature ", 0,10000)
    rpm = st.number_input("Rotational speed ", 0,10000)

    if st.button('Prediksi'):
        torsiprediction = model.predict([[air_temperature, process_temperature, rpm]])

        torsi_machine_str = np.array(torsiprediction)
        torsi_machine_float = float(torsi_machine_str[0])

        torsi_machine_formatted = "{:,.2f}".format(torsi_machine_float)
        st.write('maka torsi mesin yang dihasilkan : ')
        st.success(torsi_machine_formatted)
elif page=='About':
    st.title('by Kelompok 3')
    st.markdown('Kurang lebihnya mohon maaf')
    st.balloons()

    audio_file='akhirnya.mp3'
    st.audio(playsound(audio_file))
    
