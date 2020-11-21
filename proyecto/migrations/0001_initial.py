# Generated by Django 3.1.3 on 2020-11-21 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_city', to='proyecto.city')),
                ('employee_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_title', to='proyecto.title')),
            ],
        ),
    ]
