
from http.server import HTTPServer
from 服務架設.連線控制器 import 連線控制器
from 資料庫.欄位資訊 import 偏漳優勢音腔口
from 斷詞標音.自動標音 import 自動標音

class 語音合成服務(連線控制器):
	標音工具 = 自動標音()
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
			章物件=self.標音工具.標音(查詢腔口, 查詢語句)
# 			self.輸出(self.標音工具.標音(查詢腔口, 查詢語句))
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
