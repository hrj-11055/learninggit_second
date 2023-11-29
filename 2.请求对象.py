# _*_ coding : utf-8_*-
# @Time:  14:11
# @AUthor: Mark

import urllib.request

url = 'https://www.baidu.com/'

"""
组成部分:
1.协议  http https
2.主机名 www.baidu.com
3.端口  80/443
4.路径  s(search)
5.查询字符串 /参数  ?wd=python
"""
headers = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

response = urllib.request.urlopen(url,headers=headers)
content = response.read().decode('utf-8')
print(content)


