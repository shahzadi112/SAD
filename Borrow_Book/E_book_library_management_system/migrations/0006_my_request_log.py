# Generated by Django 3.2.9 on 2021-12-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0005_alter_my_request_requester'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_request_log',
            fields=[
                ('requester', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]