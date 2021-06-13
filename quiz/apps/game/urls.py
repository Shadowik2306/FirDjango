from django.urls import path
from . import views


app_name = 'game'
urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('start_test/', views.start_test, name='start'),
    path('start_test/reset', views.reset, name='reset'),
    path('<str:name>/<int:question_id>/', views.question, name='question'),
    path('<str:name>/<int:question_id>/choose_question', views.choose_question,
         name='choose_question'),
    path('<str:name>/finish_part', views.finish_part, name='finish_part'),
    path('<str:name>/finish_part_post', views.finish_part_post, name='finish_part_post'),
    path('<str:name>/finish_act', views.finish_act, name='finish_act'),
    path('<str:name>/finish_act_post', views.finish_act_post, name='finish_act_post')
]