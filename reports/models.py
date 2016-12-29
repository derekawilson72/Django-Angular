from django.db import models

# Create your models here.
class Report(models.Model):
    report_title = models.CharField(max_length=64)
    report_text  = models.CharField(max_length=200)
    report_date  = models.DateTimeField('date published')
    def __str__(self):
        outString="%d:%s"%(self.id, self.report_text[:15])
        return outString

class Portfolio(models.Model):
    report  = models.ForeignKey(Report, on_delete=models.CASCADE)
    title   = models.CharField(max_length=200)
    amount  = models.IntegerField(default=0)
    def __str__(self):
        outString="%d:%s"%(self.id, self.title[:15])
        return outString





class RadialDataReport(models.Model):
    radial_ID     = models.CharField(max_length=200)
    log_files     = models.CharField(max_length=200)
    machine_name  = models.CharField(max_length=200)
    task_path     = models.CharField(max_length=200)
    user_name     = models.CharField(max_length=200)
    log_date      = models.DateTimeField('date logged')
    def __str__(self):
        outString="%s:%s"%(self.radial_ID, self.log_date)
        return outString
