# -*- coding: utf-8 -*-
from django.db import models
from 臺灣言語資料庫.資料模型 import 外語表
from 臺灣言語資料庫.資料模型 import 影音表
from 臺灣言語資料庫.資料模型 import 文本表
from 臺灣言語資料庫.資料模型 import 聽拍表

class 翻譯影音(models.Model):
	外語 = models.ForeignKey(外語表, related_name = '翻譯影音')
	影音 = models.ForeignKey(影音表, related_name = '+')

class 翻譯文本(models.Model):
	外語 = models.ForeignKey(外語表, related_name = '翻譯文本')
	文本 = models.ForeignKey(文本表, related_name = '+')

class 影音文本(models.Model):
	影音 = models.ForeignKey(影音表, related_name = '影音文本')
	文本 = models.ForeignKey(文本表, related_name = '+')

class 影音聽拍(models.Model):
	影音 = models.ForeignKey(影音表, related_name = '影音聽拍')
	聽拍 = models.ForeignKey(聽拍表, related_name = '+')

class 文本校對(models.Model):
	舊文本 = models.ForeignKey(文本表, related_name = '文本校對')
	新文本 = models.ForeignKey(文本表, related_name = '+')

class 聽拍校對(models.Model):
	舊聽拍 = models.ForeignKey(聽拍表, related_name = '聽拍校對')
	新聽拍 = models.ForeignKey(聽拍表, related_name = '+')
