# Generated by Django 4.1.7 on 2023-04-12 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0009_profile_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crudapp.profile', verbose_name='name'),
        ),
    ]
