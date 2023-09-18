import requests

cookies = {
    'll': '"118328"',
    'bid': 'Vy4bXXTbY68',
    '_pk_id.100001.4cf6': 'c1bca45257dd4933.1694419854.',
    '__yadk_uid': 'F4cqOLBAmvtcJ5ummP5C02CJUhxd1RHX',
    '_vwo_uuid_v2': 'D772C45B1FFD2A7ECB745FAAC52A809BD|c90a9b51c57aed587258824bc4001972',
    '__utma': '30149280.876266246.1694419854.1694419854.1694675123.2',
    '__utmc': '30149280',
    '__utmz': '30149280.1694675123.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '__utmt': '1',
    '__utmb': '30149280.1.10.1694675123',
    '__utma': '223695111.367808795.1694419854.1694419854.1694675174.2',
    '__utmb': '223695111.0.10.1694675174',
    '__utmc': '223695111',
    '__utmz': '223695111.1694675174.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1694675174%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2tB4dVx2lj2rejBCFQwaUhbzfYRLRAwkK8qgGrqAO6E-EOdbMvBzGFlg5PCqMNCL%26wd%3D%26eqid%3Df524f1bc00002be6000000066502b0e6%22%5D',
    '_pk_ses.100001.4cf6': '1',
    'ap_v': '0,6.0',
}

headers = {
    #  'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'll="118328"; bid=Vy4bXXTbY68; _pk_id.100001.4cf6=c1bca45257dd4933.1694419854.; __yadk_uid=F4cqOLBAmvtcJ5ummP5C02CJUhxd1RHX; _vwo_uuid_v2=D772C45B1FFD2A7ECB745FAAC52A809BD|c90a9b51c57aed587258824bc4001972; __utma=30149280.876266246.1694419854.1694419854.1694675123.2; __utmc=30149280; __utmz=30149280.1694675123.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1694675123; __utma=223695111.367808795.1694419854.1694419854.1694675174.2; __utmb=223695111.0.10.1694675174; __utmc=223695111; __utmz=223695111.1694675174.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1694675174%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2tB4dVx2lj2rejBCFQwaUhbzfYRLRAwkK8qgGrqAO6E-EOdbMvBzGFlg5PCqMNCL%26wd%3D%26eqid%3Df524f1bc00002be6000000066502b0e6%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0',
    'Referer': 'https://movie.douban.com/typerank?type_name=%E6%AD%8C%E8%88%9E&type=7&interval_id=100:90&action=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'type': '7',
    'interval_id': '100:90',
    'action': '',
    'start': '40',
    'limit': '60',
}

response = requests.get('https://movie.douban.com/j/chart/top_list',
                        params=params, headers=headers)

with open('list.json', 'w', encoding='utf-8') as f:
    f.write(response.text)
