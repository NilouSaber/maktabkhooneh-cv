from django.shortcuts import render

# Create your views here.

def cv_index(request):
    context = {'name_family':'Amir Shabanpour', 
    'email':'amir.shabanpoor92@gmail.com', 
    'birthday':'7 Feb 1992',
    'phone': '+98 911 216 7714',
    'city': 'Babolsar, Iran',
    'degree': 'Master',
    'freelance' : 'Available',
    'age': '32'}
    return render(request, "website/index.html", context)