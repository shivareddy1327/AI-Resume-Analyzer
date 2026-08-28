"""
Dashboard module for Smart Resume AI
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from config.database import get_database_connection, get_detailed_ai_analysis_stats


class DashboardManager:
    def __init__(self):
        pass

    def render_dashboard(self):
        """Render the main dashboard"""
        st.title("📊 Dashboard")
        st.markdown("Overview of resume analyses and system statistics.")

        try:
            stats = get_detailed_ai_analysis_stats()
            conn = get_database_connection()

            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)

            # Total resumes from database
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) as total FROM resume_data")
            total_resumes = cursor.fetchone()["total"]

            cursor.execute("SELECT AVG(ats_score) as avg FROM resume_analysis")
            avg_ats = cursor.fetchone()["avg"] or 0

            with col1:
                st.metric("📄 Total Resumes", total_resumes)
            with col2:
                st.metric("🤖 AI Analyses", stats["total_analyses"])
            with col3:
                st.metric("📈 Avg AI Score", f"{stats['average_score']}/100")
            with col4:
                st.metric("🎯 Avg ATS Score", f"{round(avg_ats, 1)}%")

            conn.close()

            st.markdown("---")

            # Charts section
            col_left, col_right = st.columns(2)

            with col_left:
                st.subheader("Score Distribution")
                if stats["score_distribution"]:
                    df = pd.DataFrame(stats["score_distribution"])
                    fig = px.bar(
                        df, x="range", y="count",
                        color="range",
                        color_discrete_sequence=px.colors.qualitative.Set2,
                        labels={"range": "Score Range", "count": "Count"},
                    )
                    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font=dict(color="white"),
                        showlegend=False,
                        height=300
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No data yet. Analyze some resumes to see statistics.")

            with col_right:
                st.subheader("Top Job Roles Analyzed")
                if stats["top_job_roles"]:
                    df_roles = pd.DataFrame(stats["top_job_roles"])
                    fig2 = px.pie(
                        df_roles, values="count", names="role",
                        hole=0.4,
                        color_discrete_sequence=px.colors.qualitative.Bold
                    )
                    fig2.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(color="white"),
                        height=300
                    )
                    st.plotly_chart(fig2, use_container_width=True)
                else:
                    st.info("No role data yet.")

            # Recent analyses table
            st.subheader("Recent AI Analyses")
            if stats["recent_analyses"]:
                df_recent = pd.DataFrame(stats["recent_analyses"])
                df_recent.columns = [c.replace("_", " ").title() for c in df_recent.columns]
                st.dataframe(df_recent, use_container_width=True, hide_index=True)
            else:
                st.info("No recent analyses found.")

            # Resume data table
            st.subheader("Recent Resumes Submitted")
            try:
                conn2 = get_database_connection()
                cursor2 = conn2.cursor()
                cursor2.execute("""
                    SELECT name, email, target_role, created_at
                    FROM resume_data ORDER BY created_at DESC LIMIT 10
                """)
                rows = cursor2.fetchall()
                conn2.close()
                if rows:
                    df_resumes = pd.DataFrame(
                        [dict(r) for r in rows],
                        columns=["name", "email", "target_role", "created_at"]
                    )
                    df_resumes.columns = ["Name", "Email", "Target Role", "Submitted At"]
                    st.dataframe(df_resumes, use_container_width=True, hide_index=True)
                else:
                    st.info("No resumes submitted yet.")
            except Exception as e:
                st.warning(f"Could not load resume data: {e}")

        except Exception as e:
            st.error(f"Dashboard error: {str(e)}")
            st.info("The dashboard will populate once you start analyzing resumes.")
