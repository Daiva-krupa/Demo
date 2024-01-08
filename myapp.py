import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("types of Dogs")

col1,col2,col3=st.columns(3)
with col1:
  st.subheader("Retriever Dog")
  st.image("./Retriver.jpg",width=500,use_column_width=True)
  st.write("Retriver dogs are honest and faithfull")

with col2:
  st.subheader("Shitzu Dog")
  st.image("./Shitzu.jpg",,width=500,use_column_width=True)
  st.write("Shitzu dogs are small and cute")

with col3:
  st.subheader("Bull Dog")
  st.image("./Bull.jpg",,width=500,use_column_width=True)
  st.write("Bull dogs are much aggressive")
