# -*- coding: utf-8 -*-
from 臺灣言語資料庫.試驗.加關係.加關係試驗 import 加關係試驗
import json
from 臺灣言語資料庫.資料模型 import 外語表
from 臺灣言語資料庫.資料模型 import 影音表
from 臺灣言語資料庫.關係模型 import 翻譯影音表

class 加翻譯影音試驗(加關係試驗):
	def setUp(self):
		super(加翻譯影音試驗, self).setUp()
		self.原本資料表 = 外語表
		self.原本資料內容一 = {
			'收錄者':json.dumps({'名':'鄉民', '出世年':'1950', '出世地':'臺灣'}),
			'來源':json.dumps({'名':'Dr. Pigu', '出世年':'1990', '出世地':'花蓮人'}),
			'版權':'會使公開',
			'種類':'字詞',
			'語言腔口':'閩南語',
			'著作所在地':'花蓮',
			'著作年':'2014',
			'外語語言':'華語',
			'外語資料':'漂亮',
			}
		self.原本資料內容二 = {
			'收錄者':json.dumps({'名':'鄉民', '出世年':'1950', '出世地':'臺灣'}),
			'來源':json.dumps({'名':'Dr. Pigu', '出世年':'1990', '出世地':'花蓮人'}),
			'版權':'會使公開',
			'種類':'字詞',
			'語言腔口':'閩南語',
			'著作所在地':'花蓮',
			'著作年':'2014',
			'外語語言':'英語',
			'外語資料':'She is beautiful.',
			}
		self.對應資料內容一 = {
			'收錄者':json.dumps({'名':'鄉民', '出世年':'1950', '出世地':'臺灣'}),
			'來源':json.dumps({'名':'Dr. Pigu', '出世年':'1990', '出世地':'花蓮人'}),
			'版權':'會使公開',
			'種類':'字詞',
			'語言腔口':'閩南語',
			'著作所在地':'花蓮',
			'著作年':'2014',
			'原始影音資料':self.詞檔案,
			}
		self.對應資料內容二 = {
			'收錄者':json.dumps({'名':'Dr. Pigu', '出世年':'1990', '出世地':'花蓮人'}),
			'來源':json.dumps({'名':'鄉民', '出世年':'1950', '出世地':'臺灣'}),
			'版權':'袂使公開',
			'種類':'語句',
			'語言腔口':'四縣話',
			'著作所在地':'臺灣',
			'著作年':'195x',
			'原始影音資料':self.句檔案,
			}
	def 加詞(self, 外語):
		原來外語資料數 = 外語表.objects.all().count()
		原來影音資料數 = 影音表.objects.all().count()
		原來翻譯影音數 = 翻譯影音表.objects.all().count()
		影音 = 外語.錄影音(self.對應資料內容一)
		self.assertEqual(self.外語表.objects.all().count(), 原來外語資料數)
		self.assertEqual(self.影音表.objects.all().count(), 原來影音資料數 + 1)
		self.assertEqual(self.翻譯影音表.objects.all().count(), 原來翻譯影音數 + 1)
		self.assertEqual(外語.翻譯影音.影音.get(pk=影音.pk), 影音)
		self.assertEqual(影音.收錄者, self.臺灣人)
		self.assertEqual(影音.來源, self.花蓮人)
		self.assertEqual(影音.版權, self.會使公開)
		self.assertEqual(影音.種類, self.字詞)
		self.assertEqual(影音.語言腔口, self.閩南語)
		self.assertEqual(影音.著作所在地, self.花蓮)
		self.assertEqual(影音.著作年, self.二空一四)
		self.assertEqual(影音.屬性, '{}')
		self.assertEqual(影音.原始影音資料, self.詞檔案)
	def 加句(self, 外語):
		原來外語資料數 = 外語表.objects.all().count()
		原來影音資料數 = 影音表.objects.all().count()
		原來翻譯影音數 = 翻譯影音表.objects.all().count()
		影音 = 外語.錄影音(self.對應資料內容二)
		self.assertEqual(self.外語表.objects.all().count(), 原來外語資料數)
		self.assertEqual(self.影音表.objects.all().count(), 原來影音資料數 + 1)
		self.assertEqual(self.翻譯影音表.objects.all().count(), 原來翻譯影音數 + 1)
		self.assertEqual(外語.翻譯影音.影音.get(pk=影音.pk), 影音)
		self.assertEqual(影音.收錄者, self.花蓮人)
		self.assertEqual(影音.來源, self.臺灣人)
		self.assertEqual(影音.版權, self.袂使公開)
		self.assertEqual(影音.種類, self.語句)
		self.assertEqual(影音.語言腔口, self.四縣話)
		self.assertEqual(影音.著作所在地, self.臺灣)
		self.assertEqual(影音.著作年, self.一九五空年代)
		self.assertEqual(影音.屬性, '{}')
		self.assertEqual(影音.原始影音資料, self.句檔案)
