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

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By
# - 정보 획득
# from selenium.webdriver.support.ui import Select      # Select : dropdown 메뉴다루는 클래스
# - 주소 입력
browser.get("https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B0%2C1%2C2%5D%2C%22selling_type%22%3A%5B0%2C1%2C2%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B126.6800716%2C37.2201072%5D%2C%5B127.3488643%2C37.767624%5D%5D%2C%22center%22%3A%5B127.01446798508894%2C37.494367328004216%5D%2C%22zoom%22%3A11%7D&search=%7B%22id%22%3A%22%22%2C%22type%22%3A%22%22%2C%22name%22%3A%22%22%7D&tab=all")
time.sleep(2)

## 스크래핑 타겟 : 제목(title), 보증금(deposit), 월세가격(rentFee), 1인실 or 그 외(roomType), 옵션(roomOption), 지역(region), 회사(회사가 아니면 일반사업자-brandType),
#                 성별(남,여, 공용-gender), 평수(추후 범주형 변환-py), url, imgUrl
## 성별 : 없으면 '공용'
## 방 수 1개면 1인실, 2개면 '그 외'
'''
# text = '1000/56'
# deposit , rentFee = text.split('/')
## region : 주소 전체
## brandType : 일반사업자
## 성별없으므로 생략
## imgUrl : 첫 번째 대표사진(src)
'''

## 필터 영역 정보
selector_value = "#content > div.styled__SubHeader-sc-6mq5f9-0.mlNkP > div.styled__FilterWrap-sc-6mq5f9-1.dbGMaK"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

# 월세,전세,매매 필터 영역 클릭
click_rent = browser.find_element(by=By.CSS_SELECTOR, value= "#content > div.styled__SubHeader-sc-6mq5f9-0.mlNkP")
click_rent.click()
time.sleep(2)
# 월세,전세,매매 필터 클릭
click_rent_filter = browser.find_element(by=By.CSS_SELECTOR, value= "div.styled__FilterWrap-sc-6mq5f9-1.dbGMaK > div:nth-child(2)")
click_rent_filter.click()
time.sleep(2)
# 전세 클릭버튼 해제
click_charter = browser.find_element(by=By.CSS_SELECTOR, value= "div > div > div.styled__Wrap-sc-10hrqqq-1.ebOjwi > div > label:nth-child(2) > input")
click_charter.click()
time.sleep(2)
# 매매 클릭버튼 해제
click_sales = browser.find_element(by=By.CSS_SELECTOR, value= "div > div > div.styled__Wrap-sc-10hrqqq-1.ebOjwi > div > label:nth-child(3) > input")
click_sales.click()
time.sleep(2)


## 전체 방 영역 정보
room_value = "#content > div.styled__Content-sc-1nnkzie-0.fTqXoR > div.styled__ListWrap-sc-5dgg47-0.fOZpfA"
element_whole = browser.find_elements(by=By.CSS_SELECTOR, value=room_value)

for i in range(24):
    # 상품 클릭(click)
    click_item = browser.find_elements(by=By.CSS_SELECTOR, value= "div.simplebar-mask > div > div > div > ul > li")
    click_item.click()
    time.sleep(2)

    # 상품 제목(매물번호-title)
    try:
        element_title = browser.find_element(by=By.CSS_SELECTOR,value = "div > div > div.styled__TagWrap-sc-1h4thfr-2.gWqFHA > div > div").text
    except NoSuchElementException:
        element_title = ""

    # 보증금,월세가격(depositAndRentFee)       
    try:
        element_deposit = browser.find_element(by=By.CSS_SELECTOR,value = "section:nth-child(1) > ul > li").text
        deposit,rentFee = element_deposit.split('/') # 보증금/월세 split
    except NoSuchElementException:
        element_deposit = ""

    # 1인실 or 그 외(roomType) - 방 수 1개면 1인실, 2개면 '그 외'
        ## (방 수/욕실 수) -> split 필요?
    try:
        element_roomType = browser.find_element(by=By.CSS_SELECTOR,value = "li:nth-child(4) > div.styled__ListContent-ialnoa-7.iMduqg > p").text
        roomtype_list = list(element_roomType.split('/'))
        roomType = roomtype_list[0]
    except NoSuchElementException:
        element_roomType = ""

    # 옵션(roomOption)
    try:
        element_roomOption = browser.find_element(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(3)").text
    except NoSuchElementException:
        element_roomOption = ""

    # 지역(region)
    try:
        element_region = browser.find_element(by=By.CSS_SELECTOR,value = "ul > li.styled__SubInfo-sc-1h4thfr-14.btBOxM > div:nth-child(2) > p.content").text
    except NoSuchElementException:
        element_region = ""

    # 회사 or 일반사업자(brandType)
    try:
        element_brandType = browser.find_element(by=By.CSS_SELECTOR,value = "div.styled__LessorWrap-sc-1h4thfr-15.fJDJgS > div > p").text
    except NoSuchElementException:
        element_brandType = ""

    # 평수(py)
    try:
        element_py = browser.find_element(by=By.CSS_SELECTOR,value = "ul > li:nth-child(1) > div:nth-child(2) > span").text
    except NoSuchElementException:
        element_py = ""

    # url
    now_url = browser.current_url

    # imgUrl
    try:
        img_element = browser.find_element(by=By.CSS_SELECTOR,value = "#content > div.styled__PhotoContainer-sc-173484h-0.eqMfDJ > div > div > div:nth-child(1) > div")
        element_img = img_element.get_attribute('src')
    except NoSuchElementException:
        element_img = ""
gender = '공용'
print(element_title, element_deposit, element_roomType, element_roomOption, element_region, element_brandType, gender, element_py, now_url, element_img)
pass