# Generated by Django 3.2.5 on 2021-10-01 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('birth', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
