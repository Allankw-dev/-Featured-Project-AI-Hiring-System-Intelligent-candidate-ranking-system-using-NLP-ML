import streamlit as st
import streamlit.components.v1 as components


def render():
    nav_target = st.query_params.get("nav", "")
    if nav_target:
        st.query_params.clear()
        st.session_state.page = nav_target
        st.rerun()

    components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

html, body {
    font-family: 'Inter', sans-serif;
    background: #05060f;
    color: #e2e8f0;
    overflow-x: hidden;
}

canvas {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 0;
    pointer-events: none;
    opacity: 0.6;
}

.page { position: relative; z-index: 1; padding: 56px 40px 64px; max-width: 1080px; margin: 0 auto; }

/* ── HERO ── */
.hero { display: grid; grid-template-columns: 1fr 420px; gap: 48px; align-items: start; margin-bottom: 80px; }

.badge {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 5px 14px; border-radius: 999px;
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.25);
    color: #a5b4fc; font-size: 12px; font-weight: 500;
    letter-spacing: 0.5px; margin-bottom: 24px;
}

.badge-dot { width: 6px; height: 6px; border-radius: 50%; background: #6366f1; animation: blink 2.5s ease-in-out infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 52px; line-height: 1.08; font-weight: 700;
    color: #f1f5f9; margin-bottom: 20px; letter-spacing: -1px;
}

.hero-title .accent {
    background: linear-gradient(135deg, #818cf8, #38bdf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

.hero-desc {
    font-size: 16px; line-height: 1.8;
    color: #94a3b8; margin-bottom: 36px;
    max-width: 480px;
}

.btn-group { display: flex; gap: 12px; flex-wrap: wrap; }

.btn {
    padding: 12px 24px; border-radius: 8px;
    font-family: 'Inter', sans-serif; font-size: 14px;
    font-weight: 500; cursor: pointer; text-decoration: none;
    display: inline-block; text-align: center;
    transition: all 0.2s ease; letter-spacing: 0.2px;
    border: none;
}

.btn-primary {
    background: #6366f1; color: #fff;
    box-shadow: 0 1px 2px rgba(0,0,0,0.3), 0 0 0 1px rgba(99,102,241,0.3);
}
.btn-primary:hover { background: #5355d4; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(99,102,241,0.35); }

.btn-secondary {
    background: rgba(255,255,255,0.05);
    color: #cbd5e1;
    border: 1px solid rgba(255,255,255,0.1);
}
.btn-secondary:hover { background: rgba(255,255,255,0.09); border-color: rgba(255,255,255,0.18); color: #f1f5f9; }

/* ── PANEL ── */
.panel {
    background: rgba(15,18,35,0.8);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px; padding: 28px;
    backdrop-filter: blur(12px);
}

.panel-label {
    font-size: 11px; font-weight: 600; letter-spacing: 1.2px;
    text-transform: uppercase; color: #475569; margin-bottom: 20px;
}

.panel-item {
    display: flex; gap: 14px; align-items: flex-start;
    padding: 14px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.panel-item:last-child { border-bottom: none; padding-bottom: 0; }

.panel-icon {
    width: 36px; height: 36px; border-radius: 8px; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; background: rgba(99,102,241,0.12);
    border: 1px solid rgba(99,102,241,0.15);
}

.panel-item-name { font-size: 14px; font-weight: 500; color: #e2e8f0; margin-bottom: 3px; }
.panel-item-desc { font-size: 12px; color: #64748b; line-height: 1.5; }

/* ── METRICS ── */
.metrics { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: rgba(255,255,255,0.06); border-radius: 12px; overflow: hidden; margin-bottom: 80px; }

.metric {
    background: rgba(10,12,28,0.9);
    padding: 28px 24px; text-align: center;
}

.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 32px; font-weight: 700; color: #f1f5f9;
    letter-spacing: -0.5px; margin-bottom: 6px;
}

.metric-label { font-size: 12px; color: #475569; letter-spacing: 0.5px; text-transform: uppercase; }

/* ── DIVIDER ── */
.section-divider { height: 1px; background: rgba(255,255,255,0.06); margin: 0 0 64px; }

/* ── SECTION ── */
.section-header { margin-bottom: 40px; }
.section-tag { font-size: 11px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: #6366f1; margin-bottom: 10px; }
.section-title { font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 700; color: #f1f5f9; letter-spacing: -0.5px; margin-bottom: 12px; }
.section-desc { font-size: 15px; color: #64748b; line-height: 1.7; max-width: 520px; }

/* ── STEPS ── */
.steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2px; background: rgba(255,255,255,0.05); border-radius: 12px; overflow: hidden; margin-bottom: 80px; }

.step {
    background: rgba(10,12,28,0.9); padding: 28px 22px;
    position: relative;
}

.step-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 13px; font-weight: 700; color: #6366f1;
    letter-spacing: 1px; margin-bottom: 14px;
}

.step-title { font-size: 15px; font-weight: 600; color: #e2e8f0; margin-bottom: 8px; }
.step-desc { font-size: 13px; color: #475569; line-height: 1.6; }

/* ── FEATURES ── */
.features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; background: rgba(255,255,255,0.05); border-radius: 12px; overflow: hidden; margin-bottom: 80px; }

.feature { background: rgba(10,12,28,0.9); padding: 28px 24px; }

.feature-icon {
    width: 40px; height: 40px; border-radius: 10px;
    background: rgba(99,102,241,0.1); border: 1px solid rgba(99,102,241,0.15);
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; margin-bottom: 16px;
}

.feature-title { font-size: 15px; font-weight: 600; color: #e2e8f0; margin-bottom: 8px; }
.feature-desc { font-size: 13px; color: #475569; line-height: 1.7; }

/* ── SCORE BREAKDOWN ── */
.score-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 80px; }

.score-card {
    background: rgba(15,18,35,0.8);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px; padding: 20px 22px;
    display: flex; align-items: center; gap: 18px;
}

.score-bar-wrap { flex: 1; }
.score-label { font-size: 13px; font-weight: 500; color: #cbd5e1; margin-bottom: 8px; display: flex; justify-content: space-between; }
.score-pct { font-size: 13px; font-weight: 700; color: #818cf8; }
.score-bar-bg { height: 4px; background: rgba(255,255,255,0.07); border-radius: 2px; overflow: hidden; }
.score-bar-fill { height: 100%; border-radius: 2px; background: linear-gradient(90deg, #6366f1, #38bdf8); }
.score-desc { font-size: 11px; color: #475569; margin-top: 5px; }

/* ── CTA ── */
.cta {
    background: rgba(15,18,35,0.8);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px; padding: 52px 48px;
    display: flex; justify-content: space-between; align-items: center; gap: 40px;
}

.cta-left {}
.cta-title { font-family: 'Space Grotesk', sans-serif; font-size: 28px; font-weight: 700; color: #f1f5f9; letter-spacing: -0.5px; margin-bottom: 10px; }
.cta-desc { font-size: 15px; color: #64748b; line-height: 1.6; }
.cta-actions { display: flex; gap: 10px; flex-shrink: 0; }

@media (max-width: 768px) {
    .hero { grid-template-columns: 1fr; }
    .hero-title { font-size: 34px; }
    .metrics { grid-template-columns: repeat(2, 1fr); }
    .steps { grid-template-columns: repeat(2, 1fr); }
    .features { grid-template-columns: 1fr; }
    .score-grid { grid-template-columns: 1fr; }
    .cta { flex-direction: column; padding: 36px 28px; }
    .page { padding: 40px 20px 48px; }
}
</style>
</head>
<body>

<canvas id="c"></canvas>

<div class="page">

    <!-- HERO -->
    <div class="hero">
        <div>
            <div class="badge"><div class="badge-dot"></div> AI-Powered Recruitment</div>
            <h1 class="hero-title">Hire the right people,<br><span class="accent">faster than ever.</span></h1>
            <p class="hero-desc">Automate resume screening, rank candidates with AI, and make confident hiring decisions — all in one platform built for modern teams.</p>
            <div class="btn-group">
                <a class="btn btn-primary" href="?nav=Sign Up" target="_top">Get started free</a>
                <a class="btn btn-secondary" href="?nav=Login" target="_top">Sign in</a>
            </div>
        </div>

        <div class="panel">
            <div class="panel-label">Platform capabilities</div>

            <div class="panel-item">
                <div class="panel-icon">📄</div>
                <div>
                    <div class="panel-item-name">Resume parsing</div>
                    <div class="panel-item-desc">Extracts skills, experience, and contact info from uploaded PDFs automatically.</div>
                </div>
            </div>

            <div class="panel-item">
                <div class="panel-icon">🧠</div>
                <div>
                    <div class="panel-item-name">Semantic scoring</div>
                    <div class="panel-item-desc">Ranks candidates using NLP — not just keyword matching.</div>
                </div>
            </div>

            <div class="panel-item">
                <div class="panel-icon">🛡</div>
                <div>
                    <div class="panel-item-name">Fraud detection</div>
                    <div class="panel-item-desc">Flags keyword stuffing, inconsistent dates, and suspicious patterns.</div>
                </div>
            </div>

            <div class="panel-item">
                <div class="panel-icon">📊</div>
                <div>
                    <div class="panel-item-name">Live rankings</div>
                    <div class="panel-item-desc">Candidate leaderboards update in real time as applications arrive.</div>
                </div>
            </div>

            <div class="panel-item">
                <div class="panel-icon">✉</div>
                <div>
                    <div class="panel-item-name">Direct communication</div>
                    <div class="panel-item-desc">Send shortlist or rejection emails directly from the admin panel.</div>
                </div>
            </div>
        </div>
    </div>

    <!-- METRICS -->
    <div class="metrics">
        <div class="metric"><div class="metric-value">98%</div><div class="metric-label">Match accuracy</div></div>
        <div class="metric"><div class="metric-value">10x</div><div class="metric-label">Faster screening</div></div>
        <div class="metric"><div class="metric-value">500+</div><div class="metric-label">Jobs processed</div></div>
        <div class="metric"><div class="metric-value">24/7</div><div class="metric-label">AI availability</div></div>
    </div>

    <div class="section-divider"></div>

    <!-- HOW IT WORKS -->
    <div class="section-header">
        <div class="section-tag">Process</div>
        <div class="section-title">How it works</div>
        <div class="section-desc">From job post to hire in four steps — no manual screening required.</div>
    </div>

    <div class="steps">
        <div class="step">
            <div class="step-num">01</div>
            <div class="step-title">Post a job</div>
            <div class="step-desc">Create a listing with required skills, experience level, and job description.</div>
        </div>
        <div class="step">
            <div class="step-num">02</div>
            <div class="step-title">Candidates apply</div>
            <div class="step-desc">Applicants sign up, upload their CV, and submit — no third-party forms.</div>
        </div>
        <div class="step">
            <div class="step-num">03</div>
            <div class="step-title">AI scores instantly</div>
            <div class="step-desc">Each resume is analyzed, verified, and ranked automatically on submission.</div>
        </div>
        <div class="step">
            <div class="step-num">04</div>
            <div class="step-title">Hire with confidence</div>
            <div class="step-desc">Review ranked candidates, shortlist, and communicate — all from one panel.</div>
        </div>
    </div>

    <div class="section-divider"></div>

    <!-- SCORING BREAKDOWN -->
    <div class="section-header">
        <div class="section-tag">AI Engine</div>
        <div class="section-title">How candidates are scored</div>
        <div class="section-desc">Every application receives a composite score based on four weighted signals.</div>
    </div>

    <div class="score-grid">
        <div class="score-card">
            <div class="score-bar-wrap">
                <div class="score-label">Semantic match <span class="score-pct">45%</span></div>
                <div class="score-bar-bg"><div class="score-bar-fill" style="width:45%"></div></div>
                <div class="score-desc">TF-IDF cosine similarity between resume and job description</div>
            </div>
        </div>
        <div class="score-card">
            <div class="score-bar-wrap">
                <div class="score-label">Skills coverage <span class="score-pct">25%</span></div>
                <div class="score-bar-bg"><div class="score-bar-fill" style="width:25%"></div></div>
                <div class="score-desc">Percentage of required skills found in the resume</div>
            </div>
        </div>
        <div class="score-card">
            <div class="score-bar-wrap">
                <div class="score-label">Experience fit <span class="score-pct">20%</span></div>
                <div class="score-bar-bg"><div class="score-bar-fill" style="width:20%"></div></div>
                <div class="score-desc">Candidate years vs. role requirement ratio</div>
            </div>
        </div>
        <div class="score-card">
            <div class="score-bar-wrap">
                <div class="score-label">Verification <span class="score-pct">10%</span></div>
                <div class="score-bar-bg"><div class="score-bar-fill" style="width:10%"></div></div>
                <div class="score-desc">Resume authenticity — flags fraud signals and inconsistencies</div>
            </div>
        </div>
    </div>

    <div class="section-divider"></div>

    <!-- FEATURES -->
    <div class="section-header">
        <div class="section-tag">Features</div>
        <div class="section-title">Everything you need</div>
        <div class="section-desc">Built for recruiters who want signal, not noise.</div>
    </div>

    <div class="features">
        <div class="feature">
            <div class="feature-icon">📄</div>
            <div class="feature-title">Resume intelligence</div>
            <div class="feature-desc">Structured extraction from PDF uploads — name, skills, experience, education, contact info.</div>
        </div>
        <div class="feature">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">NLP matching</div>
            <div class="feature-desc">Understands context and meaning — not just whether a keyword appears.</div>
        </div>
        <div class="feature">
            <div class="feature-icon">🛡</div>
            <div class="feature-title">Fraud detection</div>
            <div class="feature-desc">Detects keyword stuffing, inflated claims, future dates, and missing contact info.</div>
        </div>
        <div class="feature">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Real-time rankings</div>
            <div class="feature-desc">Leaderboard updates as each application lands — always see the best candidates first.</div>
        </div>
        <div class="feature">
            <div class="feature-icon">✉</div>
            <div class="feature-title">Email communication</div>
            <div class="feature-desc">Send tailored shortlist or rejection emails without leaving the platform.</div>
        </div>
        <div class="feature">
            <div class="feature-icon">🔐</div>
            <div class="feature-title">Secure by default</div>
            <div class="feature-desc">JWT auth, bcrypt hashing, rate limiting, CORS protection, and input sanitization.</div>
        </div>
    </div>

    <!-- CTA -->
    <div class="cta">
        <div class="cta-left">
            <div class="cta-title">Ready to hire smarter?</div>
            <div class="cta-desc">Set up takes minutes. No credit card required.</div>
        </div>
        <div class="cta-actions">
            <a class="btn btn-primary" href="?nav=Sign Up" target="_top">Create account</a>
            <a class="btn btn-secondary" href="?nav=Jobs" target="_top">Browse jobs</a>
        </div>
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

window.addEventListener('resize', () => {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
});

const COUNT = 60, MAX = 140;
const pts = Array.from({length: COUNT}, () => ({
    x: Math.random()*W, y: Math.random()*H,
    vx: (Math.random()-.5)*.4, vy: (Math.random()-.5)*.4,
    r: Math.random()*1.5+.5
}));

function draw() {
    ctx.clearRect(0,0,W,H);
    pts.forEach(p => {
        p.x += p.vx; p.y += p.vy;
        if(p.x<0||p.x>W) p.vx*=-1;
        if(p.y<0||p.y>H) p.vy*=-1;
        ctx.beginPath();
        ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
        ctx.fillStyle='rgba(99,102,241,0.5)';
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
                ctx.strokeStyle=`rgba(99,102,241,${(1-d/MAX)*0.12})`;
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
    """, height=2400, scrolling=False)