# Generated by Django 4.2.2 on 2023-07-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_kibocha_app', '0005_review_delete_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='profile_photo',
            field=models.ImageField(blank=True, default='default_user.png', null=True, upload_to='review_images'),
        ),
    ]
