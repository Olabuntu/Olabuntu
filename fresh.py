import streamlit as st
import pandas as pd

unit = 1
all = 0
st.title('BUNTU GPA CALCULATOR')

a = int(st.number_input('NUMBER OF COURSE', min_value=0, step=1))
for i in range(a):
    n = st.text_input(f'{i+1}.COURSE NAME').capitalize()

    if n:
        u =int(st.number_input(f'{n} UNIT', min_value=1, max_value=5 , step=1))
        s = int(st.number_input(f'{n} SCORE', min_value=0, max_value=100 , step=1))
        unit += u -1
        if s >= 70: 
            sum = u * 4 
        elif 60 <= s <= 69:
            sum = u * 3
        elif 50 <= s <= 59:
            sum = u * 2
        elif 45 <= s <= 49:
            sum = u * 1
        else:
            sum = 0
        all += sum

if st.button('Calculate GPA'):


    total = all/unit  
     
    st.write(f'GPA = {total}')   

