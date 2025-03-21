import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

TWITCH_CHAT_URL = "https://www.twitch.tv/bbbb87/chat"

TWITCH_SID = "nzrqq59oeg6fgfux3s3xr3ybzxb0eq"

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # 最大化視窗
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def login_with_cookie(driver):
    driver.add_cookie({"name": "auth-token", "value": TWITCH_SID, "domain": ".twitch.tv"})
    driver.refresh()  # 刷新頁面使 Cookie 生效
    print("✅ 使用 Cookie 自動登入 Twitch 成功！")

def send_chat_message():
    """ 自動發送 Twitch 訊息 """
    driver = setup_driver()
    driver.get(TWITCH_CHAT_URL)
    login_with_cookie(driver)
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-a-target='chat-input']")))
        chat_input = driver.find_element(By.CSS_SELECTOR, "div[data-a-target='chat-input']")
        chat_input.send_keys(" ")

        # 聊天室規則
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-test-selector='chat-rules-ok-button']")))
        ok_btn=driver.find_element(By.XPATH, "//button[@data-test-selector='chat-rules-ok-button']")
        ok_btn.send_keys(Keys.RETURN)

        while True:
            chat_input.send_keys(" guanwe1Mao6 bbbb87Dog1 ")
            chat_input.send_keys(Keys.RETURN)
            time.sleep(2)
            chat_input.send_keys(" bbbb87Dog1 guanwe1Mao6 ")
            chat_input.send_keys(Keys.RETURN)
            time.sleep(2)

    except Exception as e:
        print(f"發生錯誤: {e}")

    finally:
        input("按 Enter 鍵關閉瀏覽器...")
        driver.quit()

send_chat_message()