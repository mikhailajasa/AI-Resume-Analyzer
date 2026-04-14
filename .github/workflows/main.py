from openai import OpenAI
import os

client = OpenAI(api_key="YOUR_API_KEY")

resume = input("Paste your resume:\n")
job = input("\nPaste job description:\n")

prompt = f"""
Compare this resume to the job description.

Resume:
{resume}

Job Description:
{job}

Give:
1. Match score (0-100%)
2. Missing skills
3. Suggestions to improve
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print("\nAI Feedback:\n")
print(response.choices[0].message.content)