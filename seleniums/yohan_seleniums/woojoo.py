# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# webdriver_manager_directory = ChromeDriverManager().install()
# browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# driver = webdriver.Chrome(ChromeDriverManager().install())
chromedriver_path = "/usr/bin/chromedriver"
browser = webdriver.Chrome()

# 몽고db 저장
from pymongo import MongoClient
# mongodb에 접속
# mongoClient = MongoClient("mongodb://192.168.10.10:27017")
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["project_coliving"]
# collection 작업
room_infor = database['woojoo']

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By

browser.get("https://www.woozoo.kr/houses")
time.sleep(2)

selector_element = '#search-result'
element_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)

from selenium.webdriver.common.keys import Keys

element_body = browser.find_element(by=By.CSS_SELECTOR,value='body')

# 스크롤 부분
previous_scrollHeight = 0

while True:
    # python 방식 변수 매칭
    # javascript와 python 결합 방식 변수 매칭
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element_scrollableDiv)

    current_scrollHeight = browser.execute_script("return arguments[0].scrollHeight",
                                                  element_scrollableDiv)
    
    
    if previous_scrollHeight >= current_scrollHeight:
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass

# 가져오기
element_get = browser.find_elements(by=By.CSS_SELECTOR,value='#search-result>div')

counter = 0
for element in element_get:
    counter +=1
    try :
        element_click = browser.find_element(by=By.CSS_SELECTOR,value=f'#search-result > div:nth-child({counter})')
        element_click.click()
        time.sleep(2)
        url = browser.current_url
        inside_element_get = browser.find_elements(by=By.CSS_SELECTOR,value='#body')
        # 타이틀
        try:
            selector_value_title = "#house-show > div.detail_tab_wrapper > div.apply_wrapper-w > h2"
            element_title = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_value_title)
            title = element_title.text
        except:
            title = ""
        # 옵션
        try:
            # 공용옵션
            selector_options = "#house-show > div.house_intro_wrapper.detail1.scroll > div.area_info > div.area_item.shared_area > ul"
            element_options = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_options)
            options = element_options.text
            try:
                # 개인옵션
                selector_options = "#house-show > div.house_intro_wrapper.detail1.scroll > div.area_info > div.area_item.privat_area > ul"
                element_options = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_options)
                options += ' '
                options += element_options.text
            except:
                pass
        except:
            options = ""

        # 지역
        try:
            selector_region = "#house-show > div.house_intro_wrapper.detail1.scroll > div.house_intro"
            element_region = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_region)
            region_test = element_region.text.split()
            for i in region_test:
                if i[-1] == '역':
                    region = i
                    break
        except:
            region = ""


        brandType = "일반사업자"    


        contents_wrap = '#image-slider > div.tab_content_wrapper'
        detail_element_get = browser.find_elements(by=By.CSS_SELECTOR,value=contents_wrap)
        
        
     
        # 테이블 검사해서 room이면 진입하는 로직 짜야됨

        incounter = -1
        for i in detail_element_get:
            # 페이지 구성이 0부터 시작... 밑으로 내리기 귀찮...
            incounter += 1
            menu_element_get = browser.find_element(by=By.CSS_SELECTOR,value=f'#image_tab_{incounter} > div.room_info > div.room_name')
            menu_name_list = list(menu_element_get.split())
            if menu_name_list[0] == 'Room':
                # 기본 타입 초기화
                roomType = ''
                gender = '공용'
                room_name = ""
                room_name += menu_name_list[0]
                room_name += ' '
                room_name += menu_name_list[1]
                
                for j in menu_name_list:
                    # 성별
                    if '여성' in j:
                        gender = '여'
                    elif '남성' in j:
                        gender = '남'

                    # 평수
                    if 'm' in j:
                        py = j

                    #인실
                    if '인실' in j:
                        roomType = j

                # 보증금
                try:
                    selector_value_deposti = f"#image_tab_{incounter} > div.room_info > div.cost_list > div.cost_item.deposit > span > span > em"
                    element_deposit= inside_element_get(by=By.CSS_SELECTOR,value=selector_value_deposti)
                    deposit = element_deposit.text
                except:
                    deposit = ""
                # 월세
                try:
                    selector_value_monthly_rent = f"#image_tab_{incounter} > div.room_info > div.cost_list > div.cost_item.monthly_rent > span > span > em"
                    element_monthly_rent= inside_element_get(by=By.CSS_SELECTOR,value=selector_value_monthly_rent)
                    monthly_rent = element_monthly_rent.text
                except:
                    monthly_rent = ""


            else:
                pass

    except :
        pass   



# 브라우저 종료
browser.quit()