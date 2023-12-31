# Generated by Django 4.2.2 on 2023-07-20 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_kibocha_app', '0010_milestone_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milestone',
            name='date_range',
        ),
        migrations.AddField(
            model_name='milestone',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='milestone',
            name='start_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
