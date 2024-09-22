from processos import adicionar_processos
import time #para uso da função sleep


#função que retorna o tempo de chegada de cada processo
def get_tempo_chegada(processo):
    return processo.tempo_chegada 


def fifo(processos):
    processos.sort(key=get_tempo_chegada) #ordenando processos por tempo de chegada

    fila = [] #fila de processos pronto para execução
    tempo_total = 0 #tempo total de toda execução
    momento_atual = 0 #momento atual da execução
    executando = None
    
    #definindo o tempo total de serviço e o último tempo de chegada de um processo.
    tempo_servico_total = 0
    maior_tempo_chegada = 0
    for processo in processos():
        tempo_servico_total += processo.tempo_servico
        if processo.tempo_chegada > maior_tempo_chegada:
            maior_tempo_chegada = processo.tempo_chegada

    tempo_total = tempo_servico_total + maior_tempo_chegada


    #enquanto o momento_atual for menor ou igual ao tempo_total
    while momento_atual <= tempo_total:
        for processo in processos:
            #se o tempo de chegada do processo for igual momento_atual, adiciona ele na fila de processos pronto para execução.
            if processo.tempo_chegada == momento_atual:
                fila.append(processo)

        #se não estiver nada executando e a fila for true, ou seja, ainda tem itens na fila
        if executando is None and fila:
            if momento_atual >= fila[0].tempo_chegada + 1: #se o momento_atual for maior ou igual o tempo de chegada do processo, ele pode ser executado.
                executando = fila[0] #executando guarda o primeiro objeto da fila
                fila.pop(0) #aqui remove o primeiro objeto da fila

        #aqui começa a execução dos processos, acredito que outras variaveis vao ter q ser criadas la na classe de processos.
        if executando is not None:
