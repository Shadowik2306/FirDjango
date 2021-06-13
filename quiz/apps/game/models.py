from django.db import models


class Question(models.Model):
    question_text = models.CharField("Вопрос", max_length=50)
    answer_a = models.CharField("Вариант А", max_length=30)
    answer_b = models.CharField("Вариант B", max_length=30)
    answer_c = models.CharField("Вариант C", max_length=30)
    answer_d = models.CharField("Вариант D", max_length=30)
    right_answer = models.CharField('Правильный вариант', max_length=5)
    radio = models.BooleanField('Один вариант ответа')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class User(models.Model):
    nickname = models.CharField('Ник', max_length=100, unique=True)
    choice = models.TextField('Ответы')
    finish = models.IntegerField('Какой процент выполнен')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'