# -*- coding:utf-8 -*-
import requests
import execjs
import unicodedata

cookies = {
    'SUNWAY-ESCM-COOKIE': '49f2f5f5-7c18-41e2-a510-117607e472fe',
    '__jsluid_s': 'fad744a4fa32b8ba70e1c807616eff1d',
    'JSESSIONID': 'DFA73DA52982B7BF942A036AA175B3C8',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'SUNWAY-ESCM-COOKIE=49f2f5f5-7c18-41e2-a510-117607e472fe; __jsluid_s=fad744a4fa32b8ba70e1c807616eff1d; JSESSIONID=DFA73DA52982B7BF942A036AA175B3C8',
    'Origin': 'https://ec.minmetals.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.post(
    'https://ec.minmetals.com.cn/open/homepage/public', cookies=cookies, headers=headers).text
with open(r'c:\Users\22097\Desktop\Network_crawler\Self-study_Crawler_Practice\JS逆向学习\webpacks\demo.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
    jscode = unicodedata.normalize('NFKC', jscode)
    # 出现unicode错误是因为js代码中太多的空格。
param = execjs.compile(jscode).call('main12', response, 4)


json_data = {
    'param': param
}

response = requests.post(
    'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
    cookies=cookies,
    headers=headers,
    json=json_data,
).text

with open('jjj.json', 'w', encoding='utf-8') as f:
    f.write(response)
