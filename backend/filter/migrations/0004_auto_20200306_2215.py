# Generated by Django 3.0.2 on 2020-03-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0003_auto_20200306_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='tweet1',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='filter',
            name='tweet2',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='filter',
            name='tweet3',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='filter',
            name='tweet4',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='filter',
            name='tweet5',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]