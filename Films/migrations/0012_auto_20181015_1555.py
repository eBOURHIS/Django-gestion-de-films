# Generated by Django 2.1.2 on 2018-10-15 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0011_auto_20181015_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='comments',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Films.Comment'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ForeignKey(default='', on_delete=False, to='Films.Actor'),
        ),
    ]