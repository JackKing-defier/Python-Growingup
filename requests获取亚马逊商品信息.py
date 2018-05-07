import requests
url = 'https://www.amazon.cn/dp/B075L9T8HF/ref=sr_1_2?s=wireless&ie=UTF8&qid=1525679634&sr=1-2'
kv = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url, headers = kv)
    r.raise_for_status()# 如果状态不是200，引发HTTPError异常
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print('产生异常')
