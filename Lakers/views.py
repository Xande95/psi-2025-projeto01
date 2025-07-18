from django.shortcuts import render

def index(request):
    return render(request, "Lakers/index.html")


lista_jogadores = [ 
    {
        "id": 1,
        "nome": "LeBron James",
        "posicao": "Ala-Pivô",
        "numero": "23",
        "foto": "Lakers/img/LeBronJames.jpg",
    },
    {
        "id": 2,
        "nome": "Luka Dončić",
        "posicao": "Armador",
        "numero": "77",
        "foto": "Lakers/img/luka_don.jpeg",
    },
    {
        "id": 3,
        "nome": "Austin Reaves",
        "posicao": "Armador",
        "numero": "15",
        "foto": "Lakers/img/austin_reaves.jpeg",
    },
    {
        "id": 4,
        "nome": "Bronny James",
        "posicao": "Armador",
        "numero": "9",
        "foto": "Lakers/img/bronny.jpeg",
    },
    {
        "id": 5,
        "nome": "Rui Hachimura",
        "posicao": "ala-pivô",
        "numero": "28",
        "foto": "Lakers/img/hachimura.jpeg",
    },
    {
        "id": 6,
        "nome": "Gabe Vicent",
        "posicao": "Ala-Armador",
        "numero": "7",
        "foto": "Lakers/img/gabe_vicent.jpeg",
    },
    {
        "id": 7,
        "nome": "Jaxon Hayes",
        "posicao": "Pivô",
        "numero": "11",
        "foto": "Lakers/img/jaxson_Hayes.jpeg",
    },
    {
        "id": 8,
        "nome": "Dalton Knecht",
        "posicao": "Armador",
        "numero": "4",
        "foto": "Lakers/img/dalton.jpeg",
    },
    {
        "id": 9,
        "nome": "Alex Len",
        "posicao": "Pivô",
        "numero": "27",
        "foto": "Lakers/img/len.jpeg",
    },
    {
        "id": 10,
        "nome": "Shake Milton",
        "posicao": "Ala-Pivô",
        "numero": "20",
        "foto": "Lakers/img/shake_milton.png",
    },
    {
        "id": 11,
        "nome": "Trey Jemisson III",
        "posicao": "Pivô",
        "numero": "55",
        "foto": "Lakers/img/trey.png",
    },
]

def jogadores(request):
    context = {
        "jogadores": lista_jogadores,
        }
    return render(request, "Lakers/jogadores.html", context)
    


lista_sobre = {
    "historia": """    O Los Angeles Lakers é uma das franquias mais tradicionais e vitoriosas da história da NBA. Fundado em 1947, originalmente em Minneapolis, o time era conhecido como Minneapolis Lakers e conquistou cinco títulos antes de se mudar para Los Angeles em 1960. Ao longo das décadas, o Lakers se destacou com grandes estrelas como Magic Johnson, Kareem Abdul-Jabbar, Shaquille O'Neal, Kobe Bryant e atualmente LeBron James. A equipe é reconhecida por suas inúmeras conquistas, rivalidades históricas, especialmente com o Boston Celtics, e por sua grande influência na cultura esportiva e popular dos Estados Unidos. Os Lakers possuem dezenas de títulos de conferência e mais de 15 campeonatos da NBA, sendo considerados uma das franquias mais icônicas do basquete mundial.
""",    
    "titulos": """Conferencia Leste: 32,
    NBA: 17 títulos (segundo maior campeão),
    Copa NBA: 1 e Wellington Mouse"""
}

def sobre(request):
    return render(request, "Lakers/sobre.html", lista_sobre)