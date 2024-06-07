# Equipe:
# Ianny Raquel Ferreira de Souza - 559096
# Maria Alice Freitas Araújo - 557516

# NOSSO PROJETO:
# Um sistema de login para arrecadação de fundos. Pessoas contribuem para um futuro mais azul.

usuarios = []
senhas = []

saldo_1 = 0   
saldo_2 = 0
saldo_3 = 0

def boas_vindas():
    print("-" * 100)
    print("Seja bem vindo(a) ao AquaSentry")
    print("-" * 100)    


def pagina_cadastro():
    while True:
        print("\nPágina inicial")
        print("1 - Cadastrar")
        print("2 - Login")
        
        codigo_cadastro = int(input("\nOpção desejada: "))

        match codigo_cadastro:
            case 1:
                print("\nPágina de Cadastro\n")
                
                cadastro_usuario = input("Usuário: ")

                if cadastro_usuario in usuarios:
                    print("Este usuário já está em uso.")
                    continue

                cadastro_senha = input("Senha: ")
                usuarios.append(cadastro_usuario)
                senhas.append(cadastro_senha)

            case 2:
                print("\nPágina de Login\n")
                login_usuario = input("Usuário: ")
                login_senha = input("Senha: ")

                if login_usuario in usuarios and senhas[usuarios.index(login_usuario)] == login_senha:
                    print("\nUsuário logado com sucesso!\n")
                    break
                
                else: 
                    print("\nUsuário ou senha incorretos. Tente Novamente.")

            case _: 
                print("\nOpção inválida.\n")

def pagina_inicial():
    while True:
        print("-" * 100)
        print("\nPágina Inical\n")
        print("1 - Arrecadação de fundos")
        print("2 - Comentários")
        print("3 - Logout")

        codigo_inicio = int(input("\nOpção desejada: "))

        match codigo_inicio:
            case 1:
                pagina_arrecadacao()
                
            case 2:
                pagina_comentarios()

            case 3:
                pagina_cadastro()

            case _:
                print("Opção inválida")

def pagina_arrecadacao():
    global saldo_1
    global saldo_2
    global saldo_3
    while True:
        print("-" * 100)
        print("Página de Arrecadação de fundos para Eventos AquaSentry.")
        print("-" * 100)
        print("1 - Doe para o AquaSentry")
        print("2 - Saiba mais sobre nosso processo de doações")
        print("3 - Voltar\n")

        codigo_arrecadacao = int(input("Código desejado: "))

        match codigo_arrecadacao:
            case 1:
                while True:

                    print("\nPara qual causa deseja doar?\n")
                    print("1 - Monitoramento e pesquisa sobre mudanças climáticas e seus impactos nos oceanos.")
                    print(f"Saldo total: R$ {saldo_1:.2f}\n")
                    print("2 - Proteção dos recifes de corais")
                    print(f"Saldo total: R$ {saldo_2:.2f}\n")
                    print("3 - Restaurar manguezais e ecossistemas costeitos")
                    print(f"Saldo total: R$ {saldo_3:.2f}\n")
                    print("4 - Voltar")

                    opcao_doar = int(input("Opção desejada: "))

                    match opcao_doar:
                        case 1:
                            fundos_1 = float(input("Digite a quantia que deseja doar: "))

                            if 0 < fundos_1 < 10000000000:
                                certeza_1 = input(f"Você tem certeza que deseja doar R$ {fundos_1:.2f}? ").upper()

                                if certeza_1 == "SIM" or certeza_1 == "S":
                                    print("\nObrigado pela sua doação. Você faz a diferença!\n")
                                    
                                    saldo_1 = saldo_1 + fundos_1
                                    break

                                elif certeza_1 == "NAO" or certeza_1 == "N" or certeza_1 == "NÃO":
                                    print("\nVocê ainda pode fazer a diferença!\n")
                                    break

                                else:
                                    print("\nResposta inválida, responda com 'sim' ou 'não'.\n")
                                    break
                                
                            else:
                                break

                        case 2: 
                            fundos_2 = float(input("Digite a quantia que deseja doar: "))

                            if 0 < fundos_2 < 10000000000:
                                certeza_2 = input(f"Você tem certeza que deseja doar R$ {fundos_2:.2f}? ").upper()

                                if certeza_2 == "SIM" or certeza_2 == "S":
                                    print("\nObrigado pela sua doação. Você faz a diferença!\n")
                                    
                                    saldo_2 = saldo_2 + fundos_2
                                    break

                                elif certeza_2 == "NAO" or certeza_2 == "N" or certeza_2 == "NÃO":
                                    print("\nVocê ainda pode fazer a diferença!\n")
                                    break

                                else:
                                    print("\nResposta inválida, responda com 'sim' ou 'não'.\n")
                                    break
                                
                            else:
                                break

                        case 3:
                            fundos_3 = float(input("Digite a quantia que deseja doar: "))

                            if 0 < fundos_3 < 10000000000:
                                certeza_3 = input(f"Você tem certeza que deseja doar R$ {fundos_3:.2f}? ").upper()

                                if certeza_3 == "SIM" or certeza_3 == "S":
                                    print("\nObrigado pela sua doação. Você faz a diferença!\n")
                                    
                                    saldo_3 = saldo_3 + fundos_3
                                    break

                                elif certeza_3 == "NAO" or certeza_3 == "N" or certeza_3 == "NÃO":
                                    print("\nVocê ainda pode fazer a diferença!\n")
                                    break

                                else:
                                    print("\nResposta inválida, responda com 'sim' ou 'não'.\n")
                                    break
                                
                            else:
                                break

                        case 4:
                            pagina_arrecadacao()     
                            break
            
            case 2:
                print('exemplo')

            case 3:
                pagina_inicial()
                break

def pagina_comentarios():
    comentarios = []

    while True:
        print("-" * 100)
        print("Página de Comentários")
        print("-" * 100)
        print("1 - Deixar um comentário")
        print("2 - Ver comentários")
        print("3 - Voltar")
        
        opcao_comentario = int(input("Escolha uma opção: "))

        match opcao_comentario:
            case 1:
                nome = input("Nome de exibição: ")
                comentario = input("Comentário: ")
                comentarios.append((nome, comentario))
                print("\nObrigado pelo seu comentário!\n")
            
            case 2:
                print("\nComentários:\n")
                if comentarios:
                    for i, (nome, comentario) in enumerate(comentarios, 1):
                        print(f"{i}. {nome}: {comentario}\n")
                else:
                    print("Ainda não há comentários.")
                print("\n")
            
            case 3:
                print("Voltando ao menu anterior...\n")
                break
            
            case _:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.\n")


boas_vindas()
pagina_cadastro()
pagina_inicial()
pagina_arrecadacao()
pagina_comentarios()