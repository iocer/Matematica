#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Question


def indexs(request):
    return HttpResponse(
        '''!!!!Bibenido¡¡¡¡
                  <br/> Esta es una pagina web de prueba 
                  <br/> Estamos trabajando para mejorarla'''
    )

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "Usted esta buscando el resultado de la pregunta: %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estás votando sobre la pregunta %s." % question_id)




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))