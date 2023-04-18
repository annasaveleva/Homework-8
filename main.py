import kate_def as kate_def
import elena_def as elena_def
import ingrida_def as ingrida_def
import anna_def as anna_def
import margarita_def as margarita_def
import anastasia_def as anastasia_def
import yulia_def as yulia_def
import streamlit as st

st.image("https://animeshka.org/uploads/posts/2023-01/1675139931_animeshka-org-p-titanic-background-vkontakte-4.jpg")

st.title("Работа с Титаником")

KATE = "Екатерина П. (kat-1003) - вариант 8"
ELENA = "Елена П. (ProkhorovaElena) - вариант 9"
INGRIDA = "Ингрида С. (Ingridik177) - вариант 12"
ANNA = "Анна С. (annasaveleva) - вариант 13"
MARGARITA = "Маргарита Ф. (f-morgan) - вариант 7"
ANASTASIA = "Анастасия Ш. (Asharpilova) - вариант 11"
YULIA = "Юлия Ш. (yulschew4uck) - вариант 12"

members_list = [KATE, ELENA, INGRIDA, ANNA, MARGARITA, ANASTASIA, YULIA]

member = st.radio("Выберите, какую задачу хотите просмотреть", members_list)

if member == KATE:
    kate_def.do_kate_code()
elif member == ELENA:
    elena_def.do_elena_code()
elif member == INGRIDA:
    ingrida_def.do_ingrida_code()
elif member == ANNA:
    anna_def.do_anna_code()
elif member == MARGARITA:
    margarita_def.do_margarita_code()
elif member == ANASTASIA:
    anastasia_def.do_anastasia_code()
elif member == YULIA:
    yulia_def.do_yulia_code()
else:
    print("Девушки возражают - выбран неверный вариант!")

