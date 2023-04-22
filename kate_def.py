import streamlit as st

st.text("Посчитать количество пассажиров (выбрав пол, и спасенных или погибших)")

def do_kate_code():
    st.title('пассажиры Титаника')

    if st.checkbox("Спасен?"):
        save = '1'
    else:
        save = '0'

    with open("data.csv") as titanic_file:
        count_save_male = 0
        count_save_female = 0
        count_died_female = 0
        count_died_male = 0
        next(titanic_file)
        for line in titanic_file:
            lst = line.split(",")
            sex = lst[5]
            survived = lst[1]
            if sex == 'male':
                if save == '1' and save == survived:
                    count_save_male += 1
                elif save == '0' and save == survived:
                    count_died_male += 1
            elif sex == 'female':
                if save == '1' and save == survived:
                    count_save_female += 1
                elif save == '0' and save == survived:
                    count_died_female += 1
    if save == '1':
        st.text(f'количество спасенных мужчин {count_save_male}')
        st.text(f'количество спасенных женщин {count_save_female}')
    else:
        st.text(f'количество погибших мужчин {count_died_male}')
        st.text(f'количество погибших женщин {count_died_female}')