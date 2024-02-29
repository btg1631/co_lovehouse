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
dabangs = database['dabang_five']

# - 주소 입력
## 기존 링크
# browser.get("https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B0%2C1%2C2%5D%2C%22selling_type%22%3A%5B0%2C1%2C2%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B126.6800716%2C37.2201072%5D%2C%5B127.3488643%2C37.767624%5D%5D%2C%22center%22%3A%5B127.01446798508894%2C37.494367328004216%5D%2C%22zoom%22%3A11%7D&search=%7B%22id%22%3A%22%22%2C%22type%22%3A%22%22%2C%22name%22%3A%22%22%7D&tab=all")
for k in browser :
    ## 서초동
    browser.get("https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B2%2C0%2C1%5D%2C%22selling_type%22%3A%5B0%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B126.97503%2C37.4582036%5D%2C%5B127.1054927%2C37.5109874%5D%5D%2C%22center%22%3A%5B127.0402613%2C37.4846001%5D%2C%22zoom%22%3A14%7D&search=%7B%22id%22%3A%22region_11650108%22%2C%22type%22%3A%22region%22%2C%22name%22%3A%22%EC%84%9C%EC%B4%88%EB%8F%99%22%7D&tab=all")
    ## 백현동
    browser.get("https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B2%2C0%2C1%5D%2C%22selling_type%22%3A%5B0%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B127.0541659%2C37.3670213%5D%2C%5B127.1846286%2C37.4198694%5D%5D%2C%22center%22%3A%5B127.1193972%2C37.39345%5D%2C%22zoom%22%3A14%7D&search=%7B%22id%22%3A%22region_41135110%22%2C%22type%22%3A%22region%22%2C%22name%22%3A%22%EB%B0%B1%ED%98%84%EB%8F%99%22%7D&tab=all")
    # ## 노고산동
    browser.get("https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B0%2C1%2C2%5D%2C%22selling_type%22%3A%5B0%2C1%2C2%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B126.8772701%2C37.530512%5D%2C%5B127.0048145%2C37.580728%5D%5D%2C%22center%22%3A%5B126.94104234137455%2C37.55562422893384%5D%2C%22zoom%22%3A14%7D&search=%7B%22id%22%3A%22region_11440110%22%2C%22type%22%3A%22region%22%2C%22name%22%3A%22%EB%85%B8%EA%B3%A0%EC%82%B0%EB%8F%99%22%7D&tab=all")
    # ## 창신동
    browser.get("https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B0%2C1%2C2%5D%2C%22selling_type%22%3A%5B0%2C1%2C2%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B126.9496649%2C37.5508541%5D%2C%5B127.0772093%2C37.6010563%5D%5D%2C%22center%22%3A%5B127.013437126061%2C37.57595945351064%5D%2C%22zoom%22%3A14%7D&search=%7B%22id%22%3A%22region_11110174%22%2C%22type%22%3A%22region%22%2C%22name%22%3A%22%EC%B0%BD%EC%8B%A0%EB%8F%99%22%7D&tab=all")
    # ## 신설동
    browser.get("https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B0%2C1%2C2%5D%2C%22selling_type%22%3A%5B0%2C1%2C2%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B126.9629862%2C37.5494265%5D%2C%5B127.0905306%2C37.5996297%5D%5D%2C%22center%22%3A%5B127.0267584239059%2C37.57453233889117%5D%2C%22zoom%22%3A14%7D&search=%7B%22id%22%3A%22region_11230101%22%2C%22type%22%3A%22region%22%2C%22name%22%3A%22%EC%8B%A0%EC%84%A4%EB%8F%99%22%7D&tab=all")         
    time.sleep(2)


    # 메인 페이지 핸들 생성
    main_window_handle = browser.current_window_handle # 초기 창 핸들로 저장
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


    for i in range(24):
        # url = browser.current_url
        # browser.get(url)
        time.sleep(2)
        button_list = browser.find_elements(by=By.CSS_SELECTOR,value = '#content > div.styled__Content-sc-1nnkzie-0.fTqXoR > div.styled__ListWrap-sc-5dgg47-0.fOZpfA > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div')
        for button in button_list:
            click_button_next = button.find_element(by=By.CSS_SELECTOR,value = 'button:nth-child(8)')
        

        ## 전체 방 영역 정보
        room_value = "#content > div.styled__Content-sc-1nnkzie-0.fTqXoR > div.styled__ListWrap-sc-5dgg47-0.fOZpfA > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > ul>li"
        element_whole = browser.find_elements(by=By.CSS_SELECTOR, value=room_value)
        # 상품 클릭(click)
        counter = 0
        for room_element in element_whole:
            counter += 1
            click_item = room_element.find_element(by=By.CSS_SELECTOR, value= f"#content > div.styled__Content-sc-1nnkzie-0.fTqXoR > div.styled__ListWrap-sc-5dgg47-0.fOZpfA > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > ul > li:nth-child({counter}) > div")
            click_item.click()
            time.sleep(2)
            # 탭 스위치 기능 있어야 새로 열린 창 url 가져올 수 있음
            # 새로운 창(탭) 핸들링해서 이동
            all_window_handles = browser.window_handles # 모든 창 저장
            # 새 창 핸들을 찾기
            new_window_handle = None
            for handle in all_window_handles:
                if handle != main_window_handle:    # 현재 창이 메인창이 아닐때
                    new_window_handle = handle  # 현재 창이 새로운창으로 핸들
                    break
            # 새 창 핸들로 전환
            browser.switch_to.window(new_window_handle) # 현재 창으로 핸들
            # 새 창의 URL 가져오기
            url = browser.current_url
            browser.get(url)
            pass
            ## 매물번호 영역
            element_rental_info = browser.find_elements(by=By.CSS_SELECTOR,value = "#content > div.styled__DetailContainer-sc-1xo573q-0.eTmfeO > div > aside > div > div.styled__InfoWrap-sc-1h4thfr-0.cWFdmE")
            for element in element_rental_info:
                # 상품 제목(매물번호-title)
                try:
                    element_title = element.find_element(by=By.CSS_SELECTOR,value = "div > div > div.styled__TagWrap-sc-1h4thfr-2.gWqFHA > div > div").text
                except NoSuchElementException:
                    element_title = ""
                # 평수(py)
                try:
                    element_py = element.find_element(by=By.CSS_SELECTOR,value = "ul > li:nth-child(1) > div:nth-child(2) > span").text
                except NoSuchElementException:
                    element_py = ""
                # 지역(region)
                try:
                    element_region = element.find_element(by=By.CSS_SELECTOR,value = "ul > li.styled__SubInfo-sc-1h4thfr-14.btBOxM > div:nth-child(2) > p.content").text
                except NoSuchElementException:
                    element_region = ""
            ## 가격 정보 영역
            element_price_info = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(1)")
            for element in element_price_info:
                # 보증금,월세가격(depositAndRentFee)
                try:
                    element_deposit = element.find_element(by=By.CSS_SELECTOR,value = "#content > div.styled__DetailContainer-sc-1xo573q-0.eTmfeO > div > div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(1) > ul > li:nth-child(1) > div.styled__ListContent-mttebe-1.bQSaMO > p").text
                    deposit,rentFee = element_deposit.split('/') # 보증금/월세 split
                    deposit += '만원'
                    rentFee += '만원'
                    pass
                except NoSuchElementException:
                    deposit,rentFee = "",""
            ## 상세정보 영역
            element_detail_info = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(2)")
            for element in element_detail_info:
                # 1인실 or 그 외(roomType) - 방 수 1개면 1인실, 2개면 '그 외'
                    ## (방 수/욕실 수) -> split 필요?
                try:
                    element_roomType = element.find_element(by=By.CSS_SELECTOR,value = "li:nth-child(4) > div.styled__ListContent-ialnoa-7.iMduqg > p").text
                    roomtype_list = list(element_roomType.split('/'))
                    roomType = roomtype_list[0]
                    if roomType == '1개':
                        roomType = '1인실'
                    else:
                        roomType = '그 외'
                    pass
                except NoSuchElementException:
                    roomType = ""
            ## 옵션,보안/안전시설 영역
            element_option_one = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(3)")
            element_option_two = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(4)")
            # 옵션(roomOption)
            for element in element_option_one:
                try:
                    element_roomOption_one = element.find_element(by=By.CSS_SELECTOR, value = 'div > div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(3) > ul').text
                    pass
                except NoSuchElementException:
                    element_roomOption_one = ""
                    pass
            # 보안/안전시설
            for element in element_option_two:
                try:
                    element_roomOption_two = element.find_element(by=By.CSS_SELECTOR, value = 'div > div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(4) > ul').text
                except NoSuchElementException:
                    element_roomOption_two = ""
                pass
            element_roomOption_total = element_roomOption_one +'\n'+ element_roomOption_two
            # 출력값 : '벽걸이형\n침대\n신발장\n냉장고\n세탁기\n싱크대\n가스레인지\nTV\n벽걸이형\n침대\n신발장\n냉장고\n세탁기\n싱크대\n가스레인지\nTV'
            gender = '공용'
            brandType = '일반사업자'
            imgUrl = 'https://d1774jszgerdmk.cloudfront.net/1024/uCtHEMbF1I79lfPgIhws5'
            data={
                'title' : element_title,
                'roomName' : element_title,
                'gender' : gender,
                'roomType' : roomType,
                'py' : element_py,
                'deposit' : deposit,
                'rentFee' : rentFee,
                'region' : element_region,
                'brandType' : brandType,
                'roomOption' : element_roomOption_total,
                'url' : url,
                'imgUrl' : imgUrl
            }
            dabangs.insert_one(data)
            browser.close()
            browser.switch_to.window(main_window_handle)
            time.sleep(1)
        time.sleep(5)
        click_button_next.click()  # 페이지 넘기기(2~24페이지)
        
        pass