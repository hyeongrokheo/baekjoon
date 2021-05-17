
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab

# 로그인url
url1 = "https://login.11st.co.kr/auth/login.tmall?returnURL=http%253A%252F%252Fm.11st.co.kr%252FMW%252FMyPage%252FmypageHome.tmall"
# 상품url
url2 = 'http://www.11st.co.kr/products/3167879989'

print('페이지 로딩중...')
mobile_emulation = {"deviceName": "iPhone X"}
chrome_options = webdriver.ChromeOptions()

prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(
    "C:/Users/syndr/Documents/chromedriver", chrome_options=chrome_options)
driver.get(url1)

driver.find_element_by_name('memId').send_keys('gjgudfhr') # 아이디
driver.find_element_by_name('memPwd').send_keys('aa') # 패스워드

login = driver.find_element_by_class_name("bbtn")
login.click()
print('로그인 완료')
time.sleep(1)
driver.get(url2)
print('구매실행프로세스 대기중')
time.sleep(1)
print('구매실행프로세스 작동시작')

while True:
    check = driver.find_element_by_class_name("no_sale")
    print(check)
    try:
        if check.text == '현재 판매중인 상품이 아닙니다.':
            driver.refresh()
            print("상품없음 새로고침진행...")
            driver.implicitly_wait(100)
        else:
            buy = driver.find_element_by_name("buy")
            buy.click()
            break
    except Exception as e:
        time.sleep(1)
        pass
time.sleep(2)

print("일반결제...")
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, "//input[@id='payOthers']/following::span[1]")))
driver.execute_script("arguments[0].click();", radio)
noaccount_table = driver.find_element_by_id("paymentGeneralTab5")
print("무통장입금 선택")
noaccount_table.click()
bankKindCtl = driver.find_element_by_id("bankKindCtl04")
bankKindCtl.click()
buying = driver.find_element_by_class_name("btn_order")
buying.click()
print("주문이 완료되었습니다.")
