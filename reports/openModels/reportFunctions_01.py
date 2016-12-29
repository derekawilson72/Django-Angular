from genreport.models import Report, Portfolio, RadialDataReport
from genreport.forms import  PortFolioForm, RadialForm

def processReport(request):
    """
    This function will process a POST request from the data form in /genreport/createnewreport.
    The post struct should contain form fields as follows:
    postStruct={u'report': [u'2'],  u'amount': [u'0'], u'title': [u'none']}
    The backend database will then process the fields and insert as rows into the Portfolio table.
    
    """
    postStruct=request.POST  ##the data structure from the POST data
    form = PortFolioForm( postStruct)  ##recreate a form from the submited post data
    port=form.save()         ##create an object from which the form was based on
    return port.id  ##simply return the id of the model object


def processGetReport(request):
    """
    This function will process a POST request from the data form in /genreport/createnewreport.
    The post struct should contain form fields as follows:
    postStruct={u'report': [u'2'],  u'amount': [u'0'], u'title': [u'none']}
    The backend database will then process the fields and insert as rows into the Portfolio table.
    
    """
    postStruct=request.GET  ##the data structure from the POST data
    form = PortFolioForm( postStruct)  ##recreate a form from the submited post data
    port=form.save()         ##create an object from which the form was based on
    return port.id  ##simply return the id of the model object


def processRadialReport(request):
    """
    This function will process a POST request from the data form in /genreport/createnewradial.
    The post struct should contain form fields as follows:
    postStruct={u'report': [u'2'],  u'amount': [u'0'], u'title': [u'none']}
    The backend database will then process the fields and insert as rows into theRadialDataReport  table.
    
    """
    postStruct=request.POST  ##the data structure from the POST data
    form = RadialForm( postStruct)  ##recreate a form from the submited post data
    rad  =form.save()         ##create an object from which the form was based on
    return rad.id  ##simply return the id of the model object
