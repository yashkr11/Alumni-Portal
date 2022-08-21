# Generated by Django 4.0.6 on 2022-07-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
