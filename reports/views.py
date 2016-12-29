from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
##from django.views.decorators.csrf  import csrf_protect
from django.shortcuts import render
from openModels import viewFunctions_01, reportFunctions_01


from .forms import mainForm, PortFolioForm

# Create your views here.



def index(request):
    
    templateResults=viewFunctions_01.reportIndex(request)
    return templateResults



def detail(request, report_id):

    resp=viewFunctions_01.getDetail(request, report_id)
    return resp 

def results(request, report_id):
    response = "You're looking at the results of report %s."%(report_id)
    return HttpResponse(response )

def portfolio(request, report_id):
    response = "You're seeing portfolios on report %s." % report_id
    return HttpResponse(response)


def createnewreport(request):
    """
    Create the report form field to process a request to create a new portfolio entry.  Will generate an html form based on the db model.  
    if this is a POST request we need to process the form data
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PortFolioForm(request.POST) # replaces old mainForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PortFolioForm() #replaces old mainForm()
    print 'here is the report'
    print form.as_table()  ##output this to test the functionality
    return render(request, 'mainform.html', {'form': form})


def createAjaxReport(request):
    templateResults=viewFunctions_01.createAjaxPage(request)
    return templateResults

def yourreport(request):
    """
    The output page from the createnewreport page.  Will call the functions to enter a db row of the model data.
    """
    outString="got request"
    #print outString
    print request.POST
    outString = reportFunctions_01.processReport(request)
    
    return HttpResponse(outString )


def yourgetreport(request):
    """
    The output page from the createnewreport page.  Will call the functions to enter a db row of the model data.
    """
    outString="got request"
    #print outString
    print request.GET
    outString = reportFunctions_01.processGetReport(request)
    
    return HttpResponse(outString )


def testJson(request):
    """
    test a simple json request 
    """
    getString=request.GET
    testStruct=dict(a=range(10),b='this')
    testStruct.update(getString)
    return JsonResponse(testStruct)


def returnReportJson(request):
    """
    Return a json output of all reports and portfolios.  Return list of all reports. Containing report title, date, and list of portfolios
    """
    jsonStruct=viewFunctions_01.getReportJSON(request)
    return JsonResponse(jsonStruct)
