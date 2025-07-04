from django.shortcuts import render

def index(request):
    return render(request, "Lakers/index.html")

def elenco(request):
    return render(request, "Lakers/elenco.html")
    jogadores{
        "id": 1,
        "Nome": "LeBron James",
        "Posição": "Ala-Pivô",
        'Número': "23",

        "id": 2,
        "Nome": "Luka Doncit",
        "Posição": "Armador",
        'Número': "77",

        "id": 3,
        "Nome": "Austin Reaves",
        "Posição": "Armador",
        'Número': "15",
    }

def sobre(request):
    return render(request, "Lakers/sobre.html")

