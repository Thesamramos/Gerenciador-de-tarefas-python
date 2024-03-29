def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefa(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustada = int(indice_tarefa) - 1
    if indice_tarefa_ajustada >= 0 and indice_tarefa_ajustada < len(tarefas):
        tarefas[indice_tarefa_ajustada]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa inválido.")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustada = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustada]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return

def deletar_tarefa_completada(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas deletadas")
    return

tarefas = []

while True:
    print("\nMenu do gerenciador de tarefa")
    print("1. Adicionar Tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefa(tarefas)
    elif escolha == "3":
        ver_tarefa(tarefas)
        indice = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice, novo_nome)
    elif escolha == "4":
        ver_tarefa(tarefas)
        indice = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice)
    elif escolha == "5":
        deletar_tarefa_completada(tarefas)
        ver_tarefa(tarefas)
    elif escolha == "6":
        break

print("Programa finalizado")