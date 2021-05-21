  
import requests
from bs4 import BeautifulSoup

def parsing_beautifulsoup(url):
    """
    뷰티풀 수프로 파싱하는 함수
    :param url: paring할 URL. 여기선 YES24 Link
    :return: BeautifulSoup soup Object
    """

    data = requests.get(url, verify=False)

    html = data.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_weather(soup):
    """
    BeautifulSoup Object에서 book data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """

    upload_contents = ''
    #print(soup)
    #new_twits = soup.select('p > a')
    new_twits = soup.find_all('div', {"class": "cmp-view-announce"})
    date_ = str(new_twits[0]).split('<span>')[1].split('</span>')[0]

    new_twits = soup.find_all('span', {"class": "depth_1"})
    news_ = str(new_twits[0]).split('>')[1].split('<')[0]

    print(date_)
    print(news_)

    upload_contents = date_ + news_

    return upload_contents

