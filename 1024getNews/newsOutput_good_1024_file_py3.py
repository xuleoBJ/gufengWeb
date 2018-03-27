import requests
import os
from bs4 import BeautifulSoup
import sys 

type = sys.getfilesystemencoding()
print(type)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

proxyDic = dict(http='http://10.122.14.79:8787',https='http://10.122.14.79:8787')  ##办公室杜lantern

filePath = os.path.abspath(__file__)
osPath = os.path.split(filePath)[0]
print(filePath)

def writeHtmlPage(title):
	html_str = """
	<!DOCTYPE html>
	<html>
	<head>
		<title>{0}</title>
		<meta http-equiv=Content-Type content="text/html; charset=gb2312">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css">
		<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
		<script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		<!-- Global site tag (gtag.js) - Google Analytics -->
		<script async src="https://www.googletagmanager.com/gtag/js?id=UA-113881659-1"></script>
		<script type="text/javascript" src="globalGF.js"></script>

		<style type="text/css">

		</style>
	</head>
	<body>
	<div class="container">
		<nav class="navbar navbar-default" role="navigation">
			<div>
				<ul class="nav navbar-nav">
					<li class="active"><a href="../fenxiang.html">回上一页</a></li>
			</div>
		</nav>
	</div>
	<div class="container">
		<h4>{1}</h4>
		<br>
	</div>

	</body>
	<div style="text-align: center;">
		<iframe src="../footer.html" frameborder="0" scrolling="no"></iframe>
	</div>
	</html>
	""".format(title,title)

	Html_file= open(title+".html","w")
	Html_file.write(html_str)
	Html_file.close()

def writeHtml(soup):
	soup = BeautifulSoup(page.content,'html.parser') # 按照html格式解析页面
	print(soup.title)
	titleStr = str(soup.title.text).split()[0].replace(' ','')
	writeHtmlPage(titleStr)
	fileWrited=open(titleStr+".txt",'w',encoding="utf8")
	inforGet =  soup.findAll("div", {"class":'tpc_content do_not_catch'})
	soupNewHtml = BeautifulSoup(str(inforGet[0]), 'html.parser')
	fileWrited.write(str(soupNewHtml.prettify()))
	print (soupNewHtml.prettify())
	fileWrited.close()

	
if __name__ == '__main__':
	lineIndex=0

	pageStrUrl = 'http://t66y.com/htm_data/7/1803/3078282.html'
	print(pageStrUrl)
	page  = requests.get(pageStrUrl,headers = headers,proxies = proxyDic)
	print("proxy is OK")
	soup = BeautifulSoup(page.content,'html.parser') # 按照html格式解析页面
	writeHtml(soup)


	
