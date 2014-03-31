/# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import os

class 切音結果佮標仔佮拼準備合成():
	def __init__(self):
		語料路徑='/home/Ihc/research/'
		切音結果路徑 = 語料路徑 + 'mono.final.result.mlf'
		標仔原本路徑=語料路徑+'labels全文/'
		切音標仔路徑=語料路徑+'labels/full/'
		單音標仔路徑=語料路徑+'labels/mono/'
		os.makedirs(切音標仔路徑, exist_ok = True)
	# 	os.chdir(語料路徑+'labe')
		切音結果=open(切音結果路徑)
		if 切音結果.readline().strip()=='#!MLF!#':
			狀態='一開始'
			for 每行 in 切音結果.readlines():
				每行=每行.strip()
				if 狀態=='一開始':
					音檔名=每行
					切音標籤=[]
					狀態='切音資料'
				elif 狀態=='切音資料':
					if 每行=='.':
						音檔碼=音檔名.split('.')[0][3:]+'.lab'
	# 					print(音檔碼)
						合成標籤=list(open(標仔原本路徑+音檔碼))
# 						if 模式=='愛聲調':
# 							合成標籤=['sil']+合成標籤+['sil']
	# 					print(len(切音標籤))
	# 					print(len(合成標籤))
# 						print((切音標籤))
# 						print((合成標籤))
						if len(切音標籤)!=len(合成標籤):
							print(音檔碼+'長度對袂齊')
						單音標仔=open(
							單音標仔路徑+音檔名.split('.')[0][3:]+
							'.lab','w')
						for i in range(len(切音標籤)):
	# 						print(切音標籤[i].split())
							切音=切音標籤[i].split()
							print(切音[0],切音[1],切音[2],file=單音標仔)
						單音標仔.close()
						合成聲韻標籤檔=open(
							切音標仔路徑+音檔名.split('.')[0][3:]+
							'.lab','w')
						for i in range(len(切音標籤)):
	# 						print(切音標籤[i].split())
							切音=切音標籤[i].split()
							print(切音[0],切音[1],合成標籤[i].strip(),file=合成聲韻標籤檔)
						合成聲韻標籤檔.close()
						狀態='一開始'
					else:
						切音標籤.append(每行)
		else:
			print('檔案揣毋著矣')
	
if __name__ == '__main__':
	切音結果佮標仔佮拼準備合成()
