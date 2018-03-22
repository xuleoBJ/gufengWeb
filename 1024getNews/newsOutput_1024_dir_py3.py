import requests
import os
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

proxyDic = dict(http='socks5://127.0.0.1:1080',https='127.0.0.1:1080')


def writeHtml(titleStr,inforContent):
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
		{2}
	</div>

	</body>
	<div style="text-align: center;">
		<iframe src="../footer.html" frameborder="0" scrolling="no"></iframe>
	</div>
	</html>
	""".format(titleStr,titleStr,inforContent)

	Html_file= open(titleStr+".html","w")
	Html_file.write(html_str)
	Html_file.close()
	
if __name__ == '__main__':
        fileOpened=open('websites.txt','r')

        lineIndex=0
        for line in fileOpened.readlines():
                pageStrUrl = line
                print(line)
                page  = requests.get(pageStrUrl,headers = headers,proxies = proxyDic)

                soup = BeautifulSoup(page.content,'html.parser') # 按照html格式解析页面
                titleStr = str(soup.title.text).split()[0]
                print(titleStr)
                inforGet =  soup.findAll("div", {"class":'tpc_content do_not_catch'})
                if len(inforGet)>1:
                        inforContent = str(inforGet[0])
                        print (inforContent)
                        writeHtml(titleStr,inforContent)

	
