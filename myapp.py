import streamlit as st
st.set_page_config(page_title='Cats')
st.header("types of Cats")

col1,col2=st.columns(2)
with col1:
  st.subheader("Retriever Dog")
  st.image("./Retriver.jpg",width=500,use_column_width=True)
  st.write("Retriver dogs are honest and faithfull")

with col2:
  st.subheader("Shitzu Dog")
  st.image("./Shitzu.jpg",,width=500,use_column_width=True)
  st.write("Shitzu dogs are small and cute")
