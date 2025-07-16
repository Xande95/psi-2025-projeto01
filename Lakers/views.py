from django.shortcuts import render

def index(request):
    return render(request, "Lakers/index.html")


lista_jogadores = [ 
    {
        "id": 1,
        "Nome": "LeBron James",
        "posicao": "Ala-Pivô",
        'Número': "23",
        "foto": "{% static 'Lakers/img/LebBronJames.jpg' %} ",
        },
    {
        "id": 2,
        "Nome": "Luka Dončić",
        "posicao": "Armador",
        'Número': "77",
        "foto":"{% static 'Lakers/img/luka_don.jpeg' %} ",
        },
    {
        "id": 3,
        "Nome": "Austin Reaves",
        "posicao": "Armador",
        'Número': "15",
        "foto":"{% static 'Lakers/img/austin_reaves.jpeg' %} ",
    },
    {   "id": 4,
        "Nome": "Bronny James",
        "posicao": "Armador",
        'Número': "9",
        "foto":"{% static 'Lakers/img/bronny.jpeg' %} ",
        },

        {"id": 5,
        "Nome": "Rui Hachimura",
        "posicao": "ala-pivô",
        'Número': "28",
        "foto":"{% static 'Lakers/img/hachimura.jpeg' %} ",},

        {"id": 6,
        "Nome": "Gabe Vicent",
        "posicao": "Ala-Armador",
        'Número': "7",
        "foto":"{% static 'Lakers/img/gabe_vincent.jpeg' %} ",},

        {"id": 7,
        "Nome": "Jaxon Hayes",
        "posicao": "Pivô",
        'Número': "11",
        "foto":"{% static 'Lakers/img/jaxson_reyes.jpeg' %} ",},

        {"id": 8,
        "Nome": "Dalton Knecht",
        "posicao": "Armador",
        'Número': "4",
        "foto":"{% static 'Lakers/img/dalton.jpeg' %} ",},

        {"id": 9,
        "Nome": "Alex Len",
        "posicao": "Pivô",
        'Número': "27",
        "foto":"{% static 'Lakers/img/len.jpeg' %} ",},

        {"id": 10,
        "Nome": "Shake Milton",
        "posicao": "Ala-Pivô",
        'Número': "20",
        "foto":"{% static 'Lakers/img/shake_milton.png' %} ",},

        {"id": 11,
        "Nome": "Trey Jemisson III",
        "posicao": "Pivô",
        'Número': "55",
        "foto":"{% static 'Lakers/img/trey.png' %} ",},
        ]


def jogadores(request):
    context = {
        'jogadores': lista_jogadores
    }
    return render(request, "Lakers/jogadores.html", context)
    


lista_sobre = {
    "historia": """1947–1958: Início e a dinastia de Minneapolis 
    A franquia dos Lakers começou em 1947, quando Ben Berger e Morris Chalfen, de Minnesota, compraram a recentemente dissolvida franquia Detroit Gems da National Basketball League (NBL) por US$15,000 do fundador/proprietário dos Gems, 
    C. King Boring, e seu parceiro de negócios, Maury Winston.[11] Eles contrataram John Kundla como seu primeiro treinador principal.Berger e Chalfen realocaram o time para Minneapolis, com jogos em casa sendo disputados no Minneapolis Auditorium e no Minneapolis Armory. O time que Berger e Chalfen compraram consistia apenas de equipamentos; já que o time parecia estar prestes a fechar, todos os seus jogadores já haviam sido designados para outras equipes da NBL. A franquia foi rebatizada como "Lakers" em referência ao apelido de Minnesota, 
    "A Terra dos 10.000 Lagos".[12] Berger e Chalfen trouxeram Max Winter, que mais tarde se tornaria um dos fundadores e proprietários do Minnesota Vikings da NFL, para ser o novo gerente geral dos Lakers. Winter também adquiriu uma participação na equipe, que ele manteria até deixar os Lakers em 1955.

    Como os Gems tinham o pior recorde da NBL, os Lakers tiveram a primeira escolha no draft de dispersão da Professional Basketball League of America de 1947, que usaram para selecionar George Mikan, que mais tarde se tornaria um dos maiores pivôs de sua época. Com Mikan, o novo treinador John Kundla e uma infusão de ex-jogadores da Universidade de Minnesota para substituir os que foram perdidos antes da realocação, os Lakers venceram o título da NBL em sua primeira temporada.[13] Uma semana antes das finais da NBL, os Lakers venceram o torneio anual World Professional Basketball, onde Mikan foi nomeado MVP após marcar um recorde de 40 pontos contra o New York Renaissance no jogo decisivo do título.[14]
    1975–1979: O Capitão – Kareem Abdul-Jabbar

    Los Angeles adquiriu Kareem Abdul-Jabbar em 1975. Ele ganhou três Prêmios de MVP da NBA, um Prêmio de MVP das Finais e cinco títulos com a equipe.
    Lew Alcindor, agora conhecido como Kareem Abdul-Jabbar, queria sair de Milwaukee, e os Lakers o adquiriram em uma troca. Seu primeiro ano em Los Angeles resultou em seu quarto prêmio de MVP da NBA, após ele ter média de 27,7 pontos e liderar a NBA com médias de 16,9 rebotes e 4,12 bloqueios. Mas os Lakers falharam em chegar aos playoffs novamente com um recorde de 40-42.[41] Os Lakers voltaram à forma na temporada de 1976-77, com o melhor recorde da NBA em 53-29.[42] Depois de vencerem o Golden State Warriors,[43] eles foram varridos por 4-0 nas Finais da Conferência Oeste pelo eventual campeão da NBA, Portland Trail Blazers de Bill Walton.[44]

    Em 9 de dezembro de 1977 ocorreu um dos momentos mais feios da história dos esportes profissionais. O futuro treinador dos Lakers, Rudy Tomjanovich, então do Houston Rockets, correu para a quadra na tentativa de interromper uma briga entre Kermit Washington dos Lakers e Kevin Kunnert dos Rockets. Washington, no canto do olho, viu que havia um jogador adversário correndo em sua direção. Instintivamente, pensando que seria atacado, Washington se virou e desferiu um golpe devastador no rosto de Tomjanovich, que corria diretamente em direção ao soco. Tomjanovich foi atingido tão fortemente que seu primeiro pensamento ao acordar foi que o placar da arena deve ter caído do teto sobre ele. O soco havia rachado o crânio de Tomjanovich e quase acabou com sua carreira. Ele ficou de fora pelo resto da temporada, precisando de cirurgia reconstrutiva para reparar sua mandíbula, olho e bochecha. Alguns dos que testemunharam o evento disseram que o golpe foi tão esmagador que, até verem Tomjanovich se movendo enquanto ele estava no chão, temiam que ele pudesse estar morto. Washington recebeu uma punição de suspensão de 60 jogos e uma multa, e o incidente permanece um capítulo sombrio na história dos Lakers. A cena chocante se tornou o momento definidor não apenas da temporada de 1977-78 dos Rockets (uma equipe finalista da conferência no ano anterior, colapsaram para o último lugar com um recorde de 28-54), mas também das carreiras profissionais de dois jogadores. Tomjanovich passou os cinco meses seguintes em reabilitação, eventualmente retornando para jogar e sendo até selecionado para o All-Star Game da NBA.

    Na temporada de 1977-78, os Lakers terminaram apenas em 4º na sua divisão com um recorde de 45-37[45] e foram eliminados nos playoffs pelos eventual campeões Seattle SuperSonics.[46] Na temporada seguinte, tiveram um recorde de 47-35 e terminaram em terceiro na divisão.[47] Eles venceram os Denver Nuggets nos playoffs e mais uma vez caíram para os SuperSonics.[48]
    1996–2004: Dinastia de O'Neal e Bryant


    Os futuros Hall da Fama Shaquille O'Neal (esquerda) e Kobe Bryant (direita), ajudaram os Lakers a vencer o tri-campeonato da NBA. Apesar de se entenderem bem na quadra, eles tiveram muitos problemas de relacionamente fora dela.
    Durante a temporada de 1996-97, os Lakers adquiriram o jovem de 17 anos Kobe Bryant do Charlotte Hornets em troca de Vlade Divac; Bryant foi selecionado na 13ª posição no draft daquele ano, vindo da Lower Merion High School em Ardmore, Pensilvânia, pelo Charlotte.[87] Los Angeles também assinou com o agente livre e ex-pivô do Orlando Magic, Shaquille O'Neal.[88""",    
    "titulos": """Conferencia Leste: 32
    NBA: 17 títulos (segundo maior campeão)
    Copa NBA: 1"""
}

def sobre(request):
    return render(request, "Lakers/sobre.html", lista_sobre)