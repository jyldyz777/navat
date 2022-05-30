# Generated by Django 4.0.4 on 2022-05-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name_plural': 'Food'},
        ),
    ]
