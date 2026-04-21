import streamlit as st
import json
import os
import random
import base64
import time
import streamlit.components.v1 as components

# ---------- LOAD IMAGE ----------
def get_base64_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64_image("bg.jpg")

# Page state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Memory
MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

# AI
def ask_ai(role, topic):

    if topic == "Should AI replace teachers?":
        pro = "AI can personalize learning and provide 24/7 support."
        against = "AI cannot replace human emotions and mentorship."

    elif topic == "Is social media harmful to society?":
        pro = "Social media connects people globally."
        against = "It harms mental health and spreads misinformation."

    elif topic == "Should college degrees be mandatory for jobs?":
        pro = "Degrees ensure structured education."
        against = "Skills matter more than degrees."

    elif topic == "Is remote work better than office work?":
        pro = "Remote work gives flexibility."
        against = "It reduces collaboration."

    elif topic == "Should governments regulate AI strictly?":
        pro = "Regulation ensures safety."
        against = "It slows innovation."

    elif topic == "Is technology making people less social?":
        pro = "Technology connects people."
        against = "It reduces real interaction."

    elif topic == "Should students rely on AI for studying?":
        pro = "AI helps faster learning."
        against = "It reduces thinking ability."

    elif topic == "Is privacy more important than security?":
        pro = "Privacy protects freedom."
        against = "Security protects society."

    else:
        pro = "Positive view."
        against = "Critical view."

    if role == "pro":
        return pro
    elif role == "against":
        return against
    elif role == "bias":
        return f"Bias Analysis: '{topic}' may include general assumptions."
    else:
        confidence = random.randint(65, 95)
        return f"Balanced decision needed.\n\nConfidence Score: {confidence}%"

# UI CONFIG
st.set_page_config(page_title="AI Debate System")

# ---------- CSS ----------
st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(15,25,20,0.85), rgba(15,25,20,0.95)),
                      url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    color: #FFF7E2;
}}

.title {{
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    margin-top: 40px;
}}

.subtitle {{
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
    margin-bottom: 40px;
}}

.card {{
    background: rgba(79, 99, 61, 0.7);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}}

.stButton > button {{
    background-color: #8BA194;
    color: black;
    border-radius: 10px;
    width: 100%;
}}
</style>
""", unsafe_allow_html=True)

# ---------- HOME ----------
if st.session_state.page == "home":

    st.markdown('<div class="title">Multimind AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Experience AI arguing both sides of reality</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-top:60px;">
        <h3>AI Neural Interaction</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.2, 1, 1.2])

    with col2:
        if st.button("Enter Debate"):
            st.session_state.page = "debate"
            st.rerun()

# Topics
topics = [
    "Should AI replace teachers?",
    "Is social media harmful to society?",
    "Should college degrees be mandatory for jobs?",
    "Is remote work better than office work?",
    "Should governments regulate AI strictly?",
    "Is technology making people less social?",
    "Should students rely on AI for studying?",
    "Is privacy more important than security?"
]

# ---------- ANIMATION ----------
import streamlit.components.v1 as components

def show_ai_animation():
    components.html("""
    <html>
    <head>
    <style>
        body {
            margin: 0;
            background: transparent;
            color: white;
            font-family: sans-serif;
            text-align: center;
        }

        svg {
            width: 300px;
            height: 200px;
            margin-top: 20px;
        }

        .node {
            fill: #8BA194;
            animation: pulse 1.5s infinite;
        }

        .line {
            stroke: #8BA194;
            stroke-width: 2;
            stroke-dasharray: 100;
            stroke-dashoffset: 100;
            animation: draw 2s ease forwards;
        }

        @keyframes draw {
            to { stroke-dashoffset: 0; }
        }

        @keyframes pulse {
            0% { r: 4; opacity: 0.6; }
            50% { r: 6; opacity: 1; }
            100% { r: 4; opacity: 0.6; }
        }
    </style>
    </head>

    <body>

    <svg viewBox="0 0 300 200">

        <!-- Lines -->
        <line x1="50" y1="50" x2="150" y2="100" class="line"/>
        <line x1="150" y1="100" x2="50" y2="150" class="line"/>
        <line x1="150" y1="100" x2="250" y2="80" class="line"/>

        <!-- Nodes -->
        <circle cx="50" cy="50" r="5" class="node"/>
        <circle cx="150" cy="100" r="5" class="node"/>
        <circle cx="50" cy="150" r="5" class="node"/>
        <circle cx="250" cy="80" r="5" class="node"/>

    </svg>

    <h3>AI is connecting ideas...</h3>

    </body>
    </html>
    """, height=260)

# ---------- DEBATE ----------
if st.session_state.page == "debate":

    st.markdown('<div class="title">Debate Arena</div>', unsafe_allow_html=True)

    topic = st.selectbox("Choose Topic", topics)

    if st.button("Run Debate", key="run_btn"):

        placeholder = st.empty()

        with placeholder:
            show_ai_animation()

        time.sleep(5)
        placeholder.empty()

        memory = load_memory()

        pro = ask_ai("pro", topic)
        against = ask_ai("against", topic)
        conclusion = ask_ai("conclusion", topic)
        bias = ask_ai("bias", topic)

        memory.append({"topic": topic, "conclusion": conclusion})
        save_memory(memory)

        st.markdown(f'<div class="card"><h3>🟢 Pro Argument</h3><p>{pro}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card"><h3>🔴 Against Argument</h3><p>{against}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card"><h3>⚖️ Conclusion</h3><p>{conclusion}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card"><h3>🧠 Bias Analysis</h3><p>{bias}</p></div>', unsafe_allow_html=True)

        st.success("Memory updated! 🚀")

    if st.button("⬅ Back", key="back_btn"):
        st.session_state.page = "home"
        st.rerun()

