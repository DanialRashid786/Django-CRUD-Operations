# Generated by Django 4.1.7 on 2023-04-08 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_registration_abc'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='color',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('B', 'Blue')], default=2, max_length=1),
            preserve_default=False,
        ),
    ]