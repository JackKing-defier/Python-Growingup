import requests
import os
root = 'E://PythonPics//'
url = 'https://www.nationalgeographic.com/content/dam/photography/rights-exempt/best-of-photo-of-the-day/2018/april/01_best-pod-april-18.ngsversion.1525431610985.adapt.768.1.jpg'
path = root + url.split('/')[-1]  # 使用网站中的文件名存到本地

try:
    if not os.path.exists(root):
        os.mkdir(root)

    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已经存在')     
except:
    print('爬取失败')

