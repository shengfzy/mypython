from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests, sys, time, random, pickle

"""
类说明: 下载代理服务器及端口列表
Parameters:
    无
Returns:
    无
Modify:
    2019-01-23
"""

class proxies_downloader(object):
    def __init__(self):
        self.server = 'https://www.xicidaili.com/'
        self.target = 'https://www.xicidaili.com/wt/'
        self.urls = []              #存放服务器列表连接
        self.nums = 0               #服务器列表数
        self.ip_list = []           #存放服务器地址及端口号
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
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-13
    """
    
    def get_download_url(self):
        while True:
            try:
                #print(requests.get(url = 'https://icanhazip.com', **self.params).text)
                req = requests.get(url = self.target, **self.params, timeout = 5)
            except Exception as e:
                print('get URLs timesout\n')
                print(str(e))
                self.getParams()
                print(self.params)
                continue
            else:
                html = req.text
                div_bf = BeautifulSoup(html, features = 'html.parser')
                div = div_bf.find_all('div', class_ = 'pagination')
                if div == []:
                    print('return NULL\r')
                    time.sleep(2)
                    self.getParams()
                    print(self.params)
                else:
                    break
        a_bf = BeautifulSoup(str(div[0]), features = 'html.parser')
        a = a_bf.find_all('a')
        self.nums = int(int(a[-2].string))
        for i in range(self.nums):
            self.urls.append(self.server + '/wt/' + str(i + 1) )
    
    """
    函数说明:获取代理服务器内容
    Parameters:
        target -  下载服务器列表连接(string)
    Returns:
        texts - 服务器地址和端口号(string)
    Modify:
        2019-01-22
    """

    def get_proxies(self, target):
        while True:
            try:
                #print(requests.get(url = 'https://icanhazip.com', **self.params).text)
                req = requests.get(url = target, **self.params, timeout = 5)
            except Exception as e:
                print('URL timesout\n')
                print(str(e))
                self.getParams()
                print(self.params)
                continue
            else:
                html = req.text
                bf = BeautifulSoup(html, features = 'html.parser')
                tr = bf.find_all('tr')
                if tr == []:
                    print('return NULL\r')
                    time.sleep(2)
                    self.getParams()
                    print(self.params)    
                else:
                    break
        self.ip_list = []
        for each in tr[1:]:
            tr_bf = BeautifulSoup(str(each), features = 'html.parser')
            td = tr_bf.find_all('td')
            print(td[1].string + ':' + td[2].string + '\r')
            self.ip_list.append(td[1].string + ':' + td[2].string)
        return self.ip_list

if __name__ == '__main__':
    dl = proxies_downloader()
    with open("C:\\Users\\沈恺\\Desktop\\ip_list.pk.bak", 'rb') as f:
        dl.ip_pool = pickle.load(f)
    dl.get_download_url()
    for i in range(dl.nums):
        print('\n -------start new--------- \n')
        ip_list = dl.get_proxies(dl.urls[i]) 
        with open("C:\\Users\\沈恺\\Desktop\\ip_list.pk", 'ab') as f:
            pickle.dump(ip_list, f)
        sys.stdout.write("  已下载:%.3f%%" % float((i + 1) * 100 / dl.nums) + '\r')
        sys.stdout.flush()
        time.sleep(1)
    print('finished\n')
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        