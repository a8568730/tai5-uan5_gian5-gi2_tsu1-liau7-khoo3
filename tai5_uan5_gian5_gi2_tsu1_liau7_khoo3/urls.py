from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tai5_uan5_gian5_gi2_tsu1_liau7_khoo3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^臺灣言語資料庫/', include('臺灣言語資料庫.網址')),
    url(r'^校對/', include('臺灣言語資料庫校對.網址')),
)
