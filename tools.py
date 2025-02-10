from smolagents import tool
import requests
from bs4 import BeautifulSoup

@tool
def fetch_url_content(url: str) -> str:
    """
    Fetches and returns the main textual content from the specified URL.

    Args:
        url: The URL of the webpage to fetch.

    Returns:
        The main textual content of the webpage.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    content = '\n'.join(para.get_text() for para in paragraphs)
    return content

@tool
def format_blog_post(title: str, content: str) -> str:
    """
    Formats the provided content into a blog post structure.

    Args:
        title: The title of the blog post.
        content: The main body of the blog post.

    Returns:
        A formatted blog post as a string.
    """
    blog_post = f"# {title}\n\n{content}"
    return blog_post
