from processos import adicionar_processos
import time

def obter_tempo_chegada(processo):
    return processo.tempo_chegada

def fifo_escalonamento(processos):
    processos.sort(key=obter_tempo_chegada)

    ultimo_processo = max([p.tempo_chegada for p in processos])
    for processo in processos:
        if ultimo_processo == processo.tempo_chegada:
            ultimo_servico = processo.tempo_servico

    tempo_total = ultimo_processo + ultimo_servico
    momento_atual = 0
    fila = []
    processo_em_andamento = None
    

    while momento_atual <= tempo_total:
        for processo in processos:
            #se o tempo de chegada do processo for igual momento_atual, adiciona ele na fila de processos pronto para execução.
            if processo.tempo_chegada == momento_atual:
                fila.append(processo)

        #se não estiver nada executando e a fila for true, ou seja, ainda tem itens na fila
        if processo_em_andamento is None and fila:
            if momento_atual >= fila[0].tempo_chegada + 1: #se o momento_atual for maior ou igual o tempo de chegada do processo, ele pode ser executado.
                processo_em_andamento = fila[0] #processo_em_andamento guarda o primeiro objeto da fila
                fila.pop(0)


        if processo_em_andamento is not None:
            processo_em_andamento.tempo_restante -= 1
            total_caracteres = processo_em_andamento.tempo_servico
            progresso = total_caracteres - processo_em_andamento.tempo_restante
            #IMPLEMENTAR A LOGICA DA MATRIZ
            linha_grafica = "█" * progresso + "□" * processo_em_andamento.tempo_restante
            print(f"Processo {processo_em_andamento.nome} em andamento: {linha_grafica}", end="\r")
            time.sleep(0.5)  
            
            if processo_em_andamento.tempo_restante == 0:
                print(f"\nProcesso {processo_em_andamento.nome} finalizado.")
                processo_em_andamento.momento_do_termino = momento_atual
                processo_em_andamento = None

        else:
            print("Esperando processo.", end="\r")
            time.sleep(0.5)

        momento_atual += 1

    print("\nTodos os processos foram executados.")
    for p in processos:
        print(f"Processo {p.nome}: Tempo de término = {p.momento_do_termino}, Turnaround time = {p.momento_do_termino - p.tempo_chegada}")


    for p in processos:
        p.momento_de_inicio = ((p.momento_do_termino - p.tempo_servico) + 1)


    for p in processos: 
        print(p.momento_de_inicio)

# Executar o simulador
processos = adicionar_processos()
fifo_escalonamento(processos)

