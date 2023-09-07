import requests
import requests.utils
import re
import execjs

headers = {
    'authority': 'www.youzhicai.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da=1694074586',
    'referer': 'https://www.youzhicai.com/nv/0101010001010139.html',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.youzhicai.com/nd/fe6fccf3-7ae2-4d0e-93d8-d61375cf07e2-1.html',
    headers=headers,
)
response1 = re.sub(r'\s', '', response.text)
var_a = re.findall("vara='(.*?)';", response1)[0]
var_b = re.findall("varb='(.*?)';", response1)[0]

# 第一次cookie1
cookies = requests.utils.dict_from_cookiejar(response.cookies)

# 第二次cookie2
with open(r'c:\Users\22097\Desktop\Network_crawler\Self-study_Crawler_Practice\JS逆向学习\Cookie类\demo2.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
# 使用cookie的键头
spvrscode = execjs.compile(jscode).call('main12', var_a, var_b)
cookies['spvrscode'] = spvrscode


# 第二次请求
response1 = requests.get(
    'https://www.youzhicai.com/nd/fe6fccf3-7ae2-4d0e-93d8-d61375cf07e2-1.html',
    headers=headers, cookies=cookies
).text
print(response1)
