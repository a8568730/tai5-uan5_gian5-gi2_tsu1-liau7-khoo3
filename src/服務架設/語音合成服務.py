
from http.server import HTTPServer
from 服務架設.連線控制器 import 連線控制器
from 資料庫.欄位資訊 import 偏漳優勢音腔口
from 斷詞標音.自動標音 import 自動標音
from 語音合成.合音檔.句物件轉合成標籤 import 句物件轉合成標籤
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句

class 語音合成服務(連線控制器):
	標音工具 = 自動標音()
	合成標籤工具 = 句物件轉合成標籤()
	def do_GET(self):
		try:
			self.送出連線成功資訊()
			# 共上頭前的「/」提掉
			查詢字串 = self.連線路徑()[1:]
			切開資料 = 查詢字串.split('/', 2)
			查詢腔口 = None
			查詢語句 = None
			集選擇 = []
			if len(切開資料) == 3:
				查詢腔口, 查詢語句, 集選擇字串 = 切開資料
				for 選擇 in 集選擇字串.split(','):
					if 選擇.isdigit():
						集選擇.append(int(選擇))
			if 查詢腔口 not in self.標音工具.支援腔口:
				查詢腔口 = 偏漳優勢音腔口
				查詢語句 = 查詢字串
			章物件=self.標音工具.斷詞標音物件(查詢腔口, 查詢語句)
			所在=0
			集陣列=[]
			for 句物件 in 章物件.內底句:
				for 集物件 in 句物件.內底集:
					if 所在<len(集選擇):
						選擇=集選擇[所在]
					else:
						選擇=0
					if 選擇<len(集物件.內底組):
						組陣列=集物件.內底組[選擇:選擇+1]
					else:
						組陣列=集物件.內底組[:1]
					集陣列.append(集(組陣列))
			self.輸出(self.合成標籤工具.句物件轉標籤(句(集陣列)))
			return
		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)



if __name__ == '__main__':
	try:
		server = HTTPServer(('localhost', 8003), 語音合成服務)
		print ('服務啟動！！')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
