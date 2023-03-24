import urllib.request
import urllib.parse


def create_request(page):
    url = 'https://movie.douban.com/j/chart/top_list?'
    data = {
        'type': 25,
        'start': (page - 1) * 20,
        'limit': 20,
        'interval_id': '75:65',
    }
    print(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                      'Safari/537.36 Edg/111.0.1661.44 ',
    }
    data = urllib.parse.urlencode(data)
    url = url + data
    print(url)
    requests = urllib.request.Request(url=url, headers=headers)
    return requests


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load_json(page, content):
    with open('豆瓣第' + str(page) + '页.json', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始页码"))
    end_page = int(input("请输入结束页码"))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        if len(content) > 0:
            down_load_json(page, content)
