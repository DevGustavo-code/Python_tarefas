import random
import json
import os

TASKS = [
    "Estudar Python",
    "Beber água",
    "Lavar a louça",
    "Descansar 10 minutos",
    "Fazer alongamento",
    "Ler um artigo",
    "Organizar a mesa",
    "Revisar código antigo",
    "Escrever uma ideia nova"
]

def gerar_tarefa():
    tarefa = random.choice(TASKS)
    prioridade = random.choice(["Baixa", "Média", "Alta"])
    return {"tarefa": tarefa, "prioridade": prioridade}

def salvar_tarefas(lista):
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

def carregar_tarefas():
    if not os.path.exists("tarefas.json"):
        return []
    with open("tarefas.json", "r", encoding="utf-8") as f:
        return json.load(f)

def mostrar_tarefas(lista):
    print("\n=== Lista de Tarefas ===")
    if not lista:
        print("Nenhuma tarefa registrada.")
        return

    for i, t in enumerate(lista, 1):
        print(f"{i}. {t['tarefa']} (Prioridade: {t['prioridade']})")

def main():
    tarefas = carregar_tarefas()

    while True:
        print("\n1 - Gerar nova tarefa")
        print("2 - Mostrar tarefas")
        print("3 - Limpar lista")
        print("4 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
            nova = gerar_tarefa()
            tarefas.append(nova)
            salvar_tarefas(tarefas)
            print(f"Tarefa criada: {nova['tarefa']} - Prioridade {nova['prioridade']}")

        elif opc == "2":
            mostrar_tarefas(tarefas)

        elif opc == "3":
            tarefas = []
            salvar_tarefas(tarefas)
            print("Lista apagada!")

        elif opc == "4":
            print("Encerrado.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
