import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局 WebDriver 实例
driver = None


def get_driver():
    global driver
    return driver

def wait_page_load():
    global driver
    driver.set_page_load_timeout(30)

def wait_untl_element(xpath):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

def get(url):
    driver.get(url)
    driver.set_page_load_timeout(30)
    xpath_locator = "//*[@id='header']/div[1]/div[3]/ul/li[2]"
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator))
    )

def open_browser_with_options(url, browser):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)

    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser == "edge":
        driver = webdriver.Edge()
        driver.maximize_window()
    elif browser == "safari":
        driver = webdriver.Safari()
        driver.maximize_window()
    else:
        raise ValueError("Browser type not supported")

    driver.get(url)

    driver.set_page_load_timeout(30)
    # 等待直到页面包含特定的 XPath 元素
    xpath_locator = "//*[@id='header']/div[1]/div[3]/div/a"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator))
    )
    print("open finish===================>")

def log_in():
    print("login start===================>")

    global driver

    # 点击按钮
    login_xpath = "//*[@id='header']/div[1]/div[3]/div/a"
    login_button = driver.find_element(By.XPATH, login_xpath)
    login_button.click()

    # 等待微信登录按钮出现
    xpath_locator_wechat_login = "//*[@id='wrap']/div/div[2]/div[2]/div[2]/div[1]/div[4]/a"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_wechat_login))
    )

    wechat_button = driver.find_element(By.XPATH, "//*[@id='wrap']/div/div[2]/div[2]/div[2]/div[1]/div[4]/a")
    wechat_button.click()

    xpath_locator_wechat_logo = "//*[@id='wrap']/div/div[2]/div[2]/div[1]/div[2]/div[1]/img"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_wechat_logo))
    )

    xpath_locator_login_success = "//*[@id='header']/div[1]/div[3]/ul/li[2]/a"
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_login_success))
    )

def open_job():
    index = 3
    xpath_job = f"//*[@id='wrap']/div[2]/div[2]/div/div[1]/div[2]/ul/li[{index}]/div[1]/a/div[1]"
    wait_untl_element(xpath_job)
    open_job = driver.find_element(By.XPATH, xpath_job)
    open_job.click()
    wait_page_load()
    # time.sleep(10)

def get_job_desc():
    global driver

    # 获取所有窗口句柄
    window_handles = driver.window_handles

    # 切换到新窗口（假设新窗口是最后一个打开的窗口）
    driver.switch_to.window(window_handles[-1])

    # 在新窗口中执行操作
    print(driver.title)  # 输出新窗口的标题

    # 关闭新窗口
    # driver.close()

    # 切换回原始窗口
    # driver.switch_to.window(window_handles[0])

    # 在原始窗口中继续执行操作
    # print(driver.title)  # 输出原始窗口的标题

    print('driver.title',driver.title)
    try:
        # //*[@id="main"]/div[3]/div/div[2]/div[1]/div[3]
        # //*[@id="main"]/div[3]/div/div[2]/div[1]/div[3]
        description_selector = "//*[@id='main']/div[3]/div/div[2]/div[1]/div[3]"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, description_selector))
        )
        job_description_element = driver.find_element(By.XPATH, description_selector)
        return job_description_element.text

    except NoSuchElementException:
        print(f"No job found at index.")                                         
        return None

def chat_now():
    global driver
    xpath_chat = " //*[@id='main']/div[1]/div/div/div[1]/div[3]/div[1]/a[2]"
    # 点击按钮
    chat_now = driver.find_element(By.XPATH, xpath_chat)
    chat_now.click()

