from django.shortcuts import render

# Create your views here.

def cv_index(request):
    return render(request, "index.html")