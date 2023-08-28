import urllib.request
import urllib.parse

url = 'https://www.kisssub.org/search.php?keyword='

kw = '无职转生'

url_s = url+urllib.parse.quote(kw)

headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
'Cookie':
'Hm_lvt_bab0ae65b49b7efd4fde9bf6858ec60b=1693140214,1693197954,1693200794,1693204542; Hm_lpvt_bab0ae65b49b7efd4fde9bf6858ec60b=1693204964'
}

request = urllib.request.Request(url=url_s,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')
fp = open('s.html','w',encoding='utf-8')
fp.write(content)
fp.close()

print(content)