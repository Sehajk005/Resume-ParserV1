import streamlit as st
import tempfile, shutil, os
from parser import extract_text, extract_entities, clean_text
from scoring import score_resume
from utils import load_job_profiles

job_profiles = load_job_profiles()

st.set_page_config(page_title="Intelligent Resume Parser", layout="centered", page_icon="🚀")
st.title("Intelligent Resume Parser")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = "role_selection"
if "user_type" not in st.session_state:
    st.session_state.user_type = None

# Sidebar User Role Selection
st.sidebar.title("Navigation")
user_type = st.sidebar.radio("Who are you?", ["HR / Recruiter", "Job Seeker"])
st.session_state.user_type = user_type

# Display job statistics in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### Available Positions")
for category, roles in job_profiles.items():
    st.sidebar.markdown(f"**{category}**: {len(roles)} roles")

# Highlight trending roles
st.sidebar.markdown("---")
st.sidebar.markdown("### Trending Roles")
trending_roles = ["AI/ML Engineer", "Cloud Developer", "AI/ML Architect", "Cloud Architect", "AI Product Manager"]
for role in trending_roles:
    st.sidebar.markdown(f"{role}")

# Step 1: HR / Recruiter Flow
if user_type == "HR / Recruiter":
    st.header("Advanced Resume Evaluation System")
    st.markdown("*Evaluate candidates across all experience levels with AI-powered analysis*")

    col1, col2 = st.columns(2)
    with col1:
        job_post = st.selectbox("Select Candidate Type", 
                               list(job_profiles.keys()),
                               help="Choose the experience level you're hiring for")
    with col2:
        job_roles = list(job_profiles[job_post].keys())
        job_category = st.selectbox("Select Job Role", 
                                  job_roles,
                                  help="Select the specific role you're recruiting for")

    # Show role details in expandable section
    with st.expander(f"View {job_category} Requirements"):
        selected_profile = job_profiles[job_post][job_category]
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Required Skills:**")
            for skill in selected_profile.get("required_skills", []):
                st.markdown(f"• {skill}")
        with col2:
            st.markdown("**Preferred Skills:**")
            for skill in selected_profile.get("preferred_skills", []):
                st.markdown(f"• {skill}")
        
        st.markdown(f"**Minimum Experience:** {selected_profile.get('min_experience', 0)} years")

    uploaded_files = st.file_uploader("Upload Multiple Resumes", 
                                    type=["pdf", "docx"], 
                                    accept_multiple_files=True,
                                    help="Upload multiple resumes for batch processing")
    
    col1, col2 = st.columns(2)
    with col1:
        top_n = st.slider("Number of top candidates to show", 1, 20, 5)
    with col2:
        min_score = st.slider("Minimum score threshold", 0, 100, 50)

    if st.button("🔍 Evaluate Resumes", type="primary") and uploaded_files:
        progress_bar = st.progress(0)
        st.info(f"🔄 Processing {len(uploaded_files)} resumes...")

        results = []
        for i, resume_file in enumerate(uploaded_files):
            # Update progress
            progress_bar.progress((i + 1) / len(uploaded_files))
            
            # Preserve extension
            file_ext = os.path.splitext(resume_file.name)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
                shutil.copyfileobj(resume_file, tmp)
                tmp_path = tmp.name

            raw_text = extract_text(tmp_path)
            cleaned_text = clean_text(raw_text)
            parsed = extract_entities(cleaned_text)
            job_profile = job_profiles[job_post][job_category]
            score_data = score_resume(parsed, job_profile, cleaned_text, file_extension=file_ext.lstrip("."))

            results.append((resume_file.name, score_data["total_score"], score_data))

        # Filter by minimum score and sort
        filtered_results = [(name, score, details) for name, score, details in results if score >= min_score]
        sorted_results = sorted(filtered_results, key=lambda x: x[1], reverse=True)[:top_n]
        
        progress_bar.empty()
        
        if sorted_results:
            st.success(f"Found {len(sorted_results)} candidates above {min_score}% threshold")
            
            # Summary statistics
            scores = [score for _, score, _ in sorted_results]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Highest Score", f"{max(scores)}/100")
            with col2:
                st.metric("Average Score", f"{sum(scores)/len(scores):.1f}/100")
            with col3:
                st.metric("Qualified Candidates", len(sorted_results))
            
            st.markdown("---")
            
            for rank, (name, score, details) in enumerate(sorted_results, 1):
                with st.expander(f"#{rank} {name} — Score: {score}/100", expanded=(rank <= 3)):
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.json(details["breakdown"])
                    with col2:
                        # Score visualization
                        score_color = "🟢" if score >= 80 else "🟡" if score >= 60 else "🔴"
                        st.markdown(f"### {score_color} {score}/100")
                        
                        # Quick stats
                        breakdown = details["breakdown"]
                        st.markdown("**Quick Stats:**")
                        for key, value in breakdown.items():
                            if isinstance(value, (int, float)):
                                st.markdown(f"• {key}: {value}")
        else:
            st.warning(f"No candidates found above {min_score}% threshold. Consider lowering the threshold.")

# Step 2: Job Seeker Flow
elif user_type == "Job Seeker":
    st.header("Personal Resume Optimizer")
    st.markdown("*Get detailed feedback and improve your resume for your target role*")

    col1, col2 = st.columns(2)
    with col1:
        job_post = st.selectbox("I am applying as", 
                               list(job_profiles.keys()),
                               help="Select your experience level")
    with col2:
        job_roles = list(job_profiles[job_post].keys())
        job_category = st.selectbox("Target Job Role", 
                                  job_roles,
                                  help="Choose the role you're targeting")

    # Show role insights
    with st.expander(f"Insights for {job_category} ({job_post})"):
        selected_profile = job_profiles[job_post][job_category]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Must-Have Skills:**")
            for skill in selected_profile.get("required_skills", []):
                st.markdown(f"• {skill}")
            
            st.markdown("**Bonus Skills:**")
            for skill in selected_profile.get("preferred_skills", [])[:5]:  # Show top 5
                st.markdown(f"• {skill}")
        
        with col2:
            st.markdown("**Resume Keywords to Include:**")
            keywords = selected_profile.get("keywords", [])
            for keyword in keywords[:8]:  # Show top 8
                st.markdown(f"• {keyword}")
            
            st.markdown("**Job-Specific Terms:**")
            job_keywords = selected_profile.get("job_specific_keywords", [])
            for keyword in job_keywords[:5]:  # Show top 5
                st.markdown(f"• {keyword}")
        
        exp_req = selected_profile.get("min_experience", 0)
        if exp_req > 0:
            st.info(f"Typical experience requirement: {exp_req}+ years")
        else:
            st.info("Entry-level position - perfect for starting your career!")

    uploaded_file = st.file_uploader("Upload Your Resume", 
                                   type=["pdf", "docx"],
                                   help="Upload your resume in PDF or DOCX format")

    if st.button("Analyze My Resume", type="primary") and uploaded_file:
        with st.spinner("AI is analyzing your resume..."):
            file_ext = os.path.splitext(uploaded_file.name)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
                shutil.copyfileobj(uploaded_file, tmp)
                tmp_path = tmp.name

            raw_text = extract_text(tmp_path)
            cleaned_text = clean_text(raw_text)
            parsed = extract_entities(cleaned_text)
            job_profile = job_profiles[job_post][job_category]
            score_data = score_resume(parsed, job_profile, cleaned_text, file_extension=file_ext.lstrip("."))

        # Score display with visual indicator
        score = score_data['total_score']
        if score >= 80:
            st.success(f"Excellent! Your resume scores {score}/100")
            score_emoji = "🟢"
        elif score >= 65:
            st.info(f"Good job! Your resume scores {score}/100")
            score_emoji = "🟡"
        else:
            st.warning(f"Room for improvement! Your resume scores {score}/100")
            score_emoji = "🔴"

        # Detailed breakdown
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Detailed Analysis")
            st.json(score_data["breakdown"])
        
        with col2:
            st.markdown(f"### {score_emoji} Overall Score")
            st.markdown(f"# {score}/100")
            
            # Score interpretation
            if score >= 80:
                st.markdown("**Status:** Ready to apply!")
            elif score >= 65:
                st.markdown("**Status:** Minor tweaks needed")
            else:
                st.markdown("**Status:** Needs improvement")

        # Enhanced feedback section
        st.markdown("---")
        st.markdown("### Personalized Improvement Tips")
        
        breakdown = score_data["breakdown"]
        
        # Specific feedback based on score components
        feedback_given = False
        
        if breakdown.get("skills_score", 0) < 70:
            st.markdown("#### Skills Enhancement")
            st.markdown("- Add more relevant technical skills from the required list")
            st.markdown("- Include specific tools and technologies mentioned in job descriptions")
            st.markdown("- Consider getting certifications in trending technologies (AI/ML, Cloud)")
            feedback_given = True
        
        if breakdown.get("keywords_score", 0) < 70:
            st.markdown("#### Keyword Optimization")
            st.markdown("- Include more industry-specific keywords")
            st.markdown("- Use action verbs like 'developed', 'implemented', 'optimized'")
            st.markdown("- Add job-specific terminology from the role requirements")
            feedback_given = True
        
        if breakdown.get("experience_score", 0) < 70:
            st.markdown("#### Experience Section")
            st.markdown("- Add more quantifiable achievements (numbers, percentages, metrics)")
            st.markdown("- Include relevant projects, internships, or volunteer work")
            st.markdown("- Highlight leadership and collaboration experiences")
            feedback_given = True
        
        # General tips based on overall score
        if score < 70:
            st.markdown("#### General Improvements")
            if not feedback_given:
                st.markdown("- Ensure your resume is well-formatted and error-free")
                st.markdown("- Add a professional summary highlighting your key strengths")
                st.markdown("- Include relevant coursework, projects, or certifications")
            
            # Role-specific advice
            if "AI" in job_category or "ML" in job_category:
                st.markdown("- Showcase any data science projects or machine learning coursework")
                st.markdown("- Mention programming languages like Python, R, SQL")
                st.markdown("- Include any experience with ML frameworks (TensorFlow, PyTorch)")
            elif "Cloud" in job_category:
                st.markdown("- Highlight any cloud platform experience (AWS, Azure, GCP)")
                st.markdown("- Mention containerization tools (Docker, Kubernetes)")
                st.markdown("- Include infrastructure or DevOps related projects")
        else:
            st.success("Your resume is in great shape! Just fine-tune based on specific job requirements.")
        
        # Additional resources
        st.markdown("---")
        st.markdown("### Additional Resources")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Skill Building:**")
            st.markdown("- Online courses (Coursera, edX, Udemy)")
            st.markdown("- Professional certifications")
            st.markdown("- Open source contributions")
        with col2:
            st.markdown("**Resume Tips:**")
            st.markdown("- Keep it concise (1-2 pages)")
            st.markdown("- Use consistent formatting")
            st.markdown("- Tailor for each application")

# Footer
st.markdown("---")
st.markdown("### Future-Ready Career Guidance")