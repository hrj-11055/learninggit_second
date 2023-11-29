# 基本的爬虫使用
# import requests
# res = requests.get('http://www.douban.com')
# print(res.status_code)
# print("Hello,World")

# 出现bug 不懂, 用鼠标点击"run",可以运行,
# 但在终端输入python xx.py 运行不了 显示没有安装requests模块



"""
看尚硅谷的爬虫视频学习
"""

# 一般情况,只能把字符串写入文件中
with open('test.txt', 'w') as file:  # 把'hello,world'字符串写入文件
    file.write('Hello,wolrd')


# 序列化
import json

name_list1 = ['zs', 'ls', 'wangwu']
with open('test.txt', 'w') as file:  # 把python对象 写入文件中
    name = json.dumps(name_list1)
    file.write(name)

with open('test.txt', 'w') as file:
    json.dump(name_list1, file)  # 直接把python对象数据写到文件中

# 反序列化 json >> Python对象
import json
with open('test.txt','r') as file:  # 将test.txt 文件 读取
    content = file.read()   # 用content 表示文件的数据
    print(content)
    print(type(content))

with open('test.txt','r') as file:
    result = json.loads(content)    # 把JSON字符串转成python对象
    print(result)
    print(type(result))


# # load 直接读取文件

with open('test.txt','r') as f:
    result = json.load(f)
    print(result)
    print(type(result))

