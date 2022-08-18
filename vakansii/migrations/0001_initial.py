# Generated by Django 4.0.5 on 2022-08-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacansii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('requirement', models.CharField(max_length=150, null=True, verbose_name='Требования')),
                ('responsibilities', models.CharField(max_length=300, null=True, verbose_name='Обязанности')),
                ('terms', models.CharField(max_length=150, null=True, verbose_name='Условия')),
                ('income', models.CharField(max_length=150, null=True, verbose_name='Доход')),
                ('city', models.CharField(max_length=150, null=True, verbose_name='Город')),
                ('contact_person', models.CharField(max_length=150, verbose_name='Контактное лицо')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Создать ваканцию',
            },
        ),
    ]