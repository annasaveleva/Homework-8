import streamlit as st
import csv

def do_anastasia_code():
    st.title("Титаник")

    st.subheader("Задание")
    st.info("Посчитать среднюю стоимость билета (поле Fare) у пассажиров, указав - спасен или нет")
    st.subheader("Решение")
    st.write("---")

    Sur_midl_price = 0
    NoSur_midl_price = 0
    Sur_price = 0
    NoSur_price = 0
    Survived = 0
    no_Survived = 0

    variables = ["Спасен", "Не спасен"]

    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                if row["Survived"] == "1":
                    Sur_price += float(row["Fare"])
                    Survived += 1
                else:
                    NoSur_price += float(row["Fare"])
                    no_Survived += 1
            line_count += 1
        Sur_midl_price = Sur_price / Survived
        NoSur_midl_price = NoSur_price / no_Survived
        titanic = Sur_midl_price, NoSur_midl_price

    # Устанавливаем значение по умолчанию для списка
    default_variable = variables[0]

    # Создаем выпадающее меню для выбора переменной
    selected_variable = st.selectbox("Выберите Значение:", variables, index=variables.index(default_variable))

    # Создаем выбранную пользователем переменную
    if selected_variable == "Спасен":
        st.write("Средняя стоимость билета для спасенных: {:.2f}".format(Sur_midl_price))
    elif selected_variable == "Не спасен":
        st.write("Средняя стоимость билета для не спасенных: {:.2f}".format(NoSur_midl_price))
