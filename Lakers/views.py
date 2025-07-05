from django.shortcuts import render

def index(request):
    return render(request, "Lakers/index.html")


jogadores = [ 
    {
        "id": 1,
        "Nome": "LeBron James",
        "Posição": "Ala-Pivô",
        'Número': "23",
        "foto": 0,
        },
    {
        "id": 2,
        "Nome": "Luka Doncit",
        "Posição": "Armador",
        'Número': "77",
        "foto":0,
        },
    {
        "id": 3,
        "Nome": "Austin Reaves",
        "Posição": "Armador",
        'Número': "15",
        "foto":0,
    },
]


def jogadores(request):
    return render(request, "Lakers/jogadores.html")
    


def sobre(request):
    return render(request, "Lakers/sobre.html") 

