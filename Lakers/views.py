from django.shortcuts import render

def index(request):
    return render(request, "Lakers/index.html")

def elenco(request):
    return render(request, "Lakers/elenco.html")

def sobre(request):
    return render(request, "Lakers/sobre.html")

