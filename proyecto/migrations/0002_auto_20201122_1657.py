# Generated by Django 3.1.3 on 2020-11-22 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='nombre_medicamento',
            new_name='medicamento',
        ),
    ]
