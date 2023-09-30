# Topics and links
import requests
import bs4

# Helper functions to scrape paragraphs from wiki pages
def link_to_content(link : str) -> bs4.BeautifulSoup:
    """_summary_

    Args:
        link (str): _description_

    Returns:
        bs4.BeautifulSoup: _description_
    """
    doc = requests.get(link)
    content_soup = bs4.BeautifulSoup(doc.content, 'html5lib')
    return content_soup

def content_to_paragraphs(soup : bs4.BeautifulSoup) -> list[str]:
    paragraph_list = [p.get_text().replace('\n', '') for p in soup.find_all("p") if len(p.get_text()) > 300]
    return paragraph_list