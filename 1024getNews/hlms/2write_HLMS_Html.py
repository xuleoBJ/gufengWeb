import sys,os
import codecs 
if __name__=='__main__':
    sourceDirPath="hlms1"
    fileNames=os.listdir(sourceDirPath)
    for filename in fileNames:

        f = open(sourceDirPath+"//"+filename, "r")
        content = f.read().replace("????","    ")
        f.close()
        #contentGbk= codecs.encode(content, encoding='gbk', errors='ignore')
        title = filename.replace(".txt","")
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
                                        <div class="navbar navbar-default" role="navigation">
                                                <div class="navbar-header">
                                                        <!-- .navbar-toggle样式用于toggle收缩的内容，即nav-collapse collapse样式所在元素 -->
                                                        <button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".navbar-responsive-collapse">
                                                                <span class="sr-only">Toggle Navigation</span>
                                                                <span class="icon-bar"></span>
                                                                <span class="icon-bar"></span>
                                                                <span class="icon-bar"></span>
                                                        </button>
                                                        <!-- 确保无论是宽屏还是窄屏，navbar-brand都显示 -->
                                                        <a href="../红楼遗秘.html" class="navbar-brand">前页</a>
                                                </div>
                                                <!-- 屏幕宽度小于768px时，div.navbar-responsive-collapse容器里的内容都会隐藏，显示icon-bar图标，当点击icon-bar图标时，再展开。屏幕大于768px时，默认显示。 -->
                                                <div class="collapse navbar-collapse navbar-responsive-collapse">
                                                        <ul class="nav navbar-nav">
                                                                <li><a href="../../index.html">首页</a></li>
                                                                <li><a href="../../tiyandianping.html">体验点评</a></li>
                                                                <li><a href="../../youhui.html">优惠活动</a></li>
                                                                <li><a href="../../qqQun.html">私密小群</a></li>
                                                                <li><a href="../../fenxiang.html">精彩分享</a></li>
                                                                <li><a href="../../adultReader.html">文学品读</a></li>
                                                                <li><a href="../../youqingjieda.html">友情解答</a></li>
                                                        </ul>
                                                </div>
                </div>
                <div class="container">
                        <h4>{1}</h4>
                        <br>
                {2}
                </div>

                </body>
                <div style="text-align: center;">
                        <iframe src="../../footer.html" frameborder="0" scrolling="no"></iframe>
                </div>
                </html>
                
        """.format(title,title,content)

        Html_file= open(title+".html",'w')
        Html_file.write(html_str)
        Html_file.close()
