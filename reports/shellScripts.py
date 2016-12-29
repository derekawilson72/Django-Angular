##Run this in the django shell to query results and test new features
from genreport.models import Report, Portfolio

allReports=Report.objects.all()

rep1=Report.objects.get(id=1)  #get a report


repStructs=[[report , report.portfolio_set.all()]
            for report in
            Report.objects.order_by('-report_date')[:5]
    ]

report.portList=report.portfolio_set.all()

repStructs=[report #, report.portfolio_set.all()]
                for report in
                Report.objects.order_by('-report_date')[:5]
    ]

for report in repStructs:
    report.portList=report.portfolio_set.all()


import json
struct01={'a':1, 'b':2}
jsonString=json.dumps(struct01 )
newStruct01=json.loads(jsonString )
newStruct01



import urllib, urllib2
url='http://127.0.0.1:8000/genreport/yourgetreport'  ##for get requests
url='http://127.0.0.1:8000/genreport/yourreport'     ##for post requests
dataStruct={'amount':'2', 'title': 'hi',  'report':'1'}
data=urllib.urlencode(dataStruct)
req=urllib2.urlopen(url,data=data)
rsp=req.readlines()

##in Linux POST enviroment
##POST http://127.0.0.1:8000/genreport/yourreport
##report=1&amount=10&title=ok&
##ctrl-D


class stuff():
    a=1
    def getStuff(*a):
        
