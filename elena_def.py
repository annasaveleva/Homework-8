import streamlit as st


def count_people(file):
    count_all = 0
    count_favorites_young = 0
    count_favorites_old = 0
    count_young = 0
    count_old = 0
    for line in file:
        count_all += 1
        lst = line.split(',')
        age = lst[6]
        save = lst[1]
        if age and float(age) < 30:
            if save == '1':
                count_favorites_young += 1
            elif save == '0':
                count_young += 1
        if age and float(age) > 60:
            if save == '1':
                count_favorites_old += 1
            elif save == '0':
                count_old += 1
    return count_all, count_favorites_young, count_favorites_old, count_young, count_old


def do_elena_code():
    st.subheader("Задание:")
    st.info("Посчитать долю пассажиров, указав: вести поиск среди спасенных или погибших, "
            "искать в возрастных группах «до 30 лет» или «старше 60»")
    st.subheader("Результат:")
    st.info("Чтобы узнать долю пассажиров в процентах, установите параметры :point_down:")

    saved = True if st.checkbox("Поставьте галочку, если пассажир спасен") else False
    choice = st.radio("Выберите возрастную группу:", ["моложе 30", "старше 60"])

    with open("data.csv") as file:
        next(file)
        count_all, count_favorites_young, count_favorites_old, count_young, count_old = count_people(file)

    if saved and choice == "моложе 30":
        st.success(f"Ответ: {round((count_favorites_young/count_all)*100)} %")
    elif not saved and choice == "моложе 30":
        st.success(f"Ответ: {round((count_young/count_all)*100)} %")
    if saved and choice == "старше 60":
        st.success(f"Ответ: {round((count_favorites_old/count_all)*100)} %")
    elif not saved and choice == "старше 60":
        st.success(f"Ответ: {round((count_old/count_all)*100)} %")
