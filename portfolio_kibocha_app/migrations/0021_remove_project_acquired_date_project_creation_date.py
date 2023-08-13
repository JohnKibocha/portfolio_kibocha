# Generated by Django 4.2.2 on 2023-07-21 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_kibocha_app', '0020_alter_review_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='acquired_date',
        ),
        migrations.AddField(
            model_name='project',
            name='creation_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
