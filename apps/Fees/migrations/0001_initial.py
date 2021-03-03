# Generated by Django 3.1.4 on 2021-02-06 18:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('students', '0002_student_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fees_Amount', models.FloatField()),
                ('Fees_Type', models.CharField(choices=[('Class Fees', 'Class Fees'), ('Exam Fees', 'Exam Fees')], default='Class Fees', max_length=10)),
                ('Start_Date', models.DateField(default=django.utils.timezone.now)),
                ('end_Date', models.DateField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.students')),
                ('student_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
            ],
        ),
    ]
