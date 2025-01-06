from docx2python import docx2python
from openai import OpenAI
client = OpenAI(api_key="")

# def read_docxfile(file_path):
#     content = ""
#     with docx2python(file_path) as docx_content:
#         content += docx_content.text
#     docx_content.close()
#     return content
# file_contents = read_docxfile("Resumes\Saptarshi_Das_Resume.docx")
# print("****************************************************")
# print(file_contents)
# print("****************************************************\n\n\n")
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful AI assistant"},
#     {"role": "user", "content": f'''Analyse the given resume {file_contents} , extract the following information:
#    Give the exact information mentioned in the resume, don't provide the predicted or hallucinated response, if you could not find just respond don't know
#         Output format:
#         example:
#         {{
#             "Name": "Likitha",
#             "DOB": "14-07-2001",
#             "Address": "ABC, Tirupathi",
#             "Total_Experience": "2",
#             "Mobile_Number": "1234567890",
#             "Email": "122liki@gmail.com",
#             "Skills": ["SAP", "Java", "Python"],
#             "Certifications": ["AZ-900", "AZ-104"],
#             "Education":[{{
#                 "Degree": "Bachelor of Technology",
#                 "College_Name": "Siddartha Institute of Science and Technology",
#                 "Graduation_Year": "2022",
#                 "Percentage": "91"
#             }}],
#             "Objective": "Having 5 years 2 months of work experience as a Business Analyst, my primary objective is to gather the requirements of the clients and stakeholders, analyze their day-to-day issues, and provide constant assistance until the closure. I aim to utilize my strong prioritization skills and analytical abilities to achieve the desired goals of the company. I am an enthusiastic team player and have been successful in completing my objectives and making the most of the available resources. I am looking forward to working with data science, having good statistical knowledge, and applying machine learning techniques that I have learned in the last 1 year.",
#             "Employers": [{{
#                 "Employer_Name": "Wipro",
#                 "Role": "Data Analyst",
#                 "Worked_From": "30-05-2022",
#                 "Worked_To": "15-10-2023",
#                 "Projects": [{{
#                     "Project_Name": "ABC",
#                     "Brief_Description": "In CGI, I have worked in the EAS (Engagement Assessment Services) team as a System Administrator. EAS is a corporate team, and I have played a vital role in managing the different applications used by the Business Partners and PM/SDMs. I was also the EAS Shared Service Coordinator managing a team to plan, execute, and deliver reports to the management as and when required."
#                 }}]
#             }}]
#         }}
        
#         Respond only in the following JSON format:
#         {{
#             "Name": "Name of the employee",
#             "DOB": "Employee Date of Birth",
#             "Address": "Address of the employee",
#             "Total_Experience": "Employee total work experience",
#             "Mobile_Number": "Employee mobile number",
#             "Email": "Email of the employee",
#             "Skills": ["Skill1", "Skill2", ...],
#             "Certifications": ["Certification1", "Certification2", ...],
#             "Education": [{{
#                 "Degree": "Name of the course",
#                 "College_Name": "Name of the college or Institution",
#                 "Graduation_Year": "Passed out year",
#                 "Percentage": "Percentage of marks obtained"
#             }}, ...],
#             "Objective": "About me or objective or professional summary of the employee",
#             "Employers": [{{
#                 "Employer_Name": "Company Name",
#                 "Role": "Role of the employee",
#                 "Worked_From": "Date of joining",
#                 "Worked_To": "Date of exit",
#                 "Projects": [{{
#                     "Project_Name": "Project Name",
#                     "Brief_Description": "Analyse the entire project description and give it in a brief way"
#                 }}, ...]
#             }}, ...]
#         }}
# '''}
# ]
# )

# print(completion.choices[0].message)

def ask_openai(file_contents):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant"},
            {"role": "user", "content": f'''Analyse the given resume {file_contents} , extract the following information:
            Give the exact information mentioned in the resume, don't provide the predicted or hallucinated response, if you could not find just respond don't know
                Output format:
                example:
                {{
                    "Name": "Likitha",
                    "DOB": "14-07-2001",
                    "Address": "ABC, Tirupathi",
                    "Total_Experience": "2",
                    "Mobile_Number": "1234567890",
                    "Email": "122liki@gmail.com",
                    "Skills": ["SAP", "Java", "Python"],
                    "Certifications": ["AZ-900", "AZ-104"],
                    "Education":[{{
                        "Degree": "Bachelor of Technology",
                        "College_Name": "Siddartha Institute of Science and Technology",
                        "Graduation_Year": "2022",
                        "Percentage": "91"
                    }}],
                    "Objective": "Having 5 years 2 months of work experience as a Business Analyst, my primary objective is to gather the requirements of the clients and stakeholders, analyze their day-to-day issues, and provide constant assistance until the closure. I aim to utilize my strong prioritization skills and analytical abilities to achieve the desired goals of the company. I am an enthusiastic team player and have been successful in completing my objectives and making the most of the available resources. I am looking forward to working with data science, having good statistical knowledge, and applying machine learning techniques that I have learned in the last 1 year.",
                    "Employers": [{{
                        "Employer_Name": "Wipro",
                        "Role": "Data Analyst",
                        "Worked_From": "30-05-2022",
                        "Worked_To": "15-10-2023",
                        "Projects": [{{
                            "Project_Name": "ABC",
                            "Brief_Description": "In CGI, I have worked in the EAS (Engagement Assessment Services) team as a System Administrator. EAS is a corporate team, and I have played a vital role in managing the different applications used by the Business Partners and PM/SDMs. I was also the EAS Shared Service Coordinator managing a team to plan, execute, and deliver reports to the management as and when required."
                        }}]
                    }}]
                }}
                
                Respond only in the following JSON format:
                {{
                    "Name": "Name of the employee",
                    "DOB": "Employee Date of Birth",
                    "Address": "Address of the employee",
                    "Total_Experience": "Employee total work experience",
                    "Mobile_Number": "Employee mobile number",
                    "Email": "Email of the employee",
                    "Skills": ["Skill1", "Skill2", ...],
                    "Certifications": ["Certification1", "Certification2", ...],
                    "Education": [{{
                        "Degree": "Name of the course",
                        "College_Name": "Name of the college or Institution",
                        "Graduation_Year": "Passed out year",
                        "Percentage": "Percentage of marks obtained"
                    }}, ...],
                    "Objective": "About me or objective or professional summary of the employee",
                    "Employers": [{{
                        "Employer_Name": "Company Name",
                        "Role": "Role of the employee",
                        "Worked_From": "Date of joining",
                        "Worked_To": "Date of exit",
                        "Projects": [{{
                            "Project_Name": "Project Name",
                            "Brief_Description": "Analyse the entire project description and give it in a brief way"
                        }}, ...]
                    }}, ...]
                }}
            '''}
        ]
    )
    return completion.choices[0].message
