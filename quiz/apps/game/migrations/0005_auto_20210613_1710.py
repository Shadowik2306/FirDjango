# Generated by Django 3.2 on 2021-06-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20210613_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='number_of_question',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_b',
            field=models.CharField(max_length=30, verbose_name='Вариант B'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_c',
            field=models.CharField(max_length=30, verbose_name='Вариант C'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_d',
            field=models.CharField(max_length=30, verbose_name='Вариант D'),
        ),
    ]
