# 🌾 Bhāṣāvid 🇮🇳  
### Multilingual AI Trade Companion for Bharat

---

## 📖 Meaning

**Bhāṣāvid (भाषाविद्)** means:

> “One who understands languages.”

The name reflects the purpose of the project — enabling understanding, fairness, and trust across India’s linguistically diverse marketplaces.

---

## 🧩 Problem Statement

Local markets (*mandis*) form the backbone of Bharat’s economy.  
However, everyday trade faces major challenges:

- Language barriers between buyers and sellers  
- Lack of transparency in daily commodity prices  
- Unfair negotiations due to information asymmetry  
- Dependence on middlemen  
- Limited access to digital tools in regional languages  

These issues reduce income for small vendors and weaken trust in local trade systems.

---

## 💡 Solution Overview

**Bhāṣāvid** is a multilingual AI-powered trade companion designed to act as a **real-time linguistic and economic bridge** for Indian local markets.

The platform enables:

- Communication across Indian and global languages  
- Fair market price discovery  
- Respectful, AI-assisted negotiation  
- Voice-first and low-literacy-friendly interaction  

Bhāṣāvid prioritizes **inclusion, transparency, and dignity** in everyday commerce.

---

## ✨ Key Features

### 🌐 Multilingual Communication
- Real-time translation between Indian and international languages  
- Automatic language detection  
- Culturally appropriate phrasing  

### 🎙 Voice + Text Interaction
- Users can type or speak naturally  
- Audio playback of translated messages  
- Accessible for elderly and low-literacy users  

### 💰 AI Price Discovery
- Commodity-based fair price estimation  
- Displays minimum, maximum and average prices  

### 🤝 AI Negotiation Assistant
- Respectful counter-offer suggestions  
- Balanced buyer–seller negotiation logic  

### 🧑‍🌾 Bharat-First Design
- Built specifically for Indian mandis  
- Mobile-friendly and simple interface  

---

## 🎙 Voice Architecture

### Current Flow

```
User Speech
   ↓
Browser Microphone
   ↓
streamlit-mic-recorder
   ↓
Speech → Text
   ↓
AI Translation Pipeline
   ↓
Text Output
   ↓
gTTS (Text → Speech)
```

### Planned Enhancement

- Whisper AI integration for robust multilingual speech recognition  
- Improved accuracy in noisy mandi environments  

---

## 🧠 How Kiro Is Used

This project follows **prompt-driven development** using **Kiro**.

Kiro enables:

- Requirement definition before coding  
- Clear separation of AI responsibilities  
- Transparent and explainable AI behavior  

### Kiro modules:

- Language Bridge prompts  
- Price Discovery prompts  
- Negotiation Assistant prompts  

The `.kiro` directory serves as the AI design blueprint.

---

## 🏗 Architecture Overview

```
User
 │
 ▼
Voice / Text Input
 │
 ▼
Language Detection
 │
 ▼
AI Language Bridge
 │
 ├── Cultural Context
 │── Politeness Control
 │── Trade-aware phrasing
 │
 ▼
Translated Output
 │
 ▼
Price Discovery Module
 │
 ▼
Negotiation Assistant Module
```

---

## 🧩 Modular AI Architecture

Bhāṣāvid is built using a **modular AI architecture**, where each capability operates independently.

### Core Modules

- **Language Bridge**
  - Translation
  - Tone preservation
  - Cultural context awareness  

- **Price Discovery**
  - Market-specific fair pricing  
  - Transparent reasoning  

- **Negotiation Assistant**
  - Ethical bargaining logic  
  - Balanced counter-offer generation  

This modular design enables seamless scaling and future integrations.

---

## 🛠 Technology Stack

### Frontend
- Streamlit

### Backend
- Python 3.10+

### AI & Language
- Language Detection: `langdetect`  
- Translation: `googletrans`  
- Text-to-Speech: `gTTS`  
- Voice Input: `streamlit-mic-recorder`  

### Architecture
- Prompt-driven design using **Kiro**
- Modular AI services
- Session-state managed interactions

---

## ▶ How to Run Locally

```bash
git clone https://github.com/shkashyap-web/bhashavid
cd bhashavid
pip install -r requirements.txt
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

## 🔮 Future Roadmap

- Whisper AI speech recognition  
- Live government mandi price APIs  
- Offline-first mobile deployment  
- Farmer and vendor profiles  
- Image-based crop quality analysis  
- Voice-only interaction mode  

---

## 🌍 Impact

Bhāṣāvid empowers:

- Farmers with price transparency  
- Small vendors with fair negotiations  
- Buyers with informed decisions  
- Tourists with language accessibility  

It bridges not just languages —  
but **economic opportunity gaps**.

---

## 🏁 Hackathon Statement

Built for **AI for Bharat – 26 January Prompt Challenge 🇮🇳**

- Uses Kiro for prompt-driven system design  
- Focused on Bharat-scale inclusion  
- Addresses real-world local trade challenges  

---

### 🇮🇳 Bhāṣāvid  
**Connecting Bharat and the World through Language, Trust & AI**
