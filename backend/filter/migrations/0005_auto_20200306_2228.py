# Generated by Django 3.0.2 on 2020-03-06 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0004_auto_20200306_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filter',
            name='tweet1',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='tweet2',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='tweet3',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='tweet4',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='tweet5',
        ),
    ]