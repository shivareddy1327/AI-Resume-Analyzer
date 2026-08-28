# 🚀 Smart Resume AI

An AI-powered resume analyzer and builder built with **Streamlit** and **Google Gemini**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **Resume Analyzer** | Standard ATS scoring with keyword match, format & section analysis |
| 🤖 **AI Analyzer** | Deep analysis powered by Google Gemini with PDF report export |
| 📝 **Resume Builder** | Build and download professional DOCX resumes |
| 📊 **Dashboard** | Analytics on all resumes and AI analyses |
| 🎯 **Job Search** | Live job listings (with API) or direct links to top job boards |
| 💬 **Feedback** | Collect and visualize user feedback |

---

## 🗂 Project Structure

```
smart-resume-ai/
├── app.py                     # Main Streamlit application
├── ui_components.py           # Shared UI components
├── requirements.txt
├── .env.example
├── .gitignore
│
├── config/
│   ├── database.py            # SQLite database operations
│   ├── job_roles.py           # Job roles & required skills
│   └── courses.py             # Course & video recommendations
│
├── utils/
│   ├── resume_analyzer.py     # Standard ATS resume analyzer
│   ├── ai_resume_analyzer.py  # Gemini AI analyzer + PDF report
│   └── resume_builder.py      # DOCX resume generator
│
├── dashboard/
│   └── dashboard.py           # Analytics dashboard
│
├── feedback/
│   └── feedback.py            # Feedback form & stats
│
├── jobs/
│   └── job_search.py          # Job search (live + links)
│
├── style/
│   └── style.css              # Global styles
│
└── .streamlit/
    ├── config.toml            # Streamlit theme config
    └── secrets.toml           # API keys (local only, not committed)
```

---

## ⚡ Quick Start (Local)

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/smart-resume-ai.git
cd smart-resume-ai
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API keys
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

Or create `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your_key_here"
RAPIDAPI_KEY   = "your_key_here"   # optional, for live job search
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## ☁️ Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repo and set **Main file** to `app.py`
4. Add your secrets in **Settings → Secrets**:
   ```toml
   GEMINI_API_KEY = "your_gemini_api_key"
   RAPIDAPI_KEY   = "your_rapidapi_key"
   ```
5. Click **Deploy** 🎉

---

## 🔑 API Keys

| Key | Required | Where to get |
|---|---|---|
| `GEMINI_API_KEY` | ✅ Yes (for AI Analyzer) | [Google AI Studio](https://makersuite.google.com/app/apikey) |
| `RAPIDAPI_KEY` | ❌ Optional (live jobs) | [RapidAPI JSearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) |

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **AI:** Google Gemini 1.5 Flash
- **Database:** SQLite
- **PDF Generation:** ReportLab / fpdf2
- **Resume Export:** python-docx
- **Charts:** Plotly
- **PDF Parsing:** pdfplumber, pypdf

---

## 📄 License

MIT License — feel free to use and modify.
