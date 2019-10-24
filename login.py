import requests
from bs4 import BeautifulSoup

def fetch_login_url(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    url = soup.select('a')[0]['href']
    requests.get(url)

def fetch_saved_login_url():
    ''' used for debugging '''
    with open('data/login_page.html') as fh:
        fetch_login_url(fh)

def fetch_live_login_url():
    response = requests.get('http://example.com')
    fetch_login_url(response.content)

if __name__ == '__main__':
    fetch_live_login_url()
