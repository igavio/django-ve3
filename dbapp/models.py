from django.db import models
import datetime

class Parapono(models.Model):
    katanalotis = models.CharField(max_length = 40)
    etairia = models.CharField(max_length = 60)
    ypovoli = models.DateField(default = datetime.date.today)
    prostimo = models.FloatField()

    armodios = models.CharField(max_length = 20, default = 'admin', verbose_name = 'Αρμόδιος')
    eisagogi = models.DateTimeField(auto_now_add = True)
    epitopios = models.BooleanField(verbose_name = 'Επιτόπιος' )

    def __str__(self):
        return self.katanalotis[:20] + ' - ' + self.etairia[:20] 
    