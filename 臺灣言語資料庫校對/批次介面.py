# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from 臺灣言語資料庫.模型 import 編修
from 臺灣言語資料庫.模型 import 文字
from 臺灣言語資料庫.模型 import 關係
from 臺灣言語資料庫.模型 import 演化
from 臺灣言語資料庫校對.資料分類 import 資料分類
from 臺灣言語資料庫.腔口資訊 import 閩南語
from itertools import chain
from 臺灣言語工具.斷詞.型音辭典 import 型音辭典
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語資料庫.欄位資訊 import 免改
from 臺灣言語資料庫.欄位資訊 import 愛改
from 臺灣言語工具.字詞組集句章.基本元素.公用變數 import 標點符號
from 臺灣言語資料庫.欄位資訊 import 標準
from 臺灣言語資料庫.欄位資訊 import 免檢查
from django.db.models import Count
import Pyro4
from 臺灣言語工具.字詞組集句章.解析整理.物件譀鏡 import 物件譀鏡
import sys
import traceback
from 臺灣言語工具.字詞組集句章.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.字詞組集句章.解析整理.詞物件網仔 import 詞物件網仔
from 臺灣言語資料庫校對.表格 import 文字校對表格
from 臺灣言語資料庫.欄位資訊 import 改過
from 臺灣言語資料庫.欄位資訊 import 愛查
from 臺灣言語資料庫.欄位資訊 import 外來詞
from 臺灣言語資料庫.欄位資訊 import 人工校對
from 臺灣言語資料庫.腔口資訊 import 國語
from 臺灣言語資料庫.欄位資訊 import 字典無收著
from 臺灣言語資料庫校對.建議漢字 import 建議漢字
from 臺灣言語資料庫校對.檢查校對資料 import 校對資料整理
from 臺灣言語資料庫.欄位資訊 import 電腦校對
from 臺灣言語資料庫校對.主動校對 import 主動校對
from 臺灣言語資料庫.欄位資訊 import 猶未檢查
from 臺灣言語資料庫.欄位資訊 import 無效資料
from 臺灣言語資料庫.欄位資訊 import 電腦算的結果

__資料分類 = 資料分類()
__分析器 = 拆文分析器()
__篩仔 = 字物件篩仔()
__網仔 = 詞物件網仔()
__譀鏡 = 物件譀鏡()
__建議漢字 = 建議漢字()
__校對資料整理 = 校對資料整理()
Pyro4.config.SERIALIZER = 'pickle'
__閩南語標音 = Pyro4.Proxy("PYRONAME:閩南語標音")
__主動校對 = 主動校對()

def 定教育部辭典做標準(request):
	來源 = ['教育部臺灣閩南語常用詞辭典', '駱嘉鵬老師對應表']
	猶未設的標準資料 = __資料分類.揣出指定來源準備做檔準(閩南語, 來源=來源)
	for 猶未設 in 猶未設的標準資料:
		猶未設.狀況 = 標準
		猶未設.save()
	return HttpResponse("設{}做標準矣".format(來源))

def 國語改免檢查(request):
	國語資料 = __資料分類.揣國語猶未檢查()
	for 國語文字 in 國語資料:
		國語文字.狀況 = 免檢查
		國語文字.save()
	return HttpResponse("國語攏改免檢查矣")
		
def 檢查猶未標的資料(request):
	愛檢查的資料 = __資料分類.揣出檢查字音的資料(閩南語)
	分析器 = 拆文分析器()
	家私 = 轉物件音家私()
	音標工具 = 臺灣閩南語羅馬字拼音
	for 愛檢查 in 愛檢查的資料[:]:
		文 = 愛檢查.文字
		if __校對資料整理.型音是毋是攏佇辭典內底(文.型體, 文.音標):
			愛檢查.狀況 = 免改
		else:
			愛檢查.狀況 = 愛改
		愛檢查.save()
	版 = loader.get_template('臺灣言語資料庫/全部資料.html')
	文 = RequestContext(request, {
		'全部資料': 愛檢查的資料[:10],
	})
	return HttpResponse(版.render(文))

def 自動改有國語語句的資料(request):
	全部 = 0
	有改 = 0
	print(__資料分類.揣出愛改的資料().count())
	for 愛改資料 in __資料分類.揣出愛改的資料()[:]:
# 	for 愛改資料 in 編修.objects.filter(流水號=2394836):
		try:
			(愛改文字資料, 參考語句, 參考語句音轉漢字, \
				參考國語文字, 閩南語唸參考國語文字, 建議結果, 建議結果來源) = __建議漢字.問建議(愛改資料)
			print(全部, 有改, 愛改文字資料.音標, 愛改文字資料.型體, 建議結果, 建議結果來源)
			if 建議結果來源 == __建議漢字.閩南語唸國語:
				插入結果 = __校對資料整理.加校對資料(愛改資料, 電腦校對, 電腦校對,
					 建議結果, 愛改文字資料.音標)
				if 插入結果 == None:
					有改 += 1
					print('插入成功：{}，{}'.format(愛改文字資料.型體, 愛改文字資料.音標))
				else:
					print('插入失敗：{}，{}，插入結果：{}'
						.format(愛改文字資料.型體, 愛改文字資料.音標, 插入結果))
			elif 建議結果來源 == __建議漢字.參考語句音轉漢字 or\
				(建議結果 in 標點符號 and 愛改文字資料.音標 in 標點符號):
				插入結果 = __校對資料整理.加校對資料(愛改資料, 電腦算的結果, 電腦算的結果,
					 建議結果, 愛改文字資料.音標)
				print(建議結果, 愛改文字資料.音標)
				if 插入結果 == None:
					有改 += 1
				else:
					print('插入失敗：{}，{}，插入結果：{}'
						.format(愛改文字資料.型體, 愛改文字資料.音標, 插入結果))
			elif 建議結果來源 == __建議漢字.原本字:
				print(建議結果, 愛改文字資料.音標,'外來詞')
# 				插入結果 = __校對資料整理.加校對資料(愛改資料, 電腦校對, 電腦校對,
# 					 建議結果, 愛改文字資料.音標)
		except:
			pass
		全部 += 1
	return HttpResponse("全部：{}，有改：{}".format(全部, 有改))

def 揣資料庫有的來校對(request):
	改幾个 = 0
	for 音標 in __資料分類.揣出愛改的音():
		編修資料 = 編修.objects.filter(種類='文字', 狀況=愛改)\
			.filter(文字__音標=音標[0]).first()
		if 編修資料 != None:
			print(編修資料)
			電腦校對資料(request, 編修資料)
			改幾个 += 1
	return HttpResponse('攏總改{}个'.format(改幾个))

def 揣上尾一个改的來校對(request):
	編修資料 = __資料分類.揣出上尾一个改的()
# 	return HttpResponse('{} {} {} {}'.format(編修資料.流水號,
# 				編修資料.文字.型體, 編修資料.文字().音標,
# 				編修資料.文字.來源,))
	if 編修資料 == None:
		return HttpResponse('無資料愛處理喲～～')
	return 電腦校對資料(request, 編修資料)

def 揣來校對(request, 流水號):
	編修資料 = 編修.objects.get(流水號=流水號)  # 昨日1656444 2188298  # 言論203421 1817313
	return 電腦校對資料(request, 編修資料)

def 電腦校對資料(request, 編修資料):
	愛改的資料, 標準漢字, 仝款音標 = __主動校對.鬥校對仝音的資料(編修資料)
	__校對資料整理.電腦校對改一堆資料(愛改的資料, 標準漢字, 仝款音標)
	版 = loader.get_template('臺灣言語資料庫/全部資料.html')
	文 = RequestContext(request, {
		'全部資料': 愛改的資料,
	})
	return HttpResponse(版.render(文))

def 清掉無愛的資料(request):
	狀況 = [猶未檢查, 愛改, 免檢查]
	來源 = ['華語台語雙語語料庫系統']
	要求狀況 = Q(狀況=狀況[0])
	for 況 in 狀況[1:]:
		要求狀況 = 要求狀況 | Q(狀況=況)
	要求來源 = Q(文字__來源=來源[0])
	for 源 in 來源[1:]:
		要求來源 = 要求來源 | Q(文字__來源=源)
	全部編修 = 編修.objects.filter(要求狀況).filter(要求來源)
# 	for 編修資料 in 全部編修:
# 		編修資料.狀況 = 無效資料
# 		編修資料.save()
	版 = loader.get_template('臺灣言語資料庫校對/最近改的資料.html')
	文 = RequestContext(request, {
		'全部資料': 全部編修[:10],
	})
	return HttpResponse(版.render(文))

def 清掉無路用的關係演化(request):
	要求來源 = Q(關係甲__乙編修__狀況=無效資料) | Q(關係乙__甲編修__狀況=無效資料)\
		| Q(演化甲__乙編修__狀況=無效資料) | Q(演化乙__甲編修__狀況=無效資料)
	全部編修 = 編修.objects.exclude(狀況=無效資料).filter(要求來源).distinct()
	for 編修資料 in 全部編修:
		編修資料.狀況 = 無效資料
		編修資料.save()
	版 = loader.get_template('臺灣言語資料庫校對/最近改的資料.html')
	文 = RequestContext(request, {
		'全部資料': 全部編修[:10],
	})
	return HttpResponse(版.render(文))
