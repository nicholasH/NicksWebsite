# Generated by Django 2.0.3 on 2018-04-13 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180411_0630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businesscard',
            old_name='biz_name',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='businesscard',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='businesscard',
            old_name='Message',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='businesscard',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='businesscard',
            name='title',
        ),
    ]
