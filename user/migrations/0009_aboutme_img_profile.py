# Generated by Django 4.1.1 on 2022-10-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_aboutme_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='img_profile',
            field=models.ImageField(null=True, upload_to='profiles'),
        ),
    ]
