# Generated by Django 3.1.4 on 2021-03-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csandphysicsblog', '0015_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Matter',
            field=models.TextField(default='', max_length=20000),
        ),
    ]