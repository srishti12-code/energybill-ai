import streamlit as st

st.title("Electricity Bill Automation")

uploaded_file = st.file_uploader(
    "Upload Bill Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.success("Bill uploaded successfully!")
