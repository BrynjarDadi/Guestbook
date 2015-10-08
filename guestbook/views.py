from django.shortcuts import render

# Create your views here.
from .models import Text
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404



def index(request):
    latest_question_list = Text.objects.order_by('-pub_date')[:5]
    template = loader.get_template('guestbook/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def entry(request, question_id):
    try:
        entry = Text.objects.get(pk=question_id)
    except Text.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'guestbook/entry.html', {'entry': entry})

    """
    response = "You're looking at the results of question."
    return HttpResponse(response)
"""
