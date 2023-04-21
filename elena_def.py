import streamlit as st
def do_elena_code():
    st.header ("Веб-приложение на Streamlit :globe_with_meridians:")
    st.subheader ("Задание:")
    st.info ("Посчитать долю пассажиров, указав: вести поиск среди спасенных или погибших, искать в возрастных группах «до 30 лет» или «старше 60»")
    st.subheader ("Результат:")
    st.info ("Чтобы узнать долю пассажиров Титаника в процентах, установите параметры :point_down:")

    saved = True if st.checkbox("Поставьте галочку, если пассажир спасен") else False
    choise = st.radio("Выберите возрастную группу:" , ["моложе 30", "старше 60"])

    with open("data.csv") as file:
        next(file)
        count_all = 0
        count_favorites_young = 0
        count_favorites_old = 0
        count_young = 0
        count_old = 0
        for line in file:
            count_all +=1
            lst = line.split(',')
            age = lst[6]
            save = lst[1]
            if age < '30' :
                if save == '1':
                    count_favorites_young +=1
                else:
                    count_young +=1
            if age > '60':
                if save == '1':
                    count_favorites_old += 1
                else:
                    count_old +=1
    if saved and choise == "моложе 30":
        st.success(f"Ответ: {round((count_favorites_young/count_all)*100)} %")
    elif not saved and choise == "моложе 30":
        st.success(f"Ответ: {round((count_young/count_all)*100)} %")
    if saved and choise == "старше 60":
        st.success(f"Ответ: {round((count_favorites_old/count_all)*100)} %")
    elif not saved and choise == "старше 60":
        st.success(f"Ответ: {round((count_old/count_all)*100)} %")