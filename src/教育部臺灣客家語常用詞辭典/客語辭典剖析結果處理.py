'''
Created on 2013/7/31

@author: chhsueh
'''
from 教育部臺灣客家語常用詞辭典.客話辭典網頁剖析工具 import 客話辭典網頁剖析工具
import os
from curses.ascii import isalpha, isdigit

class 客語辭典剖析結果處理():
    剖析結果=[]
    字體內量=0
    表格內=False
    #['詞目', '【熱天】', '詞性: 名', '各家用字表', '四縣音', 'ngied5tien24', '', '海陸音', 'ngied2tien53', '', '大埔音', 'ngied54tien33', '', '饒平音', 'ngied5tien11', '', '詔安音', 'ngied43teen11', '', '釋義', '夏天。例：熱天个時節，阿姆會摎被骨收起來。（夏天的時候，媽媽會把被子收起來。）', '近義詞', '', '反義詞', '', '文白讀', '', '又\u3000音', '', '多音字', '', '對應華語', '夏天', '圖片', '']
    def 標籤名(self):
        return ['詞目','詞性', '四縣音',  '海陸音', '大埔音', '饒平音',  '詔安音',
                '釋義',  '近義詞',  '反義詞', '文白讀',  '又音',  '多音字','對應華語']
    def 欄位值(self,剖析結果):
        if '詞性' in 剖析結果[2]:
            詞性=剖析結果[2].split(':')[1].strip()
        else:
            詞性=''
        return [剖析結果[1][1:-1],詞性,self.分開音標(剖析結果[5]),self.分開音標(剖析結果[8]),
                self.分開音標(剖析結果[11]),self.分開音標(剖析結果[14]),self.分開音標(剖析結果[17]),
                剖析結果[20],剖析結果[22],剖析結果[24],剖析結果[26],剖析結果[28],剖析結果[30],剖析結果[32], ]
    def 轉資料庫格式(self,剖析結果):
        return '("'+'","'.join(self.標籤名())+"\") VALUES ('"+"','".join(self.欄位值(剖析結果))+"')"
    def 分開音標(self,連做伙音標):
        頂一个音=None
        音標結果=''
        for 音 in 連做伙音標:
            if 頂一个音!=None and isalpha(音) and isdigit(頂一个音):
                音標結果+=' '
            音標結果+=音
            頂一个音=音
        return 音標結果
            
        


if __name__ == "__main__":
    網頁剖析工具 = 客話辭典網頁剖析工具(strict=False)
    客語辭典剖析結果=客語辭典剖析結果處理()
#    su=open('/home/chhsueh/su.html').read()
##     print(su)
#    a=網頁剖析工具.剖析客話辭典網頁(su)
#    print(a)
#    word=open('/home/chhsueh/word.html').read()
#     print(word)
#    a=網頁剖析工具.剖析客話辭典網頁(word)
#    print(a)
    os.chdir('/home/ihc/桌面/1020801/hakka/')
    a=set()
    b=set()
    for 檔名 in os.listdir(".")[:10]:
        if 檔名.startswith("result"):
#            print(檔名)
            客話辭典資料=網頁剖析工具.剖析客話辭典檔案(檔名)
            資料庫指令=客語辭典剖析結果.轉資料庫格式(客話辭典資料)
            print(資料庫指令)
#            a.add(客語辭典剖析結果.欄位值(客話辭典資料)[0][0])
#            b.add(客語辭典剖析結果.欄位值(客話辭典資料)[0][-1])
            
#    客話辭典資料=網頁剖析工具.剖析客話辭典檔案('/home/chhsueh/su2.html')
#    print(客話辭典資料)
#    b=網頁剖析工具.剖析客話辭典檔案('/home/chhsueh/word2.html')
#    print(b)
#    print(客語辭典剖析結果.標籤名())
#    print(客語辭典剖析結果.欄位值(客話辭典資料))
#    print(客語辭典剖析結果.轉資料庫格式(客話辭典資料))
#    print(客語辭典剖析結果.轉資料庫格式(b))
