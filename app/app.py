import streamlit as st

st.set_page_config(page_title="Offline Cloud Narrator", layout="centered")

st.title("🌩️ Offline Cloud Narrator")
st.image("data/cloud_sample.jpg", caption="Cyclonic Cloud System")

st.subheader("English Forecast")
st.audio("audio/forecast_en.mp3")

st.subheader("Telugu Forecast")
st.audio("audio/forecast_te.mp3")

st.subheader("Hindi Forecast")
st.audio("audio/forecast_hi.mp3")
