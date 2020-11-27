from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static

from django.views import View

class MyView(View):

    def get(self, request):
        print(request.GET)
        return HttpResponse("This is GET")

    def post(self, request):
        print(request.POST)
        return HttpResponse("This is POST")

def main(request):
    # return HttpResponse("<button>Some Button</button>")
    return render(request, "main.html")

def text(request):
    return HttpResponse("This is the text from backend to user interface")

def file(request):
    # image = open(static('img/001.jpg'), 'rb+')
    image = open('lesson_3/static/img/001.jpg', 'rb+')
    print(image)
    # print(static('img/001.jpg'))
    return FileResponse(image)

def redirect(request):
    return HttpResponseRedirect("https://www.google.com")

def not_allowed(request):
    return HttpResponseNotAllowed("You Shall Not Pass!!!")

def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)