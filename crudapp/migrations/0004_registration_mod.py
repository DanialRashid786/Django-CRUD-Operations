# Generated by Django 4.1.7 on 2023-04-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_registration_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='mod',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
