*DISCLAIMER: This project is not meant to replace actually writing a cover letter. It is a fun project for me to play around with langchains and test the boundaries of current LLMs. To potential recruiters checking the repository: No, I have not used this tool to create the cover letter for your company - all handcrafted! :)*
# auto-coverletter
A LLM langchain-based tool for automatically creating a cover letter based on a link to a job posting and a PDF file with the CV.

## Getting started
Create a virtual environment
```shell
python3 -m venv .venv
```

Activate venv
```shell
source .venv/bin/activate
```

Install the required packages
```shell
pip install -r requirements.txt
```

## Usage
### Arguments
- `--job_url`: URL of job posting.
- `--cv_file_path`: Path to file that stores CV. Must be a PDF file.
- `--openai_api_key`: Key for OpenAI API.

### Example
*In*
```shell
bash create_cover_letter \
  --job_url="https://www.linkedin.com/jobs/view/3683787213" \
  --cv_file_path="/Users/your_user/path_to_cv/cv.pdf" \
  --openai_api_key="<api_key>"
```
*Out*

> Dear Sir or Madam, 
> 
> I am writing to apply for the position of Data Scientist at SumUp. With a Master's degree in Business Analytics and more than three years of experience in data science, I believe my qualifications make me an ideal candidate for the role.
> 
> During my studies, I have developed expertise in Python, PySpark, pandas, scikit-learn, Tensorflow, SQL, dbt, Docker, AWS, Terraform, and Metabase, all of which are essential for the job. Additionally, I have experience with AWS cloud platform and strong knowledge of feature engineering, model evaluation, and natural language processing techniques. My research assistant role at Nova SBE Data Science Knowledge Center has further enabled me to develop analytical and problem-solving skills.
> 
> I have also worked as a Data Engineer at Lhotse, a Data Science consultant for Accenture, and a Business Analyst intern at Picnic Technologies. Through these experiences, I have gained the ability to collaborate with cross-functional teams across multiple organizations and to translate business requirements into complex AI solutions.
> 
> Given my background and experience, I am confident that I would be a great asset to your team. I am excited about the opportunity to use my skills and experience to help SumUp stay at the forefront of technological advancement in the field of AI.
> 
> Thank you for your time and consideration. 
> 
> Sincerely, 
> Erik Fubel
