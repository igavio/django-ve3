# Generated by Django 2.2.3 on 2019-07-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0005_parapono_epitopios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parapono',
            name='armodios',
            field=models.CharField(default='admin', max_length=20, verbose_name='Αρμόδιος'),
        ),
        migrations.AlterField(
            model_name='parapono',
            name='epitopios',
            field=models.BooleanField(verbose_name='Επιτόπιος'),
        ),
    ]
