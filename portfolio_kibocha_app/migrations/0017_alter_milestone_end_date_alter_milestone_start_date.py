# Generated by Django 4.2.2 on 2023-07-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_kibocha_app', '0016_milestone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='start_date',
            field=models.DateField(),
        ),
    ]