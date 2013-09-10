import unittest
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器

class 基本元素測試(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()

	def tearDown(self):
		pass

	def test_對齊孤字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		詞 = self.分析器.產生對齊詞([型], [音])
		self.assertEqual(len(詞.內底字), 1)
		self.assertEqual(詞.內底字[0].型, 型)
		self.assertEqual(詞.內底字[0].音, 音)
		self.assertEqual(詞.內底字[-1].型, 型)
		self.assertEqual(詞.內底字[-1].音, 音)

	def test_對齊濟字(self):
		型一 = '媠'
		型二 = '姑'
		型三 = '娘'
		音一 = 'ㄙㄨㄧˋ'
		音二 = 'ㄍㆦ'
		音三 = 'ㄋㄧㄨˊ'
		詞 = self.分析器.產生對齊詞([型一, 型二, 型三], [音一, 音二, 音三])
		self.assertEqual(len(詞.內底字), 3)
		self.assertEqual(詞.內底字[0].型, 型一)
		self.assertEqual(詞.內底字[0].音, 音一)
		self.assertEqual(詞.內底字[1].型, 型二)
		self.assertEqual(詞.內底字[1].音, 音二)
		self.assertEqual(詞.內底字[2].型, 型三)
		self.assertEqual(詞.內底字[2].音, 音三)

	def test_對齊詞(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		字物件 = 字(型, 音)
		字陣列 = [字物件, 字物件]
		詞物件 = 詞(字陣列)
		另外字陣列 = [字(型, 音), 字(型, 音)]
		self.assertEqual(詞物件.內底字, 另外字陣列)

	def tst_詞(self):
		print(標點處理工具.切開語句('bin5-si7-sin1-bun5-po3-to7'))
		print(標點處理工具.切開語句('tsit8-ui7 tan5-sio2-tsia2 kap4 han5-kok4-tsik8 e5 ang1-sai3 tshut4-kok4 ，'))
		print(標點處理工具.切開語句('bo5-siunn7-tioh8 thong1-kuan1 tsa1-giam7 ho1u7-tsio3 e5 si5-tsun7 ，'))
		print(標點處理工具.切開語句('pi7 ko1-hiong5 sio2-kang2-ki1-tiunn5 e5 tsa1-giam7-uan5 suan1-tshio3 。'))
		print(標點處理工具.切開語句('kong2 i1 ke3-ho1u7 tsit8-e5 bun5-hua3 「 thau1-khioh4-tsia2 」 ，'))
		print(標點處理工具.切開語句('khi3-kah8 tan5-sio2-tsia2 tong1-tiunn5 lau5-bak8-sai2 tshi1-tsham2-khau3 ，'))
		print(標點處理工具.切開語句('tshin1-iu2 hiong3 bin5-si7 sin1-bun5-tai5 tau5-ue7 。'))
		print(標點處理工具.切開語句('king1-kue3 hiong3 iu2-kuan1-tan1-ui7 tsa1-tsing3 ，'))
		print(標點處理工具.切開語句('i5-bin5-su2 than2-sing5 tsa1-giam7-uan5 sit4-gian5 ，'))
		print(標點處理工具.切開語句('i2-king1 tiau3-li7 hian7-tsit4 gian2-gi2 tshu2-hun1 。'))
		print(標點處理工具.切開語句('Pang-liau5 hi5-kang2 「 Toa7-tiau5-hang7 」 siang7-khoah nng7-kong-chhioh'))
		print(標點處理工具.計算音標語句音標數量('kau2-chap8-lak8-hoe3'))

if __name__ == '__main__':
	unittest.main()
