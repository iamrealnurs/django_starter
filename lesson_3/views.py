from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static

def main(request):
    # return HttpResponse("<button>Some Button</button>")
    return render(request, "main.html")

def text(request):
    return HttpResponse("This is the text from backend to user interface")

def file(request):
    print(static('img/001.jpg'))
    return FileResponse(open(static('img/001.jpg'), "rb+"))

def redirect(request):
    return HttpResponseRedirect("https://www.google.com")

def not_allowed(request):
    return HttpResponseNotAllowed("You Shall Not Pass!!!")

def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)