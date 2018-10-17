# Generated by Django 2.1.2 on 2018-10-16 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0015_auto_20181016_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='movie',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='realisator',
            name='realisator',
            field=models.ForeignKey(default='', on_delete=False, related_name='movies', to='Films.Movie'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='users', to='Films.User'),
        ),
    ]