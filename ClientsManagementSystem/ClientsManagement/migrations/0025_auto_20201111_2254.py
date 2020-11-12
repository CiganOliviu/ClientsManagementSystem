# Generated by Django 3.0.8 on 2020-11-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientsManagement', '0024_auto_20201110_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsdetail',
            name='client_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='clientsdetail',
            name='email',
            field=models.EmailField(default='', max_length=248),
        ),
        migrations.AddField(
            model_name='clientsdetail',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='clientsdetail',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='clientsdetail',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='clientsdetail',
            name='social_media_presence',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='clientsdetail',
            name='website',
            field=models.URLField(default=''),
        ),
    ]
