# Generated by Django 2.2.3 on 2019-07-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parapono',
            name='prostimo',
            field=models.FloatField(),
        ),
    ]
