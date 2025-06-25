from llm_explainer_openai import get_resume_feedback

job_desc = """We are seeking a Data Analyst with strong Python skills, experience in data visualization, and knowledge of cloud computing. The ideal candidate will have experience with Docker and CI/CD pipelines, and be able to communicate insights clearly to stakeholders."""

resume = """John Doe is a Data Analyst with over 5 years of experience in data analysis and visualization. He has strong skills in Python and has worked with various data visualization tools. John has experience in cloud computing and has used Docker for containerization. He is also familiar with CI/CD pipelines and has a proven track record of communicating insights effectively to stakeholders.
"""



result = get_resume_feedback(resume_text=resume,
                            score=85,
                            job_description=job_desc)

print("\n\n",result)