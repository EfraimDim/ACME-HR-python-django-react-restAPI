# Generated by Django 4.0.3 on 2022-03-09 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
         migrations.AlterModelOptions(
            name='department',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='deptemp',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='deptmanager',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='salary',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'managed': False},
        ),
    ]
