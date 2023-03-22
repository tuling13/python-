import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?ie=UTF-8&wd='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36 Edg/111.0.1661.44 '
}
url = url + urllib.parse.quote('赵今麦')
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('UTF-8')
with open('response.txt', 'w', encoding='utf-8') as f:
    f.write(content)
