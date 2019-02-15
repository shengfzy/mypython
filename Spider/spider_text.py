from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests, sys, time, random

"""
类说明:下载《笔趣看》网小说《一念永恒》
Parameters:
    无
Returns:
    无
Modify:
    2019-01-22
"""
class downloader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数
        self.ip_pool = [
                    '119.101.115.7:9999',
                    '60.182.165.40:808',
                    '222.217.30.110:9999',
                    '121.61.3.83:9999',
                    '111.181.49.77:9999',
                    '119.101.118.197:9999',
                    '58.54.139.122:9999'
        ]
        self.getParams()
        
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
                req = requests.get(url = self.target, **self.params, timeout = 5)
            except Exception as e:
                self.getParams()
                print('download URL timesout\n')
                print(str(e))
                continue
            else:
                html = req.text
                div_bf = BeautifulSoup(html, features = 'html.parser')
                div = div_bf.find_all('div', class_ = 'listmain')
                if div == []:
                    print('return NULL\n')
                else:
                    break
        a_bf = BeautifulSoup(str(div[0]),features = 'html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a[15:])
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
            
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
        proxies = {'http': ip}
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
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'},
            proxies = self.ip_proxy()
        )
            
    """
    函数说明:获取章节内容
    Parameters:
        target -  下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2019-01-22
    """

    def get_contents(self, target):
        while True:
            try:  
                req = requests.get(url = target, **self.params, timeout = 5)
            except Exception as e:
                print('URL timeout\n')
                print(e)
                self.getParams()
                print(self.params)
                continue
            else:    
                html = req.text
                bf = BeautifulSoup(html, features = 'html.parser')
                texts = bf.find_all('div', class_ = 'showtxt')
                if texts == []:
                    time.sleep(2)
                    self.getParams()
                    print(self.params)
                else:
                    break
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts
        

    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2019-01-22
    """

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding = 'utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
       
if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print("开始下载:\n")
    for i in range(dl.nums):
        print('\n -------start new--------- \n')
        dl.writer(dl.names[i], "C:\\Users\\沈恺\\Desktop\\一念永恒.txt", dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float((i + 1) * 100 / dl.nums) + '\r')
        sys.stdout.flush()
        time.sleep(1)
    print("下载完成")