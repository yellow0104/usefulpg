
import requests
from bs4 import BeautifulSoup
def news_search(inp):
    url = f"https://search.naver.com/search.naver?query={inp}&where=news&ie=utf8&sm=nws_hty"
    res = requests.get(url)
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    titles = soup.find_all("a", attrs={"class":"news_tit"})
    for title in titles:
    
        t = title.get_text()
        link = title["href"]
    return t, link