def avaliar_peca(peso, cor, comprimento):

    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("Peso fora do padrão")

    if cor != "azul" and cor != "verde":
        motivos.append("Cor inválida")

    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora do padrão")

    return motivos


# Estruturas principais

pecas = []

caixas_fechadas = []

caixa_atual = []

motivos_reprovacao = {
    "Peso fora do padrão": 0,
    "Cor inválida": 0,
    "Comprimento fora do padrão": 0
}


def cadastrar_peca():

    print("\n===== CADASTRAR NOVA PEÇA =====")

    id_peca = int(input("Digite o ID da peça: "))
    peso = float(input("Digite o peso da peça (g): "))
    cor = input("Digite a cor da peça: ").lower()
    comprimento = float(input("Digite o comprimento da peça (cm): "))

    # Verifica os critérios de qualidade
    motivos = avaliar_peca(peso, cor, comprimento)

    # Define o status
    if len(motivos) == 0:
        status = "Aprovada"
    else:
        status = "Reprovada"

    # Cria o registro da peça
    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivos": motivos
    }

    # Adiciona a peça à lista
    pecas.append(peca)

    # Se a peça foi aprovada, adiciona à caixa atual
    if status == "Aprovada":

        caixa_atual.append(id_peca)

        # Quando atingir 10 peças, fecha a caixa
        if len(caixa_atual) == 10:

            caixas_fechadas.append(caixa_atual.copy())

            caixa_atual.clear()

            print("\nPEÇA APROVADA")
            print("Caixa atingiu 10 peças e foi fechada.")

        else:
            print("\nPEÇA APROVADA")
            print("Peça adicionada à caixa atual.")

    else:

        # Registra os motivos da reprovação
        for motivo in motivos:
            motivos_reprovacao[motivo] += 1

        print("\nPEÇA REPROVADA")

        print("Motivos:")

        for motivo in motivos:
            print("-", motivo)


def listar_pecas():

    print("\n===== LISTA DE PEÇAS =====")

    if len(pecas) == 0:
        print("Nenhuma peça cadastrada.")
        return

    for peca in pecas:

        print("\nID:", peca["id"])
        print("Peso:", peca["peso"], "g")
        print("Cor:", peca["cor"])
        print("Comprimento:", peca["comprimento"], "cm")
        print("Status:", peca["status"])

        if peca["status"] == "Reprovada":

            print("Motivos:")

            for motivo in peca["motivos"]:
                print("-", motivo)


def remover_peca():

    print("\n===== REMOVER PEÇA =====")

    id_remover = int(input("Digite o ID da peça que deseja remover: "))

    for peca in pecas:

        if peca["id"] == id_remover:

            # Não permite remover uma peça que já esteja
            # dentro de uma caixa fechada
            if id_remover in [id for caixa in caixas_fechadas for id in caixa]:
                print("Essa peça pertence a uma caixa já fechada.")
                print("Não é possível removê-la.")
                return

            pecas.remove(peca)

            # Se a peça estiver na caixa atual, remove também
            if id_remover in caixa_atual:
                caixa_atual.remove(id_remover)

            # Atualiza os motivos da reprovação
            if peca["status"] == "Reprovada":

                for motivo in peca["motivos"]:
                    motivos_reprovacao[motivo] -= 1

            print("Peça removida com sucesso.")

            return

    print("Peça não encontrada.")


def listar_caixas():

    print("\n===== CAIXAS FECHADAS =====")

    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa fechada.")
    else:

        for i, caixa in enumerate(caixas_fechadas, start=1):

            print("\nCaixa", i)
            print("Quantidade de peças:", len(caixa))
            print("IDs das peças:", caixa)

    # Mostra a caixa que ainda está sendo preenchida
    if len(caixa_atual) > 0:

        print("\n===== CAIXA ATUAL =====")
        print("Quantidade de peças:", len(caixa_atual))
        print("IDs das peças:", caixa_atual)


def gerar_relatorio():

    print("\n========== RELATÓRIO FINAL ==========")

    total_aprovadas = 0
    total_reprovadas = 0

    for peca in pecas:

        if peca["status"] == "Aprovada":
            total_aprovadas += 1
        else:
            total_reprovadas += 1

    print("Total de peças cadastradas:", len(pecas))
    print("Total de peças aprovadas:", total_aprovadas)
    print("Total de peças reprovadas:", total_reprovadas)

    print("\nMotivos das reprovações:")

    encontrou_motivo = False

    for motivo, quantidade in motivos_reprovacao.items():

        if quantidade > 0:

            print("-", motivo + ":", quantidade)

            encontrou_motivo = True

    if not encontrou_motivo:
        print("Nenhuma reprovação registrada.")

    print("\nCaixas fechadas:", len(caixas_fechadas))

    if len(caixa_atual) > 0:
        print("Peças na caixa atual:", len(caixa_atual))
    else:
        print("Não há caixa em aberto.")

    print("======================================")


# ==============================
# MENU PRINCIPAL
# ==============================

while True:

    print("\n")
    print("================================")
    print(" SISTEMA DE CONTROLE INDUSTRIAL")
    print("================================")

    print("1 - Cadastrar nova peça")
    print("2 - Listar peças aprovadas/reprovadas")
    print("3 - Remover peça cadastrada")
    print("4 - Listar caixas fechadas")
    print("5 - Gerar relatório final")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        cadastrar_peca()

    elif opcao == "2":

        listar_pecas()

    elif opcao == "3":

        remover_peca()

    elif opcao == "4":

        listar_caixas()

    elif opcao == "5":

        gerar_relatorio()

    elif opcao == "0":

        print("\nPrograma encerrado.")
        break

    else:

        print("\nOpção inválida. Escolha uma opção do menu.")
