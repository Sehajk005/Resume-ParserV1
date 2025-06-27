from parser import extract_text, extract_entities

# Test with a sample resume (PDF or DOCX)
file_path = "resume_samples/sample2.pdf" # or sample1.docx
try:
    resume_text = extract_text(file_path)
    entities = extract_entities(resume_text)
    print("Parsed resume text:")
    for key, value in entities.items():
        print(f"{key}: {value}")
except Exception as e:
    print(f"Error: {e}") # Print first 1000 characters to keep output readable
