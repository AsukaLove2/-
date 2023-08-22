# 使用urllib爬取淘宝个人界面源码
import urllib.request

url = 'https://i.taobao.com/user/baseInfoSet.htm?spm=0.0.0.0.ua9TUX'

# 准备UA和Cookie来实现绕过登录
# 为保护隐私，上传版本的headers内容将会不完整
headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
'Cookie':
'm_h5_tk_enc=2238844e78fcd481566233413e18a39d; cna=01trHZfcGTwCAYvMa2gaxotX; cookie2=1432a37c28ed1a2f745a9d0e69170dd2; t=70a1efa6f83d6b35a8fb17249743bbfc; _tb_token_=377ee3a6683e; _samesite_flag_=true; xlly_s=1; sgcookie=E100Scvg6J6A2s4gUbLl3dlun7jBGULFZ3wUU5WhLBASXfnsyxGruXXvoadtzmzWBJYbDd5uMKHEgwEpGOBjLUgIS3zz9mfkLPUW9zwimt5Q0jPkWfhZoB87euuetgeYjc9P; unb=2085247472; uc3=id2=UUjZd91J6J8cqw%3D%3D&vt3=F8dCsGZMnqxMumuk4LI%3D&nk2=F4T%2BpbG8wA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; csg=059c5302; lgc=trans69; cancelledSubSites=empty; cookie17=UUjZd91J6J8cqw%3D%3D; dnk=trans69; skt=97eb46de6c1b203b; existShop=MTY5MjY5MzgwMw%3D%3D; uc4=id4=0%40U2o7nDZFSqJr2o2NcM4soLl%2FXb71&nk4=0%40FZ7hK9LwFTh7u7lxQiETOdL0; tracknick=trans69; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=927; _nk_=trans69; cookie1=U7KqUuofWFnYY%2FWY85NPNMeXdbz7Wy9zUp4qEXDP%2FJo%3D; mt=ci=5_1; thw=cn; uc1=cookie14=Uoe9b68K%2BDd%2FZw%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&pas=0&cookie21=VFC%2FuZ9aiKCaj7AzMpJs&existShop=false; isg=BE1NmEkkFcgOXLHkipO3YStBXGnHKoH8dwHj1I_SPeRThmw4V35AzbgE9hrgXZm0; l=fBrQ9OT4N5IvVG2yBOfaFurza77OSIRYYuPzaNbMi9fP_31B5vIfW1tRhpY6C3GVFs6wR3lbLcMkBeYBqQAonxv9w8VMULkmndLHR35..; tfstk=dJiefoiaQHKeBcUorrrr33uSyirL2odXU0N7EYDudWVnRY2u4fcWpWMk9bozsfWB97TKazlS6zc7Nv6KWjMcADTLVgrL2uAXGntXpvE8qUeHcnOMuCOpGItXcvHL2uAjVIeQ5tVGqumzKUe3PjhqdcyU-FM3sg2tbJzUivb5qOucwRY0d03FZaz3BRPXQdu9EPwd.',

}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('gb2312')

print(content)