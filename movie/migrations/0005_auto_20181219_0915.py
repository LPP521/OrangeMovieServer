# Generated by Django 2.1.4 on 2018-12-19 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20181219_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100, verbose_name='role')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Actor', verbose_name='actor')),
            ],
        ),
        migrations.RemoveField(
            model_name='actortable',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='actortable',
            name='movie',
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', related_query_name='movie', through='movie.Membership', to='movie.Actor', verbose_name='actors'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(related_name='movies', related_query_name='movie', to='movie.Tag', verbose_name='tags'),
        ),
        migrations.DeleteModel(
            name='ActorTable',
        ),
        migrations.AddField(
            model_name='membership',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie', verbose_name='movie'),
        ),
    ]