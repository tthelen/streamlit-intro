import streamlit as st

st.header("Hello, world!")

if st.button("Cheers!"):
    st.balloons()

if st.button("Don't click me!"):
    st.error("You clicked the button!")