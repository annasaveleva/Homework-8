import streamlit as st
import pandas as pd


def do_dataframe(dataframe, save):
    if save:
        df = dataframe.loc[(dataframe['Survived'] == 1) & (dataframe['Fare'] == 0)]
    elif not save:
        df = dataframe.loc[(dataframe['Survived'] == 0) & (dataframe['Fare'] == 0)]
    if df.empty:
        return "There is no items"
    return df

def do_margarita_code():
    st.subheader("Задание")
    st.info("Вывести данные пассажиров с билетом нулевой стоимости, выбрав спасен/нет")
    st.subheader("Решение")

    save = True if st.checkbox("Выжил") else False
    df = pd.read_csv("data.csv")
    st.write(do_dataframe(df, save).reset_index(drop=True))

do_margarita_code()
