from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    return HttpResponse("homepage")


def about_page_view(request):
    context = {
        "name": "Ernest",
        "age": 20,
    }
    return render(request, "pages/about.html",context)
