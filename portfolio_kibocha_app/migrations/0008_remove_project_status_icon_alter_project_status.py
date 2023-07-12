# Generated by Django 4.2.2 on 2023-07-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_kibocha_app', '0007_alter_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='status_icon',
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('designing', 'Designing'), ('developing', 'Developing'), ('testing', 'Testing'), ('deploying', 'Deploying'), ('live', 'Live'), ('acquired', 'Acquired')], default='designing', max_length=10),
        ),
    ]