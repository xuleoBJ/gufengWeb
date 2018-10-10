import time
import re
import os

def outPinglun(strSpaName,bot, contact):
	filePath =  os.path.join("D:\qqRotQA\pinglun",strSpaName+".txt")
	fileOpened=open(filePath,'r')
	for sLine in fileOpened.readlines():
		if sLine.strip() !="":
			bot.SendTo(contact, sLine)
	return True

def onQQMessage(bot, contact, member, content):
	##请问 格式 请问+空格+内容
	strContent = content
	if content.strip()!="" and strContent.startswith('请问') :
		answer  = False
		if	len(content.strip().split())>=2:
			strContent = content.split()[1].strip()
			## 咨询有区域店	
			if strContent in '望京有吗？':
				bot.SendTo(contact, '青丘，玉颜堂，谧享')
				answer  = True
			if strContent in '大屯路有吗？':
				bot.SendTo(contact, '御殿，花涧溪')
				answer  = True
			if strContent in '海淀有吗？':
				bot.SendTo(contact, '樱木子，御仙阁，舞丝阁')
				answer  = True
			if strContent in '10号线有吗？':
				bot.SendTo(contact, '太阳宫揽月阁，宜生堂，双井蜜桃会')
				answer  = True
			if strContent in '望京有吗？':
				bot.SendTo(contact, '有青丘，玉颜堂，谧享')
				answer  = True
			if strContent in '通州有吗？':
				bot.SendTo(contact, '君悦')
				answer  = True
			if strContent in '南边有吗？':
				bot.SendTo(contact, '旧宫丝云阁，流翠轩')	
				answer  = True
			if strContent in '西边有吗？':
				bot.SendTo(contact, '御仙阁，樱沐子')	
				answer  = True
				
			## 咨询有区域店的位置	
			if strContent in '君悦在哪里?':
				bot.SendTo(contact, '朝阳双桥')
				answer  = True
			if strContent in '玉颜堂在哪里?':
				bot.SendTo(contact, '望京南地铁A口')
				answer  = True
			if strContent in '90主题在哪里?':
				bot.SendTo(contact, '马连道')
				answer  = True
			if strContent in '宜生堂在哪?':
				bot.SendTo(contact, '太阳宫')
				answer  = True
			if strContent in '舞丝阁在哪里?':
				bot.SendTo(contact, '宇宙中心五道口')
				answer  = True
			if strContent in '樱沐子在哪里?':
				bot.SendTo(contact, '魏公村附近')
				answer  = True
			if strContent in '谧享在哪里?':
				bot.SendTo(contact, '望京东湖渠')
				answer  = True
			if strContent in '青丘在哪里?':
				bot.SendTo(contact, '望京南')
				answer  = True
			if strContent in '百媚在哪里?':
				bot.SendTo(contact, '北苑')
				answer  = True
			
			#分类评价
			if strContent in {'大尺有哪几家？','大尺哪几家？','大尺有哪几家？','有哪些大尺店?'} or '大尺有哪' in strContent:
				bot.SendTo(contact, '旧宫丝云，流翠轩，90主题，青塔LL')
				answer  = True
			if strContent in {'小尺有哪几家？','小尺哪几家？','有哪些小尺店?'} or '小尺有哪' in strContent:
				bot.SendTo(contact, '谧享，君悦，宜生堂')
				answer  = True
			if strContent in {'中尺有哪几家？','中尺哪几家？','有哪些中尺店?'} or '中尺有哪' in strContent:
				bot.SendTo(contact, '除了小尺大尺就是中尺')
				answer  = True
			if strContent in '哪个胸大颜值高服务好?':
				bot.SendTo(contact, 'sorry, 这个问题我还没想好')
				answer  = True
			if strContent in '哪个老妹儿活儿好':
				bot.SendTo(contact, 'sorry, 我知道，但是我不敢说，怕被友商客服骂死：)')
				answer  = True
			if strContent in '丝足哪家强':
				bot.SendTo(contact, '玉颜堂有妞腿很长')
				answer  = True
			if strContent in '新友商是哪几家？':
				bot.SendTo(contact, '玉颜堂，樱木子，舞丝阁')
				answer  = True
			if strContent in {'友商谁家按摩最好','谁家按摩好'}:
				bot.SendTo(contact, '宜生堂')
				answer  = True
				
			##各店点评
			if strContent in '谧享的特色是啥？':
				bot.SendTo(contact, '水床AV')
				answer  = True
			if strContent in '君悦的特色是啥？':
				bot.SendTo(contact, '1 极致小尺享受 2 花式诱惑欲罢不能 3 手冰火特色十足 ')
				answer  = True
			if strContent in '百媚的特色是啥？':
				bot.SendTo(contact, '1 角色扮演 2 定制制服 3 诱惑舞蹈 4 安全性好，可开发票。 ')
				answer  = True
			if strContent in '宜生堂的特色是啥？':
				bot.SendTo(contact, '男士养生好店，环境卫生极好，客服非常用心，三起三落的高端养生项目值得体验，好评率100%。 ')
				answer  = True
			if strContent in '花涧溪的特色是啥？':
				bot.SendTo(contact, '态度极好，妩媚妖娆 ')
				answer  = True
			if strContent in '90后主题的特色是啥？':
				bot.SendTo(contact, '1 安全性非常好 2 技师主打90后 3 态度好，服务标准化，浴室的服务有特色。 ')
				answer  = True
			if strContent in '御殿的特色是啥？':
				bot.SendTo(contact, '环境非常好，非常好 ')
				answer  = True
			if strContent in '玉颜堂的特色是啥？':
				bot.SendTo(contact, '有美人兮， 见之不忘。一日不见兮，思之如狂。 ')
				answer  = True
			if strContent in '御盛阁的特色是啥？':
				bot.SendTo(contact, '思悠悠，恨悠悠， 恨到归时方始休，月明人倚楼。 ')
				answer  = True
			if strContent in '蜜桃会的哪个美女做饭好吃':
				bot.SendTo(contact, '客服爱做饭，做饭也好吃')
			if strContent in {'搞活动的是哪几家?','搞活动的是哪家?'}:
				bot.SendTo(contact, '玉颜堂')
				bot.SendTo(contact, '君悦')
				answer  = True
		if answer == False :
			bot.SendTo(contact, '抱歉，您的问题和答案暂时没有收录。')
		
	if content.strip()!="" and strContent.startswith('评论') :
		answer  = False
		if	len(content.strip().split())>=2:
			strContent = content.split()[1].strip()		
			if strContent in '君悦':
				strSpaName = '君悦'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '青丘':
				strSpaName = '青丘'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '花涧溪':
				strSpaName = '花涧溪'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '蜜桃会':
				strSpaName = '蜜桃会'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '玉颜堂':
				strSpaName = '玉颜堂'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '御殿':
				strSpaName = '御殿'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '揽月阁':
				strSpaName = '揽月阁'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '宜生堂':
				strSpaName = '宜生堂'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '百媚':
				strSpaName = '百媚'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '舞丝阁':
				strSpaName = '舞丝阁'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '90后主题':
				strSpaName = '90后'
				answer  = outPinglun(strSpaName,bot, contact)
			if strContent in '谧享spa':
				strSpaName = '谧享'
				answer  = outPinglun(strSpaName,bot, contact)
		if answer == False :
			bot.SendTo(contact, '抱歉，该会所评论暂时没有收录。')
	##查号	查号+空格+内容
	if strContent.startswith('查号')  :
		linesplit=strContent.split()
		if len(linesplit)==2:
			qqName = linesplit[0]
			qqNum = linesplit[1]
			filePath = "D:\qqRotQA\chahao\qqInfor.txt"
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
			else:
				bot.SendTo(contact, '查询结果：'+qqNum +" 不在小分队")
	##其它有趣			
	if strContent!="" :
		if strContent in {'帮助','help','问答'}:
			bot.SendTo(contact, '句型1 请问+空格+区域（地铁）有吗，例如 1 请问 望京有吗？ 2 请问 10号线有吗？')
			bot.SendTo(contact, '句型2 请问+空格+店名的特色，例如 1 请问 君悦的特色 2 宜生堂的特色')
			bot.SendTo(contact, '句型3 请问+空格+店名在哪里，例如 1 请问 青丘在哪里 2 舞丝阁在哪里')
			bot.SendTo(contact, '句型4 评论+空格+店名，例如 1 评论 青丘 2 评论 百媚')
		if strContent in '雪哥最爱':
			bot.SendTo(contact, '君悦冉冉')
		if strContent == '君悦的婷婷怎么样？':
			bot.SendTo(contact, '人美，腿长，不上钟')
		if strContent in '奈何评论':
			bot.SendTo(contact, '小分队最浪的人，最，没有之一。')
		if strContent in '孤风评论':
			bot.SendTo(contact, '怂货一枚！大家多担待！')
			bot.SendTo(contact, '欢迎您')
		if strContent in '当前时间':
			localtime = time.strftime("%Y-%m-%d-%H:%M")
			bot.SendTo(contact, "当前时间："+localtime)
		if strContent in '群的网址是什么':
			bot.SendTo(contact, 'www.gufengBJ.com')

	