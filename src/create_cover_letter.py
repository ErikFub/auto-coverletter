"""Creation of cover letter based on a job posting an CV."""
import argparse
import os

from src.cv_parser import get_cv_content
from src.jobpost_parser import get_post_content
from src.llm_chain import chains


def main(job_url: str, cv_file_path: str) -> str:
    job_info_raw = get_post_content(url=job_url)
    job_info = chains.JobPostSerializationChain().run(job_info_raw)

    cv_raw = get_cv_content(file_path=cv_file_path)
    cv = chains.CVSerializationChain().run(cv_raw)

    cover_letter = chains.CoverLetterCreationChain().run(
        cv=cv,
        job_posting=job_info
    )
    return str(cover_letter).strip()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--job_url', required=True, type=str)
    parser.add_argument('--cv_file_path', required=True, type=str)
    parser.add_argument('--openai_api_key', required=True, type=str)
    args = parser.parse_args()
    os.environ["OPENAI_API_KEY"] = args.openai_api_key
    print(main(job_url=args.job_url, cv_file_path=args.cv_file_path))
