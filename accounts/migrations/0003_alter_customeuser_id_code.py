# Generated by Django 4.2.5 on 2023-10-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customeuser_id_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='id_code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]