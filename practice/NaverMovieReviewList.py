#네이버 영화에서 영화를 선택하고
# => 영화리뷰, 점수, 작성자, 날짜 정보를 수집하는 코드
import pprint

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

review_list = doc.select('div.score_result > ul > li')

for i, one in enumerate(review_list):
    print('####################################')

    #review score 수집
    score = one.select('div.star_score > em')[0].get_text()

    #review 정보 수집

    #관람각 키워드 O=> Len 2 / [관람객, 리뷰정보]
    review = one.select('div.score_reple > p > span')[-1].get_text().strip()

    #if len(review_select) ==2 : #관람객 키워드 0
    #    review = review_select[1].get_text()
    #elif len(review_select)==1: #관람객 키워드 X
    #    review = review_select[0].get_text()

    #j = 0
    #if len(review_select) == 2:
    #    j = 1
    #review = review_select[j].get_text()

    #수집 된 정보 출력
    print("SCORE => {}".format(score))
    print("review => {}".format(review))
