from processos import adicionar_processos
import time

def instrucoes():
    print('-'*100)
    print('''\033[1m\033[32mOlá! Esse é um simulador de escalonamento de processos do tipo FIFO(First in, first out). 
Você pode acessar o nosso material caso ainda tenha dúvidas sobre FIFO!

O simulador pode ser usado para complementar o seu aprendizado e auxiliar nos estudos.
Não deixe de utilizar os gráficos de Grantt vistos com o professor.

Abaixo, insira a quantidade de processos que deseja analisar. Logo após, insira seus tempos de chegada e tempos de serviço.

Por fim, o programa calculará: o tempo de turnaround e o tempo de espera. Além disso, mostrará o tempo de início e o tempo de término \033[0;0m''')
    print('-'*100)

def obter_tempo_chegada(processo):
    return processo.tempo_chegada

def fifo_escalonamento(processos):
    processos.sort(key=obter_tempo_chegada)

    ultimo_processo = max([p.tempo_chegada for p in processos]) # descobre-se o último processo
    '''
    tempo_total = 0
    for processo in processos:
        if processo.tempo_chegada == ultimo_processo:
            tempo_total = processo.tempo_chegada + processo.tempo_servico # calcula-se o tempo total de execução
    '''
    servico_total = 0
    for processo in processos:
        servico_total += processo.tempo_servico

    tempo_total = ultimo_processo + servico_total
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
    # cálculo do momento de início
    for p in processos:
        p.momento_de_inicio = ((p.momento_do_termino - p.tempo_servico) + 1)

    for p in processos:
        print(f'''
\033[1m\033[34mProcesso {p.nome}:\033[0;0m 
Tempo de espera: {p.momento_de_inicio - p.tempo_chegada - 1}
Tempo de início: {p.momento_de_inicio}
Tempo de término = {p.momento_do_termino}
Turnaround time = {p.momento_do_termino - p.tempo_chegada}''')
        print()

# Executar o simulador
instrucoes()
processos = adicionar_processos()
fifo_escalonamento(processos)

