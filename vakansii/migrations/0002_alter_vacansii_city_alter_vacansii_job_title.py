# Generated by Django 4.0.5 on 2022-08-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vakansii', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacansii',
            name='city',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Чуй', 'Чуй'), ('Нарын', 'Нарын'), ('Ысык-Кол', 'Ысык-Кол'), ('Баткен', 'Баткен'), ('Талас', 'Талас'), ('Ош', 'Ош'), ('Другой город', 'Другой город')], max_length=150, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='vacansii',
            name='job_title',
            field=models.CharField(choices=[('Администратор', 'Администратор'), ('Официант', 'Официант'), ('Бармен', 'Бармен'), ('Уборщица', 'Уборщица'), ('Посудамойщица', 'Посудамойщица'), ('Повар', 'Повар'), ('Шеф-повар', 'Шеф-повар'), ('Хостес', 'Хостес')], max_length=100, null=True, verbose_name='Должность'),
        ),
    ]
