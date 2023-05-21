import streamlit as st
import pandas as pd


def count_men_women_of_selected_class(df, selected_class):
    filtered_df = df[df['Pclass'] == selected_class]
    count_male = (filtered_df[filtered_df['Sex'] == "male"]).shape[0]
    count_female = (filtered_df[filtered_df['Sex'] == "female"]).shape[0]
    return count_male, count_female


def do_anna_code():
    st.title('Home Work 9')
    st.subheader('Задание:')
    st.subheader('Найти количество мужчин и женщин по указанному классу обслуживания')
    st.subheader('Решение:')
    df = pd.read_csv('data.csv')
    pclass = df['Pclass'].unique()
    selected_class = st.selectbox('Выберите класс обслуживания пассажиров:', pclass)
    count_men_women_of_selected_class(df, selected_class)
    count_male, count_female = count_men_women_of_selected_class(df, selected_class)

    st.text(f'Количество мужчин и женщин: Class {selected_class}. men: {count_male}, women: {count_female}')
