# Generated by Django 2.1.2 on 2018-12-18 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0015_movie_synopsis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='realease_date',
            new_name='release_date',
        ),
    ]
