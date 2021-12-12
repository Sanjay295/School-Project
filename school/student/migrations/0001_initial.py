# Generated by Django 3.2.6 on 2021-12-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30)),
                ('f_name', models.CharField(max_length=30)),
                ('s_DOB', models.IntegerField()),
                ('s_class', models.CharField(max_length=30)),
                ('s_address', models.CharField(max_length=30)),
                ('s_school', models.CharField(max_length=30)),
                ('s_email', models.EmailField(max_length=30)),
                ('s_city', models.CharField(max_length=30)),
                ('s_state', models.CharField(max_length=30)),
                ('s_pin', models.IntegerField()),
            ],
        ),
    ]