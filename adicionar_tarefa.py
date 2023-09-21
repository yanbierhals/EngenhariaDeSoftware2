# Sistema de Gerenciamento de Tarefas

# Inicialize a lista de tarefas vazia
tarefas = []

# Função para adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = input("Digite a descrição da tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Chame a função para adicionar uma tarefa
adicionar_tarefa()

# Imprima a lista de tarefas atualizada
print("Lista de Tarefas:")
for i, tarefa in enumerate(tarefas, start=1):
    print(f"{i}. {tarefa}")
