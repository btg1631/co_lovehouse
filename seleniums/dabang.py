# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행
from selenium.common.exceptions import NoSuchElementException

# 몽고db 저장
from pymongo import MongoClient
# mongodb에 접속
mongoClient = MongoClient("mongodb://192.168.10.10:27017")
# database 연결
database = mongoClient["project_coliving"]
# collection 작업
room_infor = database['NOTICE_DATA']
room_infor = database['REVIEW_DATA']
room_infor = database['ROOM_DATA']
# test
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By
# - 주소 입력
browser.get("https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B0%2C1%2C2%5D%2C%22selling_type%22%3A%5B0%2C1%2C2%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B126.6800716%2C37.2201072%5D%2C%5B127.3488643%2C37.767624%5D%5D%2C%22center%22%3A%5B127.01446798508894%2C37.494367328004216%5D%2C%22zoom%22%3A11%7D&search=%7B%22id%22%3A%22%22%2C%22type%22%3A%22%22%2C%22name%22%3A%22%22%7D&tab=all")
time.sleep(2)

# - 정보 획득

# 전체 정보
selector_value = "body"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

## 스크래핑 타겟 : 제목(title), 보증금(deposit), 월세가격(rentFee), 1인실 or 그 외(roomType), 옵션(roomOption), 지역(region), 회사(회사가 아니면 일반사업자-brandType),
#                 성별(남,여, 공용-gender), 평수(추후 범주형 변환-py), url, imgUrl
'''
# text = '1000/56'
# deposit , rentFee = text.split('/')
## region : 주소 전체
## brandType : 일반사업자
## 성별없으므로 생략
## imgUrl : 첫 번째 대표사진(src)
'''
## 월세,전세,매매 영역
#content > div.styled__SubHeader-sc-6mq5f9-0.mlNkP
# 월세,전세,매매 필터 클릭
# #content > div.styled__SubHeader-sc-6mq5f9-0.mlNkP > div.styled__FilterWrap-sc-6mq5f9-1.dbGMaK > div:nth-child(2)
# 전세 클릭버튼 해제
# #content > div.styled__SubHeader-sc-6mq5f9-0.mlNkP > div.styled__FilterWrap-sc-6mq5f9-1.dbGMaK > div.styled__Dock-sc-8m68ku-0.hKaVMr > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div.styled__Wrap-sc-10hrqqq-1.ebOjwi > div > label:nth-child(2) > input
#content > div.styled__SubHeader-sc-6mq5f9-0.mlNkP > div.styled__FilterWrap-sc-6mq5f9-1.dbGMaK > div.styled__Dock-sc-8m68ku-0.hKaVMr > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div.styled__Wrap-sc-10hrqqq-1.ebOjwi > div > label:nth-child(2)
# 매매 클릭버튼 해제
# #content > div.styled__SubHeader-sc-6mq5f9-0.mlNkP > div.styled__FilterWrap-sc-6mq5f9-1.dbGMaK > div.styled__Dock-sc-8m68ku-0.hKaVMr > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div.styled__Wrap-sc-10hrqqq-1.ebOjwi > div > label:nth-child(3) > input


## 성별 : 없으면 '공용'
## 방 수 1개면 1인실, 2개면 '그 외'

for i in range(20):
    # 상품 제목 클릭(click)
    click_item_title = browser.find_elements(by=By.CSS_SELECTOR, value= "div.simplebar-mask > div > div > div > ul > li")
    click = click_item_title[i]
    click.click()
    time.sleep(2)
    # 상품 제목(매물번호)
    try:
        element_title = browser.find_element(by=By.CSS_SELECTOR,value = "div > div > div.styled__TagWrap-sc-1h4thfr-2.gWqFHA > div > div").text
    except NoSuchElementException:
        element_title = ""
    # 보증금
    try:
        element_deposit = browser.find_element(by=By.CSS_SELECTOR,value = "").text
    except NoSuchElementException:
        element_deposit = ""