# Generated by Django 2.1.2 on 2018-10-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0002_auto_20181022_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]