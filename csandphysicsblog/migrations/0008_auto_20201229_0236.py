# Generated by Django 3.1.4 on 2020-12-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csandphysicsblog', '0007_auto_20201229_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Author_pic',
            field=models.ImageField(blank=True, upload_to='static/media'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Image',
            field=models.ImageField(blank=True, upload_to='static/media'),
        ),
    ]
