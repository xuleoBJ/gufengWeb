import time
import re
import os
import random

def outPinglun(strSpaName,bot, contact):
	for root, dirs, files in os.walk("D:\qqRotQA\pinglun"): 
		for curFile in files:  
			if strSpaName in curFile:  
				filePath =  os.path.join("D:\qqRotQA\pinglun",curFile)
				fileOpened=open(filePath,'r')
				for sLine in fileOpened.readlines():
					if sLine.strip() !="":
						bot.SendTo(contact, sLine)
				return True
	else:
		return False

def outKeyWord(strKeyword,bot, contact):
	filePath =  os.path.join("D:\qqRotQA","关键词.txt")
	listStrSpa =[]
	fileOpened=open(filePath,'r')
	for sLine in fileOpened.readlines():
		if sLine.strip() !="":
			splitWord = sLine.split()
			strSpaName = splitWord[0]
			if strKeyword in sLine:
				listStrSpa.append(strSpaName)
	if len(listStrSpa)>=1:
		bot.SendTo(contact, '  '.join(listStrSpa))
	else:
		bot.SendTo(contact, '抱歉，您的问题和答案暂时没有收录，我们将及时收录。可以访问我们的网站 http://www.gufengBJ.com')
	return True

def whereisSpaName(strSpaName,bot, contact):
	filePath =  os.path.join("D:\qqRotQA","在哪.txt")
	listStrSpa =[]
	fileOpened=open(filePath,'r')
	for sLine in fileOpened.readlines():
		if sLine.strip() !="":
			if strSpaName in sLine:
				bot.SendTo(contact, sLine)
				return True

	return False


def onQQMessage(bot, contact, member, content):
	##请问 格式 请问+空格+关键词 
	strContent = content
	if strContent.strip()!="" and ( strContent.endswith('有吗') or strContent.endswith('附近') ):
		answer  = False
		if	len(content.strip().split())>=2:
			strKeyWord = content.split()[0].strip()	
			outKeyWord(strKeyWord,bot, contact)
	
	if strContent.strip()!="" and (  strContent.startswith('附近') or strContent.startswith('有吗') or strContent.startswith('请问')  ) :
		answer  = False
		if	len(content.strip().split())>=2:
			strKeyWord = content.split()[1].strip()
			outKeyWord(strKeyWord,bot, contact)
   
   	##各店位置
	if strContent.strip()!="" and (strContent.startswith('在哪') or strContent.startswith('在哪里')  or strContent.endswith('在哪里')  or strContent.endswith('在哪') ) :
		if	len(content.strip().split())>=2:
			strSpaName = content.split()[1].strip()
			if strContent.endswith('在哪里') or  strContent.endswith('在哪') :
				strSpaName = content.split()[0].strip()
			if whereisSpaName(strSpaName,bot, contact)== False:
				bot.SendTo(contact, '抱歉，您的问题和答案暂时没有收录，我们将及时收录。可以访问我们的网站 http://www.gufengBJ.com')


	# if strContent.strip()!="" and (strContent.startswith('在哪') or strContent.startswith('在哪里')  or strContent.endswith('在哪里')  or strContent.endswith('在哪') ) :
	# 	answer  = False
	# 	if	len(content.strip().split())>=2:
	# 		strSpaName = content.split()[1].strip()
	# 		if strContent.endswith('在哪里') or  strContent.endswith('在哪') :
	# 			strSpaName = content.split()[0].strip()
	# 		if strSpaName in '君悦':
	# 			bot.SendTo(contact, '通州双桥 ')
	# 			answer  = True
	# 		if strSpaName in '谧享？':
	# 			bot.SendTo(contact, '望京东湖渠')
	# 			answer  = True
	# 		if strSpaName in '百媚':
	# 			bot.SendTo(contact, '北苑 ')
	# 			answer  = True
	# 		if strSpaName in '宜生堂':
	# 			bot.SendTo(contact, '太阳宫 ')
	# 			answer  = True
	# 		if strSpaName in '花涧溪':
	# 			bot.SendTo(contact, '大屯路')
	# 			answer  = True
	# 		if strSpaName in '90后主题':
	# 			bot.SendTo(contact, '西城马连道 ')
	# 			answer  = True
	# 		if strSpaName in '御殿':
	# 			bot.SendTo(contact, '大屯路 ')
	# 			answer  = True
	# 		if strSpaName in '玉颜堂':
	# 			bot.SendTo(contact, '望京南地铁A口 ')
	# 			answer  = True
	# 		if strSpaName in '御盛阁':
	# 			bot.SendTo(contact, '西城月坛 ')
	# 			answer  = True
	# 		if strSpaName in '御仙阁':
	# 			bot.SendTo(contact, '紫竹桥 ')
	# 			answer  = True
	# 		if strSpaName in '樱沐子':
	# 			bot.SendTo(contact, '魏公村 ')
	# 			answer  = True
	# 		if strSpaName in '蜜桃会':
	# 			bot.SendTo(contact, '双井 ')
	# 			answer  = True
	# 		if strSpaName in '舞丝阁':
	# 			bot.SendTo(contact, '五道口')
	# 			answer  = True
	# 		if strSpaName in '青丘':
	# 			bot.SendTo(contact, '望京南')
	# 			answer  = True
	# 		if strSpaName in '忆江南':
	# 			bot.SendTo(contact, '北苑')
	# 			answer  = True
	# 	if answer == False :
	# 		bot.SendTo(contact, '抱歉，您的问题和答案暂时没有收录。可以访问我们的网站 http://www.gufengBJ.com ')
			
	##各店点评
	if strContent.strip()!="" and (strContent.startswith('特色') or strContent.endswith('特色')  ) :
		answer  = False
		if	len(strContent.strip().split())>=2:
			strSpaName = strContent.split()[1].strip()
			if strContent.endswith('特色') :
				strSpaName = content.split()[0].strip()
			if strSpaName in '君悦':
				bot.SendTo(contact, '1 极致小尺享受 2 花式诱惑欲罢不能 3 手冰火特色十足 ')
				answer  = True
			if strSpaName in '谧享？':
				bot.SendTo(contact, '水床AV')
				answer  = True
			if strSpaName in '百媚':
				bot.SendTo(contact, '1 角色扮演 2 定制制服 3 诱惑舞蹈 4 安全性好，可开发票。 ')
				answer  = True
			if strSpaName in '宜生堂':
				bot.SendTo(contact, '男士养生好店，环境卫生极好，客服非常用心，三起三落的高端养生项目值得体验，好评率100%。 ')
				answer  = True
			if strSpaName in '花涧溪':
				bot.SendTo(contact, '态度极好，妩媚妖娆 ')
				answer  = True
			if strSpaName in '90后主题':
				bot.SendTo(contact, '1 安全性非常好 2 技师主打90后 3 态度好，服务标准化，浴室的服务有特色。 ')
				answer  = True
			if strSpaName in '御殿？':
				bot.SendTo(contact, '环境非常好，非常好 ')
				answer  = True
			if strSpaName in '玉颜堂？':
				bot.SendTo(contact, '有美人兮， 见之不忘。一日不见兮，思之如狂。 ')
				answer  = True
			if strSpaName in '御盛阁？':
				bot.SendTo(contact, '思悠悠，恨悠悠， 恨到归时方始休，月明人倚楼。 ')
				answer  = True
			if strSpaName in '青塔':
				bot.SendTo(contact, '双飞物美价优配合好， ')
				answer  = True
		if answer == False :
			bot.SendTo(contact, '抱歉，您的问题和答案暂时没有收录。')

	
	##查号	评论	
	if strContent.strip()!="" and (strContent.startswith('评论') or strContent.startswith('评价')):
		answer  = False
		if	len(content.strip().split())>=2:
			strSpaName = content.split()[1].strip()		
			answer  = outPinglun(strSpaName,bot, contact)
		if answer == False :
			bot.SendTo(contact, '抱歉，该会所评论暂时没有收录。')
	##查号	查号+空格+内容
	if strContent.startswith('查号')  :
		linesplit=strContent.split()
		if len(linesplit)==2:
			qqName = linesplit[0]
			qqNum = linesplit[1]
			filePath = "D:\\qqRotQA\\chahao\\qqInfor.txt"
			listLine=[]
			searchYes = False
			fileOpened=open(filePath,'r')
			for sLine in fileOpened.readlines():
				splitLine=sLine.split()
				if len(splitLine) >= 2 and splitLine[1]==qqNum:
					qqName =  splitLine[0]
					searchYes = True
					break
			if searchYes == True:
				bot.SendTo(contact,'查询结果：'+ qqNum +' 是小分队成员，网名: '+ qqName)
			
			if searchYes == False:
				filePath = "D:\\qqRotQA\\chahao\\blackName.txt"
				fileOpened=open(filePath,'r')
				for sLine in fileOpened.readlines():
					splitLine=sLine.split()
					if qqNum in  sLine:
						bot.SendTo(contact,'查询结果：'+sLine)
						searchYes = True
						break
			if searchYes == False:
				bot.SendTo(contact,strContent+  ' 没有查到相关信息。')
	##其它有趣			
	if strContent!="" :
		if strContent in {'帮助','help','问答'}:
			bot.SendTo(contact, '输入 问答 或者 帮助 查看句型引导')
			bot.SendTo(contact, '句型1 有吗+空格+关键词，请问+空格+关键词 例如 1 有吗 望京 2 请问 5号线')
			bot.SendTo(contact, '句型2 特色+空格+店名，例如 1 特色 君悦 2 特色 宜生堂')
			bot.SendTo(contact, '句型3 在哪里+空格+店名，例如 1 在哪里 青丘 2 在哪里 舞丝阁')
			bot.SendTo(contact, '句型4 评论+空格+店名，例如 1 评论 玉颜堂 2 评论 百媚')
			bot.SendTo(contact, '句型5 附近+空格+位置，例如 1 亚运村 附近 2 10号线 附近')
			return 


		if strContent in '讲个笑话':
			filePath = os.path.join("D:\\qqRotQA\\xiaohua", "笑话.txt")
			fileOpened=open(filePath,'r')
			lineList = []
			for sLine in fileOpened.readlines():
				if sLine.strip() !="":
					lineList.append(sLine)
			iNum = random.randint(0,len(lineList))
			bot.SendTo(contact, lineList[iNum])
		if strContent in '讲个成人笑话':
			filePath = os.path.join("D:\\qqRotQA\\xiaohua", "成人笑话.txt")
			fileOpened=open(filePath,'r')
			lineList = []
			for sLine in fileOpened.readlines():
				if sLine.strip() !="":
					lineList.append(sLine)
			iNum = random.randint(0,len(lineList))
			bot.SendTo(contact, lineList[iNum])
		if strContent in '喝点鸡汤':
			filePath = os.path.join("D:\\qqRotQA\\xiaohua", "鸡汤.txt")
			fileOpened=open(filePath,'r')
			lineList = []
			for sLine in fileOpened.readlines():
				if sLine.strip() !="":
					lineList.append(sLine)
			iNum = random.randint(0,len(lineList))
			bot.SendTo(contact, lineList[iNum])
		if strContent in '雪哥最爱':
			bot.SendTo(contact, '君悦冉冉')
		if strContent == '君悦的婷婷怎么样？':
			bot.SendTo(contact, '人美，腿长，不上钟')
		if strContent in '奈何评论':
			bot.SendTo(contact, '小分队最浪的人，最，没有之一。')
		if strContent in '孤风评论':
			bot.SendTo(contact, '怂货一枚！大家多担待！')
		if strContent in '当前时间':
			localtime = time.strftime("%Y-%m-%d-%H:%M")
			bot.SendTo(contact, "当前时间："+localtime)
		if strContent in '群的网址' or strContent in '群的网站':
			bot.SendTo(contact, 'htt://www.gufengBJ.com')
		if strContent in {'搞活动的是哪几家?','搞活动的是哪家?'}:
			bot.SendTo(contact, '玉颜堂')
			bot.SendTo(contact, '君悦')
		if strContent in '蜜桃会的哪个美女做饭好吃':
			bot.SendTo(contact, '客服爱做饭，做饭也好吃')


	
