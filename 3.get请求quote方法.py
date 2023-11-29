# _*_ coding : utf-8_*-
# @Time:  14:28
# @AUthor: Mark
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='
headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

# 把周杰伦三个字转成unicode编码
name = urllib.parse.quote('周杰伦')
print(name)


# 请求对象的定制

url = url + name
print(url)
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求 response 响应
response = urllib.request.urlopen(request)

# 获取响应的源码
content = response.read().decode('utf-8')
print(content)
