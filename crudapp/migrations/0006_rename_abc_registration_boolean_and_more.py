# Generated by Django 4.1.7 on 2023-04-08 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_remove_registration_mod_registration_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='abc',
            new_name='Boolean',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='code',
        ),
    ]
