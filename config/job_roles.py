"""
Job roles configuration for Smart Resume AI
"""

JOB_ROLES = {
    "Software Engineering": {
        "Software Engineer": {
            "description": "Design, develop, and maintain software systems and applications.",
            "required_skills": ["Python", "Java", "C++", "Data Structures", "Algorithms", "Git", "REST APIs", "SQL", "Agile"],
            "preferred_skills": ["Docker", "Kubernetes", "CI/CD", "Cloud (AWS/GCP/Azure)", "Microservices"]
        },
        "Frontend Developer": {
            "description": "Build user-facing web applications and interfaces.",
            "required_skills": ["HTML", "CSS", "JavaScript", "React", "TypeScript", "Responsive Design", "Git"],
            "preferred_skills": ["Next.js", "Vue.js", "Webpack", "Testing (Jest)", "Figma"]
        },
        "Backend Developer": {
            "description": "Develop server-side logic, APIs, and database architecture.",
            "required_skills": ["Python", "Node.js", "REST APIs", "SQL", "NoSQL", "Git", "Docker"],
            "preferred_skills": ["Microservices", "Redis", "Message Queues", "GraphQL", "AWS"]
        },
        "Full Stack Developer": {
            "description": "Work on both frontend and backend of web applications.",
            "required_skills": ["JavaScript", "React", "Node.js", "SQL", "REST APIs", "Git", "HTML/CSS"],
            "preferred_skills": ["TypeScript", "Docker", "MongoDB", "AWS", "CI/CD"]
        },
        "DevOps Engineer": {
            "description": "Manage infrastructure, CI/CD pipelines, and deployment automation.",
            "required_skills": ["Linux", "Docker", "Kubernetes", "CI/CD", "Git", "Bash", "Cloud Platforms"],
            "preferred_skills": ["Terraform", "Ansible", "Jenkins", "Prometheus", "Grafana"]
        },
        "Mobile Developer": {
            "description": "Build native or cross-platform mobile applications.",
            "required_skills": ["React Native", "Flutter", "iOS/Android", "REST APIs", "Git"],
            "preferred_skills": ["Swift", "Kotlin", "Firebase", "Redux", "GraphQL"]
        }
    },
    "Data Science & AI": {
        "Data Scientist": {
            "description": "Analyze complex data sets to inform business decisions using statistical and ML techniques.",
            "required_skills": ["Python", "Machine Learning", "Statistics", "SQL", "Pandas", "NumPy", "Data Visualization"],
            "preferred_skills": ["TensorFlow", "PyTorch", "Spark", "R", "Tableau", "Deep Learning"]
        },
        "Machine Learning Engineer": {
            "description": "Design and implement machine learning models and pipelines.",
            "required_skills": ["Python", "TensorFlow", "PyTorch", "Scikit-learn", "Deep Learning", "SQL", "MLOps"],
            "preferred_skills": ["Kubernetes", "Docker", "Spark", "NLP", "Computer Vision"]
        },
        "Data Analyst": {
            "description": "Collect, process, and perform statistical analysis on large datasets.",
            "required_skills": ["SQL", "Python", "Excel", "Data Visualization", "Statistics", "Tableau/Power BI"],
            "preferred_skills": ["R", "Pandas", "Google Analytics", "A/B Testing", "ETL"]
        },
        "AI Engineer": {
            "description": "Build and deploy AI-powered applications and systems.",
            "required_skills": ["Python", "LLMs", "Deep Learning", "REST APIs", "Prompt Engineering", "Vector Databases"],
            "preferred_skills": ["LangChain", "RAG", "Fine-tuning", "MLOps", "Cloud AI Services"]
        },
        "Business Intelligence Analyst": {
            "description": "Transform data into actionable business insights using BI tools.",
            "required_skills": ["SQL", "Power BI", "Tableau", "Excel", "Data Modeling", "ETL"],
            "preferred_skills": ["Python", "DAX", "SSRS", "Azure", "Looker"]
        }
    },
    "Cloud & Infrastructure": {
        "Cloud Engineer": {
            "description": "Design, implement, and manage cloud infrastructure and services.",
            "required_skills": ["AWS/GCP/Azure", "Linux", "Docker", "Kubernetes", "Terraform", "Networking"],
            "preferred_skills": ["Ansible", "CI/CD", "Security", "Cost Optimization", "Serverless"]
        },
        "Site Reliability Engineer": {
            "description": "Ensure reliability, scalability, and performance of production systems.",
            "required_skills": ["Linux", "Python/Go", "Kubernetes", "Monitoring", "Incident Management", "CI/CD"],
            "preferred_skills": ["Prometheus", "Grafana", "Chaos Engineering", "On-call", "SLOs/SLAs"]
        },
        "Solutions Architect": {
            "description": "Design end-to-end technical solutions aligned with business requirements.",
            "required_skills": ["Cloud Architecture", "AWS/Azure/GCP", "System Design", "Security", "Networking"],
            "preferred_skills": ["Cost Optimization", "Migration", "Microservices", "Enterprise Architecture"]
        }
    },
    "Cybersecurity": {
        "Security Engineer": {
            "description": "Protect systems, networks, and data from cyber threats.",
            "required_skills": ["Network Security", "SIEM", "Penetration Testing", "Python", "Firewalls", "Linux"],
            "preferred_skills": ["CISSP", "CEH", "Cloud Security", "Threat Intelligence", "Incident Response"]
        },
        "Penetration Tester": {
            "description": "Ethically hack systems to identify vulnerabilities before attackers.",
            "required_skills": ["Kali Linux", "Metasploit", "Burp Suite", "Networking", "Python/Bash", "OWASP"],
            "preferred_skills": ["CEH", "OSCP", "Web App Testing", "Social Engineering", "Reverse Engineering"]
        }
    },
    "Product & Design": {
        "Product Manager": {
            "description": "Define product vision, roadmap, and work cross-functionally to deliver value.",
            "required_skills": ["Product Roadmap", "User Stories", "Agile/Scrum", "Data Analysis", "Stakeholder Management"],
            "preferred_skills": ["SQL", "Figma", "A/B Testing", "OKRs", "Market Research"]
        },
        "UX/UI Designer": {
            "description": "Create intuitive and visually appealing user experiences.",
            "required_skills": ["Figma", "User Research", "Wireframing", "Prototyping", "Design Systems", "Usability Testing"],
            "preferred_skills": ["Adobe XD", "HTML/CSS", "Motion Design", "Accessibility", "Design Thinking"]
        }
    },
    "Business & Management": {
        "Project Manager": {
            "description": "Plan, execute, and close projects on time and within budget.",
            "required_skills": ["Project Planning", "Agile/Scrum", "Risk Management", "Stakeholder Communication", "Budgeting"],
            "preferred_skills": ["PMP", "Jira", "MS Project", "Change Management", "PRINCE2"]
        },
        "Business Analyst": {
            "description": "Bridge the gap between business needs and technical solutions.",
            "required_skills": ["Requirements Gathering", "Process Modeling", "SQL", "Excel", "Communication", "Agile"],
            "preferred_skills": ["Tableau", "Visio", "BPMN", "User Stories", "Data Analysis"]
        }
    }
}
