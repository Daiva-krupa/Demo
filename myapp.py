import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Types of Dogs")

col1,col2,col3,col4=st.columns(4)
with col1:
  st.subheader("Retriever Dog")
  st.image("./Retriver.jpg",width=600,use_column_width=True)
  st.write("Retriver dogs are honest and faithfull")

with col2:
  st.subheader("Shitzu Dog")
  st.image("./Shitzu.jpg",width=500,use_column_width=True)
  st.write("Shitzu dogs are small and cute")

with col3:
  st.subheader("Bull Dog")
  st.image("./Bulldog.jpg",width=600,use_column_width=True)
  st.write("Bull dogs are much aggressive")


with col3:
  st.subheader("Alaskan Dog")
  st.image("./Alaskan.jpg",width=600,use_column_width=True)
  st.write("Alaskans are intelligent and active")


with col4:
  st.subheader("Beagle Dog")
  st.image("./Beagle.jpg",width=600,use_column_width=True)
  st.write("Beagles are loving and lovable")
