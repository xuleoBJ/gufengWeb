title = "你好，世界
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
