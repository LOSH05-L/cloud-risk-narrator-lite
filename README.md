# 🌩️ Offline Cloud Narrator Lite

**A solo, fully offline AI-powered weather narration app built overnight for the Edunet Azure AI Internship 2025.**  
This lightweight dashboard transforms a satellite cloud image into multilingual voice forecasts using free tools—no cloud services or external APIs needed.

---

## 🎯 Features

- 🌥️ Displays satellite cloud image showing cyclone activity
- 🎙️ Narrates weather forecast in **English, Hindi, and Telugu**
- 🔊 Interactive audio playback powered by offline TTS tools
- 🖥️ Built with Python + Streamlit for clean UI and fast performance
- 🚫 No internet dependency or cloud APIs—100% offline

---

## 🛠️ Tools Used

| Component           | Tool / Method                       |
|--------------------|-------------------------------------|
| Image Visualization | Static cloud image (`cloud_sample.jpg`) |
| Narration Generation | Manual scripting + GPT inspiration |
| Translation         | Google Translate (web-based)        |
| Voice Synthesis     | TTSMP3.com / FreeTTS (free tools)   |
| Frontend Dashboard  | Streamlit (`app.py`)                |
| Audio Playback      | Streamlit’s native `st.audio()`     |

---

## 🚀 How to Run

1. Clone or download this repo  
2. Install dependencies:
   ```bash
   pip install streamlit
