# Generated by Django 5.1.6 on 2025-05-08 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_carhistory_name_repair_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carhistory',
            name='date_of_repair',
            field=models.DateField(default=datetime.datetime(2025, 5, 8, 15, 13, 50, 861786)),
        ),
        migrations.AlterField(
            model_name='carhistory',
            name='status',
            field=models.CharField(choices=[('Обработка', 'В обработке'), ('Выполняется', 'В ремонте'), ('Готово', 'Готово к выдаче'), ('Выдан', 'Завершено')], default='Обработка', max_length=100),
        ),
    ]
