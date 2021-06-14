# Generated by Django 3.2.3 on 2021-06-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileManager', '0002_auto_20210604_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.RemoveField(
            model_name='file',
            name='uploader',
        ),
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
