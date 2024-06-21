import streamlit as st
from index_plate_calculator import calculate_turns

st.title("Indexing Plate Calculator")
st.write("This tool will guide you in selecting the right indexing plate for your Brown and Sharpe indexing head.")

# User input
teeth = st.number_input("Enter the number of teeth of the gear", min_value=1, step=1)

if st.button("Calculate"):
    result = calculate_turns(teeth)
    st.write(result)