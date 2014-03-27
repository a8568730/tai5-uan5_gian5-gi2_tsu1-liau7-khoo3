from django.conf.urls import patterns, url

from 臺灣言語資料庫校對.瀏覽介面 import 最近改的資料
from 臺灣言語資料庫校對.瀏覽介面 import 閩南語狀況
from 臺灣言語資料庫校對.批次介面 import 定教育部辭典做標準
from 臺灣言語資料庫校對.批次介面 import 國語改免檢查
from 臺灣言語資料庫校對.批次介面 import 檢查猶未標的資料
from 臺灣言語資料庫校對.批次介面 import 自動改有國語語句的資料
from 臺灣言語資料庫校對.批次介面 import 揣資料庫有的來校對
from 臺灣言語資料庫校對.批次介面 import 揣上尾一个改的來校對
from 臺灣言語資料庫校對.批次介面 import 揣來校對
from 臺灣言語資料庫校對.批次介面 import 清掉無愛的資料
from 臺灣言語資料庫校對.批次介面 import 清掉無路用的關係演化
from 臺灣言語資料庫校對.人工校對介面 import 改愛改的資料
from 臺灣言語資料庫校對.人工校對介面 import 檢查改的資料
from 臺灣言語資料庫校對.其他介面 import 揣出一字全羅

urlpatterns = patterns('',
	url(r'^閩南語狀況$', 閩南語狀況, name='閩南語狀況'),
	
	url(r'^改愛改的資料$', 改愛改的資料, name='改愛改的資料'),
	url(r'^檢查改的資料/(?P<pk>\d+)$', 檢查改的資料, name='檢查改的資料'),
	
	url(r'^定教育部辭典做標準$', 定教育部辭典做標準, name='定教育部辭典做標準'),
	url(r'^檢查猶未標的資料$', 檢查猶未標的資料, name='檢查猶未標的資料'),
	url(r'^國語改免檢查$', 國語改免檢查, name='國語改免檢查'),
	url(r'^自動改有國語語句的資料$', 自動改有國語語句的資料, name='自動改有國語語句的資料'),
	url(r'^揣資料庫有的來校對$', 揣資料庫有的來校對, name='揣資料庫有的來校對'),
	url(r'^揣上尾一个改的來校對$', 揣上尾一个改的來校對, name='揣上尾一个改的來校對'),
	url(r'^揣來校對/(?P<流水號>\d+)$', 揣來校對, name='揣來校對'),
	url(r'^清掉無愛的資料$', 清掉無愛的資料, name='清掉無愛的資料'),
	url(r'^清掉無路用的關係演化$', 清掉無路用的關係演化, name='清掉無路用的關係演化'),
	
	url(r'^揣出一字全羅$', 揣出一字全羅, name='揣出一字全羅'),
	url(r'^.*$', 最近改的資料, name='最近改的資料'),
)