# Generated by Django 4.1.7 on 2023-03-28 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='timestamp',
        ),
    ]
