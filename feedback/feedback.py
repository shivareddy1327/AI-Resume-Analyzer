"""
Feedback module for Smart Resume AI
"""
import streamlit as st
import pandas as pd
from config.database import get_database_connection


class FeedbackManager:
    def __init__(self):
        pass

    def save_feedback(self, rating: int, category: str, feedback_text: str):
        """Save feedback to database"""
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (rating, category, feedback_text) VALUES (?, ?, ?)",
            (rating, category, feedback_text)
        )
        conn.commit()
        conn.close()

    def render_feedback_form(self):
        """Render the feedback submission form"""
        st.subheader("📝 Share Your Feedback")

        with st.form("feedback_form", clear_on_submit=True):
            rating = st.slider("Overall Rating", min_value=1, max_value=5, value=4,
                               help="1 = Poor, 5 = Excellent")

            category = st.selectbox("Feedback Category", [
                "General Feedback",
                "Resume Analyzer",
                "Resume Builder",
                "AI Analysis",
                "Job Search",
                "UI/UX",
                "Bug Report",
                "Feature Request",
                "Other"
            ])

            feedback_text = st.text_area(
                "Your Feedback",
                placeholder="Share your experience, suggestions, or report issues...",
                height=150
            )

            submitted = st.form_submit_button("Submit Feedback 🚀", type="primary",
                                              use_container_width=True)

            if submitted:
                if not feedback_text.strip():
                    st.error("Please enter your feedback before submitting.")
                else:
                    try:
                        self.save_feedback(rating, category, feedback_text)
                        st.success("✅ Thank you for your feedback! We appreciate it.")
                        st.balloons()
                    except Exception as e:
                        st.error(f"Error saving feedback: {str(e)}")

        # Rating display
        stars = "⭐" * rating if 'rating' in dir() else ""
        st.markdown(f"""
        <div style='background:#1e1e1e; border-radius:12px; padding:1.2rem; margin-top:1rem;'>
            <h4 style='color:#4CAF50;margin:0 0 0.5rem'>How ratings work</h4>
            <p style='color:#aaa;margin:0;'>⭐ Poor &nbsp;|&nbsp; ⭐⭐ Fair &nbsp;|&nbsp; ⭐⭐⭐ Good &nbsp;|&nbsp; ⭐⭐⭐⭐ Very Good &nbsp;|&nbsp; ⭐⭐⭐⭐⭐ Excellent</p>
        </div>
        """, unsafe_allow_html=True)

    def render_feedback_stats(self):
        """Render feedback statistics"""
        st.subheader("📊 Feedback Statistics")

        try:
            conn = get_database_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) as total FROM feedback")
            total = cursor.fetchone()["total"]

            if total == 0:
                st.info("No feedback submitted yet. Be the first to share your thoughts!")
                conn.close()
                return

            cursor.execute("SELECT AVG(rating) as avg FROM feedback")
            avg_rating = round(cursor.fetchone()["avg"] or 0, 2)

            cursor.execute("""
                SELECT rating, COUNT(*) as count FROM feedback
                GROUP BY rating ORDER BY rating DESC
            """)
            rating_dist = [dict(r) for r in cursor.fetchall()]

            cursor.execute("""
                SELECT category, COUNT(*) as count FROM feedback
                GROUP BY category ORDER BY count DESC
            """)
            categories = [dict(r) for r in cursor.fetchall()]

            cursor.execute("""
                SELECT rating, category, feedback_text, created_at
                FROM feedback ORDER BY created_at DESC LIMIT 10
            """)
            recent = [dict(r) for r in cursor.fetchall()]
            conn.close()

            # Metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Feedback", total)
            with col2:
                st.metric("Average Rating", f"{avg_rating}/5")
            with col3:
                stars = "⭐" * round(avg_rating)
                st.metric("Rating", stars)

            # Distribution chart
            if rating_dist:
                import plotly.express as px
                df_dist = pd.DataFrame(rating_dist)
                df_dist["rating"] = df_dist["rating"].apply(lambda x: f"{'⭐' * x} ({x}/5)")
                fig = px.bar(df_dist, x="rating", y="count",
                             color="count",
                             color_continuous_scale="Greens",
                             labels={"rating": "Rating", "count": "Count"})
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                  plot_bgcolor='rgba(0,0,0,0)',
                                  font=dict(color="white"),
                                  showlegend=False, height=280)
                st.plotly_chart(fig, use_container_width=True)

            # Categories
            if categories:
                st.subheader("Feedback by Category")
                import plotly.express as px
                df_cat = pd.DataFrame(categories)
                fig2 = px.pie(df_cat, values="count", names="category",
                              hole=0.35,
                              color_discrete_sequence=px.colors.qualitative.Set3)
                fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                   font=dict(color="white"), height=300)
                st.plotly_chart(fig2, use_container_width=True)

            # Recent comments
            if recent:
                st.subheader("Recent Feedback")
                for item in recent:
                    stars = "⭐" * item["rating"]
                    with st.expander(f"{stars} — {item['category']} ({item['created_at'][:10]})"):
                        st.write(item["feedback_text"])

        except Exception as e:
            st.error(f"Error loading feedback stats: {str(e)}")
