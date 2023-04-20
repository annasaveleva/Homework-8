import streamlit as st
import pandas as pd


def do_margarita_code():
    st.subheader("Задание")
    st.info("Вывести данные пассажиров с билетом нулевой стоимости, выбрав спасен/нет")
    st.subheader("Решение")

    save = True if st.checkbox("Выжил") else False

    df = pd.read_csv("data.csv")

    if save:
        st.write(df.loc[(df['Survived'] == 1) & (df['Fare'] == 0)])
    elif not save:
        st.write(df.loc[(df['Survived'] == 0) & (df['Fare'] == 0)])
