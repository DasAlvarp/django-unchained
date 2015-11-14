from django.shortcuts import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])

def index(request):
    return HttpResponse("OMG YOU CAN SEE A THING!")