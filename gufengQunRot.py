import time
import re
import os
import random

dataDir = 'E:\\我的坚果云\\qqRotQA'

def outPinglun(strSpaName,bot, contact):
	if str(contact.name) in ['A小分队','B小分队','C小分队','1K乐优美评论区']:
		bot.SendTo(contact, '抱歉，本群暂时不公开评论，请加一风好友私聊评论。注，临时会话一风不响应。')
		return False
	
	for root, dirs, files in os.walk(os.path.join(dataDir,"pinglun")): 
		for curFile in files:  
			if strSpaName in curFile:  
				filePath =  os.path.join(dataDir,"pinglun",curFile)
				fileOpened=open(filePath,'r')
				for sLine in fileOpened.readlines():
					if sLine.strip() !="":
						bot.SendTo(contact, sLine)
				return True
	else:
		bot.SendTo(contact, '抱歉，该会所评论暂时没有收录。')
		return False

def outKeyWord(strKeyword,bot, contact):
	filePath =  os.path.join(dataDir,"关键词.txt")
	listStrSpa =[]
	fileOpened=open(filePath,'r')
	for sLine in fileOpened.readlines():
		if sLine.strip() !="":
			splitWord = sLine.split()
			strSpaName = splitWord[0]
			if (strKeyword in sLine ) and ('##' not in sLine ):
				listStrSpa.append(strSpaName)
	if len(listStrSpa)>=1:
		bot.SendTo(contact, '  '.join(listStrSpa))
	else:
		bot.SendTo(contact, '抱歉，您的问题和答案我们将及时收录。请输入 问答 查看提问句型或者可以访问我们的网站 http://www.gufengBJ.com')
	return True

def whereisSpaName(strSpaName,bot, contact):
	filePath =  os.path.join(dataDir,"在哪.txt")
	fileOpened=open(filePath,'r')
	for sLine in fileOpened.readlines():
		if sLine.strip() !="":
			if strSpaName in sLine:
				bot.SendTo(contact, sLine)
				return True

	return False


def fenbuSpaName(bot, contact):
	filePath =  os.path.join(dataDir,"在哪.txt")
	fileOpened=open(filePath,'r')
	##for sLine in fileOpened.readlines():
	bot.SendTo(contact, ' '.join(fileOpened.readlines()))
	return True

def TeseSpaName(strSpaName,bot, contact):
	filePath =  os.path.join(dataDir,"关键词.txt")
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
	if strContent.strip()!="" and strContent in {'帮助','help','问答'}:
			bot.SendTo(contact, '--输入 问答 或者 帮助 查看句型引导')
			bot.SendTo(contact, '--句型1 有吗+空格+关键词，请问+空格+关键词 例如 1 有吗 望京 2 请问 5号线 3 请问 新友商 4 请问 服务好')
			bot.SendTo(contact, '--句型2 特色+空格+店名，点评+空格+店名 例如 1 特色 君悦 2 点评 宜生堂')
			bot.SendTo(contact, '--句型3 在哪里+空格+店名，附近+空格+位置 例如 1 在哪 青丘 2 在哪 舞丝阁 3  亚运村 附近' )
			bot.SendTo(contact, '--句型4 评论+空格+店名，例如 1 评论 玉颜堂 2 评论 樱沐子')
			bot.SendTo(contact, '--句型5 输入 友商 查询圈内全部友商，输入 请问 新友商 ， 查看新友商')
			return  
	if strContent.strip()!="" and ( strContent.endswith('有吗') or strContent.endswith('附近') ):
		answer  = False
		if	len(content.strip().split())>=2:
			strKeyWord = content.split()[0].strip()	
			outKeyWord(strKeyWord,bot, contact)
	
	
	##关键词
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

	##友商分布
	if strContent.strip()!="" and (strContent.startswith('友商') ) :
		fenbuSpaName(bot, contact)
		return
		
	##点评
	if strContent.strip()!="" and (strContent.startswith('特色') or strContent.startswith('请问') or strContent.startswith('点评') ) :
		if	len(strContent.strip().split())>=2:
			strSpaName = strContent.split()[1].strip()
			if strContent.endswith('特色') :
				strSpaName = content.split()[0].strip()
			if TeseSpaName(strSpaName,bot, contact)== False:
				bot.SendTo(contact, '抱歉，您的问题和答案暂时没有收录，我们将及时收录。可以访问我们的网站 http://www.gufengBJ.com')
		return

	
	##查号	评论	
	if strContent.strip()!="" and (strContent.startswith('评论') or strContent.startswith('评价')):
		answer  = False
		if	len(content.strip().split())>=2:
			strSpaName = content.split()[1].strip()		
			answer  = outPinglun(strSpaName,bot, contact)
		if answer == False :
			pass
			
	##查号	查号+空格+内容
	if strContent.startswith('查号')  :
		qqName = "查号"
		qqNum = strContent.lstrip("查号").strip()
		
		listLine=[]
		searchYes = False

		##搜索黑名单
		if searchYes == False:
			filePath = os.path.join(dataDir,"chahao","blackName.txt")
			fileOpened=open(filePath,'r')
			for sLine in fileOpened.readlines():
				splitLine=sLine.split()
				if qqNum in  sLine:
					bot.SendTo(contact,'查询结果：'+sLine)
					searchYes = True
					break
		##搜索小分队			
		if searchYes == False:
			filePath = os.path.join(dataDir,"chahao","qqInfor.txt")
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
			bot.SendTo(contact,'查询结果：'+strContent+  ' 没有查到相关信息。')
	##其它有趣			
	if strContent!="" :
		if strContent in '讲个笑话':
			filePath = os.path.join(dataDir,"xiaohua", "笑话.txt")
			fileOpened=open(filePath,'r')
			lineList = []
			for sLine in fileOpened.readlines():
				if sLine.strip() !="":
					lineList.append(sLine)
			iNum = random.randint(0,len(lineList))
			bot.SendTo(contact, lineList[iNum])
		if strContent in '讲个成人笑话':
			filePath = os.path.join(dataDir,"xiaohua", "成人笑话.txt")
			fileOpened=open(filePath,'r')
			lineList = []
			for sLine in fileOpened.readlines():
				if sLine.strip() !="":
					lineList.append(sLine)
			iNum = random.randint(0,len(lineList))
			bot.SendTo(contact, lineList[iNum])
		if  '鸡汤' in strContent :
			filePath = os.path.join(dataDir,"xiaohua", "鸡汤.txt")
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
			bot.SendTo(contact, 'http://www.gufengBJ.com')
		if strContent in {'搞活动的是哪几家?','搞活动的是哪家?'}:
			bot.SendTo(contact, '玉颜堂')
			bot.SendTo(contact, '君悦')


	
