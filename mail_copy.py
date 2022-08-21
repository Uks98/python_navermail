import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 어떤 엘리먼트가 나올때 까지 기다리는데 기다리는 조건을 넣을 수 있다.
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import pyautogui
import pyperclip

my_id = ""
my_pw = ""

mail_list = ["bareman9@naver.com","      rozyfactory@gmail.com","      bareman12@gmail.com"]
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

browser = webdriver.Chrome("c://chromedriver")
browser.maximize_window()
browser.get(url)

browser.implicitly_wait(5) #페이지가 로딩 될때까지 최대 10초 기다려줌
browser.maximize_window()
browser.get(url) #페이지 열기

#아이디 입력창, 태그를 자동으로 찾아줌
id = browser.find_element(By.CSS_SELECTOR, "#id")
id.click()
# id.send_keys("barema9") #키보드를 이용하겠다.

pyperclip.copy(my_id)
pyautogui.hotkey("ctrl","v")
time.sleep(2)

pw = browser.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy(my_pw)
pyautogui.hotkey("ctrl","v")
time.sleep(2)
#pw.send_keys("265133jkj45@!@!") #키보드를 이용하겠다.

login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()

mail_home = browser.find_element(By.XPATH,'//a[text() = "메일"]')
mail_home.click()

browser.get("https://mail.naver.com/")
time.sleep(2)

send_mail = browser.find_element(By.CSS_SELECTOR, "#nav_snb > div.btn_workset > a.btn_quickwrite._c1\(mfCore\|popupWrite\|new\)._ccr\(lfw\.write\)._stopDefault > strong")
send_mail.click()
time.sleep(1)



for mail in range(len(mail_list)):
#받는사람
    browser.find_element(By.CSS_SELECTOR,"#toInput")
    pyautogui.write(mail_list[mail],interval= 0.05) #0.25초 간격을 준다
# pyautogui.press("tab") #tab키를 눌러서 전환
# pyautogui.press("tab")
    time.sleep(1)

#제목 
    browser.find_element(By.CSS_SELECTOR,"#subject").click()
    pyperclip.copy("이 메일은 파이썬으로 보내는 메일입니다.") #파이썬에서 한글로 작성할때 사용
    pyautogui.hotkey("ctrl","v")
    time.sleep(1)

#iframe 안으로 들어가기
#본문 태그의 부모를 찾는다
    browser.switch_to.frame("se2_iframe") 
#본문 내용 작성
#클래스 선택자는 ctrl + f누른 후 . 을 통해 식별자 찾는다.
    browser.find_element(By.CSS_SELECTOR,".se2_inputarea").send_keys("이 메일은 테스트용으로 작성되었습니다.")
    time.sleep(1)
#iframe 밖으로 나가기
    browser.switch_to.default_content()
#메일 전송하기 
    browser.find_element(By.CSS_SELECTOR,"#sendBtn").click()
    time.sleep(3)

#재전송
    browser.find_element(By.XPATH,'//span[text() = "메일쓰기"]').click()
    time.sleep(3)


