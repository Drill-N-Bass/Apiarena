from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view_pawel(request):
    # return HttpResponse('Test')
    return render(request, 'home_page_pawel_template/pawel_pedryc.html')