# Sistema de Gerenciamento de Tarefas

# Lista de tarefas (suponha que já tenhamos algumas tarefas adicionadas)
tarefas = ["Lavar a louça", "Fazer compras", "Estudar Python"]

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida():
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

    indice = int(input("Digite o número da tarefa concluída: "))
    
    if 1 <= indice <= len(tarefas):
        tarefas.pop(indice - 1)
        print("Tarefa  concluída")
    else:
        print("Índice inválido. Tarefa não encontrada.")

# Chame a função para marcar uma tarefa como concluída
marcar_tarefa_concluida()
