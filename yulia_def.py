import streamlit as st
import pandas as pd


def mean_age_for_class(data, selected_class):
    # Фильтруем данные по выбранному классу и находим средний возраст
    filtered_data = data[data['Pclass'] == selected_class]
    mean_age = filtered_data['Age'].mean()
    return mean_age


def do_yulia_code():
    st.subheader("Задание")
    st.info("Найти средний возраст пассажиров по каждому указанному классу обслуживания (Pclass)")
    st.subheader("Решение")
    st.write("---")
    data = pd.read_csv('data.csv')
# Создаем список классов обслуживания
    class_list = data['Pclass'].unique()
# Создаем выпадающее меню для выбора класса обслуживания
    selected_class = st.selectbox('Выберите класс обслуживания пассажиров:', class_list)
    mean_age = mean_age_for_class(data, selected_class)
# Выводим данные в приложение по выбору класса обслуживания пассажиров
    st.write(f'Средний возраст пассажиров в классе {selected_class} равен {mean_age:.2f} лет.')
