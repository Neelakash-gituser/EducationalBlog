# Generated by Django 3.1.4 on 2020-12-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csandphysicsblog', '0010_auto_20201229_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Added_by',
            field=models.TextField(default='', max_length=2000),
        ),
    ]
