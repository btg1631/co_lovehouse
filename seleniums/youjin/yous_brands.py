# 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException    # Element : 웹요소 찾지 못할 때 / Window : 창이 없거나 찾을 수 없을 때
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By
# - 정보 획득
# from selenium.webdriver.support.ui import Select      # Select : dropdown 메뉴 다루는 클래스
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 몽고db 저장
from pymongo import MongoClient
# mongodb에 접속
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["project_coliving"]
# collection 작업
dabangs = database['yous_brands']
# - 주소 입력
# 셀립 가디
browser.get("https://celib.kr/property/gadi")
# 셀립 여의
browser.get("https://celib.kr/property/yeoui")
# 셀립 은평
browser.get("https://celib.kr/property/eunpyeong")
# 셀립 순라
browser.get("https://celib.kr/property/soonra")
# 업플로 당산
browser.get("https://www.upflo.kr/dangsan")
# 업플로 한남
browser.get("https://www.upflo.kr/hannam")
# 업플로 서초
browser.get("https://www.upflo.kr/seocho")
# 에피소드(X)
browser.get("https://www.epsd.co.kr/")
# 로컬스티치(X)
browser.get("https://localstitch.kr/")
# 콤피(X)
browser.get("http://comfi-stay.com/")
# 홈즈스튜디오
browser.get("https://www.homes-studio.kr/Urbanhouse_")
time.sleep(2)


# 메인 페이지 핸들 생성
main_window_handle = browser.current_window_handle # 초기 창 핸들로 저장
# # 스크래핑 타겟 : 제목(title), 보증금(deposit), 월세가격(rentFee), 1인실 or 그 외(roomType), 옵션(roomOption), 지역(region), 회사(회사가 아니면 일반사업자-brandType),
#                 성별(남,여, 공용-gender), 평수(추후 범주형 변환-py), url, imgUrl
# # 성별 : 없으면 '공용'
# # 방 수 1개면 1인실, 2개면 '그 외'


## 셀립 가디 정보 (roomType, roomOption, gender 정보 X)
celib_rooms_gadi = [
    {
        'title': 'celib',
        'roomName' : 'A type',
        'deposit': 500000,
        'rentFee': '55만원',
        'region': '서울특별시 금천구 가산동',
        'brandType': '셀립',
        'py': '10.97',
        'imgUrl': '#ko_page > section > div.room-type > div > div > div.room.room-Atype',
        'url': 'https://celib.kr/property/gadi'
    },
    {
        'title': 'celib',
        'roomName': 'B type',
        'deposit': '600만원',
        'rentFee': '65만원',
        'region': '서울특별시 금천구 가산동',
        'brandType': '셀립',
        'py': '12.5',
        'imgUrl': '#ko_page > section > div.room-type > div > div > div.room.room-Btype',
        'url': 'https://celib.kr/property/gadi'
    },
    {
        'title': 'C type',
        'deposit': '700만원',
        'rentFee': '95만원',
        'region': '서울특별시 금천구 가산동',
        'brandType': '셀립',
        'py': '21.10',
        'imgUrl': '#ko_page > section > div.room-type > div > div > div.room.room-Ctype',
        'url': 'https://celib.kr/property/gadi'
    }
]
## 셀립 여의 정보(roomType, roomOption, gender, py 정보 X)
celib_rooms_Yeoui = [
    {
        'title': '수납의 방',
        'deposit': '400만원',
        'rentFee': '140만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#A-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '바닥의 방',
        'deposit': '400만원',
        'rentFee': '140만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#B-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '뒹굶의 방',
        'deposit': '400만원',
        'rentFee': '140만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#C-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '배움의 방',
        'deposit': '400만원',
        'rentFee': '140만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#D-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '다있는 방',
        'deposit': '400만원',
        'rentFee': '150만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#E-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '여유의 방',
        'deposit': '400만원',
        'rentFee': '150만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#F-type',
        'url': 'https://celib.kr/property/yeoui'
    }
]
## 셀립 은평 정보(roomType, roomOption, gender, py 정보 X)
celib_rooms_eunpyeong = [
    {
        'title': '수납의 방',
        'deposit': '400만원',
        'rentFee': '140만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#A-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '바닥의 방',
        'deposit': '400만원',
        'rentFee': '140만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#B-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '뒹굶의 방',
        'deposit': '400만원',
        'rentFee': '140만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#C-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '배움의 방',
        'deposit': '400만원',
        'rentFee': '140만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#D-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '다있는 방',
        'deposit': '400만원',
        'rentFee': '150만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#E-type',
        'url': 'https://celib.kr/property/yeoui'
    },
    {
        'title': '여유의 방',
        'deposit': '400만원',
        'rentFee': '150만원',
        'region': '서울특별시 영등포구 신길동',
        'brandType': '셀립',
        'imgUrl': '#F-type',
        'url': 'https://celib.kr/property/yeoui'
    }
]