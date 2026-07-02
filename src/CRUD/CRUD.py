
nome = None 
nome2 = None
idade = None
idade2 = None


def Menu():
    
    while True:
        print(f"\n === MENU PRINCIPAL === ")
        print("1. Adicionar nome e idade [+]")
        print("2. Editar nome e idade [Edit]")
        print("3. Ler nome e idade [Read]")
        print("4. Apagar nome e idade [X]")
        print("0. Sair [...]")

        op = int(input(("Insira numero da opção escolhida - > ")))
        print("")
        
        match op:
            case 1: Criar()
            case 2: Editar()
            case 3: Ler()
            case 4: Apagar()
            case 0: 
                print("Encerrando programa...")
                break
            case _: print(f"\n +++ Opção inexiste! Tente uma que esteja no menu +++ \n")

def Ler():
    global nome, idade, nome2, idade2
    
    print("")
    print(" === Lista de nomes e idade ===") 
    if nome and idade and nome2 and idade2 == None:
        print(f"\n +++ Lista totalmente vazia! +++ \n")
    else:
        print(f"1. Nome: {nome}  | Idade: {idade}")
        print(f"2. Nome: {nome2} | Idade: {idade2}")
    print("")
    
def Criar():
    global nome, idade, nome2, idade2
    op = int(input("[#] Insira o indice da linha que deseja criar: "))
    
    
    if nome or nome2 or idade or idade2 != None:
        print(f"\n +++ Linha já preenchida! Tente uma livre. +++\n1")
        return 
    

    if op == 1:
        nome = input(" [+] Crie o nome 1 -> ")
        idade = int(input(" [+] Crie idade 1 -> "))
    
    elif op == 2:
        nome2 = input(" [+] Crie o nome 2 -> ")
        idade2 = int(input(" [+] Crie idade 2 -> "))
    
    else:
        print(f"\n +++++ Invalido! Tente uma opção que esteja no menu. +++++ \n")
    print("")

def Apagar():
    
    global nome, idade, nome2, idade2
    print("")
    op = int(input("[X] Insira o indice da linha que deseja apagar: "))
    if op == 1:
        nome = None
        idade = None
    
    elif op == 2:
        nome2 = None
        idade2 = None
    
    else:
        print(f"\n +++++ Invalido! Tente uma opção que esteja no menu. +++++ \n")
    print("")

def Editar():
    
    global nome, idade, nome2, idade2
    print("")
    op = int(input("[Edit] Insira o indice da linha que deseja editar: "))
        
    if op == 1:
            nome = input("Edite o nome 1 -> ")
            idade = int(input("Edite idade 1 -> "))
    
    elif op == 2:
            nome2 = input("Edite o nome 2 -> ")
            idade2 = int(input("Edite idade 2 -> "))
    
    else:
            print(f"\n +++++ Invalido! Tente uma que esteja no menu. +++++ \n")
    print("")        

Menu()