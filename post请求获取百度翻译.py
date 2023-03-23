import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': 'User'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36 Edg/111.0.1661.44 '
}
data = urllib.parse.urlencode(data).encode('utf-8')
requests = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(requests)
content = response.read().decode('utf-8')
print(type(content))
# 此处content类型未str 要转成json
obj = json.loads(content)
print(obj)
translate = obj.get('data')
print(translate)
print(type(translate[1]))
