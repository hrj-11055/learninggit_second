# _*_ coding : utf-8_*-
# @Time:  19:08
# @Author: Mark

# 使用urllib获取百度搜索结果
import urllib.request
# url = "http://www.baidu.com"
#
# # 模拟浏览器向服务器发送请求 response 响应
# response = urllib.request.urlopen(url)
#
# print(response) # <http.client.HTTPResponse object at 0x0000022A5CB7DEB0>
#
# # 获取响应中的源码
# #content = response.read().decode('utf-8')   # 右键查看源码
# #content = response.readline()  # 读取一行
#
# content = response.readlines() # 读取所有行,放在[]list中
# print(content)
#
# print(response.getcode()) # 获取状态码  200 表示逻辑没错
#
# print(response.geturl())   # 返回url
#
# print("返回响应头:",response.getheaders())    # 返回响应头 一个状态信息


"""
下载网页
下载图片
下载视频
"""
url_page = "https://www.baidu.com"
urllib.request.urlretrieve(url_page, "baidu.html") # 下载网页



url_img = "https://img2.baidu.com/it/u=675987159,1575026508&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=541"
urllib.request.urlretrieve(url_img, "baidu.jpg") # 下载图片

url_video = ("https://s1.hdslb.com/bfs/seed/jinkela/short/leader-election/iframe.html?iframeID=vWEdg0UO13&leaderID=watchlaterpipwindow")

urllib.request.urlretrieve(url_video, "wudao.mp4") # 下载视频

urllib.request.Request()
# https 443
# http 80
# redis 6379


