import urllib.request

# url = 'https://www.baidu.com/'
# 获取url返回
# response = urllib.request.urlopen(url)
# print(response)
# 获取url内容即网页html
# content = response.read().decode('UTF-8')
# print(content)
# with open('response.txt', 'w') as f:
#     f.write(content)
# 下载网页
# urllib.request.urlretrieve(url,'baidu.html')
# 下载图片
urlImg = 'https://img2.baidu.com/it/u=2343578558,1542939701&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=666'
urllib.request.urlretrieve(url=urlImg,filename='zhaojinmai.jpg')