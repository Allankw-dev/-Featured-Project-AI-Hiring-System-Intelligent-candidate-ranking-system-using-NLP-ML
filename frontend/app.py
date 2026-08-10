import streamlit as st
import streamlit.components.v1 as components

from pages import home
from pages import login
from pages import sign_up
from pages import dashboard
from pages import jobs
from pages import applications
from pages import upload_resume
from pages import profile
from pages import admin_panel
from pages import forgot_password
from pages import reset_password

st.set_page_config(page_title="AI Hiring System", page_icon="🤖", layout="wide")

# ---------------------------
# GLOBAL STYLES
# ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Exo+2:wght@300;400;600;700&display=swap');

.stApp {
    background: #000510 !important;
    background-image:
        radial-gradient(ellipse at 20% 50%, rgba(120,40,200,0.15) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(40,80,200,0.12) 0%, transparent 45%) !important;
    color: #e2e8f0;
    font-family: 'Exo 2', sans-serif;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1300px;
}

section[data-testid="stSidebar"] {
    background: rgba(9, 1, 24, 0.97);
    border-right: 1px solid rgba(139, 92, 246, 0.2);
}

div.stButton > button {
    background: linear-gradient(135deg, rgba(139,92,246,0.15), rgba(59,130,246,0.15)) !important;
    border: 1px solid rgba(139,92,246,0.5) !important;
    color: #c4b5fd !important;
    border-radius: 10px !important;
    font-family: 'Exo 2', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 1.2rem !important;
    letter-spacing: 1px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 0 12px rgba(139,92,246,0.2) !important;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, rgba(139,92,246,0.3), rgba(59,130,246,0.3)) !important;
    box-shadow: 0 0 25px rgba(139,92,246,0.5), 0 0 50px rgba(139,92,246,0.2) !important;
    border-color: #8b5cf6 !important;
    color: #ffffff !important;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stNumberInput"] input {
    background: rgba(139,92,246,0.05) !important;
    border: 1px solid rgba(139,92,246,0.25) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
    font-family: 'Exo 2', sans-serif !important;
}

div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: #8b5cf6 !important;
    box-shadow: 0 0 15px rgba(139,92,246,0.4) !important;
}

label {
    color: #a78bfa !important;
    font-family: 'Exo 2', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
}

div[data-testid="stTabs"] button {
    color: rgba(167,139,250,0.6) !important;
    font-family: 'Exo 2', sans-serif !important;
    font-weight: 600 !important;
}

div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #a78bfa !important;
    border-bottom: 2px solid #8b5cf6 !important;
    text-shadow: 0 0 15px rgba(139,92,246,0.8) !important;
}

div[data-testid="stSelectbox"] > div {
    background: rgba(139,92,246,0.05) !important;
    border: 1px solid rgba(139,92,246,0.25) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

div[role="radiogroup"] {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 10px;
}

div[role="radiogroup"] label {
    background: rgba(139,92,246,0.06);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 10px;
    padding: 6px 14px;
    transition: all 0.2s ease;
}

div[role="radiogroup"] label:hover {
    background: rgba(139,92,246,0.15);
    border-color: rgba(139,92,246,0.5);
    box-shadow: 0 0 12px rgba(139,92,246,0.3);
}

div[role="radiogroup"] label p {
    color: #c4b5fd !important;
    font-family: 'Exo 2', sans-serif !important;
    font-weight: 600 !important;
}

div[data-testid="stRadio"] > label { display: none; }

div[data-testid="stAlert"] {
    border-radius: 10px !important;
    border-left: 3px solid #8b5cf6 !important;
    background: rgba(139,92,246,0.08) !important;
}

hr { border-color: rgba(139,92,246,0.2) !important; }

div[data-testid="stDataFrame"] {
    border: 1px solid rgba(139,92,246,0.2) !important;
    border-radius: 10px !important;
}

.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139,92,246,0.6), rgba(59,130,246,0.6), transparent);
    margin: 1rem 0;
    border: none;
    box-shadow: 0 0 10px rgba(139,92,246,0.3);
}

.nav-bar {
    background: rgba(9,1,24,0.85);
    border: 1px solid rgba(139,92,246,0.25);
    border-radius: 14px;
    padding: 12px 18px;
    margin-bottom: 16px;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 30px rgba(139,92,246,0.08), inset 0 1px 0 rgba(139,92,246,0.1);
}

.nav-label {
    color: rgba(167,139,250,0.5);
    font-size: 0.7rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.status-box {
    padding: 0.7rem 1.2rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    font-weight: 600;
}

.status-admin {
    background: rgba(139,92,246,0.1);
    color: #c4b5fd;
    border: 1px solid rgba(139,92,246,0.35);
    box-shadow: 0 0 20px rgba(139,92,246,0.15), inset 0 0 20px rgba(139,92,246,0.05);
}

.status-candidate {
    background: rgba(59,130,246,0.1);
    color: #93c5fd;
    border: 1px solid rgba(59,130,246,0.35);
    box-shadow: 0 0 20px rgba(59,130,246,0.15), inset 0 0 20px rgba(59,130,246,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SESSION DEFAULTS
# ---------------------------
if "token" not in st.session_state:
    st.session_state.token = None
if "role" not in st.session_state:
    st.session_state.role = None
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------------------
# AUTO DETECT RESET TOKEN
# ---------------------------
reset_token = st.query_params.get("reset_token", "")
if reset_token and st.session_state.page != "Reset Password":
    st.session_state.page = "Reset Password"

# ---------------------------
# HELPERS
# ---------------------------
def is_logged_in():
    return st.session_state.get("token") is not None

def is_admin():
    return st.session_state.get("role") == "admin"

def is_candidate():
    return st.session_state.get("role") == "candidate"

def logout():
    st.session_state.token = None
    st.session_state.role = None
    st.session_state.user_email = None
    st.session_state.page = "Home"
    st.rerun()

def route_guard(page_name: str):
    public_pages = ["Home", "Login", "Sign Up", "Forgot Password", "Reset Password"]
    candidate_pages = ["Dashboard", "Jobs", "Applications", "Upload Resume", "Profile"]
    admin_pages = ["Admin Panel"]

    if page_name in public_pages:
        return

    if page_name in candidate_pages:
        if not is_logged_in():
            st.warning("Please log in first.")
            st.session_state.page = "Login"
            st.rerun()
        if not is_candidate():
            st.error("Access denied. Candidates only.")
            st.session_state.page = "Home"
            st.rerun()

    if page_name in admin_pages:
        if not is_logged_in():
            st.warning("Please log in first.")
            st.session_state.page = "Login"
            st.rerun()
        if not is_admin():
            st.error("Access denied. Admins only.")
            st.session_state.page = "Home"
            st.rerun()

# ---------------------------
# TOP NAVIGATION
# ---------------------------
nav_pages = [
    "Home", "Login", "Sign Up", "Dashboard", "Jobs",
    "Applications", "Upload Resume", "Profile", "Admin Panel"
]

current_nav_page = st.session_state.page if st.session_state.page in nav_pages else "Home"

st.markdown('<div class="nav-bar"><div class="nav-label">Navigation</div>', unsafe_allow_html=True)

col_nav, col_user = st.columns([9, 1])

with col_nav:
    selected_page = st.radio(
        "Navigation",
        nav_pages,
        index=nav_pages.index(current_nav_page),
        horizontal=True,
        label_visibility="collapsed"
    )

with col_user:
    if is_logged_in():
        if st.button("Logout"):
            logout()

st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.page in nav_pages and selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()

st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

# ---------------------------
# LOGIN STATUS
# ---------------------------
if is_logged_in() and st.session_state.user_email:
    if is_admin():
        st.markdown(
            f'<div class="status-box status-admin">🛡️ Logged in as Admin • {st.session_state.user_email}</div>',
            unsafe_allow_html=True
        )
    elif is_candidate():
        st.markdown(
            f'<div class="status-box status-candidate">👤 Logged in as Candidate • {st.session_state.user_email}</div>',
            unsafe_allow_html=True
        )

# ---------------------------
# ROUTING
# ---------------------------
page = st.session_state.page
route_guard(page)

if page == "Home":
    home.render()
elif page == "Login":
    login.render()
elif page == "Sign Up":
    sign_up.render()
elif page == "Dashboard":
    dashboard.render()
elif page == "Jobs":
    jobs.render()
elif page == "Applications":
    applications.render()
elif page == "Upload Resume":
    upload_resume.render()
elif page == "Profile":
    profile.render()
elif page == "Admin Panel":
    admin_panel.render()
elif page == "Forgot Password":
    forgot_password.render()
elif page == "Reset Password":
    reset_password.render()
else:
    st.session_state.page = "Home"
    st.rerun()

# ---------------------------
# AI ASSISTANT CHAT BUBBLE
# ---------------------------
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: transparent; }

.chat-bubble { position: fixed; bottom: 24px; right: 24px; z-index: 9999; }

.bubble-btn {
    width: 62px; height: 62px; border-radius: 50%;
    background: radial-gradient(circle at 35% 35%, #1e1040, #0d0820);
    border: 1.5px solid rgba(139,92,246,0.5);
    cursor: pointer; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 0 20px rgba(124,58,237,0.4), 0 0 40px rgba(124,58,237,0.15);
    transition: all 0.3s; position: relative;
}
.bubble-btn:hover { box-shadow: 0 0 30px rgba(124,58,237,0.7); transform: scale(1.05); }

.orbital-container { width: 62px; height: 62px; position: relative; display: flex; align-items: center; justify-content: center; }
.core { width: 22px; height: 22px; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #a78bfa, #6d28d9); box-shadow: 0 0 12px rgba(167,139,250,0.8); position: absolute; z-index: 3; animation: corePulse 2s ease-in-out infinite; }
@keyframes corePulse { 0%,100%{box-shadow:0 0 12px rgba(167,139,250,0.8);transform:scale(1)} 50%{box-shadow:0 0 20px rgba(167,139,250,1);transform:scale(1.1)} }

.ring { position: absolute; border-radius: 50%; border: 1.5px solid transparent; }
.ring-1 { width: 46px; height: 46px; border-color: rgba(139,92,246,0.7) transparent rgba(139,92,246,0.7) transparent; animation: spin1 2s linear infinite; }
.ring-2 { width: 58px; height: 20px; border-color: rgba(59,130,246,0.6) transparent; animation: spin2 3s linear infinite reverse; transform: rotateX(70deg); }
.ring-3 { width: 54px; height: 54px; border-color: transparent rgba(192,132,252,0.5) transparent rgba(192,132,252,0.5); animation: spin3 4s linear infinite; transform: rotate(45deg); }
.dot { width: 5px; height: 5px; border-radius: 50%; position: absolute; }
.dot-1 { background: #a78bfa; box-shadow: 0 0 6px rgba(167,139,250,1); animation: orbit1 2s linear infinite; }
.dot-2 { background: #60a5fa; box-shadow: 0 0 6px rgba(96,165,250,1); animation: orbit2 3s linear infinite reverse; }

@keyframes spin1 { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
@keyframes spin2 { from{transform:rotateX(70deg) rotate(0deg)} to{transform:rotateX(70deg) rotate(360deg)} }
@keyframes spin3 { from{transform:rotate(45deg)} to{transform:rotate(405deg)} }
@keyframes orbit1 { from{transform:rotate(0deg) translateX(23px) rotate(0deg)} to{transform:rotate(360deg) translateX(23px) rotate(-360deg)} }
@keyframes orbit2 { from{transform:rotate(0deg) translateX(27px) rotate(0deg)} to{transform:rotate(360deg) translateX(27px) rotate(-360deg)} }

.notif-dot { position: absolute; top: 2px; right: 2px; width: 13px; height: 13px; background: #10b981; border-radius: 50%; border: 2px solid #000510; animation: notifPulse 2s infinite; z-index: 10; }
@keyframes notifPulse { 0%,100%{transform:scale(1)} 50%{transform:scale(1.4)} }

.chat-window {
    position: fixed; bottom: 96px; right: 24px;
    width: 360px; height: 520px;
    background: rgba(4,6,22,0.97);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 20px; display: flex; flex-direction: column;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.6), 0 0 40px rgba(139,92,246,0.15);
    transform-origin: bottom right;
    transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
}
.chat-window.hidden { transform: scale(0.8); opacity: 0; pointer-events: none; }

.chat-header {
    padding: 14px 16px;
    background: rgba(139,92,246,0.1);
    border-bottom: 1px solid rgba(139,92,246,0.2);
    display: flex; align-items: center; gap: 12px;
}
.header-orbital { width: 38px; height: 38px; position: relative; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.header-core { width: 14px; height: 14px; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #a78bfa, #6d28d9); box-shadow: 0 0 8px rgba(167,139,250,0.8); position: absolute; z-index: 2; animation: corePulse 2s ease-in-out infinite; }
.header-ring { position: absolute; border-radius: 50%; border: 1px solid transparent; }
.hr1 { width: 28px; height: 28px; border-color: rgba(139,92,246,0.6) transparent rgba(139,92,246,0.6) transparent; animation: spin1 2s linear infinite; }
.hr2 { width: 34px; height: 14px; border-color: rgba(59,130,246,0.5) transparent; animation: spin2 3s linear infinite reverse; transform: rotateX(70deg); }

.header-name { font-size: 14px; font-weight: 700; color: #e2e8f0; font-family: sans-serif; }
.header-status { font-size: 11px; color: #10b981; display: flex; align-items: center; gap: 4px; margin-top: 2px; font-family: sans-serif; }
.status-dot { width: 6px; height: 6px; background: #10b981; border-radius: 50%; animation: notifPulse 2s infinite; }
.close-btn { background: none; border: none; cursor: pointer; color: rgba(148,163,184,0.6); font-size: 16px; padding: 6px; border-radius: 8px; margin-left: auto; }
.close-btn:hover { color: #e2e8f0; background: rgba(255,255,255,0.08); }

.chat-messages { flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.chat-messages::-webkit-scrollbar { width: 4px; }
.chat-messages::-webkit-scrollbar-thumb { background: rgba(139,92,246,0.3); border-radius: 2px; }

.message { display: flex; gap: 8px; align-items: flex-end; }
.message.user { flex-direction: row-reverse; }
.msg-avatar { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; flex-shrink: 0; background: linear-gradient(135deg, #7c3aed, #4f46e5); }
.msg-avatar.user-av { background: rgba(59,130,246,0.25); border: 1px solid rgba(59,130,246,0.4); }
.msg-bubble { max-width: 78%; padding: 10px 14px; border-radius: 16px; font-size: 13px; line-height: 1.6; font-family: sans-serif; }
.msg-bubble.ai { background: rgba(139,92,246,0.1); border: 1px solid rgba(139,92,246,0.2); color: #e2e8f0; border-bottom-left-radius: 4px; }
.msg-bubble.user { background: linear-gradient(135deg, rgba(124,58,237,0.3), rgba(79,70,229,0.3)); border: 1px solid rgba(139,92,246,0.35); color: #e2e8f0; border-bottom-right-radius: 4px; }

.typing { display: flex; gap: 4px; align-items: center; padding: 12px 14px; }
.typing span { width: 7px; height: 7px; background: rgba(139,92,246,0.6); border-radius: 50%; animation: bounce 1.4s infinite; }
.typing span:nth-child(2) { animation-delay: 0.2s; }
.typing span:nth-child(3) { animation-delay: 0.4s; }
@keyframes bounce { 0%,60%,100%{transform:translateY(0)} 30%{transform:translateY(-8px)} }

.quick-replies { display: flex; flex-wrap: wrap; gap: 6px; padding: 0 16px 12px; }
.quick-btn { padding: 5px 12px; background: rgba(139,92,246,0.08); border: 1px solid rgba(139,92,246,0.25); border-radius: 999px; color: #a78bfa; font-size: 11px; cursor: pointer; font-family: sans-serif; }
.quick-btn:hover { background: rgba(139,92,246,0.18); }

.chat-input-area { padding: 12px 14px; border-top: 1px solid rgba(139,92,246,0.15); display: flex; gap: 8px; align-items: center; }
.chat-input { flex: 1; padding: 10px 14px; background: rgba(139,92,246,0.06); border: 1px solid rgba(139,92,246,0.2); border-radius: 12px; color: #e2e8f0; font-size: 13px; outline: none; resize: none; font-family: sans-serif; }
.chat-input:focus { border-color: rgba(139,92,246,0.5); }
.chat-input::placeholder { color: rgba(100,116,139,0.6); }
.send-btn { width: 38px; height: 38px; background: linear-gradient(135deg, #7c3aed, #4f46e5); border: none; border-radius: 10px; cursor: pointer; color: white; font-size: 16px; flex-shrink: 0; }
.send-btn:hover { transform: scale(1.05); }
</style>
</head>
<body>

<div class="chat-bubble">
    <button class="bubble-btn" onclick="toggleChat()">
        <div class="orbital-container">
            <div class="ring ring-1"></div>
            <div class="ring ring-2"></div>
            <div class="ring ring-3"></div>
            <div class="dot dot-1"></div>
            <div class="dot dot-2"></div>
            <div class="core"></div>
        </div>
        <div class="notif-dot" id="notifDot"></div>
    </button>
</div>

<div class="chat-window hidden" id="chatWindow">
    <div class="chat-header">
        <div class="header-orbital">
            <div class="header-ring hr1"></div>
            <div class="header-ring hr2"></div>
            <div class="header-core"></div>
        </div>
        <div style="flex:1">
            <div class="header-name">Hira — AI Assistant</div>
            <div class="header-status"><div class="status-dot"></div> Online · Powered by Claude AI</div>
        </div>
        <button class="close-btn" onclick="toggleChat()">✕</button>
    </div>

    <div class="chat-messages" id="messages">
        <div class="message">
            <div class="msg-avatar">🤖</div>
            <div class="msg-bubble ai">
                👋 Hi! I'm <strong>Hira</strong>, your AI hiring assistant powered by Claude.<br><br>
                Ask me anything — resume tips, job matching, scoring, interview advice, or anything else!
            </div>
        </div>
    </div>

    <div class="quick-replies" id="quickReplies">
        <button class="quick-btn" onclick="sendQuick('How does AI scoring work?')">How scoring works?</button>
        <button class="quick-btn" onclick="sendQuick('Give me resume tips')">Resume tips</button>
        <button class="quick-btn" onclick="sendQuick('How do I apply for jobs?')">How to apply?</button>
        <button class="quick-btn" onclick="sendQuick('What is fraud detection?')">Fraud detection</button>
    </div>

    <div class="chat-input-area">
        <textarea class="chat-input" id="chatInput" placeholder="Ask me anything..." rows="1"
            onkeydown="if(event.key==='Enter'&&!event.shiftKey){event.preventDefault();sendMessage()}"
            oninput="this.style.height='auto';this.style.height=Math.min(this.scrollHeight,80)+'px'"></textarea>
        <button class="send-btn" onclick="sendMessage()">➤</button>
    </div>
</div>

<script>
let isOpen = false;
let conversationHistory = [];

const SYSTEM_PROMPT = `You are Hira, an AI assistant for an AI-powered hiring platform. You help both candidates and admins.

PLATFORM DETAILS:
- Built with FastAPI backend, Streamlit frontend, PostgreSQL (Supabase) database
- AI scoring: Semantic (45%), Skills (25%), Experience (20%), Verification (10%)
- Features: Resume upload, AI scoring, job matching, fraud detection, admin panel
- Fraud detection: keyword stuffing, inconsistent dates, short resumes, missing contact info
- Candidates: sign up, upload resumes, apply for jobs, track applications in dashboard
- Admins: post jobs, view top candidates, shortlist/reject, send emails to candidates

Be helpful, concise, friendly and accurate. Answer ANY question asked.
For platform questions give specific accurate details.
For general questions (career advice, resume writing, interview tips) give expert advice.
Keep responses under 200 words unless more detail is genuinely needed.`;

async function callClaude(message) {
    conversationHistory.push({ role: "user", content: message });
    try {
        const response = await fetch("https://api.anthropic.com/v1/messages", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                model: "claude-sonnet-4-6",
                max_tokens: 1000,
                system: SYSTEM_PROMPT,
                messages: conversationHistory
            })
        });
        const data = await response.json();
        const reply = data.content[0].text;
        conversationHistory.push({ role: "assistant", content: reply });
        return reply;
    } catch (err) {
        return "Sorry, I'm having trouble connecting right now. Please try again!";
    }
}

function toggleChat() {
    isOpen = !isOpen;
    document.getElementById('chatWindow').classList.toggle('hidden', !isOpen);
    document.getElementById('notifDot').style.display = isOpen ? 'none' : 'block';
    if (isOpen) document.getElementById('chatInput').focus();
}

function sendQuick(text) {
    document.getElementById('chatInput').value = text;
    sendMessage();
}

function addMessage(text, isUser) {
    const msgs = document.getElementById('messages');
    const div = document.createElement('div');
    div.className = `message${isUser ? ' user' : ''}`;
    div.innerHTML = `
        <div class="msg-avatar${isUser ? ' user-av' : ''}">${isUser ? '👤' : '🤖'}</div>
        <div class="msg-bubble ${isUser ? 'user' : 'ai'}">${text.replace(/\n/g,'<br>').replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>')}</div>
    `;
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
}

function addTyping() {
    const msgs = document.getElementById('messages');
    const div = document.createElement('div');
    div.className = 'message'; div.id = 'typing';
    div.innerHTML = `<div class="msg-avatar">🤖</div><div class="msg-bubble ai"><div class="typing"><span></span><span></span><span></span></div></div>`;
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
}

function removeTyping() {
    const t = document.getElementById('typing');
    if (t) t.remove();
}

async function sendMessage() {
    const input = document.getElementById('chatInput');
    const text = input.value.trim();
    if (!text) return;
    addMessage(text, true);
    input.value = '';
    input.style.height = 'auto';
    document.getElementById('quickReplies').style.display = 'none';
    addTyping();
    const reply = await callClaude(text);
    removeTyping();
    addMessage(reply, false);
}
</script>
</body>
</html>
""", height=0, scrolling=False)