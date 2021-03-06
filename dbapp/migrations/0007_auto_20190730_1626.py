# Generated by Django 2.2.3 on 2019-07-30 13:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dbapp', '0006_auto_20190724_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='parapono',
            name='perigrafi',
            field=models.TextField(default='', verbose_name='Περιγραφή'),
        ),
        migrations.AddField(
            model_name='parapono',
            name='xristis',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parapono',
            name='etairia',
            field=models.CharField(max_length=60, verbose_name='Εταιρία'),
        ),
        migrations.AlterField(
            model_name='parapono',
            name='katanalotis',
            field=models.CharField(max_length=40, verbose_name='Καταναλωτής'),
        ),
        migrations.AlterField(
            model_name='parapono',
            name='prostimo',
            field=models.FloatField(verbose_name='Επιβληθέν πρόστιμο'),
        ),
        migrations.AlterField(
            model_name='parapono',
            name='ypovoli',
            field=models.DateField(default=datetime.date.today, verbose_name='Ημ/νία υποβολής'),
        ),
    ]
