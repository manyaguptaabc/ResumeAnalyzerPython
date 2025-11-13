import pandas as pd
import re

# Sample resume text
resume_text = """
Manya Gupta
Python Developer with experience in Django, MySQL, Pandas, and Power BI.
Worked on AI Resume Analyzer and SmartGovAid projects.
"""

# Clean text
resume_text = re.sub(r'\s+', ' ', resume_text)

# Define keywords
keywords = ['python', 'django', 'mysql', 'pandas', 'power bi', 'data analysis', 'excel', 'api']

# Match skills
found_skills = [kw for kw in keywords if kw.lower() in resume_text.lower()]

# Create summary table
data = {
    "Candidate Name": ["Manya Gupta"],
    "Skills Found": [', '.join(found_skills)],
    "Resume Length (words)": [len(resume_text.split())]
}

df = pd.DataFrame(data)
print("\nResume Summary:\n", df)
df.to_csv("resume_summary.csv", index=False)
print("\n✅ Summary exported to resume_summary.csv")
