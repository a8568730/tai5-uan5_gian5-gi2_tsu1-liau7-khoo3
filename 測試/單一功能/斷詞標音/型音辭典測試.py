from unittest.case import TestCase
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 斷詞標音.型音辭典 import 型音辭典

class 型音辭典測試(TestCase):
	def setUp(self):
		self.字典 = 型音辭典(4)
		self.初胚工具 = 文章初胚工具()
		self.分析器 = 拆文分析器()
		self.孤詞物 = self.分析器.建立詞物件('你')
		self.孤詞音 = self.分析器.建立詞物件('li2')
		self.二詞物 = self.分析器.建立詞物件('好')
		self.二詞音 = self.分析器.建立詞物件('hoo2')
		self.短詞物 = self.分析器.建立詞物件('你好')
		self.短詞音 = self.分析器.建立詞物件('li2-hoo2')
		self.詞物件 = self.分析器.建立詞物件('你好無？')
		self.詞音標 = self.分析器.建立詞物件('li2-hoo2-bo5-?')
		self.對齊詞 = self.分析器.產生對齊詞('你好無？', 'li2-hoo2-bo5-?')
		self.無仝詞 = self.分析器.產生對齊詞('你有無？', 'li2-u7-bo5-?')
		self.傷長詞 = self.分析器.產生對齊詞('你有好無？', 'li2-u7-hoo2-bo5-?')
		
	def tearDown(self):
		pass
	def test_漢字加詞成功無(self):
		self.字典.加詞(self.詞物件)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), {self.詞物件}])

	def test_多對齊加詞成功無(self):
		self.字典.加詞(self.對齊詞)
		self.字典.加詞(self.對齊詞)
		self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])

	def test_查對齊詞成功無(self):
		self.字典.加詞(self.對齊詞)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.詞音標), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.無仝詞), [set(), set(), set(), set()])

	def test_相近詞無使查著(self):
		self.字典.加詞(self.無仝詞)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), set()])
		self.assertEqual(len(self.詞音標.內底字), 4)
		self.assertEqual(self.字典.查詞(self.詞音標), [set(), set(), set(), set()])
		self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), set()])
		self.assertEqual(self.字典.查詞(self.無仝詞), [set(), set(), set(), {self.無仝詞}])
		
	def test_傷長詞無使查著(self):
		self.字典.加詞(self.對齊詞)
		self.字典.加詞(self.傷長詞)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.詞音標), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.傷長詞), [set(), set(), set(), set(), set()])
		
	def test_長短詞攏愛揣出來(self):
		self.字典.加詞(self.孤詞物)
		self.字典.加詞(self.二詞物)
		self.字典.加詞(self.短詞物)
		self.字典.加詞(self.詞物件)
		self.字典.加詞(self.孤詞音)
		self.字典.加詞(self.二詞音)
		self.字典.加詞(self.短詞音)
		self.字典.加詞(self.詞音標)
		self.assertEqual(self.字典.查詞(self.詞物件),
			[{self.孤詞物}, {self.短詞物}, set(), {self.詞物件}])
		self.assertEqual(self.字典.查詞(self.詞音標),
			[{self.孤詞音}, {self.短詞音}, set(), {self.詞音標}])
		