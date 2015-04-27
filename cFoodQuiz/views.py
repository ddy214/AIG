from django.shortcuts import render
from cFoodQuiz.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request, 'cFoodQuiz/index.html', {'questions':questions})

def quizCalc(request):
    #dictionary that keeps in track of points in each type of chinese cuisine
    chinese_region = {"west":0, "east":0, "north":0, "south":0}
    questions = Question.objects.all()
    max = "west"
    #test which type of cuisine was chosen
    for question in questions:
        if request.POST[question.question_text] == "west":
            chinese_region["west"]+=1
        elif request.POST[question.question_text] == "east":
            chinese_region["east"]+=1
        elif request.POST[question.question_text] == "north":
            chinese_region["north"]+=1
        else:
            chinese_region["south"]+=1
    #find the users preference in chinese cuisine by finding which cuisine the user liked more
    for region in chinese_region:
        if chinese_region[region] > chinese_region[max]:
            max = region

    return HttpResponseRedirect(reverse('results', kwargs={'string_arg':max}))

def results(request, string_arg):
    string_arg = str(string_arg)
    if string_arg == "south":
        return HttpResponse("You Like Things That Have Flavor And Variety\nYou Won't Go Wrong With Fried Rice")

    elif string_arg =="north":
        return HttpResponse("You Like Sweet and Tangy Things\nGo With Sweet and Sour Pork!\nYou Will Get A Crunch")

    elif string_arg == "east":
        return HttpResponse("You Like Things That Are Fresh\n Go With Chicken And Brocolli!\nLight And Delicious")

    else:
        return HttpResponse("You Like To Have A Party In Your Mouth!\nDo Yourself A Favor And Order Something HOT!!\nSichuan Chili Chicken Is The Way To GO")
