import streamlit as st

def do_margarita_code():
    st.divider()
    st.subheader("Задание")
    st.info("Вывести данные пассажиров с билетом нулевой стоимости, выбрав спасен/нет")
    st.subheader("Решение")

    save = "1" if st.checkbox("Выжил") else "0"

    titanic_save = {}
    titanic_not_save = {}

    with open("data.csv") as data_file:
        next(data_file)
        for line in data_file:

            lst = line.split(',')

            passenger_id = lst[0]
            survived = lst[1]
            p_class = lst[2]
            name = lst[3] + lst[4]
            sex = lst[5]
            age = lst[6]
            sib_sp = lst[7]
            parch = lst[8]
            ticket = lst[9]
            fare = lst[10]
            cabin = lst[11]
            embarked = lst[12]

            if fare == '0' and survived == "1":
                person_info_save = {"passengerId": passenger_id, "survived": survived, "pclass": p_class, "sex": sex,
                               "age": age, "sibSp": sib_sp, "parch": parch, "ticket": ticket, "fare": fare, "cabin": cabin,
                               "embarked": embarked}
                titanic_save[person_info_save] = {name[1: -1]}

            elif fare == '0' and survived == "0":
                person_info_died = {"passengerId": passenger_id, "survived": survived, "pclass": p_class, "sex": sex,
                               "age": age, "sibSp": sib_sp, "parch": parch, "ticket": ticket, "fare": fare, "cabin": cabin,
                               "embarked": embarked}
                titanic_not_save[name[1: -1]] = person_info_died
    data_file.close()

    if save == "1":
        st.dataframe(titanic_save)
    else:
        st.dataframe(titanic_not_save)

    st.divider()