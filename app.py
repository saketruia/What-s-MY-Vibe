import streamlit as st
from textblob import TextBlob

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background: linear-gradient(to right, #8360c3, #2ebf91);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.2);
    }
    h1 {
        font-family: 'Segoe UI', sans-serif;
        color: white;
        font-size: 48px !important;
        text-align: center;
    }
    .vibe-box {
        text-align: center;
        padding: 30px;
        background-color: rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        margin-top: 30px;
        font-size: 32px;
        color: white;
        font-weight: bold;
    }
    textarea {
        font-size: 18px !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1>🔮 What's My Vibe?</h1>", unsafe_allow_html=True)

# Prompt
st.markdown("<p style='text-align:center; font-size:20px; color:white;'>Type about your day, your thoughts, or your mood — and let me read your vibe 😌</p>", unsafe_allow_html=True)

# Input
user_input = st.text_area(" ", placeholder="How are you feeling today...")

# Vibe Detector
def get_vibe(score):
    if score > 0.5:
        return "😄 Happy Vibes"
    elif score > 0:
        return "🙂 Chill Vibes"
    elif score == 0:
        return "😐 Neutral Vibes"
    elif score > -0.5:
        return "😕 Lowkey Sad Vibes"
    else:
        return "😭 Deep Sad Vibes"

# Button
if st.button("🧠 Detect My Vibe"):
    if user_input:
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        vibe = get_vibe(sentiment)

        st.markdown(f"<div class='vibe-box'>{vibe}<br><span style='font-size:18px'>(Score: {sentiment:.2f})</span></div>", unsafe_allow_html=True)
    else:
        st.warning("Please type something first!")
