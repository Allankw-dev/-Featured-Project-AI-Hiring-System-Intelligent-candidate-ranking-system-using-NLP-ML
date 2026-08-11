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
st.markdown("""
<style>
.chat-bubble-wrap { position: fixed; bottom: 24px; right: 24px; z-index: 9999; }

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
.ai-core { width: 22px; height: 22px; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #a78bfa, #6d28d9); box-shadow: 0 0 12px rgba(167,139,250,0.8); position: absolute; z-index: 3; animation: aiCorePulse 2s ease-in-out infinite; }
@keyframes aiCorePulse { 0%,100%{box-shadow:0 0 12px rgba(167,139,250,0.8);transform:scale(1)} 50%{box-shadow:0 0 20px rgba(167,139,250,1);transform:scale(1.1)} }

.ai-ring { position: absolute; border-radius: 50%; border: 1.5px solid transparent; }
.ai-ring-1 { width: 46px; height: 46px; border-color: rgba(139,92,246,0.7) transparent rgba(139,92,246,0.7) transparent; animation: aiSpin1 2s linear infinite; }
.ai-ring-2 { width: 58px; height: 20px; border-color: rgba(59,130,246,0.6) transparent; animation: aiSpin2 3s linear infinite reverse; transform: rotateX(70deg); }
.ai-ring-3 { width: 54px; height: 54px; border-color: transparent rgba(192,132,252,0.5) transparent rgba(192,132,252,0.5); animation: aiSpin3 4s linear infinite; transform: rotate(45deg); }
.ai-dot { width: 5px; height: 5px; border-radius: 50%; position: absolute; }
.ai-dot-1 { background: #a78bfa; box-shadow: 0 0 6px rgba(167,139,250,1); animation: aiOrbit1 2s linear infinite; }
.ai-dot-2 { background: #60a5fa; box-shadow: 0 0 6px rgba(96,165,250,1); animation: aiOrbit2 3s linear infinite reverse; }

@keyframes aiSpin1 { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
@keyframes aiSpin2 { from{transform:rotateX(70deg) rotate(0deg)} to{transform:rotateX(70deg) rotate(360deg)} }
@keyframes aiSpin3 { from{transform:rotate(45deg)} to{transform:rotate(405deg)} }
@keyframes aiOrbit1 { from{transform:rotate(0deg) translateX(23px) rotate(0deg)} to{transform:rotate(360deg) translateX(23px) rotate(-360deg)} }
@keyframes aiOrbit2 { from{transform:rotate(0deg) translateX(27px) rotate(0deg)} to{transform:rotate(360deg) translateX(27px) rotate(-360deg)} }

.ai-notif { position: absolute; top: 2px; right: 2px; width: 13px; height: 13px; background: #10b981; border-radius: 50%; border: 2px solid #000510; animation: aiNotif 2s infinite; z-index: 10; }
@keyframes aiNotif { 0%,100%{transform:scale(1)} 50%{transform:scale(1.4)} }

.ai-chat-window {
    position: fixed; bottom: 96px; right: 24px;
    width: 360px; height: 520px;
    background: rgba(4,6,22,0.97);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 20px; display: flex; flex-direction: column;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.6), 0 0 40px rgba(139,92,246,0.15);
    transform-origin: bottom right;
    transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
    z-index: 9998;
}
.ai-chat-window.ai-hidden { transform: scale(0.8); opacity: 0; pointer-events: none; }

.ai-chat-header {
    padding: 14px 16px;
    background: rgba(139,92,246,0.1);
    border-bottom: 1px solid rgba(139,92,246,0.2);
    display: flex; align-items: center; gap: 12px; flex-shrink: 0;
}
.ai-header-orbital { width: 38px; height: 38px; position: relative; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.ai-header-core { width: 14px; height: 14px; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #a78bfa, #6d28d9); box-shadow: 0 0 8px rgba(167,139,250,0.8); position: absolute; z-index: 2; animation: aiCorePulse 2s ease-in-out infinite; }
.ai-header-ring { position: absolute; border-radius: 50%; border: 1px solid transparent; }
.ahr1 { width: 28px; height: 28px; border-color: rgba(139,92,246,0.6) transparent rgba(139,92,246,0.6) transparent; animation: aiSpin1 2s linear infinite; }
.ahr2 { width: 34px; height: 14px; border-color: rgba(59,130,246,0.5) transparent; animation: aiSpin2 3s linear infinite reverse; transform: rotateX(70deg); }

.ai-header-name { font-size: 14px; font-weight: 700; color: #e2e8f0; }
.ai-header-status { font-size: 11px; color: #10b981; display: flex; align-items: center; gap: 4px; margin-top: 2px; }
.ai-status-dot { width: 6px; height: 6px; background: #10b981; border-radius: 50%; animation: aiNotif 2s infinite; }
.ai-close-btn { background: none; border: none; cursor: pointer; color: rgba(148,163,184,0.6); font-size: 16px; padding: 6px; border-radius: 8px; margin-left: auto; }
.ai-close-btn:hover { color: #e2e8f0; background: rgba(255,255,255,0.08); }

.ai-messages { flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.ai-messages::-webkit-scrollbar { width: 4px; }
.ai-messages::-webkit-scrollbar-thumb { background: rgba(139,92,246,0.3); border-radius: 2px; }

.ai-msg { display: flex; gap: 8px; align-items: flex-end; }
.ai-msg.ai-user { flex-direction: row-reverse; }
.ai-avatar { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; flex-shrink: 0; background: linear-gradient(135deg, #7c3aed, #4f46e5); }
.ai-avatar.ai-uav { background: rgba(59,130,246,0.25); border: 1px solid rgba(59,130,246,0.4); }
.ai-bubble { max-width: 78%; padding: 10px 14px; border-radius: 16px; font-size: 13px; line-height: 1.6; }
.ai-bubble.ai-bot { background: rgba(139,92,246,0.1); border: 1px solid rgba(139,92,246,0.2); color: #e2e8f0; border-bottom-left-radius: 4px; }
.ai-bubble.ai-usr { background: linear-gradient(135deg, rgba(124,58,237,0.3), rgba(79,70,229,0.3)); border: 1px solid rgba(139,92,246,0.35); color: #e2e8f0; border-bottom-right-radius: 4px; }

.ai-typing { display: flex; gap: 4px; align-items: center; padding: 12px 14px; }
.ai-typing span { width: 7px; height: 7px; background: rgba(139,92,246,0.6); border-radius: 50%; animation: aiBounce 1.4s infinite; }
.ai-typing span:nth-child(2) { animation-delay: 0.2s; }
.ai-typing span:nth-child(3) { animation-delay: 0.4s; }
@keyframes aiBounce { 0%,60%,100%{transform:translateY(0)} 30%{transform:translateY(-8px)} }

.ai-quick { display: flex; flex-wrap: wrap; gap: 6px; padding: 0 16px 12px; flex-shrink: 0; }
.ai-qbtn { padding: 5px 12px; background: rgba(139,92,246,0.08); border: 1px solid rgba(139,92,246,0.25); border-radius: 999px; color: #a78bfa; font-size: 11px; cursor: pointer; }
.ai-qbtn:hover { background: rgba(139,92,246,0.18); }

.ai-input-area { padding: 12px 14px; border-top: 1px solid rgba(139,92,246,0.15); display: flex; gap: 8px; align-items: center; flex-shrink: 0; }
.ai-input { flex: 1; padding: 10px 14px; background: rgba(139,92,246,0.06); border: 1px solid rgba(139,92,246,0.2); border-radius: 12px; color: #e2e8f0; font-size: 13px; outline: none; resize: none; font-family: inherit; }
.ai-input:focus { border-color: rgba(139,92,246,0.5); }
.ai-input::placeholder { color: rgba(100,116,139,0.6); }
.ai-send { width: 38px; height: 38px; background: linear-gradient(135deg, #7c3aed, #4f46e5); border: none; border-radius: 10px; cursor: pointer; color: white; font-size: 16px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; }
.ai-send:hover { transform: scale(1.05); }
</style>

<div class="chat-bubble-wrap">
    <button class="bubble-btn" onclick="aiToggleChat()">
        <div class="orbital-container">
            <div class="ai-ring ai-ring-1"></div>
            <div class="ai-ring ai-ring-2"></div>
            <div class="ai-ring ai-ring-3"></div>
            <div class="ai-dot ai-dot-1"></div>
            <div class="ai-dot ai-dot-2"></div>
            <div class="ai-core"></div>
        </div>
        <div class="ai-notif" id="aiNotifDot"></div>
    </button>
</div>

<div class="ai-chat-window ai-hidden" id="aiChatWindow">
    <div class="ai-chat-header">
        <div class="ai-header-orbital">
            <div class="ai-header-ring ahr1"></div>
            <div class="ai-header-ring ahr2"></div>
            <div class="ai-header-core"></div>
        </div>
        <div style="flex:1">
            <div class="ai-header-name">Hira — AI Assistant</div>
            <div class="ai-header-status"><div class="ai-status-dot"></div> Online · Powered by Claude AI</div>
        </div>
        <button class="ai-close-btn" onclick="aiToggleChat()">✕</button>
    </div>

    <div class="ai-messages" id="aiMessages">
        <div class="ai-msg">
            <div class="ai-avatar">🤖</div>
            <div class="ai-bubble ai-bot">
                👋 Hi! I'm <strong>Hira</strong>, your AI hiring assistant powered by Claude.<br><br>
                Ask me anything — resume tips, job matching, scoring, interview advice, or anything else!
            </div>
        </div>
    </div>

    <div class="ai-quick" id="aiQuickReplies">
        <button class="ai-qbtn" onclick="aiSendQuick('How does AI scoring work?')">How scoring works?</button>
        <button class="ai-qbtn" onclick="aiSendQuick('Give me resume tips')">Resume tips</button>
        <button class="ai-qbtn" onclick="aiSendQuick('How do I apply for jobs?')">How to apply?</button>
        <button class="ai-qbtn" onclick="aiSendQuick('What is fraud detection?')">Fraud detection</button>
    </div>

    <div class="ai-input-area">
        <textarea class="ai-input" id="aiChatInput" placeholder="Ask me anything..." rows="1"
            onkeydown="if(event.key==='Enter'&&!event.shiftKey){event.preventDefault();aiSendMessage()}"
            oninput="this.style.height='auto';this.style.height=Math.min(this.scrollHeight,80)+'px'"></textarea>
        <button class="ai-send" onclick="aiSendMessage()">➤</button>
    </div>
</div>

<script>
let aiIsOpen = false;
let aiHistory = [];

const AI_SYSTEM = `You are Hira, an AI assistant for an AI-powered hiring platform. You help both candidates and admins.

PLATFORM DETAILS:
- Built with FastAPI backend, Streamlit frontend, PostgreSQL on Supabase
- AI scoring weights: Semantic 45%, Skills 25%, Experience 20%, Verification 10%
- Features: Resume upload (PDF), AI scoring, job matching, fraud detection, admin panel
- Fraud detection: keyword stuffing, inconsistent dates, short resumes, missing contact info
- Candidates: sign up, upload resumes, apply for jobs, track applications in dashboard
- Admins: post/edit/delete jobs, view top 20 candidates, shortlist/reject, send emails

Be helpful, concise, friendly and accurate. Answer ANY question asked.
Keep responses under 200 words unless more detail is genuinely needed.`;

async function aiCallClaude(message) {
    aiHistory.push({ role: "user", content: message });
    try {
        const res = await fetch("https://ai-powered-hiring-system-using-fastapi-c1ya.onrender.com/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: message,
                history: aiHistory.slice(0, -1)
            })
        });
        const data = await res.json();
        const reply = data.reply;
        aiHistory.push({ role: "assistant", content: reply });
        return reply;
    } catch(e) {
        return "Sorry, I'm having trouble connecting. Please try again!";
    }
}

function aiToggleChat() {
    aiIsOpen = !aiIsOpen;
    document.getElementById('aiChatWindow').classList.toggle('ai-hidden', !aiIsOpen);
    document.getElementById('aiNotifDot').style.display = aiIsOpen ? 'none' : 'block';
    if (aiIsOpen) document.getElementById('aiChatInput').focus();
}

function aiSendQuick(text) {
    document.getElementById('aiChatInput').value = text;
    aiSendMessage();
}

function aiAddMessage(text, isUser) {
    const msgs = document.getElementById('aiMessages');
    const div = document.createElement('div');
    div.className = `ai-msg${isUser ? ' ai-user' : ''}`;
    div.innerHTML = `
        <div class="ai-avatar${isUser ? ' ai-uav' : ''}">${isUser ? '👤' : '🤖'}</div>
        <div class="ai-bubble ${isUser ? 'ai-usr' : 'ai-bot'}">${text.replace(/\n/g,'<br>').replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>')}</div>
    `;
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
}

function aiAddTyping() {
    const msgs = document.getElementById('aiMessages');
    const div = document.createElement('div');
    div.className = 'ai-msg'; div.id = 'aiTyping';
    div.innerHTML = `<div class="ai-avatar">🤖</div><div class="ai-bubble ai-bot"><div class="ai-typing"><span></span><span></span><span></span></div></div>`;
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
}

async function aiSendMessage() {
    const input = document.getElementById('aiChatInput');
    const text = input.value.trim();
    if (!text) return;
    aiAddMessage(text, true);
    input.value = '';
    input.style.height = 'auto';
    document.getElementById('aiQuickReplies').style.display = 'none';
    aiAddTyping();
    const reply = await aiCallClaude(text);
    const t = document.getElementById('aiTyping');
    if (t) t.remove();
    aiAddMessage(reply, false);
}
</script>
""", unsafe_allow_html=True)