"""
Job Search module for Smart Resume AI
"""
import streamlit as st
import requests


def render_job_search():
    """Render the job search page"""
    st.title("🎯 Job Search")
    st.markdown("Search for jobs matching your skills and target role.")

    # Search filters
    col1, col2, col3 = st.columns(3)
    with col1:
        job_title = st.text_input("Job Title / Keywords", placeholder="e.g. Python Developer")
    with col2:
        location = st.text_input("Location", placeholder="e.g. Hyderabad, Remote")
    with col3:
        job_type = st.selectbox("Job Type", ["All", "Full-time", "Part-time", "Contract", "Remote", "Internship"])

    search_clicked = st.button("🔍 Search Jobs", type="primary", use_container_width=True)

    if search_clicked and job_title:
        _render_job_results(job_title, location, job_type)
    elif search_clicked and not job_title:
        st.warning("Please enter a job title or keywords to search.")
    else:
        _render_job_boards()


def _render_job_boards():
    """Render popular job board links"""
    st.markdown("---")
    st.subheader("🌐 Popular Job Boards")
    st.markdown("Click any platform below to explore opportunities:")

    boards = [
        {
            "name": "LinkedIn Jobs",
            "icon": "💼",
            "url": "https://www.linkedin.com/jobs/",
            "desc": "Professional network with millions of job listings worldwide."
        },
        {
            "name": "Indeed",
            "icon": "🔎",
            "url": "https://www.indeed.com/",
            "desc": "One of the largest job search engines with listings from all sources."
        },
        {
            "name": "Naukri",
            "icon": "🇮🇳",
            "url": "https://www.naukri.com/",
            "desc": "India's largest job portal with millions of active listings."
        },
        {
            "name": "Glassdoor",
            "icon": "🏢",
            "url": "https://www.glassdoor.com/Job/index.htm",
            "desc": "Jobs with company reviews, salaries, and interview insights."
        },
        {
            "name": "AngelList / Wellfound",
            "icon": "🚀",
            "url": "https://wellfound.com/jobs",
            "desc": "Startup jobs and equity opportunities."
        },
        {
            "name": "GitHub Jobs",
            "icon": "🐙",
            "url": "https://github.com/features/",
            "desc": "Tech-focused job listings for developers."
        },
        {
            "name": "Internshala",
            "icon": "🎓",
            "url": "https://internshala.com/",
            "desc": "Internships and fresher jobs across India."
        },
        {
            "name": "Dice",
            "icon": "🎲",
            "url": "https://www.dice.com/",
            "desc": "Technology and IT jobs for experienced professionals."
        },
    ]

    cols = st.columns(2)
    for i, board in enumerate(boards):
        with cols[i % 2]:
            st.markdown(f"""
            <div style='
                background: rgba(30,30,30,0.9);
                border: 1px solid rgba(76,175,80,0.3);
                border-radius: 12px;
                padding: 1.2rem;
                margin-bottom: 1rem;
                transition: all 0.3s ease;
            '>
                <h4 style='color:white; margin:0 0 0.4rem;'>{board["icon"]} {board["name"]}</h4>
                <p style='color:#aaa; font-size:0.9rem; margin:0 0 0.8rem;'>{board["desc"]}</p>
                <a href='{board["url"]}' target='_blank' style='
                    background: linear-gradient(135deg,#4CAF50,#45a049);
                    color: white;
                    padding: 6px 16px;
                    border-radius: 20px;
                    text-decoration: none;
                    font-size: 0.85rem;
                    font-weight: 500;
                '>Visit →</a>
            </div>
            """, unsafe_allow_html=True)

    # Job search tips
    st.markdown("---")
    st.subheader("💡 Job Search Tips")
    tips = [
        "**Tailor your resume** for each application — use keywords from the job description.",
        "**Set up job alerts** on LinkedIn and Naukri to get notified about new postings.",
        "**Network actively** — 70% of jobs are filled through referrals.",
        "**Follow up** after applying — a polite email can set you apart.",
        "**Research the company** before interviews using Glassdoor and LinkedIn.",
        "**Track your applications** using a spreadsheet to stay organized.",
    ]
    for tip in tips:
        st.markdown(f"✅ {tip}")


def _render_job_results(job_title: str, location: str, job_type: str):
    """Render job search results using JSearch RapidAPI or fallback to links"""
    st.markdown("---")
    st.subheader(f"🔍 Jobs for: **{job_title}**{' in ' + location if location else ''}")

    # Try RapidAPI JSearch (requires RAPIDAPI_KEY in secrets/env)
    api_key = None
    try:
        api_key = st.secrets.get("RAPIDAPI_KEY", "")
    except Exception:
        pass
    if not api_key:
        import os
        api_key = os.getenv("RAPIDAPI_KEY", "")

    if api_key:
        _fetch_and_render_jobs(api_key, job_title, location, job_type)
    else:
        _render_search_links(job_title, location, job_type)


def _fetch_and_render_jobs(api_key: str, job_title: str, location: str, job_type: str):
    """Fetch jobs from JSearch API"""
    query = f"{job_title} {location}".strip()
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {
        "query": query,
        "page": "1",
        "num_pages": "1",
        "date_posted": "month"
    }
    if job_type != "All":
        params["employment_types"] = job_type.upper().replace("-", "_")

    try:
        with st.spinner("Fetching live job listings..."):
            response = requests.get(url, headers=headers, params=params, timeout=10)
            data = response.json()

        jobs = data.get("data", [])
        if not jobs:
            st.info("No live results found. Showing search links instead.")
            _render_search_links(job_title, location, job_type)
            return

        st.success(f"Found {len(jobs)} job listings")
        for job in jobs[:10]:
            with st.expander(f"**{job.get('job_title','N/A')}** @ {job.get('employer_name','N/A')} — {job.get('job_city','') or job.get('job_country','')}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Company:** {job.get('employer_name','N/A')}")
                    st.markdown(f"**Location:** {job.get('job_city','')} {job.get('job_state','')} {job.get('job_country','')}")
                    st.markdown(f"**Type:** {job.get('job_employment_type','N/A')}")
                with col2:
                    st.markdown(f"**Posted:** {job.get('job_posted_at_datetime_utc','N/A')[:10] if job.get('job_posted_at_datetime_utc') else 'N/A'}")
                    if job.get("job_min_salary") and job.get("job_max_salary"):
                        st.markdown(f"**Salary:** ${job['job_min_salary']:,} – ${job['job_max_salary']:,} {job.get('job_salary_period','')}")

                if job.get("job_description"):
                    st.markdown("**Description:**")
                    st.markdown(job["job_description"][:600] + "...")

                if job.get("job_apply_link"):
                    st.markdown(f"[🚀 Apply Now]({job['job_apply_link']})")

    except Exception as e:
        st.warning(f"Live search unavailable: {e}. Showing direct search links.")
        _render_search_links(job_title, location, job_type)


def _render_search_links(job_title: str, location: str, job_type: str):
    """Render direct search links to job boards"""
    import urllib.parse
    query = urllib.parse.quote(f"{job_title} {location}".strip())
    loc_q = urllib.parse.quote(location) if location else ""

    st.info("💡 Add a `RAPIDAPI_KEY` to your Streamlit secrets for live job listings. For now, use these direct search links:")

    links = [
        ("💼 LinkedIn", f"https://www.linkedin.com/jobs/search/?keywords={query}&location={loc_q}"),
        ("🔎 Indeed", f"https://www.indeed.com/jobs?q={query}&l={loc_q}"),
        ("🇮🇳 Naukri", f"https://www.naukri.com/{urllib.parse.quote(job_title.lower().replace(' ','-'))}-jobs"),
        ("🏢 Glassdoor", f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={query}&locT=N&locId=0"),
        ("🚀 Wellfound", f"https://wellfound.com/jobs?q={query}"),
    ]

    cols = st.columns(len(links))
    for col, (label, url) in zip(cols, links):
        with col:
            st.markdown(f"""
            <a href="{url}" target="_blank" style="
                display:block; text-align:center;
                background:linear-gradient(135deg,#4CAF50,#45a049);
                color:white; padding:12px 8px; border-radius:10px;
                text-decoration:none; font-weight:600; font-size:0.9rem;
                margin-bottom:8px;
            ">{label}</a>
            """, unsafe_allow_html=True)
