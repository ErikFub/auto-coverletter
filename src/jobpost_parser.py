"""Parsing content from job post HTML to python string."""
import requests
from bs4 import BeautifulSoup


def get_post_content(url: str) -> str:
    response = requests.get(url).content
    soup = BeautifulSoup(response, features="html.parser")

    # Remove all script and style elements
    for script in soup(["script", "style"]):
        script.extract()

    # Get text
    text = soup.get_text()

    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())

    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # Drop blank lines
    content = '\n'.join(chunk for chunk in chunks if chunk)

    return content
