# Generated by Django 3.1.4 on 2020-12-28 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csandphysicsblog', '0002_auto_20201227_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='Added_by',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='Content',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='Date_added',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='Sub_Topic',
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_Topic', models.CharField(default='', max_length=200)),
                ('Date_added', models.DateField()),
                ('Added_by', models.CharField(default='', max_length=200)),
                ('Content', models.TextField(default='', max_length=20000)),
                ('Heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csandphysicsblog.subject')),
            ],
        ),
    ]