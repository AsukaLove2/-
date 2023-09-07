import requests
import execjs

with open(r'c:\Users\22097\Desktop\Network_crawler\Self-study_Crawler_Practice\JS逆向学习\Cookie类\demo1.js','r',encoding='utf-8') as f:
    jscode = f.read()

cookie = execjs.compile(jscode).call('main1')

headers = {
    'authority': 'www.ontariogenomics.ca',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': cookie,
    'referer': 'https://www.ontariogenomics.ca/news-events/',
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

response = requests.get('https://www.ontariogenomics.ca/news-events/', headers=headers).text
with open('js.html','w',encoding='utf-8') as f:
    f.write(response)


