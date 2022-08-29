from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def home_view_pawel(request):
    essay = [
        {
            'title':       'Learning Python is a long run, not a sprint',
            'description': 'Intro do eseju',
            'slug':        'Learning-Python-is-a-long-run-not-a-sprint',
            'pict':        'C:/Users/b2b/Desktop/pikachu z png na jpeg.jpg',
            'location':    'Powidz'
        },
        {
            'title':       'Jakiś drugi artykuł, zapchaj dziura - może dodatkowa część tego mojego pierwszego',
            'description': 'treść artykułu',
            'slug':        'The-second-essay',
            'pict':        'C:/Users/b2b/Desktop/pikachu z png na jpeg.jpg',
            'location':    'Wrocław'
        }
    ]


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