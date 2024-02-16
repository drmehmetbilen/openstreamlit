import streamlit as st
from oiManager import OiManager

if "first_run" not in st.session_state:
    st.session_state.first_run = True
    st.session_state.oai = OiManager()



if userInput:=st.chat_input("Sorunuzu yazınız..."):
    with st.chat_message("user"):
        st.write(userInput)

    response = st.session_state.oai.runModel(userInput)
    with st.chat_message("assistant"):
        st.write(response)
    





