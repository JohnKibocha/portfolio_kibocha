# Generated by Django 4.2.2 on 2023-07-11 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_kibocha_app', '0003_alter_project_acquired_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_position', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
