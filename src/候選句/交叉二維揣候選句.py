from 剖析相關工具.剖析結構化工具 import 剖析結構化工具
from 剖析相關工具.剖析結構化工具 import 國閩單位翻譯
from 剖析相關工具.剖析工具 import 剖析工具
from 言語資料庫.公用資料 import 資料庫連線

class 交叉二維揣候選句:
	def __init__(self):
# 		self.揣剖析資料 = 資料庫連線.prepare('SELECT ' +
# 			'"甲"."流水號","丁"."流水號","甲"."型體","甲"."音標","乙"."型體","丁"."型體","丁"."音標"' +
# 			'FROM "言語"."文字" AS "甲","言語"."斷詞暫時表" AS "乙","言語"."關係" AS "丙",' +
# 			'"言語"."文字" AS "丁" ' +
# 			'WHERE "甲"."流水號"="乙"."斷詞目標流水號" AND' +
# 			'"甲"."流水號"="丙"."乙流水號" AND "丙"."關係性質"=\'會當替換\' AND ' +
# 			'"丁"."流水號"="丙"."甲流水號" ' +
# 			'ORDER BY "甲"."流水號" DESC ' +
# 			'LIMIT 10000')()
		self.揣剖析資料 = 資料庫連線.prepare('SELECT DISTINCT ' +
			'"甲"."流水號","甲"."型體","甲"."音標","乙"."型體","丁"."型體","丁"."音標"' +
			'FROM "言語"."文字" AS "甲","言語"."斷詞暫時表" AS "乙","言語"."關係" AS "丙",' +
			'"言語"."文字" AS "丁" ' +
			'WHERE "甲"."流水號"="乙"."斷詞目標流水號" AND' +
			'"甲"."流水號"="丙"."乙流水號" AND "丙"."關係性質"=\'會當替換\' AND ' +
			'"丁"."流水號"="丙"."甲流水號" ' +
			'ORDER BY "甲"."流水號" DESC ' +
			'LIMIT 100000')()
		self.揣對應資料 =lambda 流水號: 資料庫連線.prepare('SELECT DISTINCT ' +
			'"丁"."流水號","丁"."型體","丁"."音標" ' +
			'FROM "言語"."關係" AS "丙",' +
			'"言語"."文字" AS "丁" ' +
			'WHERE ' +
			'"丙"."乙流水號"=$1 AND "丙"."關係性質"=\'會當替換\' AND ' +
			'"丁"."流水號"="丙"."甲流水號" ' +
			'ORDER BY "丁"."流水號" DESC ' +
			'LIMIT 100000')(流水號)
# 		print(self.揣剖析資料)
	def 相似比較(self, 待翻句, 候選句, 評分函式):
		無合分數=-1000
		相關分數矩陣=[[0]*len(候選句)]
		相關分數矩陣[0][0]=0
		for 待翻 in 待翻句[1:]:
			相關分數陣列=[無合分數]
			for 候選 in 候選句[1:]:
				if type(待翻)==type(候選):
					if isinstance(待翻, list):
						分數,*排法=self.相似比較(待翻,候選,評分函式)
						相關分數陣列.append(分數)
					elif isinstance(待翻, tuple):
						相關分數陣列.append(評分函式(待翻,候選))
					else:
						print(待翻,end=' ')
						print(候選,end=' ')
						print('有問題')
						相關分數陣列.append(無合分數)
				else:
					相關分數陣列.append(無合分數)
			相關分數矩陣.append(相關分數陣列)
		累積分數=[[0]*len(候選句)]*len(待翻句)
		頂一个來源=[[0]*len(候選句)]*len(待翻句)
		for i in range(1,len(待翻句)):
# 			print(相關分數矩陣)
# 			print(累積分數)
# 			print(i)
			累積分數[i][0]=累積分數[i-1][0]+無合分數
			頂一个來源[i][0]=0
			for j in range(1,len(候選句)):
				累積分數[i][j]=累積分數[i-1][j]+無合分數
				頂一个來源[i][j]=0
				if 累積分數[i][j]<累積分數[i][j-1]:
					累積分數[i][j]=累積分數[i][j-1]
				if 累積分數[i][j]<相關分數矩陣[i][j]+累積分數[i-1][j-1]:
					累積分數[i][j]=相關分數矩陣[i][j]+累積分數[i-1][j-1]
					頂一个來源[i][j]=1
		return (累積分數[-1][-1],)
	
	def 相似換新(self, 翻譯句, 候選句, 對應句, 評分函式):
		候選句長度 = len(候選句)
		候選句位置 = 0
		攏總分數 = 1
		無法度直接換 = False
		結果句 = []
		for 一段剖析 in 翻譯句:
			無相仝 = True
			while 無相仝 and 候選句位置 < 候選句長度:
# 				print(一段剖析)
# 				print(type(一段剖析))
				if isinstance(一段剖析, list) and isinstance(候選句[候選句位置], list) and 一段剖析[0] == 候選句[候選句位置][0]:
					結果句.append(self.相似換新(一段剖析, 候選句[候選句位置], 對應句, 評分函式))
					無相仝 = False
				elif isinstance(一段剖析, tuple) and isinstance(候選句[候選句位置], tuple) and 一段剖析[1] == 候選句[候選句位置][1]:
					攏總分數 += 100
					結果詞 = 國閩單位翻譯(一段剖析)
					對照詞 = 國閩單位翻譯(候選句[候選句位置])
					結果句.append((結果詞, 一段剖析, 對照詞, 候選句[候選句位置],))
					if 一段剖析[0] == 候選句[候選句位置][0]:
						攏總分數 += 100
						print(對照詞, end = '')
						print(" 免變")
						if len(一段剖析) >= 3 and len(候選句[候選句位置]) >= 3 and 一段剖析[2] == 候選句[候選句位置][2]:
							攏總分數 += 100
					else:
						for 對照 in 對照詞[0]:#結果=(字,音）
							if 對照[0] in 對應句:
								print(對照,end=",")
# 							else:
# 								賰的.append(結果)
# 						print(對照詞, end = '')
						print(" ----> ", end = '')
# 						賰的=[]
						print(結果詞)
# 						for 結果 in 結果詞[0]:#結果=(字,音）
# 							if 結果[0] in 對應句:
# 								print(結果,end=",")
# 							else:
# 								賰的.append(結果)
# 						print('|',end='')
# 						print(賰的)
							
					無相仝 = False
				elif isinstance(一段剖析, str):
					結果句.append(一段剖析)
					無相仝 = False
				else:
					print(候選句[候選句位置], end = '')
					print('擲掉')
				候選句位置 += 1
# 				print(攏總分數)
# 			print(無相仝)
			if 無相仝:
				無法度直接換 = True
		if 無法度直接換:
			攏總分數 = -1
			print(候選句, end = '')
			print('規句愛換')
# 				print(一段剖析)
# 				print(候選句位置)
		return 結果句
if __name__ == '__main__':
	def 詞相關評價(甲詞,乙詞):
		分數=0
		if 甲詞[1] ==乙詞[1]:
			分數 += 100
			if 甲詞[0] ==乙詞[0]:
				分數 += 100
			if len(甲詞) >= 3 and len(乙詞) >= 3 and 甲詞[2] ==乙詞[2]:
				分數 += 100
		else:
			分數 -= 100
		return 分數
#  	print(剖析結果字串集)
	結構化工具 = 剖析結構化工具()
	揣候選句工具 = 交叉二維揣候選句()
	翻譯句 = '#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:回家))#，(COMMACATEGORY)'
	翻譯句='#1:1.[0] S(NP(Head:N:我)|Head:Vt:覺得|S(NP(Head:N:我)|Head:Vt:做|ASP:了|NP(DM:一個|V‧的(Vi:假|Head:T:的)|Head:N:作品)))#'
	
	翻譯句結構化結果 = 結構化工具.結構化剖析結果(翻譯句)
	印出 = lambda 型體佮詞性語意:print(型體佮詞性語意[0], end = ' ')
# 	print(國閩單位翻譯(('吃',)))

	for 剖析結果字串 in 揣候選句工具.揣剖析資料:
# 		print(剖析結果字串)
		結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串[3])
		分數=揣候選句工具.相似比較(翻譯句結構化結果[1], 結構化結果[1], 詞相關評價)
		if 分數[0]>0:
			print(翻譯句結構化結果)
			print(結構化結果)
			結構化工具.處理結構化結果(翻譯句結構化結果, 印出)
			print()
			結構化工具.處理結構化結果(結構化結果, 印出)
			print()
			print(分數)
# 			for 對應句 in 揣候選句工具.揣對應資料(剖析結果字串[0]):
# 				print(對應句[1])
# 				print(揣候選句工具.相似換新(翻譯句結構化結果, 結構化結果, 對應句[1], 詞相關評價))


	工具 = 剖析工具()
# 	剖析結果字串集=工具.剖析('我想吃飯，，，我想吃很多飯。假如我也用這種方式旅行。再想到蝴蝶會生滿屋的毛蟲。')
	剖析結果字串集 = ['#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#，(COMMACATEGORY)',
			'#2:1.[0] %()#，(COMMACATEGORY)',
			'#3:1.[0] %()#，(COMMACATEGORY)',
			'#4:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
			'#5:1.[0] S(C:假如|NP(Head:N:我)|ADV:也|PP(Head:P:用|NP(DM:這種|Head:N:方式))|Head:Vi:旅行)#。(PERIODCATEGORY)',
			'#6:1.[0] VP(ADV:再|Head:Vt:想到|NP(S‧的(head:S(NP(Head:N:蝴蝶)|ADV:會|Head:Vt:生|NP(Head:N:滿屋))|Head:T:的)|Head:N:毛蟲))#。(PERIODCATEGORY)',
			'#1:1.[0] VP(evaluation:Dbb:再|Head:VE2:想到|goal:NP(predication:S‧的(head:S(agent:NP(Head:Nab:蝴蝶)|epistemics:Dbaa:會|Head:VC31:生|theme:NP(Head:Na:滿屋))|Head:DE:的)|Head:Nab:毛蟲))#。(PERIODCATEGORY)',
			'#1:1.[0] S(NP(Head:N:我們)|ADV:要|Head:Vi:下班)#，(COMMACATEGORY)',
			'#2:1.[0] S(NP(Head:N:我)|PP(Head:P:和|NP(Head:N:他))|Head:Vt:想|VP(Head:Vi:回家))#，(COMMACATEGORY)',
			'#3:1.[0] S(NP(Head:N:你們)|DM:兩個|Head:Vt:想|VP(Head:Vi:睡覺))#。(PERIODCATEGORY)']
# 	for 剖析結果字串 in 剖析結果字串集:
# # 		print(剖析結果字串)
# 		結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串)
# 		print(翻譯句結構化結果)
# 		print(結構化結果)
# 		結構化工具.處理結構化結果(翻譯句結構化結果,印出)
# 		print()
# 		結構化工具.處理結構化結果(結構化結果,印出)
# 		print()
# 		print(揣候選句工具.相似比較(翻譯句結構化結果,結構化結果,None))
# 		print(揣候選句工具.相似換新(翻譯句結構化結果,結構化結果,'',None))
# # 		翻譯結果=結構化工具.處理結構化結果(結構化結果,國閩單位翻譯)
# # 		print(翻譯結果)
# # 		結構化工具.處理結構化結果(翻譯結果,印出)
# # 		print()
#
#
# # 	結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串集[0])
# # 	結構化工具.處理結構化結果(翻譯句結構化結果,印出)
# # 	print()
# # 	結構化工具.處理結構化結果(結構化結果,印出)
# # 	print()
# # 	print(揣候選句工具.相似比較(翻譯句結構化結果,結構化結果,None))
# # 	print(揣候選句工具.相似換新(翻譯句結構化結果,結構化結果,'我想欲食飯',None))
# #
# # 	print(國閩單位翻譯(['回家']))
