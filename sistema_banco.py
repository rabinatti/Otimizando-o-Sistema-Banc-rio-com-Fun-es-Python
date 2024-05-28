import sys

LIMITE_SAQUES_DIARIO = 3
LIMITE_SAQUE = 500.00

numero_depositos = 0
conta_nova = False

usuarios = {
    "1":{"cpf": "11122233344", "nome": "Teste", "data_nascimento": "01/01/1990"},
    "2":{"cpf": "12345678912", "nome": "Outro Usuário", "data_nascimento": "01/01/1999"}
}

contas_corrente = {
    "1": {"agencia": "0001", "numero_conta": "1", "usuario_id": "1", "saldo": "1000", "numero_saques": "0", "saques": [], "depositos": []},
    "2": {"agencia": "0001", "numero_conta": "2", "usuario_id": "1", "saldo": "9000", "numero_saques": "0", "saques": [], "depositos": []},
    "3": {"agencia": "0001", "numero_conta": "3", "usuario_id": "2", "saldo": "150", "numero_saques": "0", "saques": [], "depositos": []},
    "4": {"agencia": "0001", "numero_conta": "4", "usuario_id": "1", "saldo": "9000", "numero_saques": "0", "saques": [], "depositos": []},
    "5": {"agencia": "0001", "numero_conta": "5", "usuario_id": "2", "saldo": "9000", "numero_saques": "0", "saques": [], "depositos": []},
    "6": {"agencia": "0001", "numero_conta": "6", "usuario_id": "2", "saldo": "9000", "numero_saques": "0", "saques": [], "depositos": []},
    "7": {"agencia": "0001", "numero_conta": "7", "usuario_id": "1", "saldo": "9000", "numero_saques": "0", "saques": [], "depositos": []}
}

MENU_INICIAL = f"""
    Olá, sejam bem vindo ao nosso banco. Por favor, selecione a opção desejada:

    ================== Menu ==================
    
    1 - Já sou cadastrado
    2 - Não sou cadastrado (Criar cadastro)
    3 - Sair

Opção: """

MENU_USUARIO = f"""
    ================== Menu ==================

    1 - Acessar conta corrente
    2 - Listar contas ativas
    3 - Criar nova conta
    4 - Trocar usuário
    5 - Sair

Opção: """

MENU_CONTA = f"""
    ================== Menu ==================

    1 - Depositar
    2 - Sacar
    3 - Ver extrato
    4 - Sair

Opção: """

MENU_SIM_NAO = f"""
    Digite:
    1 - Sim
    2 - Não
                      
Opção: """

def depositar(saldo, agencia, numero_saques, id_conta, usuario, id_usuario, saques_lista, depositos_lista, /):
    saldo_float = float(saldo)
    valor_deposito = 0
    novo_deposito = {"agencia": agencia, "numero_conta": id_conta, "usuario_id": id_usuario, "saldo": str(saldo_float), "numero_saques": numero_saques, "saques": saques_lista, "depositos": depositos_lista}

    TEXTO_DEPOSITO_ENTRADA = f"""
    Olá {usuario}, seu saldo é de R$: {saldo_float:.2f}.

    Por favor, digite o valor que o senhor gostraria de depositar:..... """
    
    while True:

        try:
            valor_deposito = float(input(TEXTO_DEPOSITO_ENTRADA))

            if valor_deposito > 0:
                depositos_lista.append(valor_deposito)
                saldo_float += valor_deposito

                print(f"""
    Valor de R$ {valor_deposito:.2f} depositado, seu saldo agora é de R$: {saldo_float:.2f}

""")
                input("Digite enter para continuar")

                novo_deposito = {"agencia": agencia, "numero_conta": id_conta, "usuario_id": id_usuario, "saldo": str(saldo_float), "numero_saques": numero_saques, "saques": saques_lista, "depositos": depositos_lista}
                return novo_deposito
            
            else:
                print("Valor inválido, por favor, tente novamente:")

        except ValueError:
            print("Por favor, digite um núemro válido")
                    
def sacar(*, saldo, LIMITE_SAQUES_DIARIO, LIMITE_SAQUE, numero_saques, agencia, id_conta, usuario, id_usuario, saques_lista, depositos_lista):
    saldo_float = float(saldo)
    novo_saque = {"agencia": agencia, "numero_conta": id_conta, "usuario_id": id_usuario, "saldo": str(saldo_float), "numero_saques": numero_saques, "saques": saques_lista, "depositos": depositos_lista}
    
    TEXTO_SAQUE_ENTRADA = f"""
    Olá {usuario}, seu saldo é de R$: {saldo_float:.2f}.

    Por favor, digite o valor que o senhor gostraria de sacar:..... """

    while True:

        if numero_saques < LIMITE_SAQUES_DIARIO:
        
            if saldo_float > 0:
                valor_saque = float(input(TEXTO_SAQUE_ENTRADA))
                
                if (valor_saque <= saldo_float) and (valor_saque <= LIMITE_SAQUE):
                    
                    saques_lista.append(valor_saque)
                    saldo_float -= valor_saque
                    numero_saques += 1

                    novo_saque = {"agencia": agencia, "numero_conta": id_conta, "usuario_id": id_usuario, "saldo": str(saldo_float), "numero_saques": numero_saques, "saques": saques_lista, "depositos": depositos_lista}

                    print(f"""
    Valor de R$ {valor_saque:.2f} sacado, seu saldo agora é de R$ {saldo_float:.2f}
    Número de saques hojes (Limite de 3 saques diários): {numero_saques}
                    """)
                    
                    input("Digite Enter para continuar")
                                    
                    return novo_saque

                elif valor_saque > LIMITE_SAQUE:
                    print(f"Saque acima do limite de R$ {LIMITE_SAQUE:.2f}, gostaria de tentar novamente?")
                    tentar_novamente_opcao = input(MENU_SIM_NAO)

                    if tentar_novamente_opcao == "2":
                        return novo_saque

                else:
                    print(f"Saldo insulficiente, seu saldo é de R${saldo_float:.2f}. Goistaria de tentar novamente?")
                    tentar_novamente_opcao = input(MENU_SIM_NAO)

                    if tentar_novamente_opcao == "2":
                        return novo_saque
            else:
                print("Saldo insulficiente, tente novamente depois de depositar algum valor.")
                return novo_saque
                
        else:
            print("Número de saques diários exedito, por favor, volte amanhã")
            return novo_saque
        

def ver_extrato(saldo, /, usuario, agencia, id_conta, *, saques_lista, depositos_lista):
    saldo_float = float(saldo)
    numero_saques = len(saques_lista)
    total_sacado = sum(saques_lista)
    numero_depositos = len(depositos_lista)
    total_depositado = sum(depositos_lista)

    EXTRATO_DADOS = f"""
    ======================Extrato======================
    
    Usuário ----------------------- {usuario}
    Agência ----------------------- {agencia}
    Número da conta --------------- {id_conta}"""
    
    EXTRATO_DEPOSITOS = f"""
    ==================== Depósitos ====================

    Depósitos realizados ---------- {numero_depositos}

    """

    EXTRATO_SAQUES = f"""
    ===================== Saques ======================

    Saques Realizados ------------- {numero_saques}

    """

    while True:

        print(EXTRATO_DADOS)
        if numero_depositos > 0:
            print(EXTRATO_DEPOSITOS)

            i_deposito = 0
            for deposito in depositos_lista:
                i_deposito += 1
                print(f"    Deposito {i_deposito} -------------------- R$ {deposito:.2f}")
            print()
            print(f"    Total do valor depositado ----- R$ {total_depositado:.2f}")
            
        
        else:
            print()
            print("    Nenhum depósito realizado.")

        if numero_saques > 0:
            print(EXTRATO_SAQUES)

            i_saque = 0
            for saque in saques_lista:
                i_saque += 1
                print(f"    Saque {i_saque} ----------------------- R$ {saque:.2f}")
            print()
            print(f"    Total do valor sacado --------- R$ {total_sacado:.2f}")
        
        else:
            print()
            print("    Nenhum saque realizado")
        
        print ()
        print("    ===================================================")
        print()
        print(f"    Saldo atual ------------------- R$ {saldo_float:.2f}")
        print()
            
        input("Pressione enter para continuar")
        break

def listar_contas(id_usuario, usuario, **contas_corrente):
    
    contas_usuario = []

    TEXTO_LISTAR_CONTAS = f"""
    ===============================================================================
    
    Usuário ------------------------------------------------------ {usuario}

"""
    
    TEXTO_LISTAR_CONTAS_CABEÇALHO = """
    Registro --------------- Agência --------------- Número da Conta ---------------

"""
    index = 0
        
    print(TEXTO_LISTAR_CONTAS)

    while index < len(contas_corrente):
        index += 1
        verificacao_usuario = int(contas_corrente[str(index)].get("usuario_id"))

        if int(id_usuario) == verificacao_usuario:
            conta = int(contas_corrente[str(index)].get("numero_conta"))
            contas_usuario.append(conta)

    if len(contas_usuario) > 0:
        print(TEXTO_LISTAR_CONTAS_CABEÇALHO)
    else:
        print(f"Nenhuma conta ativa para o usuário: {usuario}")

    index_conta = 0
    for conta in contas_usuario:
        index_conta += 1
        agencia = contas_corrente[str(conta)].get("agencia")
        print(f"    {index_conta} ------------------------ {agencia} ----------------------- {conta} -----------------------")

    print ()
    print(f"    Total de contas: {len(contas_usuario)}")
    print ()

    input("Digite Enter para continuar")
                             
def acessar_conta(id_usuario):
    global contas_corrente
    
    conta_autenticada = False
    
    # Variavel Booleana que ficará True quando o usuário pedir pora sair, quebrando assim o laço de repetição.
    saida = False
    id_conta = 0

    while not saida:
        
        while True:
            try:
                conta_digitada = int(input("""
    Por favor, digite o número da sua conta: """))
                break
            
            except ValueError:
                print("Número inválido. Gostaria de tentar novamente?")

                tentar_novamente_opcao = input(MENU_SIM_NAO)
                if tentar_novamente_opcao == "2":
                    saida = True
                    break
        
        #Caso o usuário não queira entrar e pediu pra sair no ValueError
        if saida:
            break 

        index = 0
        while index < len(contas_corrente):
            index += 1
            verificacao_conta = contas_corrente[str(index)].get("numero_conta")
            verificacao_usuario = contas_corrente[str(index)].get("usuario_id")

            if (int(verificacao_conta) == conta_digitada) and (int(verificacao_usuario) == id_usuario):
                conta_autenticada = True
                id_conta = int(index)

                break 
                
        if conta_autenticada:
            while conta_autenticada:

                usuario = usuarios[str(id_usuario)].get("nome")
                agencia = contas_corrente[str(id_conta)].get("agencia")
                saldo = contas_corrente[str(id_conta)].get("saldo")
                saques = contas_corrente[str(id_conta)].get("saques")
                depositos = contas_corrente[str(id_conta)].get("depositos")
                numero_saques = int(contas_corrente[str(id_conta)].get("numero_saques"))

                menu_conta_opcao = input(MENU_CONTA)
                
                if menu_conta_opcao == "1":
                    deposito = depositar(saldo, agencia, numero_saques, id_conta, usuario, id_usuario, saques, depositos)

                    contas_corrente.update({str(id_conta): deposito})

                elif menu_conta_opcao == "2":
                    saque = sacar(saldo=saldo, LIMITE_SAQUES_DIARIO=LIMITE_SAQUES_DIARIO, LIMITE_SAQUE=LIMITE_SAQUE, numero_saques=numero_saques, agencia=agencia, id_conta=id_conta, usuario=usuario, id_usuario=id_usuario, saques_lista=saques, depositos_lista=depositos)
                
                    contas_corrente.update({str(id_conta): saque})

                elif menu_conta_opcao == "3":
                    ver_extrato(saldo, usuario, agencia, id_conta, depositos_lista=depositos, saques_lista=saques)

                elif menu_conta_opcao == "4":
                    saida = True
                    break

                else: 
                    print("Opção inválida, tente novamente")
        
        else:
            print("Conta ou usuário não encontrado, gostaria de tentar novamente?")

            tentar_noamente_opcao = input(MENU_SIM_NAO)
            if tentar_noamente_opcao == "2":
                    
                # Quebra o laço inicial da função
                saida = True

def criar_usuario(**usuarios):

    cpf_valido = False

    print()
    print("Bem vindo ao nosso banco")
    
    # Obtenção e validação do CPF
    while not cpf_valido:
        cpf = input("Por favor, informe seu CPF (apenas números): ")
        index = 0

        #Verifica se o número do CPF é válido (são apenas números e tem 11 dígitos)
        if (cpf.isdigit()) and (len(cpf) == 11):
    
            # Verifica se tem algum CPF já existente
            while index < len(usuarios):
                index += 1
                cpf_usuario = usuarios[str(index)].get("cpf")

                if cpf == cpf_usuario:
                    print("CPF já existente, por favor, tente novamente")
                    print()
                    cpf_valido = False
                    break
                
                cpf_valido = True

        else:
            print()
            print("CPF inválido, por favor, digite seu CPF novamente: ")

    # Obtenção e validação do nome
    nome_usuario = input("Qual o seu nome completo? ")

    # Obtenção da data de nascimento
    while True:
        dia_nascimento = (input("Qual o dia do seu nascimeto? "))

        if (dia_nascimento.isdigit()) and (int(dia_nascimento) <= 31) and (int(dia_nascimento) > 0):
            break
        else:
            print("""
    Número inválido, por favor, digite um número válido
                  """)

    while True:
        mes_nascimento = input("Qual o mes do seu nascimento? (apenas números) ")

        if (mes_nascimento.isdigit()) and (int(mes_nascimento) <= 12) and (int(mes_nascimento) > 0):
            break
        else:
            print("""
    Número inválido, por favor, digite um número válido
                  """)

    while True:
        ano_nacimento = input("Em qual ano você nasceu? (Ex: 1987)")

        if (ano_nacimento.isdigit()) and (len(ano_nacimento) == 4):
            break
        else:
            print("""
    Número inválido, por favor, digite um número válido (lembre-se de digitar os 4 dígitos)
                  """)

    data_nascimento = f"{dia_nascimento}/{mes_nascimento}/{ano_nacimento}"

    # Obetenção logadouro
    logadouro = input("Qual seu endereço? (Ex: Av. Brasil) ")

    # Obtenção do número
    while True:
        numero_endereco = input("Qual o número da sua casa ou apartamento (Apenas números) ")
        if numero_endereco.isdigit():
            break
        else:
            print("""
    Número inválido, por favor, digite um número válido
                  """)
    
    # Obtenção bairro e cidade
    bairro = input("Qual seu bairro? ")
    cidade = input("Qual sua cidade? ")

    # Obtenção estado
    while True:
        sigla = input("Qual a sigla do seu estado? (Ex: SP) ").upper()
        
        # Validação da Sigla (2 letras)
        if (sigla.isalpha()) and (len(sigla) == 2):
            break
        else:
            print("""
    Estado inválido, por favor, digite um estado válido
                  """)
    

    endereco = f"{logadouro}, {numero_endereco} - {bairro} - {cidade}/{sigla}"

    novo_usuario = {"cpf": cpf, "nome": nome_usuario, "data_nascimento": data_nascimento, "endereco": endereco}
    return novo_usuario

def criar_conta(numero_conta, usuario_id, **usuarios):
    global conta_nova
    
    AGENCIA = "0001"
    usuario_nome = usuarios[str(usuario_id)].get("nome")
    usuario_cpf = usuarios[str(usuario_id)].get("cpf")
    saldo = 0
    numero_saques = 0
    saques = []
    depositos = []

    while True:
        opcao_criar_conta = input(f"""
    Olá {usuario_nome}, vamos criar a sua conta. Para criarmos, por favor, confira seu CPF:
        
        CPF: {usuario_cpf}
        
    Seu CPF está correto?

    1 - Está correto
    2 - Não, trocar usuário
    3 - Sair

    Por favor, digite sua opção: """)

        if opcao_criar_conta == "1":
            nova_conta = {"agencia": AGENCIA, "numero_conta": str(numero_conta), "usuario_id": str(usuario_id), "usuario_nome": usuario_nome, "saldo": saldo, "numero_saques": numero_saques, "saques": saques, "depositos": depositos}

            input(f"""
    Nova conta criada com sucesso.
                
        Número da conta ------------------ {numero_conta}
        Agência -------------------------- {AGENCIA}
        Nome do titular ------------------ {usuario_nome}
        CPF do titular ------------------- {usuario_cpf}

    Pressione enter para continuar
            """)

            conta_nova = True
            return nova_conta
        
        elif opcao_criar_conta == "2":
            acessar_usuario(**usuarios)
            break
        
        elif opcao_criar_conta == "3":
            return False
        
        else:
            print ("Opção não encontrada, por favor, tente novamente")

def acessar_usuario(**usuarios):

    cpf_valido = False

    while True:
        while not cpf_valido:

            saida = False
            mensagem_erro = False
            
            usuario_id = 0
            nome_usuario = ""
            cpf = ""
            
            cpf = input("Por favor, digitre seu CPF: ")
            index = 0

            if (cpf.isdigit()) and (len(cpf) == 11):
                while index < len(usuarios):
                                    
                    index += 1
                    cpf_usuario = usuarios[str(index)].get("cpf")

                    if cpf_usuario == cpf:
                        cpf_valido = True
                        usuario_id = index
                        nome_usuario = usuarios[str(index)].get("nome")
                        break
            else: 
                mensagem_erro = True
                print("""
    Número de CPF inválido, Gostaria de tentar novamente?""")

                tentar_novamente_opcao = input(MENU_SIM_NAO)

                if tentar_novamente_opcao == "2":
                    saida = True
                    break

            if not cpf_valido and not mensagem_erro:
                print("""
    Número de CPF não encontrado, Gostaria de tentar novamente?""")

                tentar_novamente_opcao = input(MENU_SIM_NAO)

                if tentar_novamente_opcao == "2":
                    saida = True
                    break

        while not saida:
            print(f"""          
    Seja bem vindo {nome_usuario}, por favor selecione uma opção:""")
            
            menu_usuario_opcao = input(MENU_USUARIO)

            if menu_usuario_opcao == "1":
                acessar_conta(usuario_id)
                print(f"Aqui volta para acessar usuário {contas_corrente["1"]}")
                break
                # acessar_conta

            elif menu_usuario_opcao == "2":
                listar_contas(usuario_id, nome_usuario, **contas_corrente)

                # listar contas ativas

            elif menu_usuario_opcao == "3":
                
                numero_conta = len(contas_corrente) + 1
                nova_conta = criar_conta(numero_conta, usuario_id, **usuarios)

                if conta_nova:
                    contas_corrente.update({str(numero_conta): nova_conta})
                
            elif menu_usuario_opcao == "4":
                cpf_valido = False
                saida = False
                break
                # trocar usuário

            elif menu_usuario_opcao == "5":
                menu_inicial()

            else:
                print("""
    Opção inválida, por favor, tente novamente
                    """)

        if saida:
            break        
    
def menu_inicial():
    
    while True:
        menu_inicial_opcao = input(MENU_INICIAL)

        if menu_inicial_opcao == "1":
            acessar_usuario(**usuarios)

        elif menu_inicial_opcao == "2":
            novo_usuario = criar_usuario(**usuarios)
            usuario_id = len(usuarios) + 1
            usuarios.update({str(usuario_id): novo_usuario})

        elif menu_inicial_opcao == "3":
            print("Obrigado por utilizar nossos serviços. Volte sempre!")
            sys.exit(0)

        else:
            print("Opção não encontrada, por favor, tente novamente")
        
menu_inicial()