import re
import dateutil.parser
from dateutil.relativedelta import relativedelta
def score_resume(resume_data, job_profile, text, file_extension="pdf"):
    score = 0
    breakdown = {}

    # 1. Content Scoring
    content_score, content_breakdown = score_content(resume_data, job_profile)
    score += content_score
    breakdown['content'] = content_breakdown

    # 2. Formatting Scoring
    formatting_score, formatting_breakdown = score_formatting(text, resume_data, file_extension)
    score += formatting_score
    breakdown['formatting'] = formatting_breakdown
    

    # 3. Optimization Scoring
    optimization_score, optimization_breakdown = score_optimization(text, job_profile)
    score += optimization_score
    breakdown['optimization'] = optimization_breakdown

    # 4. Alignment Scoring
    alignment_score, alignment_breakdown = score_alignment(text, resume_data, job_profile)
    score += alignment_score
    breakdown['alignment'] = alignment_breakdown

    return {
        "total_score": round(score),
        "breakdown": breakdown,
        "parsed_data": resume_data,
        "content_score": content_score,
        "formatting_score": formatting_score,
        "alignment_score": alignment_score,
        "optimization_score": optimization_score
    }




action_verbs = {
    "led", "developed", "implemented", "created", "designed",
    "managed", "built", "optimized", "launched", "streamlined",
    "executed", "increased", "reduced", "automated", "delivered"
}   
# function to score content
def score_content(resume_data, job_profile):
    content_score = 0
    content_breakdown = {
        "required_matched": [],
        "preferred_matched": [],
        "missing_required": [],
        "qualifications_found": [],
        "action_verb_lines": [],
        "keywords_matches": []
    }
    
    text = "\n".join(sum(resume_data.values(), [])) # join all values of resume_data into a single string
    
    # Required Skills Matching
    required = job_profile.get("required_skills", [])
    required_matches = [skill for skill in required if skill.lower() in text.lower()]
    content_breakdown["required_matched"] = required_matches
    content_breakdown["missing_required"] = [skill for skill in required if skill.lower() not in text.lower()]
    content_score += min(len(required_matches) * 2, 10)
    
    # Preferred skill matching
    preferred = job_profile.get("preferred_skills", [])
    preferred_matches = [skill for skill in preferred if skill.lower() in text.lower()]
    content_breakdown["preferred_matched"] = preferred_matches
    content_score += min(len(preferred_matches), 5)
    
    # qualifications achievements 
    achievement_verbs = [
    "accelerated", "boosted", "cut", "drove", "enhanced", "exceeded", "generated",
    "optimized", "streamlined", "transformed", "led", "initiated", "launched",
    "executed", "revamped", "overhauled", "achieved", "surpassed", "secured",
    "managed", "mentored", "solved", "won", "closed", "built", "automated"
    ]
    recognitions = ["awarded", "recognized", "certified", "nominated", "winner", "top performer", 
                    "appreciated", "honored", "commendation", "employee of the month", "ranked"]

    if re.search(r"\d+%|\d+\s?(k|K|million|crore|billion|lacks|thosands)|\$\d+|\d+\+\s?(users|clients|projects|leads|deals|campaigns|customers|downloads)", text)\
        or any (v in text.lower() for v in achievement_verbs) or any(r in text.lower() for r in recognitions):
            content_breakdown["qualifications_found"] = True
            content_score += 10
            
    # Action Verbs 
    lines = text.split("\n")
    action_lines = [line for line in lines if any(v in line.lower() for v in action_verbs)]
    content_breakdown["action_verb_lines"] = action_lines
    content_score += min(len(action_lines), 5)
    
    # Keywords Matching
    keywords = job_profile.get("keywords", [])
    keywords_matches = [keyword for keyword in keywords if keyword.lower() in text.lower()]
    content_breakdown["keywords_matches"] = keywords_matches
    content_score += min(len(keywords_matches), 10)
    
    return content_score, content_breakdown
    
    
# Function to score formatting
def score_formatting(text, resume_data, file_extension="pdf"):
    formatting_score = 0
    formatting_breakdown = {
        "section_presence": False,
        "contact_info_present": False,
        "bullet_point_usage": False,
        "font_alignment_consistency": False,
        "date_format_consistency": False,
        "whitespace_and_spacing": False,
        "header_clarity": False,
        "file_foramt_check": False
    }
    # section presence
    headers = ["Education", "Experience", "Skills", "Projects", "Achievements", "Certifications"]
    matches = [header.lower() in text.lower() for header in headers]
    if len(matches) >= 3:
        formatting_breakdown["section_presence"] = True
        formatting_score += 5
        
    # contact info present
    if resume_data.get("email") and resume_data.get("phone"):
        formatting_breakdown["contact_info_present"] = True
        formatting_score += 2
        
    # bullet point usage
    if re.search(r"^\s*[–•●*-]\s+", text, re.MULTILINE):
        formatting_breakdown["bullet_point_usage"] = True
        formatting_score += 3
        
    # date formating
    date_patterns = re.findall(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{2,4}\b", text, re.IGNORECASE)
    if len(date_patterns) >= 2:
        formatting_breakdown["date_format_consistency"] = True
        formatting_score += 2
        
    # font, alignment consistency
    if len(date_patterns) >= 2:
        formatting_breakdown["font_alignment_consistency"] = True
        formatting_score += 2
        
    

    # whitespace and spacing
    lines = [line.strip() for line in text.split("\n") if line.strip() != ""]
    line_lengths = [len(line) for line in lines]

    # Check that the resume is broken into many well-spaced lines
    avg_length = sum(line_lengths) / len(lines) if lines else 0

    if len(lines) > 40 and avg_length < 90:
        formatting_breakdown["whitespace_and_spacing"] = True
        formatting_score += 2
        

    
    # header clarity
    section_lines = text.split("\n")
    target_headers = [h.lower() for h in headers]
    clear_headers = [
        line for line in section_lines
        if any(h in line.strip().lower() for h in target_headers)
    ]

    if len(clear_headers) >= 3:
        formatting_breakdown["header_clarity"] = True
        formatting_score += 2
        
    # file format check
    if file_extension.lower() == "pdf":
        formatting_breakdown["file_foramt_check"] = True
        formatting_score += 2
        
    return formatting_score, formatting_breakdown
    
import requests

def grammar_check(text):
    url = "https://api.languagetool.org/v2/check"
    data = {
        'text': text[:2000],  # limit text length
        'language': 'en-US'
    }
    try:
        response = requests.post(url, data=data)
        result = response.json()
        matches = result.get("matches", [])
        return len(matches)
    except Exception as e:
        print("Grammar API failed:", e)
        return None

def score_optimization(text, job_profile):
    from language_tool_python import LanguageTool
    
    optimization_score = 0
    optimization_breakdown = {
        "tailoring": [],
        "spelling_grammar_issues": 0,
        "concise": False,
        "ats_friendly": False
    }
    
    # tailoring
    keywords = job_profile.get("job_specific_keywords", [])
    matched_keywords = [kw for kw in keywords if kw.lower() in text.lower()]
    optimization_breakdown["tailoring"] = matched_keywords
    optimization_score += 4
    
    
    # Spelling/Grammar Check
    errors = grammar_check(text)
    if errors is not None:
        optimization_breakdown["spelling_grammar_issues"] = errors
        if errors <= 2:
            optimization_score += 5
        elif errors <= 5:
            optimization_score += 3
        elif errors <= 10:
            optimization_score += 1
    else:
        optimization_breakdown["spelling_grammar_issues"] = "API failed"
        optimization_score += 2  # fallback


    
    # concise
    word_count = len(text.split())
    if word_count <= 800:
        optimization_breakdown["concise"] = True
        optimization_score += 5
    elif word_count <= 1200:
        optimization_score += 3
    elif word_count <= 1600:
        optimization_score += 1
        
    # ats friendly
    if not re.search(r'<table|<td|<tr', text, re.IGNORECASE):
        optimization_breakdown["ats_friendly"] = True
        optimization_score += 4
        
    return optimization_score, optimization_breakdown


def score_alignment(text, resume_data, job_profile):
    from difflib import SequenceMatcher

    alignment_score = 0
    alignment_breakdown = {
        "meets_min_experience": False,
        "relevant_roles": [],
        "project_impact": [],
        "side_projects": False,
        "online_presence": False,
        "certifications": False,
        "multi_role_match": 0
    }
    
    # experience alignment
    date_range_pattern = re.findall(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}\s*(?:–|-|to)\s*(?:Present|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})",
        text,
        re.IGNORECASE
    )

    total_months = 0
    for match in re.finditer(
        r"((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})\s*(–|-|to)\s*((Present)|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})",
        text,
        re.IGNORECASE,
    ):
        try:
            start_str = match.group(1)
            end_str = match.group(4)

            start = dateutil.parser.parse(start_str)
            end = dateutil.parser.parse("today") if "present" in end_str.lower() else dateutil.parser.parse(end_str)

            delta = relativedelta(end, start)
            total_months += delta.years * 12 + delta.months
        except:
            continue

    # Convert months to years
    total_years = round(total_months / 12, 1)
    min_exp = job_profile.get("min_experience", 0)

    if total_years >= min_exp:
        alignment_breakdown["meets_min_experience"] = True
        alignment_score += 6
    
    # Fallback if no experience is required and no experience is found
    if not alignment_breakdown["meets_min_experience"] and job_profile.get("min_experience", 0) == 0:
        alignment_breakdown["meets_min_experience"] = True
        alignment_score += 6
        
    # relevant roles
    job_titles = ["developer", "engineer", "analyst", "researcher", "consultant", "manager"]
    matched_roles = [line for line in text.split("\n") if any(title in line.lower() for title in job_titles)]
    alignment_breakdown["relevant_roles"] = matched_roles
    alignment_score += min(len(matched_roles), 2) * 2
    
    # Project Impact
    impact_keywords = ["launched", "delivered", "increased", "optimized", "boosted", "reduced"]
    impact_lines = [line for line in text.split("\n") if any(k in line.lower() for k in impact_keywords)]
    alignment_breakdown["project_impact"] = impact_lines
    alignment_score += min(len(impact_lines), 2) * 2

    # Side Projects
    if any("github" in line.lower() or "open source" in line.lower() for line in text.split("\n")):
        alignment_breakdown["side_projects"] = True
        alignment_score += 3

    # Online Presence
    links = resume_data.get("email", []) + resume_data.get("certifications", []) + text.split("\n")
    if any("linkedin" in line.lower() or "github" in line.lower() or "portfolio" in line.lower() for line in links):
        alignment_breakdown["online_presence"] = True
        alignment_score += 2

    # Certifications
    cert_keywords = ["aws", "gcp", "azure", "pmp", "credential", "completed",
                     "certified", "certification", "badge", "course", 
                     "completed .* course", "earned .* certificate", "aws certified",
                     "microsoft certified", "google cloud certified", "scrum master",
                     "pmp", "six sigma", "cissp", "cka", "ckad", "csm", "ccnp", "ccie"]
    if any(any(cert in c.lower() for cert in cert_keywords) for c in text.split("\n")):
        alignment_breakdown["certifications"] = True
        alignment_score += 2

    # Multi-role match
    all_text = text.lower()
    if sum(all_text.count(role.lower()) for role in ["analyst", "developer", "engineer", "researcher"]) >= 2:
        alignment_breakdown["multi_role_match"] = 1
        alignment_score += 1
        
    return alignment_score, alignment_breakdown
