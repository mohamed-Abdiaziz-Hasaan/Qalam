# Generated by Django 3.1.4 on 2021-01-01 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('mobile_number', models.CharField(blank=True, max_length=20)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('date_of_register', models.DateField(default=django.utils.timezone.now)),
                ('address', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
