# Generated by Django 2.0.3 on 2018-04-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('biz_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Message', models.CharField(max_length=255)),
            ],
        ),
    ]
