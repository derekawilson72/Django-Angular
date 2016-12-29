from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from genreport.models import Report, Portfolio

def reportIndex(request):
    resp="Radial project to generate reports (genrep)."
    
    repStructs = getReportList(maxNum=5)
    
    template = loader.get_template('index.html')
    context = {
        'latest_report_list': repStructs,
        'resp': resp
    }
    # return HttpResponse(resp)
    return HttpResponse(template.render(context, request))


def createAjaxPage(request):
    resp="Radial project to generate reports (genrep)."
    template = loader.get_template('reportAjax.html')
    context = {
        
        'resp': resp
    }
    # return HttpResponse(resp)
    return HttpResponse(template.render(context, request))


def getReportJSON(request):
    """
    get all reports and embedded portfolios as a JSON request
    """
    repStructs = getReportList(maxNum=5)
    jsonStruct=[]
    for rep in repStructs:
        title=rep.report_title
        date =rep.report_date
        portList=[]
        for port in rep.portList:
            amt=port.amount
            port_title=port.title
            portList.append({'amount':amt, 'port_title':port_title})
        jsonStruct.append({'title':title, 'date':date, 'portList':portList})
    jsonStruct={'reports':jsonStruct}
    return jsonStruct

def getDetail(request, report_id):
    import datetime
    resp="You're looking at report %s: %s"%(report_id,"text goes here")
    try:
        report = Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        raise Http404("Report does not exist")
    reportOutput=report
    return render(request, 'detail.html', {'report': reportOutput})
    # return HttpResponse( resp )



def getReportList(maxNum=5):
    """
    generate a report list and all embedded portfolios within the individual reports
    """
    resp="Radial project to generate reports (genrep)."
    
    allReports_list = Report.objects.order_by('-report_date')[:maxNum]
    repStructs=[report #, report.portfolio_set.all()]
                for report in
                Report.objects.order_by('-report_date')[:maxNum]
    ]

    for report in repStructs:
        report.portList=report.portfolio_set.all()
    
    
    # return HttpResponse(resp)
    return repStructs

    
