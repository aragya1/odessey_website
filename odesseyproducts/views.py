from django.shortcuts import render

def homepage(request):
    return render(request,"odesseyproducts/templates/index.html")