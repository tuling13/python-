import urllib.request
import urllib.parse

baseUrl = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36 Edg/111.0.1661.44 '
}
param = urllib.parse.urlencode(data)
newUrl = baseUrl + param
print(newUrl)
request = urllib.request.Request(url=newUrl, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('UTF-8')
with open('content.txt','w', encoding='utf-8') as f:
    f.write(content)