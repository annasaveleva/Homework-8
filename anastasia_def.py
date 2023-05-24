import streamlit as st
import csv

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def count_middle_price(csv_file):
    sur_price = 0
    no_sur_price = 0
    survived = 0
    no_survived = 0
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count >= 0:
            if row["Survived"] == "1" and isfloat(row["Fare"]):
                sur_price += float(row["Fare"])
                survived += 1
            elif row["Survived"] == "0" and isfloat(row["Fare"]):
                no_sur_price += float(row["Fare"])
                no_survived += 1
        line_count += 1
    sur_midl_price = sur_price / survived
    no_sur_midl_price = no_sur_price / no_survived
    return sur_midl_price, no_sur_midl_price


def do_anastasia_code():
    st.title("Титаник")
    st.subheader("Задание")
    st.info("Посчитать среднюю стоимость билета (поле Fare) у пассажиров, указав - спасен или нет")
    st.subheader("Решение")
    st.write("---")

    variables = ["Спасен", "Не спасен"]

    # Устанавливаем значение по умолчанию для списка
    default_variable = variables[0]

    # Создаем выпадающее меню для выбора переменной
    selected_variable = st.selectbox("Выберите Значение:", variables, index=variables.index(default_variable))

    with open('data.csv', mode='r') as csv_file:
        sur_midl_price, no_sur_midl_price = count_middle_price(csv_file)

    # Создаем выбранную пользователем переменную
    if selected_variable == "Спасен":
        st.write("Средняя стоимость билета для спасенных: {:.2f}".format(sur_midl_price))
    elif selected_variable == "Не спасен":
        st.write("Средняя стоимость билета для не спасенных: {:.2f}".format(no_sur_midl_price))

do_anastasia_code()
