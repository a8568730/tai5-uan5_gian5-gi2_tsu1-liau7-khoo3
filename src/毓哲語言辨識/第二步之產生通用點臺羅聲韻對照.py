from 通用拼音音標 import 通用拼音音標
from 臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

def 臺羅聲韻轉辨識合成型(聲,韻):
	if 聲=='m' or 聲=='n' or 聲=='ng':
		if 韻.endswith('h') or 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
			韻=韻[:-1]+'nn'+韻[-1]
		else:
			韻+='nn'
	return (聲,韻)
	

if __name__ == '__main__':
# 	字音對照 = 通用拼音音標('bai5')
# 	print(字音對照.音標)
# 	print(字音對照.轉換到臺灣閩南語羅馬字拼音())
# 	lines = [line.strip() for line in open('/home/Ihc/辨識/Syl2Monophone.dic.txt')]
	lines = [line.strip() for line in open('/home/Ihc/處理愛對齊的語料/臺語通用拼音.dic')]
	for line in lines:
		if line=='':
			continue
		通用,*音素=line.split()
		if 通用.endswith('h') or 通用.endswith('p') or 通用.endswith('t') or 通用.endswith('k'):
			通用+='7'
		else:
			通用+='1'
		字音對照 = 通用拼音音標(通用)
		if 通用=='sil1':
			print(' '.join(line.split()))
		else:
			臺羅拼音=臺灣閩南語羅馬字拼音(字音對照.轉換到臺灣閩南語羅馬字拼音())
			聲,韻=臺羅聲韻轉辨識合成型(臺羅拼音.聲,臺羅拼音.韻)
			if 聲=='':
				print(通用[:-1],end=' ')
				print(韻)
			else:
				print(通用[:-1],end=' ')
				print(聲,end=' ')
				print(韻)
				
				