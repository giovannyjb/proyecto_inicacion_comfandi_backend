# Generated by Django 4.1.1 on 2022-10-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_aboutme_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='job_description',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
