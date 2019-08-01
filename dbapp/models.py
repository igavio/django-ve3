from django.db import models
import datetime

class Parapono(models.Model):
    katanalotis = models.CharField(max_length=40, verbose_name='Καταναλωτής')
    etairia = models.CharField(max_length=60, verbose_name='Εταιρία')
    ypovoli = models.DateField(
        default=datetime.date.today, verbose_name='Ημ/νία υποβολής')
    prostimo = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True,
                                   verbose_name='Επιβληθέν πρόστιμο')  # νέα διόρθωση
    armodios = models.CharField(
        max_length=20, default='Φλώρου Νίκη', verbose_name='Αρμόδιος')
    # αόρατο, αλλά μέσα στον πίνακα της ΒΔ
    eisagogi = models.DateTimeField(auto_now_add=True)
    epitopios = models.BooleanField(verbose_name='Επιτόπιος έλεγχος')

    perigrafi = models.TextField(
        null=True, blank=True, verbose_name='Περιγραφή')  # νέα προσθήκη
    xristis = models.ForeignKey('auth.User', default=1, on_delete=models.CASCADE,
                                verbose_name='Χρήστης')  # νέα προσθήκη

    def __str__(self):
        return self.katanalotis[:20] + ' - ' + self.etairia[:20]
    