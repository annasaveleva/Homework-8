import streamlit as st
st.text("Посчитать количество пассажиров (выбрав пол, и спасенных или погибших)")
def do_kate_code():
st.title('пассажиры Титаника')
if st.chekbox("Спасен?"):
   save = '1'
else:
   save = '0'
with open("data.csv") as titanic_file:
    count_male = 0
    count_female = 0
    str = line.split(',')[5]
    for line in titanic_file:
       if str = "sex"
	   continue
	    if str == 'male'
	       count_male += 1
st.text(f'количество мужчин' {count_male})
