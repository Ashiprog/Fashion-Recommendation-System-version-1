import streamlit as st
st.title("Fashion Recommender")
query = st.text_input("What are you looking for suggestions?")
if st.button("Find"):
    if query:
        st.write(f"searching for {query}")
    else:
        st.write("Please enter what you are looking for suggestions")
