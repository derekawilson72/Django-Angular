

from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpRequest

from genreport import classViews, views



##session Data
for session in Session.objects.all():
    data=SessionStore().decode(session.session_data)
    print session.session_key, data
    
session_key='4gured3wido2wgv3kmdugl7i3745zijd'
user_session=SessionStore(session_key=session_key)# session.session_key)
user_session['msg']
user_session.save()


##test direct views in class and functions and get response
##cms-music-example has some profound requesting
request=HttpRequest()
view=classViews.MyView()
resp=view.get(request)
resp.status_code
resp.content

request.POST.update(p=1)
resp=view.post(request)  ##will need post attribute to work
resp.status_code
resp.content
'{"a": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "p": [1], "b": "this"}'


request=HttpRequest()
resp=views.returnReportJson(request)
resp.status_code
resp.content


##data posting
request=HttpRequest()
request.POST.update({'report': 1, 'amount': 4, 'title': 'newerTitle'})
resp=views.yourreport(request)
"<QueryDict: {u'report': [1], u'amount': [4], u'title': ['newerTitle']}>"
resp.status_code
resp.content
'181'




##test the content request / response with url calls
from django.test import Client
c = Client()
response = c.get('/genreport/2/',{}) ##get.request is blank
response.status_code
response.content
##jsonresponse
response = c.get('/genreport/reportjson/',{}) ##get.request is blank
response.status_code
response.content

##post request
postStruct={'report': 1, 'amount': 5, 'title': 'newesTitle'}
response = c.post('/genreport/yourreport/',postStruct ) ##post.request 
response.status_code
response.content




