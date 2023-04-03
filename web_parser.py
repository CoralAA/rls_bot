import requests
from bs4 import BeautifulSoup
from io import BytesIO

base = "https://www.radartutorial.eu/19.kartei/"

def get_rls_list():
    rls_links_list = dict()
    html = requests.get(base + 'ka03.ru.html')
    soup = BeautifulSoup(html.text, 'html.parser')
    for div in soup.find_all("div",class_="zeile"):
        for ul in div.find_all("ul"):
            for li in ul.find_all("li"):
                for a in li.find_all("a"):
                    rls_links_list[a.contents[0]] = a['href']
    return rls_links_list

def get_document_by_url(url):
    html = requests.get(base + url)
    soup = BeautifulSoup(html.text, 'html.parser')
    img = get_image(url, soup)
    description = soup.find("section", class_="fliesstext").getText()
    return (img, description)

def get_image(url, soup):
    uri = soup.find("div", class_="pictable_c").img['src']
    page = url.split("/")[0]
    url = base + page + "/" + uri
    return  BytesIO(requests.get(url)._content)

