import requests
from lxml import etree

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# 同步数据
session = requests.Session()

resonpse = session.get(url=url, headers=headers).text
# 对服务器进行解析
tree = etree.HTML(resonpse)

# 获取特殊字段
viewstate = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
viewstategenerator = tree.xpath(
    '//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]

# 获取验证码
srcs = 'https://so.gushiwen.cn' + tree.xpath('//img[@id="imgCode"]/@src')[0]
# 下载图片可以使用二进制方式
code_img = session.get(srcs).content
with open('imgcode.jpg', 'wb') as f:
    f.write(code_img)


# 登录API
url_S = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

# 输入验证码
print("输入验证码")
codes = input()

data = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2209785495@qq.com',
    'pwd': 'ppp2236995',
    'code': codes,
    'denglu': '登录'
}

resonpse = session.post(url=url_S, data=data, headers=headers).text
with open('gushiwen.html', 'w', encoding='utf-8') as f:
    f.write(resonpse)
