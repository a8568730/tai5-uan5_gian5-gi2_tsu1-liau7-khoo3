from 臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
臺灣閩南語羅馬字拼音對照吳守禮方音聲母表 = {'p':'ㄅ', 'ph':'ㄆ', 'm':'ㄇ', 'b':'ㆠ', 't':'ㄉ', 'th':'ㄊ', 'n':'ㄋ', 'l':'ㄌ',
		'k':'ㄍ', 'kh':'ㄎ', 'ng':'ㄫ', 'g':'ㆣ', 'h':'ㄏ', 'ts':'ㄗ', 'tsh':'ㄘ', 's':'ㄙ', 'j':'ㆡ',
		'tsi':'ㄐ', 'tshi':'ㄑ', 'si':'ㄒ', 'ji':'ㆢ', '':'', }
臺灣閩南語羅馬字拼音對照吳守禮方音韻母表 = {'a':'ㄚ', 'e':'ㆤ', 'i':'ㄧ', 'oo':'ㆦ', 'o':'ㄜ', 'u':'ㄨ',
		'ai':'ㄞ', 'au':'ㄠ', 'ia':'ㄧㄚ', 'io':'ㄧㆦ', 'iu':'ㄧㄨ', 'ua':'ㄨㄚ', 'ue':'ㄨㆤ', 'ui':'ㄨㄧ', 'iau':'ㄧㄠ', 'uai':'ㄨㄞ',
		'ann':'ㆩ', 'enn':'ㆥ', 'inn':'ㆪ', 'onn':'ㆲ', 'm':'ㆬ', 'ng':'ㆭ', 'ainn':'ㆮ', 'iann':'ㄧㆩ', 'iaunn':'ㄧㆯ', 'iunn':'ㄧㆫ', 'uann':'ㄨㆩ', 'uainn':'ㄨㆮ',
		'am':'ㆰ', 'an':'ㄢ', 'ang':'ㄤ', 'im':'ㄧㆬ', 'in':'ㄧㄣ', 'ing':'ㄧㄥ', 'om':'ㆱ', 'ong':'ㆲ', 'iam':'ㄧㆰ', 'ian':'ㄧㄢ', 'iang':'ㄧㄤ', 'iong':'ㄧㆲ', 'un':'ㄨㄣ', 'uan':'ㄨㄢ',
		'ah':'ㄚㆷ', 'eh':'ㆤㆷ', 'ih':'ㄧㆷ', 'oh':'ㄜㆷ', 'uh':'ㄨ', 'auh':'ㄠㆷ', 'iah':'ㄧㄚㆷ', 'ioh':'ㄧㄜㆷ', 'iuh':'ㄧㄨㆷ', 'iauh':'ㄧㄠㆷ', 'uah':'ㄨㄚㆷ', 'ueh':'ㄨㆤㆷ', 'ooh':'ㆦㆷ',
		'annh':'ㆩㆷ', 'ennh':'ㆥㆷ', 'innh':'ㆪㆷ', 'mh':'ㆬㆷ', 'iannh':'ㄧㆩㆷ', 'ngh':'ㆭㆷ', 'ap':'ㄚㆴ', 'at':'ㄚㆵ', 'ak':'ㄚㆶ', 'op':'ㆦㆴ', 'ok':'ㆦㆶ', 'iok':'ㄧㆦㆶ',
		'ip':'ㄧㆴ', 'it':'ㄧㆵ', 'ik':'ㄧㆶ', 'iap':'ㄧㄚㆴ', 'iat':'ㄧㄚㆵ', 'iak':'ㄧㄚㆶ', 'ut':'ㄨㆵ', 'uat':'ㄨㄚㆵ',
		'ioo':'ㄧㆦ', 'ir':'', 'ere':'', 'er':'', 'irinn':'', 'ee':'', 'uee':'', 'eeh':'', 'uinn':'ㄨㆪ', 'ionn':'ㄧㆧ', 'irm':'', 'irn':'', 'irng':'', 'eng':'', 'uang':'', 'irp':'', 'irt':'', 'irk':'',
		'aih':'ㄞㆷ', 'ainnh':'ㆮㆷ', 'aunnh':'ㆯㆷ', 'erh':'', 'ereh':'', 'uih':'ㄨㄧㆷ',
		'aunn':'ㆯ', 'uenn':'ㄨㆥ', 'uaih':'ㄨㄞㆷ', 'iunnh':'ㄧㆫㆷ', 'iaunnh':'ㄧㆯㆷ', 'uennh':'ㄨㆥㆷ', 'uinnh':'ㄨㆪㆷ', 'uainnh':'ㄨㆮㆷ', 'iut':'ㄧㄨㆵ', 'uak':'ㄨㄚㆶ', 'onnh':'ㆧㆷ'
		}
臺灣閩南語羅馬字拼音對照吳守禮方音聲調表 = {'0':'˙', '1':'', '2':'ˋ', '3':'˪',
'4':'', '5':'ˊ', '6':'ˋ', '7':'˫',
'8':'㆐', '9':'^', '10':'㆐'}

class 方音符號吳守禮改良式():
	聲母表 = 臺灣閩南語羅馬字拼音對照吳守禮方音聲母表
	韻母表 = 臺灣閩南語羅馬字拼音對照吳守禮方音韻母表
	聲調符號表 = 臺灣閩南語羅馬字拼音對照吳守禮方音聲調表
	聲 = None
	韻 = None
	調 = None
	音標 = None
	def __init__(self, 臺羅音標):
		臺羅 = 臺灣閩南語羅馬字拼音(臺羅音標)
		if 臺羅.音標 != None:
			self.對臺羅聲韻調產生注音(臺羅.聲, 臺羅.韻, 臺羅.調)
	def 對臺羅聲韻調產生注音(self, 聲, 韻, 調):
		if 韻.startswith('i') and (聲 == 'ts' or 聲 == 'tsh' or 聲 == 's' or 聲 == 'j'):
			聲 += 'i'
		self.聲 = self.聲母表[聲]
		self.韻 = self.韻母表[韻]
		self.調 = self.聲調符號表[調]
		if 調 == '0':
			self.音標 = self.調 + self.聲 + self.韻
		elif 調 == '8':
			self.音標 = self.聲 + self.韻[:-1] + self.調 + self.韻[-1:]
		else:
			self.音標 = self.聲 + self.韻 + self.調
	def 產生音標組字式(self):
		if self.音標 == None:
			return None
		elif len(self.音標) == 1:
			return '⿳' + self.音標 + ' '
		else:
			return '⿳' * (len(self.音標) - 1) + self.音標
#
if __name__ == '__main__':
	print(方音符號吳守禮改良式('@@').音標)
	print(方音符號吳守禮改良式('pI̋m').音標)
	print(方音符號吳守禮改良式('pe̍m').音標)
	print(方音符號吳守禮改良式('pi̍m').音標)
	print(方音符號吳守禮改良式('pîm').音標)
	print(方音符號吳守禮改良式('pǐN').音標)
	print(方音符號吳守禮改良式('pih').音標)
	print(方音符號吳守禮改良式('cat8').音標)
	print(方音符號吳守禮改良式('Pih8').音標)

	print(方音符號吳守禮改良式('nňg').音標)
	print(方音符號吳守禮改良式('tor').音標)
	print(方音符號吳守禮改良式('tsőo').音標)
	print(方音符號吳守禮改良式('tsňg').音標)
	print(方音符號吳守禮改良式('xxtsé--á').音標)
	print(方音符號吳守禮改良式('pňg').音標)
	print(方音符號吳守禮改良式('óonn').音標)
#
