
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309' ,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music = soup.select('#body-content > div.newest-list > div > table > tbody>tr')


num=1
for i in music:
    title_tag = i.select_one('td.info > a.title.ellipsis')
    artist_tag = i.select_one('td.info > a.artist.ellipsis')
    if title_tag is not None:
        print(num, title_tag.text.lstrip() , artist_tag.text)
        num +=1
