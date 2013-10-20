
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.解析整理工具.字物件篩仔 import 字物件篩仔

class 動態規劃斷詞標音:
	篩仔 = 字物件篩仔()
	def 字陣列斷詞標音(self, 辭典, 字陣列):
		斷詞結果 = []
		# from multiprocessing import Pool
		for 所在 in range(len(字陣列)):
			斷詞結果.append(辭典.查詞(詞(字陣列[所在:所在 + 辭典.大細])))
		# 分數 頂一个位置 有啥物詞通用
		分數表 = [(0, None, None)] * (len(字陣列) + 1)
		for 所在 in range(len(字陣列)):
			for 斷詞長度 in range(len(斷詞結果[所在])):
				if 斷詞結果[所在][斷詞長度] != set():
					新分數 = 分數表[所在][0] + 1.0 / (斷詞長度 + 1)
					if 新分數 > 分數表[所在 + 斷詞長度 + 1][0]:
						分數表[所在 + 斷詞長度 + 1] = (新分數, 所在, 斷詞結果[所在][斷詞長度])
# 		print(len(字陣列),len(斷詞結果),len(分數表))
		挑出來 = []
		目前所在 = len(字陣列)
		while 目前所在 != None and 目前所在 != 0:
			挑出來.append(分數表[目前所在][2])
			目前所在 = 分數表[目前所在][1]
		集陣列=[]
		for 詞組合 in 挑出來[::-1]:
			組陣列=[] 
			for 詞物件 in 詞組合:
				組陣列.append(組([詞物件]))
			集陣列.append(集(組陣列))
		return 句(集陣列)
	def 章斷詞標音(self, 辭典, 章物件):
		if not isinstance(章物件, 章):
			raise 型態錯誤('傳入來的毋是章物件：{0}'.format(str(章物件)))
		用好句 = []
		for 一句 in 章物件.內底句:
			用好句.append(self.斷詞標音(辭典, 一句))
		return 章(用好句)
	
	# 字詞組集句=>句
	# 章=>章
	def 斷詞標音(self, 辭典, 物件):
		if isinstance(物件, 章):
			return self.章斷詞標音(辭典, 物件)
		字陣列 = self.篩仔.篩出字物件(物件)
		return self.字陣列斷詞標音(辭典, 字陣列)
