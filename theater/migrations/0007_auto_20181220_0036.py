# Generated by Django 2.1.4 on 2018-12-19 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0006_auto_20181220_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='cols',
        ),
        migrations.RemoveField(
            model_name='hall',
            name='rows',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='cols',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='rows',
        ),
    ]