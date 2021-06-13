from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import *

error_message = ''
new_user = False

def anti_cheat(name):
    print('hello anti_cheat', User.objects.get(nickname=name).finish)
    if User.objects.get(nickname=name).finish != -1:
        return True
    return False

def start_page(request):
    params = {
        'error_message': error_message,
        'new_user': new_user
    }
    return render(request, 'game/start_page.html', params)


def reset(request):
    global error_message, new_user
    error_message = ''
    user = User.objects.get(nickname=new_user)
    user.finish = -1
    user.choice = {'question': {i: '' for i in range(1, 6)}}
    user.save()
    new_user = False
    return HttpResponseRedirect(reverse('game:question', args=[user.nickname, 1]))


def start_test(request):
    global error_message, new_user
    error_message = ''
    new_user = False
    print(request.POST)
    name = request.POST['nickname']
    if 'reset' not in request.POST:
        if not name:
            error_message = "Поле ввода не заполнено"
            return HttpResponseRedirect(reverse('game:start_page'))
        k = User.objects.filter(nickname=name)
        if len(k):
            error_message = 'Пользователь с данным именем существует. Хотите заменить?'
            new_user = name
            return HttpResponseRedirect(reverse('game:start_page'))
    new_user = User(nickname=name, number_of_question=1,
                    choice={
                        'question': {i: '' for i in range(1, 6)}
                    }, finish=-1)
    new_user.save()
    return HttpResponseRedirect(reverse('game:question', args=[name, 1]))


def question(request, name, question_id):
    try:
        real_question = Question.objects.get(id = question_id)
        real_user = User.objects.get(nickname=name)
    except:
        raise Http404("Вопрос не найден")

    if anti_cheat(name):
        return HttpResponseRedirect(reverse('game:finish_act', args=[name]))

    dct = eval(real_user.choice)
    params = {
        'real_question': real_question,
        'real_user': real_user,
        'chosen': ''.join(dct['question'][question_id])
    }
    return render(request, 'game/test_page.html', params)


def choose_question(request, name, question_id):
    try:
        real_user = User.objects.get(nickname=name)
    except:
        raise Http404()
    dct = eval(real_user.choice)
    if 'A' not in request.POST:
        s = []
    else:
        s = dict(request.POST)['A']
    print(s)
    dct['question'][question_id] = s
    real_user.choice = dct
    real_user.save()
    if request.POST:
        print(request.POST)
        if 'next' in request.POST:
            if question_id + 1 > 5:
                return HttpResponseRedirect(reverse('game:finish_part', args=[name]))
            return HttpResponseRedirect(reverse('game:question', args=[name, question_id + 1]))
        elif 'return' in request.POST:
            return HttpResponseRedirect(reverse('game:question', args=[name, question_id - 1]))


def finish_part(request, name):
    try:
        real_user = User.objects.get(nickname=name)
    except:
        raise Http404()

    if anti_cheat(name):
        return HttpResponseRedirect(reverse('game:finish_act', args=[name]))

    params = {
        'real_user': real_user
    }
    return render(request, 'game/finish_part.html', params)


def finish_part_post(request, name):
    if 'next' in request.POST:
        return HttpResponseRedirect(reverse('game:finish_act', args=[name]))
    elif 'return' in request.POST:
        return HttpResponseRedirect(reverse('game:question', args=[name, 5]))


def finish_act(request, name):
    try:
        real_user = User.objects.get(nickname=name)
    except:
        raise Http404()
    if not anti_cheat(name):
        dct = eval(real_user.choice)
        right_ans = 0
        for i in range(1, 6):
            if set(dct['question'][i]) - set(Question.objects.get(id = i).right_answer) == set():
                right_ans += 1
            else:
                print(set(dct['question'][i]), set(Question.objects.get(id = i).right_answer))
        real_user.finish = int(right_ans / 5 * 100)
        real_user.save()
    params = {
        'real_user': real_user,
    }

    return render(request, 'game/finish_act.html', params)


def finish_act_post(request, name):
    return HttpResponseRedirect(reverse('game:start_page'))