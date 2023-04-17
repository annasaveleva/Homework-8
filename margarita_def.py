import streamlit as st

def do_margarita_code():
    st.divider()
    st.subheader("Задание")
    st.info("Вывести данные пассажиров с билетом нулевой стоимости, выбрав спасен/нет")
    st.subheader("Решение")
    st.text("И тут такая выводится программа Риты")

    save = "1" if st.checkbox("Выжил") else "0"

    with open("data.csv") as data_file:
        next(data_file)
        for line in data_file:
            lst = line.split(',')
            survived = lst[1]
            fare = lst[10]
            if fare == '0':
                if survived == save:
                    st.text(line.rstrip())
                if survived == save:
                    st.text(line.rstrip())
    data_file.close()
    st.divider()
