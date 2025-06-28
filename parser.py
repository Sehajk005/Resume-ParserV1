import pdfplumber
import os
from docx import Document
import spacy
import spacy
nlp = spacy.load("en_core_web_sm")
import re
# Function to extract text from a PDF or DOCX file
def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower() # function to get file extension
    # Read the file based on its extension
    if ext == ".pdf": 
        with pdfplumber.open(file_path) as pdf: # use pdfplumber to read pdf
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text() 
                if page_text:
                    text += page_text + "\n"
    elif ext == ".docx":
        text = ""
        for para in Document(file_path).paragraphs: # use python-docx to read docx
            text += para.text + "\n"
    else:
        raise ValueError("Unsupported file format: Must be a .pdf or .docx")
    
    return text
# Function to get a specific section of text
def extract_sections(text):
    headers = ["Education", "Work Experience", "Skills", "Projects", "Achievements", "Certifications"]
    pattern = r'\b(' + '|'.join(headers) + r')\b'
    parts = re.split(pattern, text, flags=re.IGNORECASE)

    section_map = {}
    current_section = None

    for part in parts:
        part = part.strip()
        if part.lower() in [h.lower() for h in headers]:
            current_section = part.lower()
            section_map[current_section] = ""
        elif current_section:
            section_map[current_section] += part + "\n"

    return section_map

# Function to extract entities from text
def extract_entities(text):
    # Preprocess the text
    doc = nlp(text)

    # Create a dictionary to store the extracted data
    data ={
    "name": [],
    "email": [],
    "phone": [],
    "education": [],
    "experience": [],
    "work_experience": [],
    "skills": [],
    "projects": [],
    "achievements": [],
    "certifications": []
}

    # Extract entities and store them in the dictionary
    for word in doc.ents:
        if word.label_ == "PERSON" and not data["name"]:
            data["name"].append(word.text)
            
    if not data["name"]:# if spacy is unable to extract name, use regex
        lines = text.split('\n')
        for line in lines[:5]:
            match = re.match(r'\b[A-Z]+\s[A-Z]+\b', line.strip())
            if match:
                data["name"].append(match.group(0).title()) # convert to title
                break
        
    email_pattern = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone_pattern = re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
        
    data["email"] = email_pattern
    data["phone"] = phone_pattern
    
    sections = extract_sections(text)

    # Extract skills
    # Section-based skills
    section_skills = [line.strip() for line in sections.get("skills", "").split("\n") if line.strip()]
    text_from_section = " ".join(section_skills)

    # Fallback: check entire resume
    fallback_skills = extract_skills(text, known_skills)

    # Combine both and deduplicate
    all_skills = set(extract_skills(text_from_section, known_skills) + fallback_skills)
    data["skills"] = sorted(all_skills)

    # Extract work experience
    data["work_experience"] = [line.strip() for line in sections.get("work experience", "").split("\n") if line.strip()]
    # Extract education
    data["education"] = [line.strip() for line in sections.get("education", "").split("\n") if line.strip()]    
    # Extract projects
    data["projects"] = [line.strip() for line in sections.get("projects", "").split("\n") if line.strip()]
    # Extract achievements
    data["achievements"] = [line.strip() for line in sections.get("achievements", "").split("\n") if line.strip()]
    # Extract certifications
    data["certifications"] = [line.strip() for line in sections.get("certifications", "").split("\n") if line.strip()]
    
    # extract experience
    lines = text.split("\n")
    summary_exp = [line.strip() for line in lines if looks_like_experience(line)]
    data["experience"].extend(summary_exp)



    return data
def looks_like_experience(line):
    keywords = [
        "years of experience", "developed", "built", "engineered",
        "implemented", "designed", "optimized", "worked on",
        "responsible for", "managed", "led", "coordinated",
        "supervised", "directed", "coached", "trained","mentored",
        "collaborated", "contributed", "participated in", "involved in"
    ]
    return any(keyword in line.lower() for keyword in keywords)

known_skills = [
    "Python", "Java", "C++", "JavaScript", "HTML", "CSS",
    "SQL", "MongoDB", "MySQL", "PostgreSQL", "Oracle",
    "Git", "Docker", "Kubernetes", "AWS", "Azure",
    "Machine Learning", "Deep Learning", "NLP", "Computer Vision",
    "Web Development", "Mobile Development", "Backend Development",
    "Frontend Development", "Full Stack Development", "DevOps",
    "Data Science", "Data Analysis", "Data Visualization",
    "Scikit-learn", "Pandas", "NumPy", "Matplotlib", "Seaborn",
    "TensorFlow", "PyTorch", "Keras", "Streamlit", "FastAPI",
    "Django", "Flask", "React", "Vue", "Angular", "Ember",
    "Spring", "Hibernate", "JPA", "Ruby On Rails", "Api Development", "Database Management", "Restful Services",
    "API Gateway", "API Security", "API Design", "API Testing", "API Documentation", "API Performance Optimization",
    "Cloud Computing", "Cloud Security", "Cloud Migration", "Cloud Deployment", "Cloud Management", "Cloud Monitoring",
    "Cloud Cost Optimization", "Cloud Scalability", "Cloud Reliability", "Cloud Performance", "Cloud Migration"
]
def extract_skills(text, known_skills):
    skills = []
    for skill in known_skills:
        if skill.lower() in text.lower():
            skills.append(skill)
    return skills

def clean_text(text):
    # Replace known icons if needed (optional)
    icon_map = {
        '\uf073': '[📅]',  # calendar icon
        '\uf08d': '[📍]',  # location icon
    }
    for icon, replacement in icon_map.items():
        text = text.replace(icon, replacement)

    # Remove private use area icons (excluding valid printable ones)
    text = re.sub(r'[\uf000-\uf0ff]', '', text)

    # Remove control characters, but **preserve** line breaks
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)

    return text
