# Generated by Django 2.1.2 on 2018-10-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0008_auto_20181022_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b'test'),
        ),
    ]
