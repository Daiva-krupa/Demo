import streamlit as st
st.set_page_config(page_title='Dogs')

st.markdown("<h3 style='color: pink;font-size:36px'>Types of Dogs</h3>", unsafe_allow_html=True)

st.markdown("<h3 style='color: blue;'>Retriever Dog</h3>", unsafe_allow_html=True)
st.image("./Retriver.jpg",width=200,use_column_width=True)
st.write("Retriver dogs are honest and faithfull")

st.subheader("Shitzu Dog")
st.image("./Shitzu.jpg",width=200,use_column_width=True)
st.write("Shitzu dogs are small and cute")

st.subheader("Bull Dog")
st.image("./Bulldog.jpg",width=200,use_column_width=True)
st.write("Bull dogs are much aggressive")


st.subheader("Alaskan Dog")
st.image("./Alaskan.jpg",width=200,use_column_width=True)
st.write("Alaskans are intelligent and active")


st.subheader("Beagle Dog")
st.image("./Beagle.jpg",width=200,use_column_width=True)
st.write("Beagles are loving and lovable")
