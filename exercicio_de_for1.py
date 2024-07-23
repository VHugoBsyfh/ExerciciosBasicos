print("*******************************")
print("**3°Minigame Ordem Paranormal**")
print("*******************************")
melhor_media = 0  # a melhor pontuação
media_de_todos = []  # todas as medias dos avaliadores
resultado_final = 0
media_todos_avaliados = []  # notas finais dos avaliados
nomes_media = []
for i in range(0, 3):
    media_do_avaliado = 0  # media geral do avaliado
    avaliado = input("O monstro de quem está sendo avaliado?")
    for a in range(0, 2):
        nome_jogador = input("Nome do avaliador:")
        criatividade = float(input("Qual sua nota pra criatividade?"))
        historia = float(input("Qual sua nota pra história?"))
        nivel_de_ameaca_medo = float(input("Qual sua nota pro nivel de ameaça/medo?"))
        paranormal = float(input("O quão bem usou o paranormal?"))
        #viavel = input("O mosntro é viavel ?")
        #if (viavel != "sim"):
            #debate = input("Defenda seu ponto, isso é debativel\nContuinua?")
            #if (debate != "sim"):
                #raise ValueError("O monstro não é mais viavel")
        media = (criatividade + historia + nivel_de_ameaca_medo + paranormal) / 4
        print(f"A media de nota do(a) {nome_jogador} é de {media}")
        print("*****************************************")
        media_de_todos.append(media)
        media_do_avaliado += media
        if (media > melhor_media):
            melhor_media = media
    print("*****************************************")
    print(f"Curiosidade: a nota mais alta que o(a) {avaliado} recebeu foi {melhor_media}")
    #print(f"A media de notas foi respectivamente {media_de_todos[i]}, ou seja...")
    print(f"A pontuação do {avaliado} é de {media_do_avaliado} \n*****************************************")
    media_todos_avaliados.append(media_do_avaliado)

    #teste = str(media_todos_avaliados)
    #teste2 = []
    #teste2.append(avaliado[i] +teste)
    #print(teste2)

    if (media_todos_avaliados[i] > resultado_final):
        resultado_final = media_todos_avaliados[i]
print(f"o ganhador foi o maluco com uma media de {resultado_final} pontos")
