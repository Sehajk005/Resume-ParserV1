import streamlit as st
def provide_content_recommendations(content_score, content_breakdown, max_possible_score=40):
    
    # Calculate percentage
    score_percentage = (content_score / max_possible_score) * 100
    feedback_given = False
    
    st.markdown(f"**Content Score: {content_score}/{max_possible_score} ({score_percentage:.1f}%)**")
    
    # 70-80% range - Good score, minor improvements
    if 70 <= score_percentage < 80:
        st.markdown("#### **Great Job! Your resume shows strong alignment with the job requirements.**")
        
        # Check for missing required skills
        if content_breakdown.get("missing_required"):
            st.markdown("#### **Skills Fine-tuning:**")
            missing_skills = content_breakdown["missing_required"][:3]  # Show top 3
            for skill in missing_skills:
                st.markdown(f"- Consider adding experience with **{skill}** if you have it")
            st.markdown("- Reorganize existing content to highlight these skills more prominently")
            feedback_given = True
        
        # Enhance quantifiable achievements
        if not content_breakdown.get("qualifications_found"):
            st.markdown("#### **Achievement Enhancement:**")
            st.markdown("- Add specific metrics to your accomplishments (percentages, numbers, dollar amounts)")
            st.markdown("- Quantify your impact: 'Increased efficiency by 25%' vs 'Improved efficiency'")
            st.markdown("- Include recognition or awards you've received")
            feedback_given = True
        
        # Keyword optimization
        if len(content_breakdown.get("keywords_matches", [])) < 5:
            st.markdown("#### **Keyword Optimization:**")
            st.markdown("- Incorporate more industry-specific terminology from the job description")
            st.markdown("- Use variations of key terms throughout your resume")
            st.markdown("- Research trending keywords in your field and include relevant ones")
            feedback_given = True
    
    # 50-70% range - Moderate improvements needed
    elif 50 <= score_percentage < 70:
        st.markdown("#### **Good foundation! Let's strengthen your resume to better match the role.**")
        
        # Required skills focus
        if content_breakdown.get("missing_required"):
            st.markdown("#### **Priority: Required Skills**")
            missing_skills = content_breakdown["missing_required"]
            for skill in missing_skills:
                st.markdown(f"- **Add {skill}** - This is a required skill for the position")
            st.markdown("- Create specific bullet points demonstrating experience with these skills")
            st.markdown("- If you lack these skills, consider online courses or projects to gain experience")
            feedback_given = True
        
        # Preferred skills enhancement
        if len(content_breakdown.get("preferred_matched", [])) < 3:
            st.markdown("#### **Preferred Skills Enhancement:**")
            st.markdown("- Add more preferred skills from the job description to stand out")
            st.markdown("- Highlight any certifications or training in preferred technologies")
            st.markdown("- Mention side projects or learning initiatives related to preferred skills")
            feedback_given = True
        
        # Achievement strengthening
        if not content_breakdown.get("qualifications_found"):
            st.markdown("#### **Achievement & Impact:**")
            st.markdown("- **Critical:** Add quantifiable achievements with specific metrics")
            st.markdown("- Include percentages, dollar amounts, time savings, or growth numbers")
            st.markdown("- Add any awards, recognitions, or performance rankings")
            st.markdown("- Use strong action verbs to start each bullet point")
            feedback_given = True
        
        # Action verb improvement
        if len(content_breakdown.get("action_verb_lines", [])) < 3:
            st.markdown("#### **Content Structure:**")
            st.markdown("- Start more bullet points with strong action verbs")
            st.markdown("- Use verbs like: accelerated, optimized, led, executed, transformed")
            st.markdown("- Rewrite passive statements into active, impact-focused ones")
            feedback_given = True
    
    # Below 50% - Major improvements needed
    elif score_percentage < 50:
        st.markdown("#### **Major Resume Overhaul Required**")
        
        st.markdown("#### **Immediate Action Items:**")
        st.markdown("**1. Skills Development (High Priority):**")
        missing_required = content_breakdown.get("missing_required", [])
        for skill in missing_required[:5]:  # Top 5 missing skills
            st.markdown(f"   - Learn **{skill}** through online courses or bootcamps")
        st.markdown("   - Dedicate 2-3 months to intensive skill building")
        st.markdown("   - Create a portfolio demonstrating these skills")
        
        st.markdown("**2. Resume Complete Rewrite:**")
        st.markdown("   - Start from scratch with a job-focused approach")
        st.markdown("   - Add a strong professional summary matching the role")
        st.markdown("   - Include 5+ quantified achievements with metrics")
        st.markdown("   - Use industry-standard resume templates")
        st.markdown("   - Have it reviewed by industry professionals")
        
        st.markdown("**3. Experience Building:**")
        st.markdown("   - Consider relevant internships or entry-level positions")
        st.markdown("   - Volunteer for projects using required technologies")
        st.markdown("   - Build 2-3 substantial projects showcasing key skills")
        st.markdown("   - Network with professionals in your target field")
        
        feedback_given = True
    
    # 80%+ range - Excellent score
    elif score_percentage >= 80:
        st.markdown("#### **Excellent Work!**")
        st.markdown("Your resume shows strong alignment with the job requirements. Consider minor keyword optimizations for even better ATS compatibility.")
        feedback_given = True
    
    # Additional recommendations based on specific breakdown elements
    if not feedback_given:
        st.markdown("#### **Good Work!**")
        st.markdown("Your resume shows alignment with the job requirements. Consider minor optimizations for better results.")
    
    # Quick Summary
    st.markdown("---")
    st.markdown("#### 📋 **Quick Summary:**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"- **Required Skills Matched:** {len(content_breakdown.get('required_matched', []))}")
        st.markdown(f"- **Missing Required Skills:** {len(content_breakdown.get('missing_required', []))}")
        st.markdown(f"- **Preferred Skills Matched:** {len(content_breakdown.get('preferred_matched', []))}")
    with col2:
        st.markdown(f"- **Quantifiable Achievements:** {'✅' if content_breakdown.get('qualifications_found') else '❌'}")
        st.markdown(f"- **Action-Oriented Content:** {len(content_breakdown.get('action_verb_lines', []))} lines")
        st.markdown(f"- **Keyword Matches:** {len(content_breakdown.get('keywords_matches', []))}")


def provide_formatting_recommendations(formatting_score, formatting_breakdown, max_possible_score=20):
    """
    Provides detailed formatting recommendations based on scoring breakdown
    """
    score_percentage = (formatting_score / max_possible_score) * 100
    feedback_given = False
    
    st.markdown(f"**Formatting Score: {formatting_score}/{max_possible_score} ({score_percentage:.1f}%)**")
    
    # 80%+ range - Excellent formatting
    if score_percentage >= 80:
        st.markdown("#### **Excellent Formatting!**")
        st.markdown("Your resume has professional formatting that's ATS-friendly and visually appealing.")
        
        # Minor suggestions for perfection
        if not formatting_breakdown.get("file_foramt_check"):
            st.markdown("**Minor Enhancement:**")
            st.markdown("- Save as PDF format for better compatibility across systems")
        feedback_given = True
    
    # 60-80% range - Good formatting with room for improvement
    elif 60 <= score_percentage < 80:
        st.markdown("#### **Good Formatting Foundation!**")
        st.markdown("Your resume has solid structure. Let's polish a few areas for maximum impact.")
        
        # Section presence
        if not formatting_breakdown.get("section_presence"):
            st.markdown("#### **Section Organization:**")
            st.markdown("- Add clear sections: Education, Experience, Skills, Projects")
            st.markdown("- Use consistent heading styles (bold, larger font, or underlining)")
            st.markdown("- Ensure each section is easily identifiable")
            feedback_given = True
        
        # Contact information
        if not formatting_breakdown.get("contact_info_present"):
            st.markdown("#### **Contact Information:**")
            st.markdown("- **Critical:** Include both email and phone number in header")
            st.markdown("- Add LinkedIn profile and portfolio links if relevant")
            st.markdown("- Ensure contact info is prominently placed at the top")
            feedback_given = True
        
        # Bullet points
        if not formatting_breakdown.get("bullet_point_usage"):
            st.markdown("#### **Content Structure:**")
            st.markdown("- Use bullet points (•, -, or *) for listing achievements")
            st.markdown("- Avoid long paragraphs - break into scannable bullet points")
            st.markdown("- Maintain consistent bullet point style throughout")
            feedback_given = True
        
        # Date formatting
        if not formatting_breakdown.get("date_format_consistency"):
            st.markdown("#### **Date Consistency:**")
            st.markdown("- Use consistent date format: 'Jan 2023 - Present' or 'January 2023 - Present'")
            st.markdown("- Align dates consistently (right-aligned is preferred)")
            st.markdown("- Include graduation dates and employment periods")
            feedback_given = True
        
        # File format
        if not formatting_breakdown.get("file_foramt_check"):
            st.markdown("#### **File Format:**")
            st.markdown("- **Important:** Save and submit as PDF format")
            st.markdown("- PDFs maintain formatting across different systems")
            st.markdown("- Avoid Word documents unless specifically requested")
            feedback_given = True
    
    # 40-60% range - Moderate formatting issues
    elif 40 <= score_percentage < 60:
        st.markdown("#### **Formatting Needs Attention**")
        st.markdown("Several formatting improvements are needed for professional presentation.")
        
        # Priority fixes
        st.markdown("#### **Priority Fixes:**")
        
        if not formatting_breakdown.get("contact_info_present"):
            st.markdown("**1. Contact Information (Critical):**")
            st.markdown("   - Add professional email address")
            st.markdown("   - Include phone number with country code if international")
            st.markdown("   - Add LinkedIn profile URL")
        
        if not formatting_breakdown.get("section_presence"):
            st.markdown("**2. Section Structure:**")
            st.markdown("   - Create clear sections with headers")
            st.markdown("   - Use consistent formatting for all section headers")
            st.markdown("   - Organize content logically: Contact → Summary → Experience → Education → Skills")
        
        if not formatting_breakdown.get("bullet_point_usage"):
            st.markdown("**3. Content Organization:**")
            st.markdown("   - Convert paragraph text to bullet points")
            st.markdown("   - Use consistent bullet symbols throughout")
            st.markdown("   - Keep bullet points concise (1-2 lines each)")
        
        if not formatting_breakdown.get("whitespace_and_spacing"):
            st.markdown("**4. Layout & Spacing:**")
            st.markdown("   - Add adequate white space between sections")
            st.markdown("   - Use consistent margins (0.5-1 inch)")
            st.markdown("   - Ensure text doesn't appear cramped")
            st.markdown("   - Break long lines into shorter, readable segments")
        
        if not formatting_breakdown.get("header_clarity"):
            st.markdown("**5. Header Clarity:**")
            st.markdown("   - Make section headers prominent and consistent")
            st.markdown("   - Use bold or larger font for headers")
            st.markdown("   - Ensure headers stand out from body text")
        
        feedback_given = True
    
    # Below 40% - Major formatting overhaul needed
    elif score_percentage < 40:
        st.markdown("#### **Major Formatting Overhaul Required**")
        st.markdown("Your resume needs significant formatting improvements for professional presentation.")
        
        st.markdown("#### **Complete Formatting Checklist:**")
        st.markdown("**Step 1: Basic Structure**")
        st.markdown("   - Use a professional resume template")
        st.markdown("   - Set up clear sections: Header, Summary, Experience, Education, Skills")
        st.markdown("   - Ensure single-page format (unless 10+ years experience)")
        
        st.markdown("**Step 2: Contact Header**")
        st.markdown("   - Full name in larger, bold font")
        st.markdown("   - Professional email address")
        st.markdown("   - Phone number")
        st.markdown("   - LinkedIn and portfolio links")
        st.markdown("   - City, State (no full address needed)")
        
        st.markdown("**Step 3: Content Formatting**")
        st.markdown("   - Use bullet points for all job responsibilities and achievements")
        st.markdown("   - Consistent date format throughout")
        st.markdown("   - Proper alignment and spacing")
        st.markdown("   - Professional font (Arial, Calibri, or Times New Roman)")
        st.markdown("   - 10-12pt font size for body text")
        
        st.markdown("**Step 4: Final Polish**")
        st.markdown("   - Save as PDF format")
        st.markdown("   - Check for consistent margins and spacing")
        st.markdown("   - Ensure ATS-friendly (no images, tables, or complex formatting)")
        st.markdown("   - Proofread for formatting consistency")
        
        feedback_given = True
    
    if not feedback_given:
        st.markdown("#### **Solid Formatting!**")
        st.markdown("Your resume formatting meets professional standards.")
    
    # Quick formatting summary
    st.markdown("---")
    st.markdown("#### 📋 **Formatting Checklist:**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"- **Clear Sections:** {'✅' if formatting_breakdown.get('section_presence') else '❌'}")
        st.markdown(f"- **Contact Info:** {'✅' if formatting_breakdown.get('contact_info_present') else '❌'}")
        st.markdown(f"- **Bullet Points:** {'✅' if formatting_breakdown.get('bullet_point_usage') else '❌'}")
        st.markdown(f"- **Date Consistency:** {'✅' if formatting_breakdown.get('date_format_consistency') else '❌'}")
    with col2:
        st.markdown(f"- **Professional Layout:** {'✅' if formatting_breakdown.get('whitespace_and_spacing') else '❌'}")
        st.markdown(f"- **Clear Headers:** {'✅' if formatting_breakdown.get('header_clarity') else '❌'}")
        st.markdown(f"- **PDF Format:** {'✅' if formatting_breakdown.get('file_foramt_check') else '❌'}")
        st.markdown(f"- **ATS Friendly:** {'✅' if formatting_breakdown.get('ats_friendly', True) else '❌'}")


def provide_optimization_recommendations(optimization_score, optimization_breakdown, max_possible_score=18):
    """
    Provides detailed optimization recommendations based on scoring breakdown
    """
    score_percentage = (optimization_score / max_possible_score) * 100
    feedback_given = False
    
    st.markdown(f"**Optimization Score: {optimization_score}/{max_possible_score} ({score_percentage:.1f}%)**")
    
    # 80%+ range - Excellent optimization
    if score_percentage >= 80:
        st.markdown("#### **Excellently Optimized Resume!**")
        st.markdown("Your resume is well-optimized for ATS systems and hiring managers.")
        
        if optimization_breakdown.get("spelling_grammar_issues", 0) > 0:
            st.markdown("**Minor Polish:**")
            st.markdown(f"- Fix {optimization_breakdown['spelling_grammar_issues']} minor grammar/spelling issues")
        feedback_given = True
    
    # 60-80% range - Good optimization with improvements
    elif 60 <= score_percentage < 80:
        st.markdown("#### **Good Optimization - Room for Enhancement**")
        
        # Tailoring improvements
        if len(optimization_breakdown.get("tailoring", [])) < 3:
            st.markdown("#### **Job-Specific Tailoring:**")
            st.markdown("- Incorporate more job-specific keywords from the posting")
            st.markdown("- Use exact terminology from the job description")
            st.markdown("- Rephrase existing experience using job-relevant language")
            st.markdown("- Research industry-specific terms and include them naturally")
            feedback_given = True
        
        # Grammar and spelling
        issues = optimization_breakdown.get("spelling_grammar_issues", 0)
        if issues > 2:
            st.markdown("#### **Proofreading Required:**")
            st.markdown(f"- Fix **{issues} grammar/spelling issues** detected")
            st.markdown("- Use tools like Grammarly or LanguageTool for thorough checking")
            st.markdown("- Have a friend or colleague review for errors")
            st.markdown("- Read aloud to catch awkward phrasing")
            feedback_given = True
        
        # Conciseness
        if not optimization_breakdown.get("concise"):
            st.markdown("#### **Content Conciseness:**")
            st.markdown("- **Reduce word count** - aim for 400-800 words total")
            st.markdown("- Remove redundant phrases and filler words")
            st.markdown("- Combine similar bullet points")
            st.markdown("- Focus on most impactful achievements only")
            st.markdown("- Use strong action verbs to convey more with fewer words")
            feedback_given = True
        
        # ATS compatibility
        if not optimization_breakdown.get("ats_friendly"):
            st.markdown("#### **ATS Compatibility:**")
            st.markdown("- **Remove tables, text boxes, and complex formatting**")
            st.markdown("- Use standard fonts (Arial, Calibri, Times New Roman)")
            st.markdown("- Avoid images, graphics, or special characters")
            st.markdown("- Use standard section headers (Experience, Education, Skills)")
            st.markdown("- Save as PDF with selectable text")
            feedback_given = True
    
    # 40-60% range - Moderate optimization needed
    elif 40 <= score_percentage < 60:
        st.markdown("#### **Optimization Improvements Needed**")
        
        st.markdown("#### **Priority Optimizations:**")
        
        # Tailoring (highest priority)
        st.markdown("**1. Job Tailoring (Critical):**")
        matched_keywords = len(optimization_breakdown.get("tailoring", []))
        st.markdown(f"   - Currently matching {matched_keywords} job-specific keywords")
        st.markdown("   - **Action:** Study the job posting and incorporate 5-10 specific terms")
        st.markdown("   - Mirror the language used in the job description")
        st.markdown("   - Research company terminology and industry buzzwords")
        
        # Content length optimization
        if not optimization_breakdown.get("concise"):
            st.markdown("**2. Content Optimization:**")
            st.markdown("   - **Significantly reduce content length**")
            st.markdown("   - Target 1-2 pages maximum")
            st.markdown("   - Remove outdated or irrelevant experience")
            st.markdown("   - Focus on last 10-15 years of experience")
            st.markdown("   - Prioritize achievements over job descriptions")
        
        # Grammar/spelling fixes
        issues = optimization_breakdown.get("spelling_grammar_issues", 0)
        if issues > 5:
            st.markdown("**3. Professional Proofreading:**")
            st.markdown(f"   - **{issues} errors detected** - needs thorough review")
            st.markdown("   - Use professional proofreading tools")
            st.markdown("   - Consider hiring a professional resume reviewer")
            st.markdown("   - Multiple rounds of editing required")
        
        # ATS optimization
        if not optimization_breakdown.get("ats_friendly"):
            st.markdown("**4. ATS System Compatibility:**")
            st.markdown("   - **Critical:** Remove all tables and complex formatting")
            st.markdown("   - Use simple, clean layout")
            st.markdown("   - Stick to standard resume sections")
            st.markdown("   - Test resume parsing with online ATS checkers")
        
        feedback_given = True
    
    # Below 40% - Major optimization overhaul
    elif score_percentage < 40:
        st.markdown("#### **Complete Resume Optimization Required**")
        
        st.markdown("#### **Comprehensive Optimization Plan:**")
        st.markdown("**Phase 1: Content Overhaul (Week 1-2)**")
        st.markdown("   - Research target company and role extensively")
        st.markdown("   - Rewrite resume from scratch with job-specific focus")
        st.markdown("   - Incorporate 10-15 relevant keywords naturally")
        st.markdown("   - Cut content to 400-800 words maximum")
        
        st.markdown("**Phase 2: Technical Optimization (Week 2)**")
        st.markdown("   - Remove all formatting that's not ATS-compatible")
        st.markdown("   - Use simple, clean template")
        st.markdown("   - Ensure all text is selectable in PDF format")
        st.markdown("   - Test with multiple ATS parsing tools")
        
        st.markdown("**Phase 3: Quality Assurance (Week 3)**")
        issues = optimization_breakdown.get("spelling_grammar_issues", 0)
        if issues > 10:
            st.markdown(f"   - **{issues} errors need fixing** - professional editing required")
        st.markdown("   - Multiple proofreading rounds")
        st.markdown("   - Industry professional review")
        st.markdown("   - A/B testing with different versions")
        
        st.markdown("**Phase 4: Validation (Week 4)**")
        st.markdown("   - Test resume with ATS systems")
        st.markdown("   - Get feedback from industry professionals")
        st.markdown("   - Compare against successful resumes in your field")
        st.markdown("   - Measure improvement with resume scoring tools")
        
        feedback_given = True
    
    if not feedback_given:
        st.markdown("#### **Well Optimized!**")
        st.markdown("Your resume optimization is on track.")
    
    # Optimization summary
    st.markdown("---")
    st.markdown("#### **Optimization Summary:**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"- **Job Keywords:** {len(optimization_breakdown.get('tailoring', []))} matched")
        st.markdown(f"- **Grammar Issues:** {optimization_breakdown.get('spelling_grammar_issues', 0)}")
    with col2:
        st.markdown(f"- **Concise Length:** {'✅' if optimization_breakdown.get('concise') else '❌'}")
        st.markdown(f"- **ATS Compatible:** {'✅' if optimization_breakdown.get('ats_friendly') else '❌'}")


def provide_alignment_recommendations(alignment_score, alignment_breakdown, max_possible_score=22):
    """
    Provides detailed alignment recommendations based on scoring breakdown
    """
    score_percentage = (alignment_score / max_possible_score) * 100
    feedback_given = False
    
    st.markdown(f"**Alignment Score: {alignment_score}/{max_possible_score} ({score_percentage:.1f}%)**")
    
    # 80%+ range - Excellent alignment
    if score_percentage >= 80:
        st.markdown("#### **Excellent Job Alignment!**")
        st.markdown("Your experience and qualifications strongly align with the target role.")
        
        # Minor enhancements for perfection
        if not alignment_breakdown.get("certifications"):
            st.markdown("**Enhancement Opportunity:**")
            st.markdown("- Consider adding relevant certifications to strengthen your profile")
        
        if not alignment_breakdown.get("online_presence"):
            st.markdown("**Professional Presence:**")
            st.markdown("- Add LinkedIn profile or professional portfolio links")
        
        feedback_given = True
    
    # 60-80% range - Good alignment with room for improvement
    elif 60 <= score_percentage < 80:
        st.markdown("#### **Strong Foundation - Let's Perfect the Alignment**")
        
        # Experience alignment
        if not alignment_breakdown.get("meets_min_experience"):
            st.markdown("#### **Experience Gap Strategy:**")
            st.markdown("- **Focus:** Highlight transferable skills from other experiences")
            st.markdown("- Emphasize relevant projects, internships, or volunteer work")
            st.markdown("- Quantify achievements to demonstrate impact despite shorter tenure")
            st.markdown("- Consider contract or freelance work to build experience")
            feedback_given = True
        
        # Relevant roles enhancement
        if len(alignment_breakdown.get("relevant_roles", [])) < 2:
            st.markdown("#### **Role Relevance:**")
            st.markdown("- Reframe job titles and descriptions to match target role language")
            st.markdown("- Highlight aspects of previous roles that align with target position")
            st.markdown("- Use industry-standard job titles when possible")
            st.markdown("- Create a functional resume format if changing industries")
            feedback_given = True
        
        # Project impact enhancement
        if len(alignment_breakdown.get("project_impact", [])) < 2:
            st.markdown("#### **Impact & Achievements:**")
            st.markdown("- **Add 3-5 quantified project outcomes** with specific metrics")
            st.markdown("- Include projects that demonstrate skills needed for target role")
            st.markdown("- Highlight leadership or initiative-taking examples")
            st.markdown("- Show progression and increasing responsibility")
            feedback_given = True
        
        # Side projects
        if not alignment_breakdown.get("side_projects"):
            st.markdown("#### **Professional Development:**")
            st.markdown("- Add GitHub profile with relevant projects")
            st.markdown("- Include open-source contributions or personal projects")
            st.markdown("- Mention relevant side projects that demonstrate passion")
            st.markdown("- Show continuous learning through personal initiatives")
            feedback_given = True
        
        # Online presence
        if not alignment_breakdown.get("online_presence"):
            st.markdown("#### **Professional Visibility:**")
            st.markdown("- **Add LinkedIn profile URL** to resume header")
            st.markdown("- Include portfolio website or GitHub profile")
            st.markdown("- Ensure online profiles match resume information")
            st.markdown("- Consider creating a professional website")
            feedback_given = True
        
        # Certifications
        if not alignment_breakdown.get("certifications"):
            st.markdown("#### **Skill Validation:**")
            st.markdown("- Pursue relevant industry certifications")
            st.markdown("- Add completed online courses from recognized platforms")
            st.markdown("- Include professional development workshops")
            st.markdown("- Highlight any in-progress certification efforts")
            feedback_given = True
    
    # 40-60% range - Moderate alignment issues
    elif 40 <= score_percentage < 60:
        st.markdown("#### **Alignment Improvements Needed**")
        
        st.markdown("#### **Strategic Alignment Plan:**")
        
        # Experience building (top priority)
        if not alignment_breakdown.get("meets_min_experience"):
            st.markdown("**1. Experience Development (Priority):**")
            st.markdown("   - **Immediate:** Look for contract/freelance opportunities")
            st.markdown("   - Volunteer for relevant projects in current role")
            st.markdown("   - Consider internships or entry-level positions")
            st.markdown("   - Highlight ALL relevant experience, including non-traditional roles")
            st.markdown("   - Reframe existing experience using target role terminology")
        
        # Role positioning
        if len(alignment_breakdown.get("relevant_roles", [])) < 1:
            st.markdown("**2. Role Positioning:**")
            st.markdown("   - Research job titles in target industry")
            st.markdown("   - Rewrite job descriptions to emphasize relevant skills")
            st.markdown("   - Use functional resume format to highlight skills over chronology")
            st.markdown("   - Focus on transferable skills and achievements")
        
        # Skill demonstration through projects
        if len(alignment_breakdown.get("project_impact", [])) < 1:
            st.markdown("**3. Project Portfolio Development:**")
            st.markdown("   - **Create 2-3 projects specifically relevant to target role**")
            st.markdown("   - Document and quantify project outcomes")
            st.markdown("   - Include both professional and personal projects")
            st.markdown("   - Show problem-solving and technical skills")
        
        # Professional development
        st.markdown("**4. Skill Gap Closure:**")
        if not alignment_breakdown.get("certifications"):
            st.markdown("   - **Urgent:** Start relevant certification programs")
            st.markdown("   - Complete online courses in key skill areas")
            st.markdown("   - Join professional associations")
        
        if not alignment_breakdown.get("online_presence"):
            st.markdown("   - Build professional LinkedIn profile")
            st.markdown("   - Create portfolio showcasing relevant work")
            st.markdown("   - Establish thought leadership through content")
        
        feedback_given = True
    
    # Below 40% - Major alignment overhaul needed
    elif score_percentage < 40:
        st.markdown("#### **Major Career Realignment Required** 🚨")
        
        st.markdown("#### **Comprehensive Career Transition Plan:**")
        
        st.markdown("**Phase 1: Gap Analysis & Planning (Month 1)**")
        st.markdown("   - Complete skills assessment vs. target role requirements")
        st.markdown("   - Identify top 5 skill gaps to address")
        st.markdown("   - Create 6-month professional development plan")
        st.markdown("   - Network with professionals in target field")
        
        st.markdown("**Phase 2: Skill Building (Months 2-4)**")
        if not alignment_breakdown.get("meets_min_experience"):
            st.markdown("   - **Critical:** Gain experience through:")
            st.markdown("     • Volunteer work in target field")
            st.markdown("     • Freelance projects")
            st.markdown("     • Industry internships or apprenticeships")
            st.markdown("     • Career transition programs")
        
        if not alignment_breakdown.get("certifications"):
            st.markdown("   - **Essential:** Complete relevant certifications")
            st.markdown("     • Industry-standard certifications")
            st.markdown("     • Online courses from recognized platforms")
            st.markdown("     • Professional development workshops")
        
        st.markdown("**Phase 3: Portfolio Development (Months 3-5)**")
        st.markdown("   - Build 3-5 substantial projects demonstrating target skills")
        st.markdown("   - Create professional portfolio website")
        st.markdown("   - Document all learning and project outcomes")
        st.markdown("   - Establish strong online professional presence")
        
        st.markdown("**Phase 4: Resume Reconstruction (Month 6)**")
        st.markdown("   - Complete resume rewrite focusing on new skills and experience")
        st.markdown("   - Use functional or combination resume format")
        st.markdown("   - Emphasize transferable skills and recent learning")
        st.markdown("   - Get professional review from industry experts")
        
        st.markdown("**Alternative Consideration:**")
        st.markdown("   - Consider targeting more entry-level positions in desired field")
        st.markdown("   - Look for bridge roles that combine current and target skills")
        st.markdown("   - Explore career transition programs or bootcamps")
        
        feedback_given = True
    
    if not feedback_given:
        st.markdown("#### **Good Alignment!**")
        st.markdown("Your qualifications align well with the target role.")
    
    # Alignment summary
    st.markdown("---")
    st.markdown("#### 📋 **Alignment Summary:**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"- **Experience Requirement:** {'✅' if alignment_breakdown.get('meets_min_experience') else '❌'}")
        st.markdown(f"- **Relevant Roles:** {len(alignment_breakdown.get('relevant_roles', []))}")
        st.markdown(f"- **Project Impact:** {len(alignment_breakdown.get('project_impact', []))} examples")
    with col2:
        st.markdown(f"- **Side Projects:** {'✅' if alignment_breakdown.get('side_projects') else '❌'}")
        st.markdown(f"- **Online Presence:** {'✅' if alignment_breakdown.get('online_presence') else '❌'}")
        st.markdown(f"- **Certifications:** {'✅' if alignment_breakdown.get('certifications') else '❌'}")


def provide_comprehensive_feedback(score_data):
    """
    Master function to provide all feedback categories
    """
    st.markdown("# **Comprehensive Resume Analysis & Recommendations**")
    
    # Overall score display
    total_score = score_data["total_score"]
    max_total = 100  # 40 + 20 + 18 + 22
    overall_percentage = (total_score / max_total) * 100
    
    st.markdown(f"## **Overall Resume Score: {total_score}/{max_total} ({overall_percentage:.1f}%)**")
    
    # Score interpretation
    if overall_percentage >= 80:
        st.markdown("### **Excellent Resume!** Your resume is highly competitive and ready for applications.")
    elif overall_percentage >= 65:
        st.markdown("### **Strong Resume!** With minor improvements, your resume will be highly competitive.")
    elif overall_percentage >= 50:
        st.markdown("### **Good Foundation!** Your resume needs moderate improvements to be competitive.")
    elif overall_percentage >= 35:
        st.markdown("### **Needs Improvement!** Significant enhancements required for competitive applications.")
    else:
        st.markdown("### **Major Overhaul Required!** Your resume needs substantial improvements.")
    
    # Progress bar
    st.progress(overall_percentage / 100)
    
    # Individual category feedback
    st.markdown("---")
    
    # Content Recommendations
    st.markdown("## **Content Analysis**")
    provide_content_recommendations(
        score_data["content_score"], 
        score_data["breakdown"]["content"]
    )
    
    st.markdown("---")
    
    # Formatting Recommendations
    st.markdown("## **Formatting Analysis**")
    provide_formatting_recommendations(
        score_data["formatting_score"], 
        score_data["breakdown"]["formatting"]
    )
    
    st.markdown("---")
    
    # Optimization Recommendations
    st.markdown("## **Optimization Analysis**")
    provide_optimization_recommendations(
        score_data["optimization_score"], 
        score_data["breakdown"]["optimization"]
    )
    
    st.markdown("---")
    
    # Alignment Recommendations
    st.markdown("## **Job Alignment Analysis**")
    provide_alignment_recommendations(
        score_data["alignment_score"], 
        score_data["breakdown"]["alignment"]
    )
    
    # Final action plan
    st.markdown("---")
    st.markdown("## **Your Action Plan**")
    
    if overall_percentage >= 80:
        st.markdown("**Immediate Actions:**")
        st.markdown("- Apply to target positions with confidence")
        st.markdown("- Continue minor optimizations based on specific job postings")
        st.markdown("- Keep resume updated with latest achievements")
    
    elif overall_percentage >= 65:
        st.markdown("**Next 1-2 Weeks:**")
        st.markdown("- Address the highest-impact recommendations above")
        st.markdown("- Focus on content and alignment improvements")
        st.markdown("- Have a colleague review your updated resume")
    
    elif overall_percentage >= 50:
        st.markdown("**Next 2-4 Weeks:**")
        st.markdown("- Prioritize content and optimization improvements")
        st.markdown("- Spend time on keyword research and tailoring")
        st.markdown("- Consider professional resume review services")
    
    else:
        st.markdown("**Next 1-3 Months:**")
        st.markdown("- Follow the comprehensive improvement plans above")
        st.markdown("- Consider significant skill development or career counseling")
        st.markdown("- Build experience through projects, volunteering, or additional training")
    
    st.markdown("---")
    st.markdown("*Remember: Tailor your resume for each specific job application for best results!*")
