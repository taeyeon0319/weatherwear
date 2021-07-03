from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
def main(request):
    # 지역은 서울로 고정
    city = 'seoul'
    # 구글의 날씨 정보를 가져옴
    html_content = requests.Session().get(f'https://www.google.com/search?q=weather+{city}').text
    # 크롤링
    soup = BeautifulSoup(html_content, 'html.parser')
    result = dict()
    # 화면에 보여주는 데이터 설정
    # 지역
    result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    # 현재 온도 (23도)
    result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    # 현재 시간, 날씨 (맑음, 흐림 ..)
    result['dayhour'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split('\n')
    # test
    print(soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text)
    print(soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text)
    print(soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text)
    print(soup.find("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).text)
    print(soup.find("span", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).text)
    print(soup.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).text)

    

    return render(request, 'mainPage/mainPage.html', {'weather': result}) 