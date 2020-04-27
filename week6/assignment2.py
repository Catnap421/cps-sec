from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "\chromedriver"

driver = webdriver.Chrome(path)

keyword = '자료구조'


try : 
    driver.get("https://library.cau.ac.kr/#/")

    element = driver.find_element_by_name('keyword')

    # 키워드 입력
    element.send_keys(keyword)

    # 키워드 검색
    driver.find_element_by_class_name("ikc-btn-search").click()
    time.sleep(3)
    # 더 많은 정보를 얻기 위한 버튼 클릭
    driver.find_element_by_class_name("btn-search-result-more").click() 
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.select("body > div.ikc-pyxis-wrap > div.ikc-container-wrap > div.ikc-container > div.ikc-content > div.ikc-main > div.ikc-search-layout > div.ikc-search-result > div:nth-child(1) > div:nth-child(3) > div.ikc-search-result > div.ikc-search-item")
    
    
    for el in elements:
        data = el.find("div", class_ = "ikc-item-info").find("ul").find_all("li")
        print("제목: " + data[0].find("span").text)
        print("저자: " + data[1].find("span").text)
        print("출판사: "+ data[2].find("span").text)
        print("보관 위치: " + data[-1].find("span", class_ = "ikc-item-branch").text + " 대출 여부: " + data[-1].find("span", class_ = "ikc-item-status").text)
        print("===============================================================================")


finally :   
    time.sleep(3)
    driver.quit()