# Generated by Django 3.1.7 on 2021-04-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_auto_20210408_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='education',
            field=models.TextField(verbose_name='Образование'),
        ),
    ]
