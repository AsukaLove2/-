# 导入包
from selenium import webdriver
# 根据使用的浏览器来导入对应的包
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
# 使用元素定位时需要导入的包
from selenium.webdriver.common.by import By
# ActionChains用于提供鼠标操作
from selenium.webdriver import ActionChains
import time

# 浏览器驱动路径
path = r'C:\Users\22097\Desktop\Network_crawler\chromedriver-win64\chromedriver.exe'

# 设置webdriver需要使用的两个参数，根据使用的浏览器来确定
options = ChromeOptions()
# 解决window.navigator.webdriver=True的反爬手段
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument("--disable-blink-features=AutomationControlled")
service = ChromeService(executable_path=path)

# 建立浏览器对象
driver = webdriver.Chrome(service=service, options=options)

url = 'https://login.taobao.com/member/login.jhtml'

driver.get(url=url)

# 定位账户和密码输入框，并输入内容
account = driver.find_element(By.NAME,'fm-login-id')
account.send_keys('trans69')
time.sleep(2)

password = driver.find_element(By.NAME,'fm-login-password')
password.send_keys('ppp2236995')
time.sleep(2)

# 点击登录
button = driver.find_element(By.XPATH,'//div[@class="fm-btn"]/button')
button.click()
# 登录后可能还会有验证，因此强制睡眠来等待验证通过
time.sleep(10)

driver.quit()
