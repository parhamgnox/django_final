# Generated by Django 4.2.5 on 2023-10-17 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_portfolio_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 21, 55, 55, 504310)),
        ),
    ]