"""
Database configuration and operations for Smart Resume AI
"""
import sqlite3
import json
import os
from datetime import datetime

DB_PATH = "resume_ai.db"


def get_database_connection():
    """Get a connection to the SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """Initialize the database with required tables"""
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            linkedin TEXT,
            github TEXT,
            portfolio TEXT,
            summary TEXT,
            target_role TEXT,
            target_category TEXT,
            education TEXT,
            experience TEXT,
            projects TEXT,
            skills TEXT,
            template TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_id INTEGER,
            ats_score REAL,
            keyword_match_score REAL,
            format_score REAL,
            section_score REAL,
            missing_skills TEXT,
            recommendations TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (resume_id) REFERENCES resume_data(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            model_used TEXT,
            resume_score REAL,
            job_role TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin_actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_username TEXT,
            action TEXT,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rating INTEGER,
            category TEXT,
            feedback_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert default admin if not exists
    cursor.execute("""
        INSERT OR IGNORE INTO admin_users (username, password) VALUES (?, ?)
    """, ("admin", "admin123"))

    conn.commit()
    conn.close()


def save_resume_data(resume_data: dict) -> int:
    """Save resume data to database and return the resume ID"""
    conn = get_database_connection()
    cursor = conn.cursor()

    personal_info = resume_data.get("personal_info", {})

    cursor.execute("""
        INSERT INTO resume_data (
            name, email, phone, linkedin, github, portfolio,
            summary, target_role, target_category,
            education, experience, projects, skills, template
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        personal_info.get("full_name", ""),
        personal_info.get("email", ""),
        personal_info.get("phone", ""),
        personal_info.get("linkedin", ""),
        personal_info.get("github", ""),
        personal_info.get("portfolio", ""),
        resume_data.get("summary", ""),
        resume_data.get("target_role", ""),
        resume_data.get("target_category", ""),
        json.dumps(resume_data.get("education", [])),
        json.dumps(resume_data.get("experience", [])),
        json.dumps(resume_data.get("projects", [])),
        json.dumps(resume_data.get("skills", [])),
        resume_data.get("template", "")
    ))

    resume_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return resume_id


def save_analysis_data(resume_id: int, analysis_data: dict):
    """Save analysis data to database"""
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO resume_analysis (
            resume_id, ats_score, keyword_match_score, format_score,
            section_score, missing_skills, recommendations
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        resume_id,
        analysis_data.get("ats_score", 0),
        analysis_data.get("keyword_match_score", 0),
        analysis_data.get("format_score", 0),
        analysis_data.get("section_score", 0),
        analysis_data.get("missing_skills", ""),
        analysis_data.get("recommendations", "")
    ))

    conn.commit()
    conn.close()


def save_ai_analysis_data(user_id, analysis_data: dict):
    """Save AI analysis data to database"""
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ai_analysis (user_id, model_used, resume_score, job_role)
        VALUES (?, ?, ?, ?)
    """, (
        user_id or "anonymous",
        analysis_data.get("model_used", "Unknown"),
        analysis_data.get("resume_score", 0),
        analysis_data.get("job_role", "")
    ))

    conn.commit()
    conn.close()


def get_ai_analysis_stats() -> dict:
    """Get basic AI analysis statistics"""
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) as total, AVG(resume_score) as avg_score FROM ai_analysis")
    row = cursor.fetchone()
    total = row["total"] or 0
    avg_score = round(row["avg_score"] or 0, 1)

    conn.close()
    return {
        "total_analyses": total,
        "average_score": avg_score,
        "score_distribution": {}
    }


def get_detailed_ai_analysis_stats() -> dict:
    """Get detailed AI analysis statistics"""
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) as total, AVG(resume_score) as avg_score FROM ai_analysis")
    row = cursor.fetchone()
    total = row["total"] or 0
    avg_score = round(row["avg_score"] or 0, 1)

    # Model usage
    cursor.execute("""
        SELECT model_used as model, COUNT(*) as count
        FROM ai_analysis GROUP BY model_used ORDER BY count DESC
    """)
    model_usage = [dict(r) for r in cursor.fetchall()]

    # Top job roles
    cursor.execute("""
        SELECT job_role as role, COUNT(*) as count
        FROM ai_analysis WHERE job_role != ''
        GROUP BY job_role ORDER BY count DESC LIMIT 5
    """)
    top_job_roles = [dict(r) for r in cursor.fetchall()]

    # Score distribution
    cursor.execute("""
        SELECT
            CASE
                WHEN resume_score BETWEEN 0 AND 20 THEN '0-20'
                WHEN resume_score BETWEEN 21 AND 40 THEN '21-40'
                WHEN resume_score BETWEEN 41 AND 60 THEN '41-60'
                WHEN resume_score BETWEEN 61 AND 80 THEN '61-80'
                ELSE '81-100'
            END as range,
            COUNT(*) as count
        FROM ai_analysis GROUP BY range ORDER BY range
    """)
    score_distribution = [dict(r) for r in cursor.fetchall()]

    # Recent analyses
    cursor.execute("""
        SELECT model_used as model, resume_score as score, job_role,
               created_at as date
        FROM ai_analysis ORDER BY created_at DESC LIMIT 10
    """)
    recent_analyses = [dict(r) for r in cursor.fetchall()]

    conn.close()
    return {
        "total_analyses": total,
        "average_score": avg_score,
        "model_usage": model_usage,
        "top_job_roles": top_job_roles,
        "score_distribution": score_distribution,
        "recent_analyses": recent_analyses
    }


def reset_ai_analysis_stats() -> dict:
    """Reset all AI analysis stats"""
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ai_analysis")
        conn.commit()
        conn.close()
        return {"success": True, "message": "AI analysis statistics reset successfully."}
    except Exception as e:
        return {"success": False, "message": str(e)}


def verify_admin(username: str, password: str) -> bool:
    """Verify admin credentials"""
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM admin_users WHERE username=? AND password=?",
        (username, password)
    )
    result = cursor.fetchone()
    conn.close()
    return result is not None


def log_admin_action(username: str, action: str, details: str = ""):
    """Log an admin action"""
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO admin_actions (admin_username, action, details) VALUES (?, ?, ?)",
        (username, action, details)
    )
    conn.commit()
    conn.close()
