# ============================================================
# Bhāṣāvid – Multilingual Mandi Assistant
# AI for Bharat | 26 January Prompt Challenge
# ============================================================

import streamlit as st
from gtts import gTTS
from langdetect import detect
from deep_translator import GoogleTranslator
import tempfile
import os
import time

# ------------------------------------------------------------
# Optional microphone input
# ------------------------------------------------------------
try:
    from streamlit_mic_recorder import mic_recorder
    MIC_AVAILABLE = True
except:
    MIC_AVAILABLE = False


# ============================================================
# Supported Languages
# ============================================================

LANGUAGE_MAP = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",

    # Foreign tourists
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Greek": "el",
    "Japanese": "ja",
    "Vietnamese": "vi",
    "Thai": "th",
    "Chinese (Simplified)": "zh-cn"
}

# ============================================================
# Reverse language map (auto-detect → dropdown)
# ============================================================

REVERSE_LANGUAGE_MAP = {
    "en": "English",
    "hi": "Hindi",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "bn": "Bengali",
    "mr": "Marathi",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "el": "Greek",
    "ja": "Japanese",
    "vi": "Vietnamese",
    "th": "Thai",
    "zh-cn": "Chinese (Simplified)"
}

# ============================================================
# Dynamic placeholders
# ============================================================

PLACEHOLDER_MAP = {
    "English": "Example: Could you please reduce the price a little?",
    "Hindi": "उदाहरण: दाम थोड़ा कम कर दीजिए",
    "Tamil": "உதாரணம்: விலையை கொஞ்சம் குறைக்க முடியுமா?",
    "Telugu": "ఉదాహరణ: ధరను కొంచెం తగ్గించగలరా?",
    "Kannada": "ಉದಾಹರಣೆ: ದಯವಿಟ್ಟು ಬೆಲೆಯನ್ನು ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ",
    "Malayalam": "ഉദാഹരണം: വില കുറച്ച് തരാമോ?",
    "Bengali": "উদাহরণ: দাম একটু কম করবেন?",
    "Marathi": "उदाहरण: किंमत थोडी कमी करता का?",
    "Gujarati": "ઉદાહરણ: ભાવ થોડો ઓછો કરશો?",
    "Punjabi": "ਉਦਾਹਰਨ: ਕੀ ਤੁਸੀਂ ਕੀਮਤ ਥੋੜ੍ਹੀ ਘਟਾ ਸਕਦੇ ਹੋ?",
    "French": "Exemple : Pourriez-vous réduire un peu le prix ?",
    "German": "Beispiel: Können Sie den Preis etwas senken?",
    "Italian": "Esempio: Potrebbe ridurre un po' il prezzo?",
    "Greek": "Παράδειγμα: Μπορείτε να μειώσετε λίγο την τιμή;",
    "Japanese": "例：少し値段を下げてもらえますか？",
    "Vietnamese": "Ví dụ: Bạn có thể giảm giá một chút không?",
    "Thai": "ตัวอย่าง: ลดราคานิดหน่อยได้ไหม?",
    "Chinese (Simplified)": "例如：可以稍微便宜一点吗？"
}


# ============================================================
# Text → Speech (safe)
# ============================================================

def text_to_speech(text, lang="en"):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp.name)
        return temp.name
    except:
        return None


# ============================================================
# Page config (mobile-first)
# ============================================================

st.set_page_config(
    page_title="Bhāṣāvid",
    page_icon="🌾",
    layout="centered"
)

def spacer(h=25):
    st.markdown(f"<div style='height:{h}px'></div>", unsafe_allow_html=True)


# ============================================================
# Header
# ============================================================

st.title("🌾 Bhāṣāvid")
st.subheader("Multilingual Mandi Assistant")

st.markdown("""
AI-powered language bridge for Indian local markets and global tourists.

• 🌐 Multilingual communication  
• 🎙️ Voice & text input  
• 🔊 Spoken translations  
• 💰 Fair price discovery  
• 🤝 Ethical negotiation  
""")

st.divider()


# ============================================================
# Session State
# ============================================================

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "auto_source_language" not in st.session_state:
    st.session_state.auto_source_language = "English"


# ============================================================
# Conversation Setup
# ============================================================

st.header("🎧 Conversation Setup")

source_language = st.selectbox(
    "Language you speak",
    list(LANGUAGE_MAP.keys()),
    index=list(LANGUAGE_MAP.keys()).index(
        st.session_state.auto_source_language
    )
)

target_language = st.selectbox(
    "Translate into",
    list(LANGUAGE_MAP.keys()),
    index=0
)

input_mode = st.radio(
    "Input method",
    ["Type text", "Speak using microphone"],
    horizontal=True
)

st.divider()


# ============================================================
# Language Bridge
# ============================================================

st.header("🌐 Language Bridge")

# ---------------- Text input ----------------
if input_mode == "Type text":
    st.session_state.input_text = st.text_area(
        "Enter message",
        value=st.session_state.input_text,
        placeholder=PLACEHOLDER_MAP.get(
            source_language,
            "Enter your message here"
        )
    )

# ---------------- Voice input ----------------
if input_mode == "Speak using microphone":
    if MIC_AVAILABLE:
        mic = mic_recorder(
            start_prompt="🎙️ Start speaking",
            stop_prompt="⏹ Stop",
            just_once=True
        )
        if mic and "text" in mic:
            st.session_state.input_text = mic["text"]
            st.success(mic["text"])
    else:
        st.warning("Microphone not available.")
        st.code("pip install streamlit-mic-recorder")


# ============================================================
# Translation
# ============================================================

if st.button("Translate with Cultural Context"):

    text = st.session_state.input_text.strip()

    if text == "":
        st.warning("Please enter or speak a message.")
    else:
        detected_lang = detect(text)

        auto_language = REVERSE_LANGUAGE_MAP.get(detected_lang)
        if auto_language:
            st.session_state.auto_source_language = auto_language

        st.markdown("### 🔍 Detected Language")
        st.code(detected_lang)

        translator = GoogleTranslator(
            source="auto",
            target=LANGUAGE_MAP[target_language]
        )

        translated = translator.translate(text)
        st.session_state.translated_text = translated

        st.markdown("### 📝 Translated Message")
        st.success(translated)

        st.markdown("### 🧠 Cultural Context Applied")
        st.info("""
Context: Indian local mandi  
Tone: Polite and respectful  
Style: Non-confrontational bargaining  
Intent: Trust-based negotiation
""")

        audio = text_to_speech(
            translated,
            LANGUAGE_MAP[target_language]
        )

        if audio:
            st.audio(audio)
            time.sleep(1)
            try:
                os.remove(audio)
            except:
                pass

        # -------- Conversation history --------
        st.session_state.conversation.append({
            "from": source_language,
            "to": target_language,
            "original": text,
            "translated": translated
        })

st.divider()


# ============================================================
# Live Conversation View
# ============================================================

if st.session_state.conversation:
    st.header("🔁 Live Conversation")

    for msg in st.session_state.conversation:
        st.markdown(f"""
**🗣 {msg['from']} said:**  
{msg['original']}

**➡ Translated to {msg['to']}:**  
{msg['translated']}

---
""")


# ============================================================
# Price Discovery
# ============================================================

st.header("💰 AI Price Discovery")

commodity = st.selectbox(
    "Commodity",
    ["Tomato", "Onion", "Potato", "Wheat", "Rice", "Chilli"]
)

market = st.selectbox(
    "Market",
    [
        "Delhi Azadpur",
        "Bengaluru KR Market",
        "Mumbai Vashi",
        "Chennai Koyambedu",
        "Kolkata Mechua",
        "Pune Gultekdi"
    ]
)

if st.button("Get Fair Price"):
    st.success("₹22 – ₹28 per kg (Average ₹25)")

st.divider()


# ============================================================
# Negotiation Assistant
# ============================================================

st.header("🤝 AI Negotiation Assistant")

buyer = st.number_input("Buyer price (₹/kg)", 1, 100, 20)
seller = st.number_input("Seller price (₹/kg)", 1, 100, 30)

if st.button("Suggest Counter Offer"):
    st.info(f"Suggested fair price: ₹{int((buyer + seller)/2)} per kg")


# ============================================================
# Footer
# ============================================================

st.caption(
    "Built for AI for Bharat • 26 January Prompt Challenge 🇮🇳"
)
