from django.shortcuts import render

# Create your views here.

def adding_css(request):
    return render(request,'adding_css.html')