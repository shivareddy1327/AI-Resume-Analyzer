"""
Resume Analyzer utility for Smart Resume AI
"""
import re
import io
from typing import Optional


class ResumeAnalyzer:
    def __init__(self):
        self.section_keywords = {
            'contact': ['email', 'phone', 'address', 'linkedin', 'github', 'portfolio'],
            'summary': ['summary', 'objective', 'profile', 'about'],
            'experience': ['experience', 'work history', 'employment', 'career'],
            'education': ['education', 'degree', 'university', 'college', 'school', 'bachelor', 'master', 'phd'],
            'skills': ['skills', 'technologies', 'tools', 'languages', 'competencies'],
            'projects': ['projects', 'portfolio', 'personal projects', 'academic projects'],
            'certifications': ['certifications', 'certificates', 'credentials', 'licenses'],
            'achievements': ['achievements', 'awards', 'honors', 'accomplishments'],
        }

    def extract_text_from_pdf(self, file) -> str:
        """Extract text from PDF file"""
        try:
            import pdfplumber
            with pdfplumber.open(file) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text
        except Exception:
            pass

        try:
            from pypdf import PdfReader
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            raise Exception(f"Could not extract text from PDF: {str(e)}")

    def extract_text_from_docx(self, file) -> str:
        """Extract text from DOCX file"""
        try:
            from docx import Document
            doc = Document(file)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text
        except Exception as e:
            raise Exception(f"Could not extract text from DOCX: {str(e)}")

    def extract_contact_info(self, text: str) -> dict:
        """Extract contact information from resume text"""
        email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
        linkedin = re.findall(r'linkedin\.com/in/[\w\-]+', text, re.IGNORECASE)
        github = re.findall(r'github\.com/[\w\-]+', text, re.IGNORECASE)

        lines = text.split('\n')
        name = lines[0].strip() if lines else ''

        return {
            'name': name,
            'email': email[0] if email else '',
            'phone': phone[0] if phone else '',
            'linkedin': linkedin[0] if linkedin else '',
            'github': github[0] if github else '',
            'portfolio': ''
        }

    def detect_sections(self, text: str) -> dict:
        """Detect which sections are present in the resume"""
        text_lower = text.lower()
        detected = {}
        for section, keywords in self.section_keywords.items():
            detected[section] = any(kw in text_lower for kw in keywords)
        return detected

    def calculate_section_score(self, sections: dict) -> float:
        """Calculate section completeness score"""
        important_sections = ['contact', 'experience', 'education', 'skills']
        optional_sections = ['summary', 'projects', 'certifications', 'achievements']

        important_score = sum(1 for s in important_sections if sections.get(s, False))
        optional_score = sum(1 for s in optional_sections if sections.get(s, False))

        score = (important_score / len(important_sections)) * 70
        score += (optional_score / len(optional_sections)) * 30
        return round(score, 1)

    def calculate_keyword_match(self, text: str, role_info: dict) -> dict:
        """Calculate keyword match score against required skills"""
        text_lower = text.lower()
        required_skills = role_info.get('required_skills', [])
        preferred_skills = role_info.get('preferred_skills', [])

        matched = [skill for skill in required_skills if skill.lower() in text_lower]
        missing = [skill for skill in required_skills if skill.lower() not in text_lower]

        if required_skills:
            score = (len(matched) / len(required_skills)) * 100
        else:
            score = 50

        return {
            'score': round(score, 1),
            'matched_skills': matched,
            'missing_skills': missing,
        }

    def calculate_format_score(self, text: str) -> float:
        """Calculate format quality score"""
        score = 50.0

        # Length check (ideal: 300-800 words)
        words = len(text.split())
        if 300 <= words <= 800:
            score += 20
        elif words > 100:
            score += 10

        # Email present
        if re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text):
            score += 10

        # Phone present
        if re.search(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text):
            score += 10

        # Bullet points / action verbs
        action_verbs = ['developed', 'managed', 'led', 'created', 'implemented',
                        'designed', 'built', 'improved', 'increased', 'reduced',
                        'achieved', 'delivered', 'coordinated', 'analyzed']
        if any(v in text.lower() for v in action_verbs):
            score += 10

        return min(round(score, 1), 100)

    def detect_document_type(self, text: str) -> str:
        """Detect if document is a resume or something else"""
        resume_signals = ['experience', 'education', 'skills', 'resume', 'cv',
                          'curriculum vitae', 'work history', 'employment']
        text_lower = text.lower()
        matches = sum(1 for s in resume_signals if s in text_lower)
        return 'resume' if matches >= 2 else 'document'

    def generate_suggestions(self, text: str, sections: dict, keyword_match: dict) -> list:
        """Generate improvement suggestions"""
        suggestions = []

        if not sections.get('summary'):
            suggestions.append("Add a professional summary to highlight your key qualifications.")
        if not sections.get('projects'):
            suggestions.append("Consider adding a projects section to showcase practical experience.")
        if not sections.get('certifications'):
            suggestions.append("Add relevant certifications to strengthen your profile.")
        if keyword_match['missing_skills']:
            suggestions.append(f"Add these missing skills if you have them: {', '.join(keyword_match['missing_skills'][:3])}")
        if len(text.split()) < 300:
            suggestions.append("Your resume seems short. Add more details about your experience and achievements.")

        return suggestions

    def analyze_resume(self, resume_data: dict, role_info: dict) -> dict:
        """Main resume analysis function"""
        text = resume_data.get('raw_text', '')

        if not text or not text.strip():
            return {'error': 'No text could be extracted from the resume.'}

        document_type = self.detect_document_type(text)
        contact_info = self.extract_contact_info(text)
        sections = self.detect_sections(text)
        keyword_match = self.calculate_keyword_match(text, role_info)
        format_score = self.calculate_format_score(text)
        section_score = self.calculate_section_score(sections)

        # ATS score: weighted average
        ats_score = round(
            keyword_match['score'] * 0.4 +
            format_score * 0.3 +
            section_score * 0.3,
            1
        )

        suggestions = self.generate_suggestions(text, sections, keyword_match)

        return {
            'document_type': document_type,
            'name': contact_info['name'],
            'email': contact_info['email'],
            'phone': contact_info['phone'],
            'linkedin': contact_info['linkedin'],
            'github': contact_info['github'],
            'portfolio': contact_info['portfolio'],
            'ats_score': ats_score,
            'keyword_match': keyword_match,
            'format_score': format_score,
            'section_score': section_score,
            'sections': sections,
            'suggestions': suggestions,
            'contact_suggestions': [
                "Add LinkedIn profile URL" if not contact_info['linkedin'] else None,
                "Add GitHub profile" if not contact_info['github'] else None,
            ],
            'summary_suggestions': ["Write a 3-5 sentence professional summary"] if not sections.get('summary') else [],
            'skills_suggestions': ["Organize skills by category (Technical, Soft, Tools)"] if sections.get('skills') else ["Add a dedicated skills section"],
            'experience_suggestions': ["Use bullet points with quantifiable achievements", "Start each bullet with an action verb"],
            'education_suggestions': ["Include GPA if above 3.5", "List relevant coursework"] if sections.get('education') else ["Add education section"],
            'format_suggestions': ["Use consistent formatting", "Keep to 1-2 pages", "Use standard fonts"],
            'education': [],
            'experience': [],
            'projects': [],
            'skills': [],
            'summary': '',
        }
