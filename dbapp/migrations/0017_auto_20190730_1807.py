# Generated by Django 2.2.3 on 2019-07-30 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dbapp', '0016_auto_20190730_1754'),
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
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
