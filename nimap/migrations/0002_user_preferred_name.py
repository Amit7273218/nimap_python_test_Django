# Generated by Django 5.1.2 on 2024-10-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nimap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preferred_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
