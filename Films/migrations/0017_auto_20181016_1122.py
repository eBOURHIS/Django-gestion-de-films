# Generated by Django 2.1.2 on 2018-10-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0016_auto_20181016_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realisator',
            name='realisator',
        ),
        migrations.AlterField(
            model_name='movie',
            name='realisator',
            field=models.ForeignKey(default='', on_delete=False, related_name='realisators', to='Films.Realisator'),
        ),
    ]