import requests

cookies = {
    'route-cell': 'ksa',
    'ASP.NET_SessionId': '4kpahuzamgko3vkbxzaydmuu',
    'Hm_lvt_5fd8501a4e4e0eddf0c4596de7bd57ab': '1694760914',
    'Hm_lpvt_5fd8501a4e4e0eddf0c4596de7bd57ab': '1694760914',
    'SERVERID': 'db2965ac6d1d4f093009cf9d5cafcc6f|1694761199|1694760890',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'route-cell=ksa; ASP.NET_SessionId=4kpahuzamgko3vkbxzaydmuu; Hm_lvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1694760914; Hm_lpvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1694760914; SERVERID=db2965ac6d1d4f093009cf9d5cafcc6f|1694761199|1694760890',
    'Origin': 'http://www.kfc.com.cn',
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'op': 'cname',
}

data = {
    # 城市
    'cname': '北京',
    'pid': '',
    # 页数
    'pageIndex': '2',
    'pageSize': '10',
}

response = requests.post(
    'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)

with open('KFC.json', 'w', encoding='utf-8') as f:
    f.write(response.text)
