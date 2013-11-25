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
'''
Created on 2013/9/22

@author: Ihc
'''
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.基本元素.公用變數 import 分字符號
from 字詞組集句章.基本元素.公用變數 import 分詞符號
from 字詞組集句章.基本元素.公用變數 import 無音

class 物件譀鏡:
	def 看型(self, 物件):
		if isinstance(物件, 字):
			return self.看字物件型(物件)
		if isinstance(物件, 詞):
			return self.看詞物件型(物件)
		if isinstance(物件, 組):
			return self.看組物件型(物件)
		if isinstance(物件, 集):
			return self.看集物件型(物件)
		if isinstance(物件, 句):
			return self.看句物件型(物件)
		if isinstance(物件, 章):
			return self.看章物件型(物件)
		raise 型態錯誤('傳入來的毋是字詞組集句章其中一種物件：{0}，{1}'
			.format(type(物件), str(物件)))

	def 看字物件型(self, 字物件):
		if not isinstance(字物件, 字):
			raise 型態錯誤('傳入來的毋是字物件：{0},{1}'
				.format(type(字物件), str(字物件)))
		return 字物件.型

	def 看詞物件型(self, 詞物件):
		if not isinstance(詞物件, 詞):
			raise 型態錯誤('傳入來的毋是詞物件：{0},{1}'
				.format(type(詞物件), str(詞物件)))
		字的型 = []
		for 一字 in 詞物件.內底字:
			字的型.append(self.看字物件型(一字))
		return ''.join(字的型)

	def 看組物件型(self, 組物件):
		if not isinstance(組物件, 組):
			raise 型態錯誤('傳入來的毋是組物件：{0},{1}'
				.format(type(組物件), str(組物件)))
		詞的型 = []
		for 一詞 in 組物件.內底詞:
			詞的型.append(self.看詞物件型(一詞))
		return ''.join(詞的型)

	def 看集物件型(self, 集物件):
		if not isinstance(集物件, 集):
			raise 型態錯誤('傳入來的毋是集物件：{0},{1}'
				.format(type(集物件), str(集物件)))
		if len(集物件.內底組) == 0:
			raise 解析錯誤('內底組是空的！！')
		if len(集物件.內底組) > 1:
			raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(集物件)))
		return self.看組物件型(集物件.內底組[0])

	def 看句物件型(self, 句物件):
		if not isinstance(句物件, 句):
			raise 型態錯誤('傳入來的毋是句物件：{0},{1}'
				.format(type(句物件), str(句物件)))
		集的型 = []
		for 一集 in 句物件.內底集:
			集的型.append(self.看集物件型(一集))
		return ''.join(集的型)

	def 看章物件型(self, 章物件):
		if not isinstance(章物件, 章):
			raise 型態錯誤('傳入來的毋是章物件：{0},{1}'
				.format(type(章物件), str(章物件)))
		句的型 = []
		for 一句 in 章物件.內底句:
			句的型.append(self.看句物件型(一句))
		return ''.join(句的型)

	def 看音(self, 物件, 物件分字符號 = 分字符號, 物件分詞符號 = 分詞符號):
		if isinstance(物件, 字):
			return self.看字物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 詞):
			return self.看詞物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 組):
			return self.看組物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 集):
			return self.看集物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 句):
			return self.看句物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 章):
			return self.看章物件音(物件, 物件分字符號, 物件分詞符號)
		raise 型態錯誤('傳入來的毋是字詞組集句章其中一種物件：{0}，{1}'
			.format(type(物件), str(物件)))

	def 看字物件音(self, 字物件, 物件分字符號 = 分字符號, 物件分詞符號 = 分詞符號):
		if not isinstance(字物件, 字):
			raise 型態錯誤('傳入來的毋是字物件：{0},{1}'
				.format(type(字物件), str(字物件)))
		return 字物件.音

	def 看詞物件音(self, 詞物件, 物件分字符號 = 分字符號, 物件分詞符號 = 分詞符號):
		if not isinstance(詞物件, 詞):
			raise 型態錯誤('傳入來的毋是詞物件：{0},{1}'
				.format(type(詞物件), str(詞物件)))
		字的音 = []
		for 一字 in 詞物件.內底字:
			音標=self.看字物件音(一字)
			if 音標!=無音:
				字的音.append(音標)
		return 物件分字符號.join(字的音)

	def 看組物件音(self, 組物件, 物件分字符號 = 分字符號, 物件分詞符號 = 分詞符號):
		if not isinstance(組物件, 組):
			raise 型態錯誤('傳入來的毋是組物件：{0},{1}'
				.format(type(組物件), str(組物件)))
		詞的音 = []
		for 一詞 in 組物件.內底詞:
			音標=self.看詞物件音(一詞)
			if 音標!=無音:
				詞的音.append(音標)
		return 物件分詞符號.join(詞的音)

	def 看集物件音(self, 集物件, 物件分字符號 = 分字符號, 物件分詞符號 = 分詞符號):
		if not isinstance(集物件, 集):
			raise 型態錯誤('傳入來的毋是集物件：{0},{1}'
				.format(type(集物件), str(集物件)))
		if len(集物件.內底組) == 0:
			raise 解析錯誤('內底組是空的！！')
		if len(集物件.內底組) > 1:
			raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(集物件)))
		return self.看組物件音(集物件.內底組[0])

	def 看句物件音(self, 句物件, 物件分字符號 = 分字符號, 物件分詞符號 = 分詞符號):
		if not isinstance(句物件, 句):
			raise 型態錯誤('傳入來的毋是句物件：{0},{1}'
				.format(type(句物件), str(句物件)))
		集的音 = []
		for 一集 in 句物件.內底集:
			音標=self.看集物件音(一集)
			if 音標!=無音:
				集的音.append(音標)
		return 物件分詞符號.join(集的音)

	def 看章物件音(self, 章物件, 物件分字符號 = 分字符號, 物件分詞符號 = 分詞符號):
		if not isinstance(章物件, 章):
			raise 型態錯誤('傳入來的毋是章物件：{0},{1}'
				.format(type(章物件), str(章物件)))
		句的音 = []
		for 一句 in 章物件.內底句:
			音標=self.看句物件音(一句)
			if 音標!=無音:
				句的音.append(音標)
		return 物件分詞符號.join(句的音)
