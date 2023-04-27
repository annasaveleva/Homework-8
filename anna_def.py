import streamlit as st
import pandas as pd

def do_anna_code():
    st.title('Home Work 9')
    st.subheader('Задание:')
    st.subheader('Найти количество мужчин и женщин по указанному классу обслуживания')
    st.subheader('Решение:')
    df = pd.read_csv('data.csv')
    pclass = df['Pclass'].unique()
    selected_class = st.selectbox('Выберите класс обслуживания пассажиров:', pclass)
    filtered_df = df[df['Pclass'] == selected_class]
    count_male = (filtered_df[filtered_df['Sex'] == "male"]).shape[0]
    count_female = (filtered_df[filtered_df['Sex'] == "female"]).shape[0]
    st.text(f'Количество мужчин и женщин: Class {selected_class}. men: {count_male}, women: {count_female}')
