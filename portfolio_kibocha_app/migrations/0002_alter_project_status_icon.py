# Generated by Django 4.2.2 on 2023-07-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_kibocha_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status_icon',
            field=models.ImageField(upload_to='project_status_icons/'),
        ),
    ]
