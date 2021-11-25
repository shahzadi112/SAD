# Generated by Django 3.2.9 on 2021-11-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('description', models.TextField(max_length=200)),
                ('user_name', models.CharField(max_length=20)),
                ('isdonated', models.CharField(default='No', max_length=3)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='request',
            fields=[
                ('reqId', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField(auto_now_add=True)),
                ('accepted', models.CharField(default='Processing', max_length=10)),
                ('isbn', models.CharField(max_length=20)),
                ('deliveryManId', models.IntegerField(default=0)),
            ],
        ),
    ]
