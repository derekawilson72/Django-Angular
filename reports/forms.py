from django import forms
from django.forms import ModelForm
from .models import Portfolio, RadialDataReport

class mainForm(forms.Form):
    """
    A standard form  to contain the input fields standard in portfolio model class.  This is only useful when users need to create a custom form rather than use the ModelForm class.
    """
    your_title = forms.CharField(label='Your Title', max_length=100)
    your_amount= forms.IntegerField(label='Your Amount')
    your_report= forms.IntegerField(label='Your Report')


class PortFolioForm(ModelForm):
    """
    create a form from the db model in Portfolio.  Specify the fields to contain or ommit.  The for then appears with all the input fields from the database model.
    """
    class Meta:
        model=Portfolio
        fields=['report', 'amount', 'title']


class RadialForm(ModelForm):
    """
    create a form from the db model in RadialDataReport.  Specify the fields to contain or ommit.  The form then appears with all the input fields from the database model.
    """
    class Meta:
        model=RadialDataReport
        fields=['radial_ID',
                'log_files',
                'machine_name',
                'task_path',
                'user_name',
        ]
        
        

