# 使用selenium实现搜索商品并依据页数进行爬取商品信息
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
account.send_keys('')
time.sleep(2)

password = driver.find_element(By.NAME,'fm-login-password')
password.send_keys('')
time.sleep(2)

# 点击登录
button = driver.find_element(By.XPATH,'//div[@class="fm-btn"]/button')
button.click()
# 登录后可能还会有验证，因此强制睡眠来等待验证通过
time.sleep(10)

# 先进入到淘宝网首页
Main_page = driver.find_element(By.XPATH,'//div[@class="site-nav-new-home"]')
Main_page.click()
time.sleep(2)

# 获取输入文本框
inputs = driver.find_element(
    By.XPATH, '//div[@data-sg-type="combobox"]/input[@id="q"]')
# 输入想要查询的内容
shops = input()
inputs.send_keys(shops)
time.sleep(2)

# 点击搜索
button_search = driver.find_element(
    By.XPATH, '//div[@class="search-button"]/button')
button_search.click()
time.sleep(2)

for i in range(1,3):
  content = driver.page_source
  fp = open(f'{i}.html','w',encoding='utf-8')
  fp.write(content)
  fp.close()
  
# 3 滑到底部
  js_bottom = 'document.documentElement.scrollTop=100000'
  driver.execute_script(js_bottom)
  time.sleep(2)

# 点击下一页
  next_page = driver.find_element(By.XPATH,'//li[@class="item next"]')
  next_page.click()
  time.sleep(2)


driver.quit()
