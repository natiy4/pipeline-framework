import streamlit as st
import requests
import json
st.title('test UI ')
t1 = st.text_input('enter1')
t2 = st.text_input('enter2')
t3 = st.text_input('enter3')
t4 = st.text_input('enter4')
if st.button :

    params= {'t1':t1, 't2':t2}
    url = 'http://localhost:5000/set'
    r = requests.post(url,
            data=json.dumps(params))


