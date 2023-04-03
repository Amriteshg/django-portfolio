# Generated by Django 4.1.7 on 2023-04-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_codeskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Soft Skill Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='skills')),
            ],
        ),
    ]