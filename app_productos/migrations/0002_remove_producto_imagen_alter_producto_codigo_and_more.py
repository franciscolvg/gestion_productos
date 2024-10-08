# Generated by Django 5.1 on 2024-08-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('local', 'Local'), ('internacional', 'Internacional')], max_length=20),
        ),
    ]
