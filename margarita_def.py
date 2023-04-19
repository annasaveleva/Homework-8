import streamlit as st
import pandas as pd

def do_margarita_code():
    st.subheader("Задание")
    st.info("Вывести данные пассажиров с билетом нулевой стоимости, выбрав спасен/нет")
    st.subheader("Решение")

    save = "1" if st.checkbox("Выжил") else "0"

    df = pd.read_csv("data.csv")

    if save == "1":
        st.write(df.loc[(df['Survived'] == 1) & (df['Fare'] == 0)])
    else:
        st.write(df.loc[(df['Survived'] == 0) & (df['Fare'] == 0)])