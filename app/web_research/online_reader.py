import requests
from bs4 import BeautifulSoup


def read_webpage(url: str) -> str:

    headers = {
        "User-Agent": "JarvisFireInspector/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    cleaned_lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n".join(cleaned_lines)