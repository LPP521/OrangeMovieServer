# Generated by Django 2.1.4 on 2018-12-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='col',
            field=models.IntegerField(blank=True, verbose_name='column'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='row',
            field=models.IntegerField(blank=True, verbose_name='row'),
        ),
    ]