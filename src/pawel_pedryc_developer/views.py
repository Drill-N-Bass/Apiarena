from django.shortcuts import render
# from django.http import HttpResponse

from .models import EssayCls

# Needed for display log with the error exeption function:
# https://realpython.com/the-most-diabolical-python-antipattern/
import logging

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
    # print("print('home_view_pawel_slug'):", home_view_pawel_slug)

    try:
        selected_essay = EssayCls.objects.get(slug=home_view_pawel_slug)
        return render(
        request,
        'pawel_pedryc_developer/learning-programming-is-a-long-run-not-a-sprint.html', 
        {
            'essay_found': True,
            'essay_all': selected_essay
        })
    except Exception as exc:
        return render(
            request,
            'pawel_pedryc_developer/learning-programming-is-a-long-run-not-a-sprint.html', 
            {
                'essay_found': False
            }
            )


            # 'essay_title': selected_essay.title,
            # 'essay_description': selected_essay.description,
            # 'essay_prog_language': selected_essay.language