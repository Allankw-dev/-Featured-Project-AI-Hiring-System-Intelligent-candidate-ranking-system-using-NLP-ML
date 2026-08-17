import streamlit as st
import streamlit.components.v1 as components


def render():
    # ── HANDLE NAVIGATION FROM IFRAME ──
    nav_target = st.query_params.get("nav", "")
    if nav_target:
        st.query_params.clear()
        st.session_state.page = nav_target
        st.rerun()

    # ── HERO NAVIGATION BUTTONS ──
    _, c1, c2, _ = st.columns([3, 1, 1, 3])
    with c1:
        if st.button("🚀 Get Started — Free", use_container_width=True, key="home_signup"):
            st.session_state.page = "Sign Up"
            st.rerun()
    with c2:
        if st.button("🔐 Login", use_container_width=True, key="home_login"):
            st.session_state.page = "Login"
            st.rerun()

    components.html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Exo+2:wght@300;400;600;700&display=swap');

    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { background: transparent; font-family: 'Exo 2', sans-serif; color: #e2e8f0; overflow-x: hidden; }

    canvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; }

    .content { position: relative; z-index: 1; padding: 20px 32px 40px; }

    .hero-grid { display: grid; grid-template-columns: 1.5fr 1fr; gap: 32px; align-items: start; margin-bottom: 40px; }

    .hero-badge {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 6px 18px; border-radius: 999px;
        background: rgba(139,92,246,0.12); border: 1px solid rgba(139,92,246,0.35);
        color: #a78bfa; font-size: 12px; letter-spacing: 1px; margin-bottom: 18px;
    }
    .badge-dot { width: 6px; height: 6px; border-radius: 50%; background: #8b5cf6; animation: blink 2s ease-in-out infinite; }
    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:.2} }

    .hero-title { font-family:'Orbitron',sans-serif; font-size:46px; line-height:1.1; font-weight:900; color:#fff; margin-bottom:18px; letter-spacing:1px; }
    .hero-title .glow { background:linear-gradient(90deg,#a78bfa,#60a5fa,#c084fc); -webkit-background-clip:text; -webkit-text-fill-color:transparent; filter:drop-shadow(0 0 20px rgba(139,92,246,.6)); }
    .hero-desc { font-size:15px; color:rgba(148,163,184,.8); line-height:1.8; margin-bottom:20px; }

    .stats-row { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin-bottom:10px; }
    .stat { background:rgba(139,92,246,.08); border:1px solid rgba(139,92,246,.2); border-radius:12px; padding:14px 10px; text-align:center; }
    .stat-num { font-family:'Orbitron',sans-serif; font-size:22px; font-weight:700; background:linear-gradient(90deg,#a78bfa,#60a5fa); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
    .stat-lbl { font-size:10px; color:#64748b; letter-spacing:1px; text-transform:uppercase; margin-top:4px; }

    .side-panel { background:rgba(4,6,22,.85); border:1px solid rgba(139,92,246,.2); border-radius:18px; padding:24px; position:relative; overflow:hidden; }
    .side-panel::before { content:''; position:absolute; top:0; left:0; right:0; height:1px; background:linear-gradient(90deg,transparent,rgba(139,92,246,.5),transparent); }
    .panel-title { font-family:'Orbitron',sans-serif; font-size:10px; color:#a78bfa; letter-spacing:3px; text-transform:uppercase; margin-bottom:16px; padding-bottom:12px; border-bottom:1px solid rgba(139,92,246,.1); }
    .panel-item { display:flex; align-items:flex-start; gap:12px; margin-bottom:12px; padding:10px; border-radius:10px; background:rgba(139,92,246,.05); border:1px solid rgba(139,92,246,.1); }
    .panel-dot { width:7px; height:7px; border-radius:50%; background:#8b5cf6; box-shadow:0 0 8px rgba(139,92,246,.8); margin-top:5px; flex-shrink:0; }
    .panel-text { font-size:12px; color:#94a3b8; line-height:1.5; }
    .panel-name { font-weight:700; color:#e2e8f0; margin-bottom:2px; display:block; }

    .divider { height:1px; background:linear-gradient(90deg,transparent,rgba(139,92,246,.4),rgba(59,130,246,.4),transparent); margin:36px 0; }

    .section-tag { font-size:10px; font-weight:600; letter-spacing:2px; text-transform:uppercase; color:#6366f1; margin-bottom:8px; }
    .section-title { font-family:'Orbitron',sans-serif; font-size:24px; font-weight:700; color:#f1f5f9; letter-spacing:-.5px; margin-bottom:10px; }
    .section-desc { font-size:14px; color:#64748b; line-height:1.7; margin-bottom:28px; }

    .steps { display:grid; grid-template-columns:repeat(4,1fr); gap:2px; background:rgba(255,255,255,.05); border-radius:12px; overflow:hidden; margin-bottom:36px; }
    .step { background:rgba(10,12,28,.9); padding:24px 18px; }
    .step-num { font-family:'Orbitron',sans-serif; font-size:12px; font-weight:700; color:#6366f1; letter-spacing:1px; margin-bottom:12px; }
    .step-title { font-size:14px; font-weight:600; color:#e2e8f0; margin-bottom:6px; }
    .step-desc { font-size:12px; color:#475569; line-height:1.6; }

    .score-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:10px; margin-bottom:36px; }
    .score-card { background:rgba(15,18,35,.8); border:1px solid rgba(255,255,255,.07); border-radius:12px; padding:18px 20px; }
    .score-label { font-size:13px; font-weight:500; color:#cbd5e1; margin-bottom:8px; display:flex; justify-content:space-between; }
    .score-pct { font-size:13px; font-weight:700; color:#818cf8; }
    .score-bar-bg { height:4px; background:rgba(255,255,255,.07); border-radius:2px; overflow:hidden; margin-bottom:6px; }
    .score-bar { height:100%; border-radius:2px; background:linear-gradient(90deg,#6366f1,#38bdf8); }
    .score-desc { font-size:11px; color:#475569; }

    .features { display:grid; grid-template-columns:repeat(3,1fr); gap:2px; background:rgba(255,255,255,.05); border-radius:12px; overflow:hidden; margin-bottom:36px; }
    .feature { background:rgba(10,12,28,.9); padding:24px 20px; }
    .feature-icon { width:36px; height:36px; border-radius:8px; background:rgba(99,102,241,.1); border:1px solid rgba(99,102,241,.15); display:flex; align-items:center; justify-content:center; font-size:16px; margin-bottom:14px; }
    .feature-title { font-size:14px; font-weight:600; color:#e2e8f0; margin-bottom:6px; }
    .feature-desc { font-size:12px; color:#475569; line-height:1.6; }

    .cta { background:rgba(15,18,35,.8); border:1px solid rgba(255,255,255,.07); border-radius:16px; padding:44px 40px; text-align:center; position:relative; overflow:hidden; }
    .cta::before { content:''; position:absolute; top:0; left:0; right:0; height:1px; background:linear-gradient(90deg,transparent,rgba(139,92,246,.5),rgba(59,130,246,.5),transparent); }
    .cta-title { font-family:'Orbitron',sans-serif; font-size:26px; font-weight:700; color:#f1f5f9; letter-spacing:-.5px; margin-bottom:8px; }
    .cta-desc { font-size:14px; color:#64748b; margin-bottom:8px; }

    @media (max-width:700px) {
        .hero-grid { grid-template-columns:1fr; }
        .hero-title { font-size:28px; }
        .stats-row { grid-template-columns:repeat(2,1fr); }
        .steps { grid-template-columns:repeat(2,1fr); }
        .features { grid-template-columns:1fr; }
        .score-grid { grid-template-columns:1fr; }
        .content { padding:16px; }
    }
    </style>
    </head>
    <body>
    <canvas id="c"></canvas>
    <div class="content">

        <div class="hero-grid">
            <div>
                <div class="hero-badge"><div class="badge-dot"></div> AI-Powered Recruitment Platform</div>
                <div class="hero-title">Hire Smarter.<br><span class="glow">Think Faster.</span><br>Win Better.</div>
                <div class="hero-desc">Automate resume screening, rank candidates with AI, and make confident hiring decisions — all in one platform built for modern teams.</div>
                <div class="stats-row">
                    <div class="stat"><div class="stat-num">98%</div><div class="stat-lbl">Match Accuracy</div></div>
                    <div class="stat"><div class="stat-num">10x</div><div class="stat-lbl">Faster Hiring</div></div>
                    <div class="stat"><div class="stat-num">500+</div><div class="stat-lbl">Jobs Matched</div></div>
                    <div class="stat"><div class="stat-num">24/7</div><div class="stat-lbl">AI Active</div></div>
                </div>
            </div>

            <div class="side-panel">
                <div class="panel-title">// Platform Capabilities</div>
                <div class="panel-item"><div class="panel-dot"></div><div class="panel-text"><span class="panel-name">AI Resume Parsing</span>Extracts skills, experience and qualifications from uploaded CVs automatically.</div></div>
                <div class="panel-item"><div class="panel-dot"></div><div class="panel-text"><span class="panel-name">Intelligent Scoring</span>Ranks candidates using semantic analysis, skill matching and experience scoring.</div></div>
                <div class="panel-item"><div class="panel-dot"></div><div class="panel-text"><span class="panel-name">Fraud Detection</span>Flags keyword stuffing, inconsistent dates and suspicious resume patterns.</div></div>
                <div class="panel-item"><div class="panel-dot"></div><div class="panel-text"><span class="panel-name">Admin Control Center</span>Full visibility into applications, shortlisting, rejection and email communication.</div></div>
                <div class="panel-item"><div class="panel-dot"></div><div class="panel-text"><span class="panel-name">Real-Time Rankings</span>Live candidate leaderboards updated instantly as new applications arrive.</div></div>
            </div>
        </div>

        <div class="divider"></div>

        <div class="section-tag">Process</div>
        <div class="section-title">How it works</div>
        <div class="section-desc">From job post to hire in four steps — no manual screening required.</div>

        <div class="steps">
            <div class="step"><div class="step-num">01</div><div class="step-title">Post a job</div><div class="step-desc">Create a listing with required skills, experience level and job description.</div></div>
            <div class="step"><div class="step-num">02</div><div class="step-title">Candidates apply</div><div class="step-desc">Applicants sign up, upload their CV and submit directly on the platform.</div></div>
            <div class="step"><div class="step-num">03</div><div class="step-title">AI scores instantly</div><div class="step-desc">Each resume is analyzed, verified and ranked automatically on submission.</div></div>
            <div class="step"><div class="step-num">04</div><div class="step-title">Hire with confidence</div><div class="step-desc">Review ranked candidates, shortlist and communicate — all from one panel.</div></div>
        </div>

        <div class="divider"></div>

        <div class="section-tag">AI Engine</div>
        <div class="section-title">How candidates are scored</div>
        <div class="section-desc">Every application receives a composite score based on four weighted signals.</div>

        <div class="score-grid">
            <div class="score-card">
                <div class="score-label">Semantic match <span class="score-pct">45%</span></div>
                <div class="score-bar-bg"><div class="score-bar" style="width:45%"></div></div>
                <div class="score-desc">TF-IDF cosine similarity between resume and job description</div>
            </div>
            <div class="score-card">
                <div class="score-label">Skills coverage <span class="score-pct">25%</span></div>
                <div class="score-bar-bg"><div class="score-bar" style="width:25%"></div></div>
                <div class="score-desc">Percentage of required skills found in the resume</div>
            </div>
            <div class="score-card">
                <div class="score-label">Experience fit <span class="score-pct">20%</span></div>
                <div class="score-bar-bg"><div class="score-bar" style="width:20%"></div></div>
                <div class="score-desc">Candidate years vs. role requirement ratio</div>
            </div>
            <div class="score-card">
                <div class="score-label">Verification <span class="score-pct">10%</span></div>
                <div class="score-bar-bg"><div class="score-bar" style="width:10%"></div></div>
                <div class="score-desc">Resume authenticity — flags fraud signals and inconsistencies</div>
            </div>
        </div>

        <div class="divider"></div>

        <div class="section-tag">Features</div>
        <div class="section-title">Everything you need</div>
        <div class="section-desc">Built for recruiters who want signal, not noise.</div>

        <div class="features">
            <div class="feature"><div class="feature-icon">📄</div><div class="feature-title">Resume intelligence</div><div class="feature-desc">Structured extraction from PDF uploads — skills, experience, education, contact info.</div></div>
            <div class="feature"><div class="feature-icon">🧠</div><div class="feature-title">NLP matching</div><div class="feature-desc">Understands context and meaning — not just whether a keyword appears.</div></div>
            <div class="feature"><div class="feature-icon">🛡</div><div class="feature-title">Fraud detection</div><div class="feature-desc">Detects keyword stuffing, inflated claims, future dates and missing contact info.</div></div>
            <div class="feature"><div class="feature-icon">⚡</div><div class="feature-title">Real-time rankings</div><div class="feature-desc">Leaderboard updates as each application lands — always see the best candidates first.</div></div>
            <div class="feature"><div class="feature-icon">✉</div><div class="feature-title">Email communication</div><div class="feature-desc">Send tailored shortlist or rejection emails without leaving the platform.</div></div>
            <div class="feature"><div class="feature-icon">🔐</div><div class="feature-title">Secure by default</div><div class="feature-desc">JWT auth, bcrypt hashing, rate limiting, CORS protection and input sanitization.</div></div>
        </div>

        <div class="cta">
            <div class="cta-title">Ready to hire smarter?</div>
            <div class="cta-desc">Set up takes minutes. No credit card required.</div>
        </div>

    </div>

    <script>
    function sendHeight() {
        const h = document.body.scrollHeight;
        window.parent.postMessage({type:'streamlit:setFrameHeight', height:h}, '*');
    }
    const ro = new ResizeObserver(sendHeight);
    ro.observe(document.body);
    window.addEventListener('load', sendHeight);
    setTimeout(sendHeight, 500);
    setTimeout(sendHeight, 1200);

    const canvas = document.getElementById('c');
    const ctx = canvas.getContext('2d');
    let W = canvas.width = window.innerWidth;
    let H = canvas.height = window.innerHeight;
    window.addEventListener('resize', () => { W = canvas.width = window.innerWidth; H = canvas.height = window.innerHeight; });

    const COUNT = 60, MAX = 140;
    const pts = Array.from({length:COUNT}, () => ({
        x:Math.random()*W, y:Math.random()*H,
        vx:(Math.random()-.5)*.4, vy:(Math.random()-.5)*.4,
        r:Math.random()*1.5+.5
    }));

    function draw() {
        ctx.clearRect(0,0,W,H);
        pts.forEach(p => {
            p.x+=p.vx; p.y+=p.vy;
            if(p.x<0||p.x>W) p.vx*=-1;
            if(p.y<0||p.y>H) p.vy*=-1;
            ctx.beginPath();
            ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
            ctx.fillStyle='rgba(99,102,241,0.4)';
            ctx.fill();
        });
        for(let i=0;i<pts.length;i++) {
            for(let j=i+1;j<pts.length;j++) {
                const dx=pts[i].x-pts[j].x, dy=pts[i].y-pts[j].y;
                const d=Math.sqrt(dx*dx+dy*dy);
                if(d<MAX) {
                    ctx.beginPath();
                    ctx.moveTo(pts[i].x,pts[i].y);
                    ctx.lineTo(pts[j].x,pts[j].y);
                    ctx.strokeStyle=`rgba(99,102,241,${(1-d/MAX)*0.1})`;
                    ctx.lineWidth=.8;
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(draw);
    }
    draw();
    </script>
    </body>
    </html>
    """, height=1800, scrolling=False)

    # ── CTA BUTTONS ──
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🚀 Create Account", use_container_width=True, key="cta_signup"):
            st.session_state.page = "Sign Up"
            st.rerun()
    with c2:
        if st.button("🔐 Sign In", use_container_width=True, key="cta_login"):
            st.session_state.page = "Login"
            st.rerun()
    with c3:
        if st.button("💼 Browse Jobs", use_container_width=True, key="cta_jobs"):
            st.session_state.page = "Jobs"
            st.rerun()