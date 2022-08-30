from django.shortcuts import render
# from django.http import HttpResponse

from .models import EssayCls

# Create your views here.


def home_view_pawel(request):
    essay = EssayCls.objects.all()

    # return HttpResponse('Test')
    return render(
        request,
        'pawel_pedryc_developer/pawel_pedryc.html',
        {
        'text_content': essay,
        'show_text_content': True
        })


def my_essays(request, home_view_pawel_slug):
    print("print('home_view_pawel_slug'):", home_view_pawel_slug)
    selected_essay = {
        'title':       'A first essay is this',
        'description': 'this is description'
        }

    return render(
        request,
        'pawel_pedryc_developer/learning-programming-is-a-long-run-not-a-sprint.html',
        {
        'essay_title': selected_essay['title'],
        'essay_description': selected_essay['description']
        })