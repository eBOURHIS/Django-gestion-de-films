# Generated by Django 2.1.1 on 2018-10-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0013_auto_20181022_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=False, related_name='directors', to='Films.Director'),
        ),
    ]
