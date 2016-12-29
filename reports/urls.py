from django.conf.urls import url

from . import views
from genreport.classViews import MyView, AboutView

urlpatterns = [
    #ex: /genreport/
    url(r'^$', views.index, name='index'),
    # ex: /genreport/1/
    url(r'^(?P<report_id>[0-9]+)/$',           views.detail,  name='detail'),
    # ex: /genreport/5/results/
    url(r'^(?P<report_id>[0-9]+)/results/$',   views.results, name='results'),
    # ex: /genreport/1/portfolio/
    url(r'^(?P<report_id>[0-9]+)/portfolio/$', views.portfolio, name='portfolio'),
    # ex: /genreport/createnewreport
    url(r'^createnewreport$', views.createnewreport, name='createnewreport'),
    # ex: /genreport/yourreport
    url(r'yourreport', views.yourreport, name='yourreport'),
    # ex: /genreport/yourreport
    url(r'yourgetreport', views.yourreport, name='yourreport'),
    # ex: /genreport/testJson
    url(r'testJson', views.testJson, name='testJson'),
    # ex: /genreport/reportjson
    url(r'reportjson', views.returnReportJson, name='returnReportJson'),
    # ex: /genreport/ajaxreport
    url(r'ajaxreport', views.createAjaxReport, name='createAjaxReport'),

    url(r'^mine/$', MyView.as_view(), name='my-view'),
    url(r'^about/', AboutView.as_view()),
    
    
]

