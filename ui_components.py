"""
UI Components for Smart Resume AI
"""
import streamlit as st


def apply_modern_styles():
    """Apply modern CSS styles"""
    st.markdown("""
    <style>
    .hero-section {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #ffffff, #4CAF50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: rgba(255,255,255,0.8);
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.7;
    }
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    .feature-card-item {
        background: rgba(30, 30, 30, 0.9);
        border: 1px solid rgba(76, 175, 80, 0.3);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s ease;
        text-align: center;
    }
    .feature-card-item:hover {
        border-color: #4CAF50;
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(76,175,80,0.15);
    }
    .feature-icon {
        font-size: 2.5rem;
        color: #4CAF50;
        margin-bottom: 1rem;
    }
    .feature-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: white;
        margin-bottom: 0.8rem;
    }
    .feature-desc {
        color: #aaa;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    .page-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .page-header h1 {
        color: white;
        font-size: 2rem;
        font-weight: 600;
        margin: 0;
    }
    .page-header p {
        color: rgba(255,255,255,0.7);
        margin: 0.5rem 0 0;
    }
    </style>
    """, unsafe_allow_html=True)


def hero_section(title: str, subtitle: str):
    """Render a hero section"""
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-title">{title}</div>
        <div class="hero-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def feature_card(icon: str, title: str, description: str):
    """Render a feature card"""
    st.markdown(f"""
    <div class="feature-card-item">
        <div class="feature-icon"><i class="{icon}"></i></div>
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{description}</div>
    </div>
    """, unsafe_allow_html=True)


def page_header(title: str, subtitle: str = ""):
    """Render a page header"""
    st.markdown(f"""
    <div class="page-header">
        <h1>{title}</h1>
        {"<p>" + subtitle + "</p>" if subtitle else ""}
    </div>
    """, unsafe_allow_html=True)


def render_analytics_section(data: dict):
    """Render analytics section"""
    import streamlit as st
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Resumes", data.get("total_resumes", 0))
    with col2:
        st.metric("Avg ATS Score", f"{data.get('avg_ats_score', 0):.1f}%")
    with col3:
        st.metric("Analyses Today", data.get("analyses_today", 0))


def render_activity_section(activities: list):
    """Render activity section"""
    import streamlit as st
    if not activities:
        st.info("No recent activity.")
        return
    for activity in activities:
        st.markdown(f"- {activity}")


def render_suggestions_section(suggestions: list):
    """Render suggestions section"""
    import streamlit as st
    if not suggestions:
        st.success("No suggestions — your resume looks great!")
        return
    for suggestion in suggestions:
        st.markdown(f"💡 {suggestion}")
