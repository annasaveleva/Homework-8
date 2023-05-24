import streamlit as st
import pandas as pd


def mean_age_for_class(data, selected_class):
    filtered_data = data[data['Pclass'] == selected_class]
    return filtered_data['Age'].mean()


def do_ingrida_code():
    st.subheader("Задание")
    st.info("Найти средний возраст пассажиров по каждому указанному классу обслуживания (Pclass)")
    st.subheader("Решение")
    st.write("---")
    data = pd.read_csv('data.csv')
    class_list = data['Pclass'].unique()
    selected_class = st.selectbox('Выберите класс обслуживания пассажиров:', class_list)
    mean_age = mean_age_for_class(data, selected_class)
    st.write(f'Средний возраст пассажиров в классе {selected_class} равен {mean_age:.2f} лет.')
