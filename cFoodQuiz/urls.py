from django.conf.urls import patterns, url
from cFoodQuiz import views

urlpatterns = patterns('',
    url(r'^$', views.index, name ='index'),
    url(r'^calculateQuiz$', views.quizCalc, name = 'quizCalc'),
    url(r'^result/(?P<string_arg>\w+)$', views.results, name = 'results'),
                       
)