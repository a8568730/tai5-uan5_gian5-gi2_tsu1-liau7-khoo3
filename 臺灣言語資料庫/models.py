from django.db import models

class 編修(models.Model):
	編修種類 = (('文字', '文字'), ('關係', '關係'), ('演化', '演化'))
	流水號 = models.AutoField(primary_key = True)
	種類 = models.CharField(max_length = 10, choices = 編修種類)
	版本 = models.CharField(max_length = 100, default = '正常')
	結果 = models.ForeignKey('self', related_name = '+',
		null = True, default = None)
	收錄時間 = models.DateField(auto_now_add = True)
	修改時間 = models.DateField(auto_now = True)
	def __str__(self):
		return ' '.join([
			str(self.流水號) , self.種類
			])
	class Meta():
		db_table = '編修'

class 資料(models.Model):
	def save(self, *args, **kwargs):
		if self.pk == None:
			self.流水號 = 編修.objects.create(種類 = self.__class__.__name__)
		return super(資料, self).save(*args, **kwargs)
	class Meta:
		abstract = True

class 文字(資料):
	文字種類 = (('字詞', '字詞'), ('語句', '語句'), ('章表冊', '章表冊'))
	流水號 = models.ForeignKey('編修', related_name = '文字',
		primary_key = True)
	來源 = models.CharField(max_length = 100)
	種類 = models.CharField(max_length = 10, choices = 文字種類)
	腔口 = models.CharField(max_length = 100)
	地區 = models.CharField(max_length = 100)
	年代 = models.IntegerField()
	組合 = models.TextField(blank = True)
	型體 = models.TextField()
	音標 = models.TextField(blank = True)
	調變 = models.TextField(blank = True)
	音變 = models.TextField(blank = True)
	收錄時間 = models.DateField(auto_now_add = True)
	修改時間 = models.DateField(auto_now = True)
# 	def save(self, *args, **kwargs):
# 		if self.pk == None:
# 			self.流水號 = 編修.objects.create(種類 = self.__class__.__name__)
# 		super(文字, self).save(*args, **kwargs)
	def __str__(self):
		return ' '.join([
			str(self.流水號) , self.來源 , self.型體])
	class Meta():
		db_table = '文字'

class 關係(資料):
	'仝字，用佇無仝言語層', '反義', '近義'
	'文讀層'
	'''會當替換	
	白話層
	袂當替換
	'''
	流水號 = models.ForeignKey('編修', related_name = '關係',
		primary_key = True,)
	甲流水號 = models.ForeignKey('編修', related_name = '關係甲')
	乙流水號 = models.ForeignKey('編修', related_name = '關係乙')
	乙對甲的關係類型 = models.CharField(max_length = 100)
	關係性質 = models.CharField(max_length = 100)
	詞性 = models.CharField(max_length = 100)
	收錄時間 = models.DateField(auto_now_add = True)
	修改時間 = models.DateField(auto_now = True)
	def __str__(self):
		return ' '.join(
			[str(self.流水號) , str(self.甲流水號) , str(self.乙流水號)
			, self.乙對甲的關係類型
			])
	class Meta():
		db_table = '關係'

class 演化(資料):
	'俗音', '合音'
	流水號 = models.ForeignKey('編修', related_name = '演化',
		primary_key = True)
	甲流水號 = models.ForeignKey('編修', related_name = '演化甲')
	乙流水號 = models.ForeignKey('編修', related_name = '演化乙')
	乙對甲的演化類型 = models.CharField(max_length = 100)
	解釋流水號 = models.ForeignKey('編修', related_name = '解釋')
	收錄時間 = models.DateField(auto_now_add = True)
	修改時間 = models.DateField(auto_now = True)
	def __str__(self):
		return ' '.join([
			str(self.流水號) , str(self.甲流水號) , str(self.乙流水號)
			, self.乙對甲的演化類型])
	class Meta():
		db_table = '演化'
