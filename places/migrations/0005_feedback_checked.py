# Generated by Django 3.2 on 2021-05-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Обработано'),
        ),
    ]