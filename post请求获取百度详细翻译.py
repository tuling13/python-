import urllib.request
import urllib.parse
import json

# 正则表达式自动加引号 ctrl + R 上面输入(.*?): (.*) 下面输入'$1':'$2', 上面勾中CC和正则表达式

url = 'https://fanyi.baidu.com/v2transapi'
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': 'de13fbc0c93e1098bf466d6bf1a04ae3',
    'domain': 'common',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36 Edg/111.0.1661.44 ',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Acs-Token': '1679556393593_1679556689638_kaCB1Yqf6D8zAhON4GgK12gxxERaMTzd+Xo45F2X94MySoLb3KeExgJTW2//TTYsXbrXaRmkXxfH/IPuw1jNIXUxkXUmeAJbV6rPFBGcJpjIu+7aBH9Ny0u16z2Cqx6WhrrSOM2wGraI1xYR39vdfPoFFD70TVmBIlAEyEvlqTj9zpbyllx6s6D7o4FdUbIgBAECYtxRWszoBFzCat0xKoXHsnfwKzWvOxXmlfYCLe6ekhWs8WmbK7YfM/aAoQgo+eIAd6xfIgSLAepCaxAZrvHanJH9Rmk6u3zEs89jx4Ctb1cUnVi0dHDj9M5su9KsNDF+znXgOiEPyGgXrOeNe8Ji6ZPT3d10cbtHfEleb0Q+mMp5bRtj5VJ8i3NAj4+C',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'PSTM=1661612003; BDUSS=UIySGs2RS1OWFMxdXlOb0dscjRidEFudn5VVlpYeWZEZUo2c05NT3AtUy11MnhqSVFBQUFBJCQAAAAAAAAAAAEAAADb7W6YycHGwbXE1fy-yNXfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL4uRWO-LkVjR; BDUSS_BFESS=UIySGs2RS1OWFMxdXlOb0dscjRidEFudn5VVlpYeWZEZUo2c05NT3AtUy11MnhqSVFBQUFBJCQAAAAAAAAAAAEAAADb7W6YycHGwbXE1fy-yNXfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL4uRWO-LkVjR; BAIDUID=9D4CDE21724528757A51EDBF6542DF8B:SL=0:NR=10:FG=1; BIDUPSID=C192D8EB0F06B0D280CC2C7E938A7779; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-158%3A; BAIDUID_BFESS=9D4CDE21724528757A51EDBF6542DF8B:SL=0:NR=10:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1679552481; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1679552481; APPGUIDE_10_0_2=1; delPer=0; PSINO=5; BA_HECTOR=a5818k8h8l818k0l2lag0h561i1nse61n; ZFY=CqD0vCT2htelbLd922URqPYXy2GhUrCD8rz2zg9HqcA:C; ZD_ENTRY=baidu; ab_sr=1.0.1_MmVhMTFhODFkYTlkODVhYzM4MWY4YmU3OGI2NWMwZjEyZDA3NzQyZDAzODIyNTY1MWU0MzgzODQxNjVhOWNlZDdlNGQ0NjVhNTVjY2Y0M2U3OTA0ZjVlZmFlNWZiN2I3MTE2MTRlYzk3YWJhMDcxN2YzYzBhOWI1YjU0MTY1Yjk3ZmZjN2FhM2M0OTMxMDg4ZTEyOTJlNWFkZDBlMDAxM2RkMDc4Mzc4Y2UxYzZiZjI3ZGIxN2JkNTY0Zjg0YjAy; H_PS_PSSID=38185_36545_38351_38366_38173_38289_38379_37925_38383_26350_37958_22159_38282_37881',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
    'X-Requested-With': 'XMLHttpRequest',
}
data = urllib.parse.urlencode(data).encode('utf-8')
requests = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(requests)
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)
