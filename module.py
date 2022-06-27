from bs4 import BeautifulSoup
import requests


def web_crawling(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    return soup