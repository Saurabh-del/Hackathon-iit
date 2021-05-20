# Generated by Django 3.1.5 on 2021-04-17 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('speciality', models.CharField(blank=True, choices=[('Allergist', 'Allergist'), ('Immunologists', 'Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Cardiologists', 'Cardiologists'), ('Neurologists', 'Neurologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'), ('Radiologists', 'Radiologists'), ('Physician', 'Physician')], max_length=50, null=True)),
                ('availablity', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('symptoms', models.CharField(choices=[('Fever', 'Fever'), ('Body Ache', 'Body Ache'), ('Cold', 'Cold'), ('Cough', 'Cough'), ('Difficulty in Breathing', 'Difficulty in Breathing'), ('Loss in smell and taste', 'Loss in smell and taste')], max_length=200, null=True)),
                ('severity', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('alloted', models.BooleanField(default=False)),
                ('assigned_doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='healthcare2.doctor')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(auto_now_add=True, null=True)),
                ('appointment_time', models.TimeField(auto_now=True)),
                ('medicine', models.TextField(max_length=100, null=True)),
                ('diet', models.TextField(max_length=500, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='healthcare2.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='healthcare2.patient')),
            ],
        ),
    ]