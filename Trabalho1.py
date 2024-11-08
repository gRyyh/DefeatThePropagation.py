#DefeatThePropagation.py
print("As pragas estão se propagando pelo universo...")
print("O Rei do Enxame voltou....")
print("Você deve derrotar ele e suas pragas...")
print("Antes que seja tarde....")

personagens = []

Aventurine = {
    "vida":15,
    "atk":8,
    "caminho": "Preservação",
    "nome": "Aventurine"
}

Blade = {
    "vida":8,
    "atk":20,
    "caminho": "Destruição",
    "nome": "Blade"
}

Feixiao={
    "vida":10,
    "atk":15,
    "caminho": "Caça",
    "nome": "Feixiao"
}

Besouros={
    "vida":12,
    "atk":4,
    "nome": "Besouro"
}

Skaracabaz={
    "vida":50,
    "atk":7,
    "nome": "Skaracabaz"
}

Tayzzyronth={
    "vida":65,
     "atk":10,
     "nome": "Tayzzyronth"
}
personagens.append(Aventurine)
personagens.append(Blade)
personagens.append(Feixiao)

inventario = []

def batalhar_inimigo(personagem, inimigo):
    if inimigo["vida"] <= 0:
        print(f"{inimigo["nome"]} foi derrotado!")
    else:
        dano = personagem["atk"]
        inimigo["vida"] -= dano
        print(f"{personagem["nome"]} causou {dano} de dano em {inimigo["nome"]}.\nEle agora ficou com {inimigo["vida"]} pontos de vida.")

personagem = int(input("Escolha seu personagem: '0 - Aventurine(A Preservação)' , '1- Blade(A Destruição)', '2- Feixiao(A Caça)': "))
personagem_principal = personagens[personagem]

while True:
    print("Você esta andando pela Estação Espacial...")
    print("Ouve um som de inseto...")
    print("*BESOUROS APARECERAM!*")
    escolha = input("voce deseja enfrentá-los? 'sim' ou 'não'? ")
    if escolha == 'não':
        print("Você não cumpriu a missão!")
        break
    elif escolha == 'sim':
        print("Derrote os Besouros para prosseguir!")
                        
        print(batalhar_inimigo(personagem_principal, Besouros))
            
        if personagem_principal["vida"] <= 0:
            break
            
        print("Você recebeu 'poção de vida'(+11 de vida)")
        inventario.append('poção de vida')
            
        personagem_principal["vida"] += 11
            
        if Besouros["vida"] <= 0:
                
            print("Você derrota os Besouros...")
            print("Porém...")
            print("Eles começam a se fundir...")
            print("Uma explosão acompanhada de um grunido alto e som de asas ecoa...")
            print("SKARACABAZ-(O Grande Besouro Sintético)")
            opcao = input("Você deseja enfrentá-lo para obter poção de Qlipoth? 'sim' ou 'não': ")
            if opcao=='não':
             print("Arregou!")
             break
            if opcao=='sim':
                while personagem_principal["vida"] > 0 or Skaracabaz["vida"] > 0:
                    print("Derrote SKARACABAZ para prosseguir")
                    agir=input("Você deseja: 'atacar',?")
                    if agir=='atacar':
                            if personagem_principal["caminho"] == "Destruição":
                                personagem_principal["vida"] -= 1
                                
                            if personagem_principal["vida"] <= 0:
                                print("Você foi morto!")
                                break
                            else:
                                batalhar_inimigo(personagem_principal, Skaracabaz)
                            
                            if Skaracabaz["vida"] <= 0:
                                print("Você derrotou SKARACABAZ...")
                                break
                            else:
                                batalhar_inimigo(Skaracabaz, personagem_principal)
                        
                                
                opc=input("Voce quer continuar sua jornada?'sim', ou 'não': ")
                if opc=="não":
                    print("Você encerrou sua jornada, mas ainda há um perigo maior solto no universo...")
                    print("FIM?")
                    break
                else:
                    print("Você continua andando pela Estação Espacial...")
                    print("Você acha outros besouros pelo caminho...")
                    print("Você resolve segui-los...")
                    print("Você encontra o coração e a causa desta infestação...")
                    print("TAYZZYRONTH-O AEON DA PROPAGAÇÃO")
                    print("Derrote TAYZZYRONTH para vencer!")
                    
                while personagem_principal["vida"] > 0 or Tayzzyronth["vida"] > 0:
                        print("Derrote TAYZZYRONTH para vencer!")
                        agir=input("Você deseja: 'atacar'?")
                        if agir=='atacar':
                            if personagem_principal["caminho"] == "Destruição":
                                personagem_principal["vida"] -= 1
                            
                            if personagem_principal["vida"]<=0:
                                print("TAYZZYRONTH derrotou você!")
                                break
                            else:
                                batalhar_inimigo(personagem_principal, Tayzzyronth)
                            if Tayzzyronth["vida"]<=0:
                                print("TAYZZYRONTH foi derrotado!")
                                break
                            batalhar_inimigo(Tayzzyronth, personagem_principal)
                                
        print("Você derrotou TAYZZYRONTH!...")
        print("A ameaça da PROPAGAÇÃO foi derrotada!")
        print("O universo esta salvo!")
        print("Por enquanto...")
        print("FIM!")
        print("Créditos:\nCriador do Programa:Gregory\nInspiração:Jogo Honkai Star Rail da Hoyoverese\nAula Python é bem legal :)")
        break        
    else:
        print("Opção inválida")
