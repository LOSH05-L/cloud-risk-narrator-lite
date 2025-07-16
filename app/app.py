import streamlit as st

# Page setup
st.set_page_config(page_title="Offline Cloud Narrator", layout="centered")

# Title
st.markdown("<h1 style='text-align:center;'>🌩️ Offline Cloud Narrator Lite</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Multilingual Weather Forecast from Cyclone Imagery</h4>", unsafe_allow_html=True)

# Display cloud image
st.image("data/cloud_sample.jpg", caption="Cyclonic Cloud System over Southern India", use_column_width=True)

# Language selector
st.subheader("🎙️ Choose Your Forecast Language")
language = st.radio("", ["English", "Telugu", "Hindi"])

# Play selected audio
if language == "English":
    st.audio("audio/forecast_en.mp3.mp3")
elif language == "Telugu":
    st.audio("audio/forecast_te.mp3.mp3")
elif language == "Hindi":
    st.audio("audio/forecast_hi.mp3.mp3")

# Footer
st.markdown("---")
st.markdown("✅ Built by Lucky | 🕒 Submitted for Edunet Azure AI Internship | 🔒 Runs entirely offline", unsafe_allow_html=True)
