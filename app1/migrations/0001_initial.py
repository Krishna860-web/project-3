# Generated by Django 4.2.2 on 2023-06-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=80)),
                ('journel', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_book',
            },
        ),
    ]
