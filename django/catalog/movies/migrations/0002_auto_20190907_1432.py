# Generated by Django 3.2.7 on 2021-10-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isPublished',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='Eklenme Tarihi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(verbose_name='Film Açıklaması'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(max_length=50, verbose_name='Film Resmi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Film Adı'),
        ),
    ]
