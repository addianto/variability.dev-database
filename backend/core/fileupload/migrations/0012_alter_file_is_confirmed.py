# Generated by Django 4.2.2 on 2025-02-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_fileupload', '0011_analysisresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='is_confirmed',
            field=models.BooleanField(default=True),
        ),
    ]
