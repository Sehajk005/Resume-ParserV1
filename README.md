# Resume-ParserV1

Resume-ParserV1 is a comprehensive, open-source application designed to revolutionize the recruitment and job-seeking process through advanced resume parsing and intelligent scoring capabilities. The application serves two distinct user groups: **recruiters** looking to efficiently screen and rank large volumes of resumes for mass hiring, and **job seekers** seeking detailed feedback to improve their resumes. Leveraging natural language processing (NLP) and intelligent scoring algorithms, Resume-ParserV1 extracts structured data from PDF and DOCX files while providing actionable insights and performance metrics.

## Key Features

### For Recruiters: Mass Recruitment & Resume Screening
- **Batch Resume Upload:** Process multiple resumes simultaneously for efficient mass recruitment campaigns.
- **Intelligent Ranking System:** Automatically scores and ranks candidates based on job requirements and resume quality.
- **Top Candidate Filtering:** Quickly identify and shortlist the best candidates from large applicant pools.
- **Structured Data Extraction:** Automatically extracts contact details, education, work experience, skills, and qualifications.
- **Comparative Analysis:** Side-by-side comparison of candidate profiles to make informed hiring decisions.

### For Job Seekers: Resume Analysis & Improvement
- **Resume Scoring:** Receive an overall score reflecting resume quality, completeness, and ATS-readiness.
- **Detailed Feedback Report:** Get comprehensive insights into resume strengths and weaknesses.
- **Section-by-Section Breakdown:** Analyze individual sections (contact info, summary, experience, education, skills) with specific recommendations.
- **Improvement Suggestions:** Receive actionable advice on areas needing enhancement, including:
  - Missing critical information
  - Formatting issues
  - Keyword optimization
  - Content quality and relevance
  - ATS compatibility concerns
- **Strengths Highlighting:** Identify what's working well in your resume to maintain those elements.

### General Features
- **Multi-format Support:** Handles PDF and DOCX resume files seamlessly.
- **Advanced NLP Processing:** Utilizes state-of-the-art NLP models for accurate information extraction.
- **User-friendly Interface:** Built with Streamlit for an intuitive, interactive web experience—no programming required.
- **Real-time Processing:** Instant feedback and results upon resume upload.
- **Modular Codebase:** Well-structured Python modules for easy maintenance and extensibility.

## Technology Stack

- **Python 3.8+**
- **Streamlit:** Web application framework for interactive UI
- **spaCy:** Natural language processing for entity extraction and text analysis
- **pdfplumber:** PDF parsing and text extraction
- **python-docx:** DOCX file parsing
- **language-tool-python:** Grammar and language quality checking
- **Additional Libraries:** pandas, re (regex), numpy, and more (see requirements.txt)

## Directory Structure

```text
Resume-ParserV1/
│
├── app.py                # Main Streamlit app script with dual-mode UI
├── requirements.txt      # List of required Python libraries
├── README.md             # Project documentation (this file)
├── utils.py              # Helper functions for parsing (if available)
├── parser.py             # Core resume parsing logic
├── scorer.py             # Resume scoring and feedback generation
├── sample_resumes/       # Example or test resumes
└── [other scripts]       # Additional helper or config files
```

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sehajk005/Resume-ParserV1.git
cd Resume-ParserV1
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Required NLP Models

Download the necessary spaCy language model:

```bash
python -m spacy download en_core_web_sm
```

## Usage Instructions

### Start the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### For Recruiters: Mass Resume Screening

1. Select **"Recruiter Mode"** from the main interface.
2. Upload multiple resume files (PDF or DOCX format) using the batch uploader.
3. The system will automatically:
   - Parse all resumes and extract key information
   - Score and rank candidates based on predefined criteria
   - Display a ranked list of top candidates
4. Review the top candidates with detailed profile information.
5. Export shortlisted candidates for further evaluation.

### For Job Seekers: Resume Analysis

1. Select **"Job Seeker Mode"** from the main interface.
2. Upload your resume file (PDF or DOCX format).
3. Receive instant feedback including:
   - **Overall Resume Score:** Numerical rating (e.g., 75/100)
   - **Strengths:** Areas where your resume excels
   - **Areas for Improvement:** Specific sections needing enhancement
   - **Detailed Breakdown:** Section-by-section analysis covering:
     - Contact Information completeness
     - Professional Summary effectiveness
     - Work Experience relevance and detail
     - Education credentials
     - Skills presentation and keyword optimization
     - Formatting and ATS compatibility
4. Download a detailed feedback report for reference.
5. Make recommended improvements and re-upload to track progress.

## Project Structure and Main Modules

- **app.py:** Main entrypoint featuring dual-mode interface (Recruiter/Job Seeker). Handles navigation, file uploads, and result display.
- **parser.py (or parse_resume function):** Core parsing logic that extracts structured information from resume text using NLP techniques.
- **scorer.py (or score_resume function):** Implements scoring algorithms and generates detailed feedback reports with strengths and improvement areas.
- **utils.py:** Helper functions for text processing, file handling, and data formatting.
- **requirements.txt:** Complete list of Python dependencies required to run the application.

## Scoring Methodology

The resume scoring system evaluates multiple dimensions:

- **Completeness:** Presence of essential sections (contact, experience, education, skills)
- **Content Quality:** Relevance, detail level, and impact of information presented
- **Keyword Optimization:** Alignment with industry-standard terms and ATS requirements
- **Formatting:** Professional appearance, consistency, and readability
- **Grammar & Language:** Writing quality and error-free content

## Example Use Cases

### Recruiter Scenario
A tech company receives 500 applications for software engineering positions. Using Resume-ParserV1, the HR team uploads all resumes, and the system ranks candidates based on technical skills, experience level, and education. The recruiter reviews the top 50 candidates, saving hours of manual screening time.

### Job Seeker Scenario
A recent graduate uploads their resume and receives a score of 68/100. The feedback highlights strong education credentials but identifies weak areas: missing quantifiable achievements in the experience section and insufficient technical keywords. After implementing suggestions, their revised resume scores 85/100.

## Contributing

Contributions are welcome! To propose improvements or new features:

1. Fork this repository
2. Create a new branch for your feature or bugfix
3. Commit your changes with clear descriptions
4. Open a pull request with detailed explanation

Please ensure new features include appropriate documentation and, where applicable, tests.

## Future Enhancements

- Integration with job description matching for better candidate-role fit analysis
- Support for additional file formats (TXT, HTML)
- Multi-language resume support
- Machine learning-based scoring refinement
- Integration with ATS platforms
- Resume template generation based on feedback

## License

This project is released under the MIT License (unless otherwise specified in a LICENSE file).

## Acknowledgements

- Inspired by modern recruitment challenges and the need for objective resume evaluation
- Built using open-source tools: Streamlit, spaCy, pdfplumber, python-docx, and language-tool-python
- Designed to help both recruiters and job seekers succeed in the hiring process

---

For questions, feature requests, or bug reports, please open an issue on GitHub or contact the repository maintainer.

**Developed by:** [Sehajk005](https://github.com/Sehajk005)

**Repository:** [Resume-ParserV1](https://github.com/Sehajk005/Resume-ParserV1)
