# Generated by Django 2.1.2 on 2018-10-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0004_auto_20181022_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
