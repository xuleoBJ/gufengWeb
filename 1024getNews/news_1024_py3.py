import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

proxyDic = dict(http='socks5://127.0.0.1:1080',https='127.0.0.1:1080')

fileWrited=open("new.txt",'w',encoding="utf8")

pageStrUrl = 'https://t66y.com/htm_data/7/1802/3008617.html'
page  = requests.get(pageStrUrl,headers = headers,proxies = proxyDic)

soup = BeautifulSoup(page.content,'html.parser') # 按照html格式解析页面
print(soup.title)
inforGet =  soup.findAll("div", {"class":'tpc_content do_not_catch'})
soupNewHtml = BeautifulSoup(str(inforGet[0]), 'html.parser')
fileWrited.write(str(soupNewHtml.prettify()))
print (soupNewHtml.prettify())



fileWrited.close()
