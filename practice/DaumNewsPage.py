#Page를 돌면서 News 목록의 제목과 본문을 수집

import requests
from bs4 import BeautifulSoup

i=0
for page_num in range(1, 3):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(page_num)

    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')

    url_list = doc.select('ul.list_news2 a.link_txt')

    for href in url_list:
        # 기사 1건의 제목과 본문을 수집하는 코드
        new_url = href['href']

        result = requests.get(new_url)
        doc = BeautifulSoup(result.text, 'html.parser')
        title = doc.select('h3.tit_view')[0].get_text()
        contents = doc.select('section p')
        contents.pop(-1)
        content = ''
        for info in contents:
            content += info.get_text()

        i += 1 #News Count
        print('■■ NEWS -> {}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(i))
        print("#URL: {}".format(new_url))
        print('#TITLE: {}'.format(title))
        print('#CONTENT: {}'.format(content))

