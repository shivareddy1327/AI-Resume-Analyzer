"""
Courses and video resources configuration for Smart Resume AI
"""

COURSES_BY_CATEGORY = {
    "Software Engineering": {
        "Software Engineer": [
            ("CS50: Introduction to Computer Science", "https://www.edx.org/course/cs50s-introduction-to-computer-science"),
            ("Data Structures and Algorithms", "https://www.coursera.org/specializations/data-structures-algorithms"),
            ("The Complete Python Bootcamp", "https://www.udemy.com/course/complete-python-bootcamp/"),
            ("System Design Interview", "https://www.educative.io/courses/grokking-the-system-design-interview"),
            ("Clean Code", "https://www.udemy.com/course/writing-clean-code/"),
            ("Git & GitHub Masterclass", "https://www.udemy.com/course/git-complete/"),
        ],
        "Frontend Developer": [
            ("The Complete JavaScript Course", "https://www.udemy.com/course/the-complete-javascript-course/"),
            ("React - The Complete Guide", "https://www.udemy.com/course/react-the-complete-guide-incl-redux/"),
            ("CSS for JavaScript Developers", "https://css-for-js.dev/"),
            ("TypeScript Masterclass", "https://www.udemy.com/course/understanding-typescript/"),
            ("Next.js & React", "https://www.udemy.com/course/nextjs-react-the-complete-guide/"),
            ("Frontend Masters", "https://frontendmasters.com/"),
        ],
        "Backend Developer": [
            ("Node.js - The Complete Guide", "https://www.udemy.com/course/nodejs-the-complete-guide/"),
            ("Django for Beginners", "https://djangoforbeginners.com/"),
            ("FastAPI Course", "https://www.udemy.com/course/fastapi-the-complete-course/"),
            ("Database Design & SQL", "https://www.coursera.org/learn/sql-for-data-science"),
            ("Docker & Kubernetes", "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/"),
            ("REST API Design", "https://www.udemy.com/course/rest-api/"),
        ],
        "DevOps Engineer": [
            ("Docker & Kubernetes Complete Guide", "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/"),
            ("Terraform for Beginners", "https://www.udemy.com/course/terraform-beginner-to-advanced/"),
            ("AWS Certified DevOps Engineer", "https://aws.amazon.com/certification/certified-devops-engineer-professional/"),
            ("CI/CD with Jenkins", "https://www.udemy.com/course/jenkins-from-zero-to-hero/"),
            ("Linux Administration", "https://www.udemy.com/course/complete-linux-training-course-to-get-your-dream-it-job/"),
            ("Ansible for DevOps", "https://www.udemy.com/course/ansible-for-the-absolute-beginner/"),
        ],
        "Full Stack Developer": [
            ("The Web Developer Bootcamp", "https://www.udemy.com/course/the-web-developer-bootcamp/"),
            ("MERN Stack Front to Back", "https://www.udemy.com/course/mern-stack-front-to-back/"),
            ("Full Stack Open", "https://fullstackopen.com/en/"),
            ("React & Node.js Complete Guide", "https://www.udemy.com/course/react-nodejs-express-mongodb-the-mern-fullstack-guide/"),
            ("PostgreSQL Bootcamp", "https://www.udemy.com/course/the-complete-python-postgresql-developer-course/"),
            ("GraphQL with React", "https://www.udemy.com/course/graphql-with-react-course/"),
        ],
        "Mobile Developer": [
            ("React Native - The Practical Guide", "https://www.udemy.com/course/react-native-the-practical-guide/"),
            ("Flutter & Dart Complete Guide", "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/"),
            ("iOS & Swift - The Complete iOS App Development Bootcamp", "https://www.udemy.com/course/ios-13-app-development-bootcamp/"),
            ("Android Development with Kotlin", "https://www.udemy.com/course/android-kotlin-developer/"),
            ("Firebase for Mobile Apps", "https://www.udemy.com/course/firebase-course/"),
            ("App Store Optimization", "https://www.udemy.com/course/app-store-optimization/"),
        ],
    },
    "Data Science & AI": {
        "Data Scientist": [
            ("Machine Learning by Andrew Ng", "https://www.coursera.org/learn/machine-learning"),
            ("Python for Data Science", "https://www.coursera.org/specializations/python"),
            ("IBM Data Science Professional Certificate", "https://www.coursera.org/professional-certificates/ibm-data-science"),
            ("Statistics for Data Science", "https://www.udemy.com/course/statistics-for-data-science-and-business-analysis/"),
            ("Deep Learning Specialization", "https://www.coursera.org/specializations/deep-learning"),
            ("Tableau for Data Science", "https://www.udemy.com/course/tableau10/"),
        ],
        "Machine Learning Engineer": [
            ("TensorFlow Developer Certificate", "https://www.coursera.org/professional-certificates/tensorflow-in-practice"),
            ("PyTorch for Deep Learning", "https://www.udemy.com/course/pytorch-for-deep-learning-in-python-bootcamp/"),
            ("MLOps Fundamentals", "https://www.coursera.org/learn/mlops-fundamentals"),
            ("Feature Engineering for ML", "https://www.udemy.com/course/feature-engineering-for-machine-learning/"),
            ("NLP with Python", "https://www.udemy.com/course/nlp-natural-language-processing-with-python/"),
            ("Computer Vision with OpenCV", "https://www.udemy.com/course/master-computer-vision-with-opencv-in-python/"),
        ],
        "Data Analyst": [
            ("Google Data Analytics Certificate", "https://www.coursera.org/professional-certificates/google-data-analytics"),
            ("SQL for Data Analysis", "https://www.udacity.com/course/sql-for-data-analysis--ud198"),
            ("Power BI Desktop", "https://www.udemy.com/course/microsoft-power-bi-up-running-with-power-bi-desktop/"),
            ("Excel for Data Analytics", "https://www.udemy.com/course/excel-for-data-analysis/"),
            ("Python Pandas Masterclass", "https://www.udemy.com/course/the-pandas-bootcamp/"),
            ("A/B Testing and Experimentation", "https://www.udemy.com/course/the-complete-guide-to-abtesting/"),
        ],
        "AI Engineer": [
            ("LangChain & LLM Apps", "https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/"),
            ("ChatGPT Prompt Engineering", "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/"),
            ("Building LLM Apps", "https://www.udemy.com/course/master-openai-api/"),
            ("Vector Databases", "https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/"),
            ("Hugging Face NLP", "https://huggingface.co/learn/nlp-course/"),
            ("RAG with LangChain", "https://www.deeplearning.ai/short-courses/building-and-evaluating-advanced-rag/"),
        ],
        "Business Intelligence Analyst": [
            ("Microsoft Power BI Masterclass", "https://www.udemy.com/course/microsoft-power-bi-up-running-with-power-bi-desktop/"),
            ("Tableau 2024 A-Z", "https://www.udemy.com/course/tableau10/"),
            ("SQL for Business Intelligence", "https://www.udemy.com/course/the-complete-sql-bootcamp/"),
            ("Data Warehouse Fundamentals", "https://www.udemy.com/course/data-warehouse-fundamentals-for-beginners/"),
            ("DAX in Power BI", "https://www.udemy.com/course/dax-for-power-bi/"),
            ("Looker Studio", "https://analytics.google.com/analytics/academy/"),
        ],
    },
    "Cloud & Infrastructure": {
        "Cloud Engineer": [
            ("AWS Solutions Architect Associate", "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/"),
            ("Google Cloud Professional Architect", "https://www.coursera.org/professional-certificates/gcp-cloud-architect"),
            ("Azure Administrator Associate", "https://www.udemy.com/course/az-104-microsoft-azure-administrator/"),
            ("Terraform - Zero to Hero", "https://www.udemy.com/course/terraform-beginner-to-advanced/"),
            ("Docker & Kubernetes", "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/"),
            ("Cloud Security Fundamentals", "https://www.coursera.org/learn/cloud-security-basics"),
        ],
        "Site Reliability Engineer": [
            ("SRE Fundamentals", "https://www.coursera.org/learn/site-reliability-engineering-slos"),
            ("Kubernetes for Administrators", "https://www.udemy.com/course/learn-kubernetes/"),
            ("Prometheus & Grafana", "https://www.udemy.com/course/monitoring-and-alerting-with-prometheus/"),
            ("Go Programming Language", "https://www.udemy.com/course/learn-go-the-complete-bootcamp-course-golang/"),
            ("Linux System Administration", "https://www.udemy.com/course/complete-linux-training-course-to-get-your-dream-it-job/"),
            ("Incident Management", "https://www.pagerduty.com/resources/learn/incident-management/"),
        ],
    },
    "Cybersecurity": {
        "Security Engineer": [
            ("CompTIA Security+", "https://www.udemy.com/course/comptia-security-certification-sy0-601-the-total-course/"),
            ("Ethical Hacking Bootcamp", "https://www.udemy.com/course/learn-ethical-hacking-from-scratch/"),
            ("CISSP Certification", "https://www.udemy.com/course/cissp-certification-exam-prep-course-in-cybersecurity/"),
            ("Network Security", "https://www.coursera.org/learn/network-security-finance"),
            ("Python for Cybersecurity", "https://www.udemy.com/course/python-for-cybersecurity-beginners/"),
            ("SOC Analyst Training", "https://www.udemy.com/course/master-in-soc-operations/"),
        ],
        "Penetration Tester": [
            ("Ethical Hacking - CEH", "https://www.udemy.com/course/learn-ethical-hacking-from-scratch/"),
            ("Kali Linux Penetration Testing", "https://www.udemy.com/course/kali-linux-tutorial-for-beginners/"),
            ("OSCP Preparation", "https://www.offensive-security.com/pwk-oscp/"),
            ("Burp Suite Web App Testing", "https://www.udemy.com/course/burp-suite-web-application-penetration-testing/"),
            ("OWASP Top 10", "https://owasp.org/www-project-top-ten/"),
            ("Metasploit Framework", "https://www.udemy.com/course/metasploit-for-beginners/"),
        ],
    },
    "Product & Design": {
        "Product Manager": [
            ("Product Management Fundamentals", "https://www.coursera.org/learn/product-management"),
            ("Agile Product Ownership", "https://www.udemy.com/course/agile-scrum-master-certification/"),
            ("Google UX Design Certificate", "https://www.coursera.org/professional-certificates/google-ux-design"),
            ("Product Analytics with SQL", "https://www.udemy.com/course/the-complete-sql-bootcamp/"),
            ("Product-Led Growth", "https://www.productled.com/"),
            ("OKR Goal Setting", "https://www.udemy.com/course/okrs-objectives-and-key-results/"),
        ],
        "UX/UI Designer": [
            ("Google UX Design Certificate", "https://www.coursera.org/professional-certificates/google-ux-design"),
            ("Figma UI UX Design Essentials", "https://www.udemy.com/course/figma-ux-ui-design-user-experience-tutorial-course/"),
            ("User Research Methods", "https://www.udemy.com/course/user-experience-research-design/"),
            ("Design Systems", "https://www.udemy.com/course/design-systems-with-figma/"),
            ("Adobe XD", "https://www.udemy.com/course/adobe-xd-cc/"),
            ("UI Animation", "https://www.udemy.com/course/motion-design-with-css/"),
        ],
    },
    "Business & Management": {
        "Project Manager": [
            ("PMP Certification", "https://www.udemy.com/course/pmp-pmbok6-exam/"),
            ("Agile Scrum Master", "https://www.udemy.com/course/agile-scrum-master-certification/"),
            ("Jira - Project Management", "https://www.udemy.com/course/the-complete-guide-to-jira-with-real-world-examples/"),
            ("Risk Management", "https://www.udemy.com/course/risk-management-for-projects/"),
            ("MS Project", "https://www.udemy.com/course/master-microsoft-project/"),
            ("Leadership & Management", "https://www.coursera.org/specializations/leadership-development-for-engineers"),
        ],
        "Business Analyst": [
            ("Business Analysis Fundamentals", "https://www.udemy.com/course/fundamentals-of-business-analysis/"),
            ("SQL for Business Analysts", "https://www.udemy.com/course/the-complete-sql-bootcamp/"),
            ("Requirements Engineering", "https://www.udemy.com/course/mastering-requirements-process/"),
            ("Process Modeling with BPMN", "https://www.udemy.com/course/bpmn-all-you-need-to-know-about-business-process-modeling/"),
            ("Tableau for Analysts", "https://www.udemy.com/course/tableau10/"),
            ("Agile BA Skills", "https://www.udemy.com/course/agile-ba-skills/"),
        ],
    },
}

RESUME_VIDEOS = {
    "Resume Writing Tips": [
        ("How to Write a Resume", "https://www.youtube.com/watch?v=y8YH0Qbu5h4"),
        ("ATS Resume Tips", "https://www.youtube.com/watch?v=J-8V7JZ4ZsY"),
    ],
    "Resume Mistakes to Avoid": [
        ("Common Resume Mistakes", "https://www.youtube.com/watch?v=bKkRHg4hLTg"),
        ("Resume Red Flags", "https://www.youtube.com/watch?v=0GkXrFSNwh0"),
    ],
}

INTERVIEW_VIDEOS = {
    "Interview Preparation": [
        ("How to Answer Tell Me About Yourself", "https://www.youtube.com/watch?v=kayOhGRcNt4"),
        ("Behavioral Interview Questions", "https://www.youtube.com/watch?v=aeSKZhit1SA"),
    ],
    "Technical Interview": [
        ("LeetCode Strategy", "https://www.youtube.com/watch?v=SVvr3ZjtjI8"),
        ("System Design Interview Tips", "https://www.youtube.com/watch?v=UzLMhqg3_Wc"),
    ],
}


def get_courses_for_role(role: str) -> list:
    """Get courses for a specific role"""
    for category, roles in COURSES_BY_CATEGORY.items():
        if role in roles:
            return roles[role]
    return []


def get_category_for_role(role: str) -> str:
    """Get the category for a specific role"""
    for category, roles in COURSES_BY_CATEGORY.items():
        if role in roles:
            return category
    return ""
