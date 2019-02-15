# -*- coding:UTF-8 -*-

import requests, json, time, sys, random, pickle
from contextlib import closing
from fake_useragent import UserAgent

class get_photos(object):
    
    def __init__(self):
        self.photos_id = []
        self.download_server = 'https://unsplash.com/photos/xxx/download?force=trues'
        self.target = 'http://unsplash.com/napi/feeds/home'
        self.headers = {'authorization':'7ecdcf21a6ae6ccf531cf87265d7f48e5160996'}
        self.params = {}
        self.ip_pool = [
            '119.101.115.7:9999',
            '60.182.165.40:808',
            '222.217.30.110:9999',
            '121.61.3.83:9999',
            '111.181.49.77:9999',
            '119.101.118.197:9999',
        ]
        self.getParams()
        
    """
    函数说明:获取代理服务器
    Parameters:
        无
    Returns:
        params - 返回代理服务器地址、端口号
    Modify:
        2019-01-22
    """
    
    def ip_proxy(self):
        ip = self.ip_pool[random.randrange(0,len(self.ip_pool))]
        proxies = {'https': ip}
        return proxies

    """
    函数说明:获取FakeAgent参数
    Parameters:
        无
    Returns:
        无
    Modify:
        2019-01-22
    """       
    def getParams(self):
        ua = UserAgent()
        self.params = dict(
            headers = {'User-Agent': ua.random},
            proxies = self.ip_proxy()
        )

    """
    函数说明:获取图片ID
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-13
    """ 
    def get_ids(self):
        while True:
            try:
                req = requests.get(url = self.target, verify = False, timeout = 5)
            except Exception as e:
                print(str(e))
                self.getParams()
                print(self.params)
                continue
            else:
                html = json.loads(req.text)
                next_page = html['next_page']
                for each in html['photos']:
                    self.photos_id.append(each['id'])
                time.sleep(1)
                for i in range(5):
                    req = requests.get(url = next_page, headers = self.headers, verify = False)
                    html = json.loads(req.text)
                    print(html)
                    next_page = html['next_page']
                    for each in html['photos']:
                        self.photos_id.append(each['id'])
                    time.sleep(1)
                break
            

    """
    函数说明:图片下载
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-13
    """   
    def download(self, photo_id, filename):
        target = self.download_server.replace('xxx', photo_id)
        with closing(requests.get(url = target, stream = True, verify = False)) as r:
            with open('C:\\Users\\沈恺\\OneDrive\\mypython\\pic\\%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size = 1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()

if __name__ == '__main__':
    gp = get_photos()
    with open("C:\\Users\\沈恺\\Desktop\\ip_list.pk.bak", 'rb') as f:
        gp.ip_pool = pickle.load(f)
    print('获取图片连接中：')
    gp.get_ids()
    print('图片下载中：')
    for i in range(len(gp.photos_id)):
        print('正在下载第%d张图片' % (i+1))
        gp.download(gp.photos_id[i], (i+1))