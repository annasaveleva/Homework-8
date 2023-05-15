import streamlit as st
import pandas as pd



def process(df, save):
    df = df.loc[(df['Survived'] == save)].groupby(['Sex'])['Survived'].count().reset_index(name='count')
    male, female = df['count'].values[1], df['count'].values[0]
    return male, female


def do_kate_code():
    st.text("Посчитать количество пассажиров (выбрав пол, и спасенных или погибших)")
    st.title('пассажиры Титаника')

    if st.checkbox("Спасен?"):
        save = '1'
    else:
        save = '0'
    df = pd.read_csv("data.csv")
    df = process(df, int(save))
    if save == '1':
        st.text(f'количество спасенных мужчин {df[0]}')
        st.text(f'количество спасенных женщин {df[1]}')
    else:
        st.text(f'количество погибших мужчин {df[0]}')
        st.text(f'количество погибших женщин {df[1]}')


do_kate_code()
