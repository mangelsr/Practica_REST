# Generated by Django 2.0.1 on 2018-01-16 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flying', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airport',
            old_name='tipe',
            new_name='type',
        ),
    ]
