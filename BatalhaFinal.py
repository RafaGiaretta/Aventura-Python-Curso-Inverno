import random
import os

moedas = 500.0
ataque = 0.0
ataque_distancia = 0.0
defesa = 0.0
vida_h = 100.0

status = "Saudavel"

def ataque_aventureiro():
    ataque_espada = random.randint(15,20) + ataque
    ataque_arco = random.randint(15,20) + ataque_distancia
    ataque_soco = random.randint(5,10)

    if ataque == 0:
       print("[1] Atacar no Soco")
    else:
        print("[1] Atacar com Espada")

    if ataque_distancia > 0:
        print("[2] Arco e Flecha")

    escolha = input("Resposta: ")

    match escolha:
        case '1':
            if ataque == 0:
                dano = ataque_soco
                print (f"O aventureiro {nome} da um soco no inimigo e tira {dano} de dano.")
            else:
                dano = ataque_espada 
                print (f"O aventureiro {nome} da uma espadada no inimigo e tira {dano} de dano.")
        case '2':
            dano = ataque_arco
            print (f"O aventureiro {nome} acerta uma no inimigo e tira {dano} de dano.")
        case _:
            print("\nOpção Invalida.")   
    return dano  

os.system("cls")
nome = input("Insera o nome do aventureiro: ")
os.system("cls")

print(f"O aventureiro {nome} começou sua aventura e se deparou com uma bifurcação.")

print("O caminho da esquerda leva o aventureiro para um castelo assombrado.")

print("O caminho da direita leva o aventureiro para um pântano sombrio.")

escolha = input(f"\nPor qual caminho o aventureiro {nome} ira seguir: \n[1] Esquerda (Castelo Assombrado).\n[2] Direita (Pântano Sombrio).\nResposta: ")
os.system ("cls")

if escolha == '1':
    print("Adentrando ao Castelo o aventureiro encontra um homem velho afiando uma espada antiga.")
    print("-- O velho homem, o que você faz nesse castelo?")
    print("-- Eu que pergunto, o que você procura neste castelo?")
    escolha = input("\n[1] -- Estou em busca do meu próprio caminho. \n[2] -- Isso não é da sua conta velho. \nResposta: ")
    os.system("cls")

    if escolha == '1': 

        print("O velho o encara perplexo:\n-- Talvez um de meus itens possa te ajudar nessa jornada, algo lhe interesse. \nDisse o velho apontando na direção de uma armário de carvalho cheio de diversos itens:")
        
        while escolha == '1' and moedas > 0:
            print("\n------------------------- LOJA -------------------------")
            print("[1] Espada Grande (10 de Ataque)                 $400.00")
            print("[2] Espada Pequena (5 de Ataque)                 $300.00")
            print("[3] Arco e Flecha (5 de Ataque à Distancia)      $100.00")
            print("[4] Escudo Grande (10 de Defesa)                 $200.00")
            print("[5] Escudo Pequeno (5 de Defesa)                 $100.00")
            print("--------------------------------------------------------")

            print(f"\nSuas Moedas: ${moedas}")
            compra = input("Qual item deseja comprar: ")

            match compra:
                case '1':
                    if moedas < 400:
                        print("\nVocê não possuí moedas o suficiente.")
                    else:
                        moedas -= 400
                        ataque += 10
                        print(f"\nO aventureiro {nome} comprou uma Espada Grande.")
                case '2':
                    if moedas < 300:
                        print("\nVocê não possuí moedas o suficiente.")
                    else:
                        moedas -= 300
                        ataque += 5
                        print(f"\nO aventureiro {nome} comprou uma Espada Pequena.")
                case '3':
                    if moedas < 100:
                        print("\nVocê não possuí moedas o suficiente.")
                    else:
                        moedas -= 100
                        ataque_distancia += 5
                        print(f"\nO aventureiro {nome} comprou um Arco e Flecha.")
                case '4':
                    if moedas < 200:
                        print("\nVocê não possuí moedas o suficiente.")
                    else:
                        moedas -= 200
                        defesa += 10
                        print(f"\nO aventureiro {nome} comprou um Escudo Grande.")
                case '5': 
                    if moedas < 100:
                        print("\nVocê não possuí moedas o suficiente.")
                    else:
                        moedas -= 100
                        defesa += 5
                        print(f"\nO aventureiro {nome} comprou um Escudo Pequeno.")
                case _:
                    print("\nOpção Invalida.")
                    break               
            
            escolha = input("\nDeseja comprar outro item?\n[1] Sim.     [2] Não.\nResposta: ")
            
            if escolha == '1' and moedas == 0:
                print("\nVocê não possuí moedas o suficiente.")
                input("Clique em qualquer tecla para sair da loja...")

            os.system("cls")          
        print(f"O aventureiro {nome} seguiu seu caminho rumo ao interior do castelo.")
        input("\nClique em qualquer tecla para continuar sua aventura...")
        os.system("cls")

    else:
        print("O velho aponta a espada antiga em sua direção e o ameaça: \n-- Então de o fora daqui, pois você tera que prestar contas com minha espada afiada, JOVEM TOLO!!!")
        print(f"O aventureiro {nome} deu as costas ao senhor e seguiu seu caminho rumo ao interior do castelo.")
        input("\nClique em qualquer tecla para continuar sua aventura...")
        os.system("cls")

else:
    sorte = random.randint(0, 3)
    print(f"Caminhando pelo Pântano Sombrio, o aventureiro {nome} se deparou com um baú misterioso a sua frente:")
    escolha = input("[1] Abrir o Baú Misterioso.\n[2] Seguir em Frente.\nResposta: ")
    os.system("cls")

    if escolha == '1':

        match sorte:
            case 0:
                print(f"O aventureiro {nome} abriu o baú e se deparou com um baú completamente vazio.")

            case 1:
                ataque += 5
                ataque_distancia += 5
                defesa += 5
                print(f"O aventureiro {nome} abriu o baú e se deparou com vários equipamentos:")
                print("Espada Pequena (5 de Ataque)")
                print("Escudo Pequeno (5 de Defesa)")
                print("Arco e Flecha (5 de Ataque à Distancia)")
                print("Você pegou os itens e os equipou..")

            case 2:
                ataque += 10
                defesa += 5
                print(f"O aventureiro {nome} abriu o baú e se deparou com vários equipamentos:")
                print("Espada Grande (10 de Ataque)")
                print("Escudo Pequeno (5 de Defesa)")
                print("Você pegou os itens e os equipou..")

            case 3:
                ataque_distancia += 5
                defesa += 20 
                print(f"O aventureiro {nome} abriu o baú e se deparou com vários equipamentos:")
                print("Escudo Colossal (20 de Defesa)")
                print("Arco e Flecha (5 de Ataque à Distancia)")
                print("Você pegou os itens e os equipou..")

            case _:
                print("\nOpção Invalida.")

        print(f"\nO aventureiro {nome} deu as costas ao baú aberto e seguiu seu caminho rumo ao interior do pântano.")
        input("\nClique em qualquer tecla para continuar sua aventura...")
        os.system("cls")
        
    else:
        print(f"O aventureiro {nome} deu as costas ao baú e seguiu seu caminho rumo ao interior do pântano.")
        input("\nClique em qualquer tecla para continuar sua aventura...")
        os.system("cls")

print (f"O aventureiro {nome} encontra o chefão.")



def bosshumano():
    print("         ..........................            .........                                                 ")             
    print("   .................................         ...-+#%#*-...                                               ")
    print("   ....................................     ...-#@%%@@@@*:...                                       		")
    print(" ..............:.......................     ...=#@%%@@@@@#:..                                       		")
    print("..........:::::::::::..................    ...=*#**%@@@@%%=..                                       		")
    print(".......:::::----::::::::................   ..:*##**#%@@@@%=....                                     		")
    print(".....:::::::+=--=+=--:::::...............  ...-**++++###%%=..                                       		")
    print("....::::----#--*+------::::..............  ...:**====*+*%-...                                       		")
    print("....::::----+===-=+*+=--:::...................*%#=++*##%*:.....                                     		")
    print("...::::----:=**++=-------::::................:+*##***#%%%@*=.....                                   		")
    print("...::::---::-*##*+==----------::::...:::::-==#+*##%##%%+-*%%%+...                                   		")
    print("...:::-----::*###=::------::::.....:+++**++=**+*#%%%#%@%==%%#*-...                                  		")
    print("...::::------#%%#=::----::::......-*+++*++++#%#%#%@%#%%%*=##*++:...                                 		")
    print("....::::-----*%%%*=-:::-:::.....:==+***######%#**#%%##%%*#%%%%#=....                                		")
    print(".....:::::--:-#%%%#=--::::....:-==+*##%%%#######**%%%%%%*%%%%@%%-...                                		")
    print("......:::::::--*####+==::...:---=+*#%%%%%%##+**#*+#%%%@@+#%%@@%%-...                                		")
    print(".........::::::-+##*+#%+=--====+*#%@@@@@@@%%%%##*+*%%#%%+*%@@@%*:...                                		")
    print(".............::-**+=*%@@%%%%###%%%@@%#%@@@@%%%%#*+*%@###=#%@%%%+...                                 		")
    print("...............=###%%%@@@@@@%%@@@@*-..-%@@@@%%%%%#*#@@#+*%%#%%%-...                                 		")
    print(" ..............:=#%@@@@@@@@@@@@#=......=%@@@@@@%@%##@@%#%%#%%%#:...                                 		")
    print(" ................:=*#@%@@@@@%*-....   ..*@@@@@@@@%##%@@@@#*#%%*:...                                 		")
    print(" .....................::-==-:....    ...:#@@@@@@@@@%%@@@@%*%%%+....                                 		")
    print("    .............................      ..=%@@@%@%%@@%@@@@@###%=.........                            		")
    print("  .........................            .:#@@@@%%%@@%@@@@@%#%%*:....                                		")
    print("     ...................               ..-#@%@%%%%@@@@@@@@@%%%%=...                                 		")
    print("            .......                    ..+%%@@%%%@@%%@@@@@@@%%%%+...                                		")
    print("                                      ..:*%%%%#%%@@@@@@@@@@@@%#%%-....                              		")
    print("                                    ....-#%%%%##%@@@%@@@@@@@@@%%%#+....                             		")
    print("                                    ....+%%%%%##@@@@@@@@%@@@@@%%##%=...                             		")
    print("                                    ...-#%%####@@@@@@@@%@@@@@@@%%%%%=....                           		")
    print("                                   ...+#%**##@@@@@@@@%%@@@@@@%@%%%@%*:....                         		")
    print("                                    ..-#%%++#%###**#%%%####%%%@@@%%%%%*:...                         		")
    print("                                  ...:*%%#++%%%%@@%#*#%@##%@%%%%@@%%%%#=...                         		")	
    print("                                 ....+%%%**%##%%######%%%%%%%@@%@@%@%##-...                         		")
    print("                                ....-%%%*+#**####%%%%%%@%%%%%%@@@@@%%+++...                         		")
    print("                                 ..:*%%###**##%%%@@@@@@@@%%%%%%%%%@@%++*-.....                      		")
    print("                                 ..=%%%#%####%%%@@@@@@@@@@@%%%%%%%@@@*:+*-....                      		")
    print("                                ..:#%%#######%%@@@@@@@@@@@@%%%%%%@@@@%*:+*:...                      		")
    print("                              ....+%%%%#####%%%@@@@@@@@@@@@@%%%%%%@@@%#=:*+...                      		")
    print("                              ...-%%@%*#####%%%@@@@@@@@@@@@%%%%%%%%@@@%+.:*=...                     		")
    print("                      ..     ....#%@%**####%%%@@@@@@@@@@@@@%%%%%%@@@@@@%=.-#-....                   		")
    print("                            ...+%@@#*##*##%%@@@@@@@@@@@@@@%%%%%%%@@@@@%#-.=#:...                   		")
    print("                            ...-#@@@###**##%@@@@@@@@@@@@@@@@%%%%%%@@@@@@%#-.+#...                   		")		
    print("                           ....*%@@%###**#%%@@@@@@@@@@@@@@@@@%%%%%@@@@@@@%#-.**..                   		")		
    print("                         .....+%@@@%%##*##%@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@%#:.*+...                 		")
    print("                          ...-#@@@@%%####%@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@#::#=..                 		")
    print("                          ...*%@@@%%####%@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@%::#:....              		")
    print("                           .=%@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@@@@@@@%=-*:..               		")
    print("                         ..:*@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@*++..               		")
    print("                       ....=%@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@%#=....            		")
    print("                       ...-#@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@%=....           		")
    print("                       ...+@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@%*:...          		")
    print("                       ..:%@@@@%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@%+....        		")
    print("                       ..+@@@@@%%%@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@#:.         		")
    print("                       .:%@@@@@@%%%@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=.....    		")
    print("                      ..=@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:...    		")
    print("                      ..#@@@@%%%@@@@@@@@@@@@@@@@@@#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=..    		")	
    print("                     .:@@@@@@%%@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:..  		")
    print("                    ..+@@@@@@%@@@@@@@@@@@@@@@@@@@*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-...		")
    print("                   ...%@@@@@%%@@@@@@@@@@@@@@@@@@@*+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-...		")
    print("                   ..=@@@@@%%@@@@@@@@@@@@@@@@@@@@*-#@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:..		")
    print("                   ..#@@@@@@@@@@@@@@@@@@@@@@@@@@@#-+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:...  		")
    print("                   .:%@@@@@@@@@@@@@@@@@@@@@@@@@@@@=:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*#-..    		")
    print("                   .=@@@@@@@@@@#..:-+%@@@@@@@@@@@@+.=@@@@@@@@@@@@@@@@%++++*%%%@@@@@@@@@+:..=*:...  		")
    print("                 ...+@#::#@@@@@-......-=*#@@@@@@%#*:.#@@@%@@@@%%@@@@@#.......:%@@@@@#=......==...  		")	
    print("                 ...#@+.:#@@@@#.       ....--::.......:-=#%#=:.-%@@@@#-...  ...:---.....  ...-:..  		")	
    print("                 ...#@-.-@@@@@=.                         ......+@@@@@%=...                 ......  		")
    print("                  ..-@..+@@@@%:...                           ..#@@@@@@*...                   ..    		")
    print("                   ..:.:%@@@@%:...                           ..#@@@@@@%+.....                      		")	
    print("                     ..=%@@@@#:.                             ..+%@@@@@@%=....                      		")	
    print("                    ...#%@@@@#:.                             ..-#@%@@@@@%*:..                      		")	
    print("                    ..=%@@@@@#:.                              ...:+%@%%%@@%:.                      		")
    print("                     .+#%@%%%%:.                                 ..=#%@%%@#..                      		")
    print("                     .-%@%%%%+..                                 .....::-:...          .. ....... .		")
    print("                      ..-=+=:..                                         ..        .................		")	
    print("															")

def bossmonstro():
    print("                       ........:-=+*#%%%#=.......:#%%%###%#+-:::..............                      ") 
    print("           ... ........:=*%%%%%%%%%%%%%%%#*=.:+++#%%%%%%%%%%%%%%%%%%%%##+=-:...........             ") 
    print("                 ....-+#%%%%%%%%%%%%%%%%%=...........=#%%%%%%%%%%%%%%%%%%%%%%%%%%%*+=:...           ") 
    print("          ......:=*#%%%%%%%%%%%%%%%%%%%%=..............+%%%%%@%@%%%%%%%%%%%%%%%%%%%%%%%#+:..        ") 
    print("          ...:+#%%%%%%%%%%%%%%%%%%%%%%%:.             ..+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+.        ") 
    print("      ....:*%%%%%%%%%%%%%%%%%%%%%%%%%%:..             ...*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*:...... ") 
    print("      ..-*#%%%%%%%%%%%%%%%@%%%%%%%%%%=...             ...:*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-... ") 
    print("   ....+##%%%%%%%%%%%%%%%%%%%%%%%%%%#:...                ..-#%%%%%%%%%%%%%%%%%%%%%%%%%%%%####%##*-..") 
    print("   ..:*#%%%%%%%%%%%%%%%%%%%%%%%%%%%+:....                ...*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*:..:----.") 
    print("  ..-*#%%%#%%%%%%%%%%%%%%%%%%%%%%%%#:....                ...:%%%%%%%%%%%%%%%%%%%%%%%%%%%%##+...   ..") 
    print("...-*###*###%%%%%%%%%%%%%%%%%%%%%%%%%-...             .....-%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*:::..   ..") 
    print(".:*###+..-##%%%%%%%%%%%%%%%%@%%%%%%%%%+..             ...:*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=....     ") 
    print(".-:++...:*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=...............:#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-..     ") 
    print("...-....:*#%%%%%%%%%%%%%%%%%%%####%%%%%%%#=............:%%%%%%%%%#####%%%%%%%%%%%%%%%%%%%%%%#-.     ") 
    print(".......:+##%%%%%%%%%%%%%%%%############%%%%*.:==-:*#=.-%%%%%#%%%%######%%%%%###%%%%%%%%%%%%%##=.... ") 
    print(".......*##%%%%%%%%%%%%%%%%############%####%%+*#**#--#%%##%#*=*###*######%#%%%##%%%%#--##%#####=... ") 
    print("   ....=#%%%%%%%%%%%%%%%%########***####**##%%%%%%######**#*:..==::##########%##%%%%*..-*#**####=.. ") 
    print("   ...=#%%%%%%%%%%%%%%%%##########+.=#*:.-#%%%%%%%%%#%#*+::........-**++#############-..::.-*##**-. ") 
    print("   ..=#%%##%%#%%%%%%%%%%#####**+-=*-.--.:*%#%%%@@%%%%%#%%=...   ....-=..-*######*::+#+......-*#==+..") 
    print(". ..-*%%#######%%%%%%%%######--=...:....*%*.-%%%%%%%%*.=%#-...   ...=....+*#####+...=#=......=#=.::.") 
    print("...:*%%####*==#%%%%%%%%######:.:.......#%=...+%%%%%%#:..:##-... .........+**###*+....-#-......**:...") 
    print("...=#%###*+-.-#%%%%%%%##*+**#-........*#:....:+%%%%#:.....+#=............*=:+*###-....+*......:#=...") 
    print("..-###=++-...:*%%%%%%##+-..*#.......-##.......-%%%%*.......=%#*:. ......:-..=**#*:....:*=... ..++...")
    print("..-*#:.......:*%%%%%###....=#.....:*%#:.......+%%%%#-.......:+%#=............**#*:....:+=... ..:+:..") 
    print("..-*-...    ..+%%%%%##*......=...=@*:....   .:#%%%%#+...    ...=%*..     ....**##-.....+-...  ..=:..") 
    print("..-=....   ...*%%%%###*.........##:.......  .:%%%%%%*:..     ....+%-.... ...-****=.....=-...   .=...") 
    print("..-:.........:#%%%#*+=#.......-#=.........  .-%%%#%#*:..     .....:#+... ...:**#*:.....=:...  .:=...") 
    print("..-:.........-%%%%#=..+......-#=...  ........=%%%%%##-..      .....=%=.. ....***+:.....=.......=:...") 
    print("..-:.........=%%%#*:..:.. ...+@#:..     .....:%%%%##%*:.       ....%%+.. ....+**=......:......:-....") 
    print("..-..........+%%%#+...    ...=%%+..... .......*%%%##*=*...   .....:#-*:. ....+**-.. ..........-.....") 
    print("..::........:##%%#=....   ...-*:*::...........=%%#%#=..*:........:=+-#-......+*+:.. .........:......") 
    print("...:........-#####+...    ...:***#=:..........-%%*%#:...+-.....::+*+*=......:=*=...        ....     ") 
    print("............:*####*:.     ......:.............-#%*%#:....+:.....:=+-:.......-*+:...        ....     ") 
    print("..............:+**#=..    ....................=%%%%%=....-=..  .......  ....=+=....                 ") 
    print(". ...  .........=***-............   ..  ......-%%%%%=....-=................=+-.....                 ") 
    print("            .....-=+*-......            ......:*%%##....:+:...:...........==:......                 ") 
    print("            ......::-+-.....            .......+%%#+..:+=.....:+:........--........                 ") 
    print("            ..........=-........  ..   ........-#%#*+=:........=+......:=:.........                 ") 
    print("            ...........:=.....................-*#%#........ ...=#=...--...........                  ") 
    print("                   .....:-................:++:.-#%#....     ...==-.::.......                        ") 
    print("                   .......-:............:+:....=#%#:...     ..:+-...........                        ") 
    print("                   .....................+:.....-###..........=+.............                        ") 
    print("                           ....  .......:=.....-###:.......==....                                   ") 
    print("                           ....  ..........-=--=#%%-.::-+=:......                                   ") 
    print("                                 ..............-##*:.........                                       ")
    print("                                  ..     ..  ..:-.......                                            ")



def igreja():
    print(f"                                      .                                  ")
    print(f"                                    .' '.                                ")
    print(f"                                  .'  |  `.                              ")
    print(f"                                .'    |    `.                            ")
    print(f"                              .`---.._|_..---'.                          ")
    print(f"                               ||    |=|    ||                           ")
    print(f"                               ||_.-'|=|`-._||                           ")
    print(f"                               ||`-._|=|_.-'||                           ")
    print(f"                          _____||    |=|    ||__                         ")
    print(f"            ____________.'     `-.   |=|  .'_.'\/`.                      ")
    print(f"          .'       _  .' _______  `-.|_|.' .'\.'`./`.                    ")
    print(f"        .'     _   _.'      _   _        .'\.' `._`./`.                  ")
    print(f"      .' _       _.' __          __    .'\.'  ___`._`./`.                ")
    print(f"    .'        _ .'   _____           .'\.'         `._`./`.              ")
    print(f"  .'  _  _    .'       ______      .'\.'  __         `._`./`.            ")
    print(f".'`--...__ _.'            ______ .'\.'           __    `._`./`.          ")
    print(f" `--...__ .'   ____            .'\.'           _         `._`./`.        ")
    print(f" |      .`--...__            .'\.'     _               ____`._`./`.      ")
    print(f" | /`-._ `--...__`--...___ .'\.'              _______       _`._`./`.    ")
    print(f" | | ) ( |       `--...____\.'     _     _  .'      .`.        `._`./    ")
    print(f" | |)   (| /`-._             |            .'      .'   `.     _ |        ")
    print(f" | |(--| | | )( |  /`-._`--._|____       /      .'       `.     |        ")
    print(f" | | ) `.| |(  )|  | )( |    | _      _ /      /   .---.  `\    |        ")
    print(f" | `--._ | |/  \|  |(  )|`-  |         /`--.._/   /     \  ' _  |        ")
    print(f" | `-.   | |)-.(|  |/  \|    |       __|      |_  |`-   |  |  _ |        ")
    print(f" |    `-.| |) |(|  |)-.(|    |  ___  _ |  __  | __| \`- |  |    |        ")
    print(f" '-._    | `--._/  |) |(|    |      __ |      |   | |`- |  | _  |        ")
    print(f"     `-._| `--.    `--._/    |  ___    | _    |   | |`- |  |   '|        ")
    print(f"         |      `--._        |       _ |    ' |   |O|`- | _| _  |        ")
    print(f"         '--._         `--._ |         | _    |_  | |`- |. |  __|        ")
    print(f"              `--._          |       __|      |   | |`- |. | __ |        ")
    print(f"                   `--._     |__       |   _  |   | |`- |  |___ |        ") 
    print(f"                        `--._|_________|_     | _ |  `- |_ |____|        ")
    print(f"                               LG        '--._|___|     |__|             ") 


def funcaux():
    print("vish")
def boss_ambientacao():
    escolha = 1
    nome = funcaux
    os.system("cls")
    print(f"O guerreiro nome ouve uma badalada de um sino ao horizonte.")
    print(f"O que nome deveria fazer?")
    print(f"[1] Seguir o som do sino")
    print(f"[2] Seguir na direção oposta do sino")
    escolha = input()
    if escolha == '2':
        print("Você acaba indo na direção oposta, mas chega no sino de qualquer jeito, que sorte!...")
    print("Ao chegar, o guerreiro se depara com uma pequena igreja...\n\n")
    input("Pressione para continuar...")
    igreja()
  
vidab = 128


def atk_normal():
    dano = random.randint(1,6) + random.randint(1,6) 
    dano *= 2
    sorte = random.randint(1,20)
    if sorte == 20:
        print(f"Foi um golpe critico!!! Que azar...")
        print(f"O monstro golpeia com sua espada bem acima do seu ombro")
        print(f"O machucado deixa um sangramento arduo, a dor é calcinante.")
        dano *= 2
        print(f"Você perde {dano} de vida!")
        return dano
    print(f"O monstro te golpeia com uma espada... ela te acerta em cheio!")
    print(f"Você recebe {dano} de dano")
    return dano

def atk_roubodevida():
    dano = random.randint(1,6)
    print("A criatura fincou a espada em você, seu sangue parece jorrar em direção a espada.")
    print(f"Voce recebe {dano} de dano")
    print("A criatura se sente com maior vitalidade.")
    vidab =+ dano
    return dano

def luta(vidab, vida_h):
    while vidab > 0 and vida_h > 0:
        print("A criatura esta esperando seu movimento, qual ação você quer fazer?")
        input(">>>")
        vidab -= ataque_aventureiro()
        ## Aqui os meninos vão escolher o dano dos ataques
        sorte = random.randint(1,20)
        if sorte > 15:
            # essa funcao retorna o dano a ser causado
            vida_h -= atk_roubodevida()
        else:
            vida_h -= atk_normal()
        


def bossfight():
    boss_ambientacao()
    print("Ao abrir a porta, uma luz fraca ilumina a igreja")
    print("Ao dar o primeiro passo para dentro, todas as luzes se acendem, em sincronia")
    print("Um unico homem esta sentado em um dos assentos, de costas a porta")
    print("Ele se levanta e vira ao guerreiro")
    print(" - Faz tempo que não recebo visitas")
    input(" Pressione para continuar...")
    bosshumano()
    input()
    print(" - Posso te fazer uma pergunta? Você me teme?")
    print("[1] Não, eu não temo nada.")
    print("[2] Sim, eu te temo.")
    caminho = input(">>>")
    if caminho == '1':
        print(" - Vou fazer voce temer.")
        print(" - VAMOS, ME ENFRENTE")
        input(">>>")
        bossmonstro()
        vidab == 150
    else:
        print("\n\n\n -Vou mostrar que esta certo em temer.")
        input(">>>")

    print("Esta bem obvio que o ser nao e humano.")
    print("Você tira sua espada da bainha")
    print("A criatura tambem.")
    luta(vidab, vida_h)
    os.system("cls")
    if vidab <= 0:
        print("A criatura se ajoelha após seu ataque.")
        print(" - Muito bem! Cough")
        print(" - Ja estava velho, voce nao teria tanta sorte no meu auge")
        print("A criatura se disolve...")
        print("Deixando para tras um bilhete")
        print("Você agarra o bilhete...")
        input(">>>")
        print("Ao agarrar ele, percebe que está escrito algo...")
        print("Infelizmente, você é um guerreiro, não sabe ler")
        print(" FIM DE JOGO")
    else:
        print(" - Voce lutou bem")
        print(" - Mas sua jornada de varios e varios dias")
        print(" - Termina agora...")
        print("Ele te apaga antes de te finalizar...")
        print(" FIM DE JOGO")

bossfight()