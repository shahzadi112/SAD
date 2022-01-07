# Generated by Django 3.2.9 on 2021-12-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0018_rename_id_report_rev_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_log',
            fields=[
                ('Rev_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('posted_by', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=200)),
                ('repoter', models.CharField(max_length=20)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='report',
        ),
    ]