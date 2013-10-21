
from 標音資料庫工具.揣音標 import 揣言語層的字詞
from 標音資料庫工具.揣音標 import 揣腔口型體資料
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 斷詞標音.型音辭典 import 型音辭典
from 標音資料庫工具.揣音標 import 揣腔口資料
from 斷詞標音.動態規劃斷詞標音 import 動態規劃斷詞標音
from 字詞組集句章.基本元素.公用變數 import 分詞符號
from 字詞組集句章.基本元素.公用變數 import 分字符號

class 標音整合:
	腔口 = '漢語族閩方言閩南語偏漳優勢音'
	文讀層 = '文讀層'
	白話層 = '白話層'
	全部 = '全部'
	初胚工具 = 文章初胚工具()
	分析器 = 拆文分析器()
	辭典 = None
	斷詞標音 = 動態規劃斷詞標音()
	def __init__(self, 腔口):
		self.腔口 = 腔口
		self.文讀字 = set()
		[self.文讀字.add(字詞[0]) for 字詞 in 揣言語層的字詞(self.腔口, '文讀層')]
		self.白話字 = set()
		[self.白話字.add(字詞[0]) for 字詞 in 揣言語層的字詞(self.腔口, '白話層')]
		self.辭典 = 型音辭典(4)
		音標工具 = 臺灣閩南語羅馬字拼音
		for 流水號, 型體, 音標 in 揣腔口資料(腔口):
			處理過的音標 = self.初胚工具.建立物件語句前處理減號(音標工具, 音標)
			# 愛加詞組無
			組物件 = self.分析器.產生對齊組(型體, 處理過的音標)
			for 詞物件 in 組物件.內底詞:
				詞物件.屬性 = {}
				if 流水號 in self.文讀字:
					詞物件.屬性['語言層'] = self.文讀層
				elif 流水號 in self.白話字:
					詞物件.屬性['語言層'] = self.白話層
				self.辭典.加詞(詞物件)

# 		print(self.文讀字)
# 	def 標音(self, 台語字, 語言層):
# # 		return self.產生標音結果(台語字, 語言層)
# 		return [選擇[0] for 選擇 in self.產生標音結果(台語字, 語言層)]
	def 產生標音結果(self, 台語字, 語言層):
		章物件 = self.分析器.建立章物件(台語字)
		return self.斷詞標音.斷詞標音(self.辭典, 章物件)

		音標工具 = 臺灣閩南語羅馬字拼音
		字 = self.分析器.拆句做字(台語字)
		標音結果 = []
		i = 0
		while i < len(字):
			for j in range(20, 0, -1):
				if i + j <= len(字):
					腔口型體資料 = 揣腔口型體資料(self.腔口, ''.join(台語字[i:i + j]))
					流水號 = set()
					[流水號.add(字詞[0]) for 字詞 in 腔口型體資料]
					if len(流水號) > 0:
						字詞選擇 = []
						文讀音編號 = 流水號 & self.文讀字
						白話音編號 = 流水號 & self.白話字
						其他音編號 = 流水號 - 文讀音編號 - 白話音編號
# 						字詞登記=set()
						文讀音字詞 = []
						白話音字詞 = []
						其他音字詞 = []
						for 流水號碼, 型體, 音標 in 腔口型體資料:
							處理過的音標 = self.初胚工具.建立物件語句前處理減號(音標工具, 音標)
							字詞資料 = self.分析器.產生對齊組(型體, 處理過的音標)
							if 字詞資料 not in 文讀音字詞 and 字詞資料 not in 白話音字詞:
								if 流水號碼 in 文讀音編號:
									文讀音字詞.append(字詞資料)
# 									字詞登記.add(文讀音字詞[-1])
								elif 流水號碼 in 白話音編號:
									白話音字詞.append(字詞資料)
# 									字詞登記.add(白話音字詞[-1])
						for 流水號碼, 型體, 音標 in 腔口型體資料:
							處理過的音標 = self.初胚工具.建立物件語句前處理減號(音標工具, 音標)
							字詞資料 = self.分析器.產生對齊組(型體, 處理過的音標)
							if 字詞資料 not in 文讀音字詞 and 字詞資料 not in 白話音字詞 and 字詞資料 not in 其他音字詞:
								if 流水號碼 in 其他音編號:
									其他音字詞.append(字詞資料)
# 									字詞登記.add(其他音字詞[-1])
						字詞選擇 = []
						if 語言層 == '文讀層':
							字詞選擇.extend(文讀音字詞)
							字詞選擇.extend(其他音字詞)
						elif 語言層 == '白話層':
							字詞選擇.extend(白話音字詞)
							字詞選擇.extend(其他音字詞)
						elif 語言層 == '全部':
							字詞選擇.extend(白話音字詞)
							字詞選擇.extend(其他音字詞)
							字詞選擇.extend(文讀音字詞)
						else:
							字詞選擇.extend(白話音字詞)
							字詞選擇.extend(其他音字詞)
							字詞選擇.extend(文讀音字詞)
						標音結果.append(集(字詞選擇))
						i += j
						break
			else:
				處理過的音標 = self.初胚工具.建立物件語句前處理減號(音標工具, 音標)
				標音結果.append(self.分析器.建立集物件(字[i]))
				i += 1
		return 句(標音結果)

if __name__ == '__main__':
	標音 = 標音整合('漢語族閩方言閩南語偏漳優勢音')
	音 = 標音.產生標音結果('台語字', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('台語字', 標音.白話層)
	print(音)
	音 = 標音.產生標音結果('台語字', 標音.全部)
	print(音)
	音 = 標音.產生標音結果('白日依山盡', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('點仔膠', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('好好鱟刣甲屎那流。', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('好好鱟刣甲屎那流,', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('好好鱟,刣甲屎那流', 標音.白話層)
	print(音)

