class Processo:

    def __int__(self):
        def __init__(self, indice, tempo_chegada, tempo_servico):
            self.indice = indice
            self.tempo_chegada = tempo_chegada
            self.tempo_servico = tempo_servico 

def adicionar_processos():
        processos = []
        n = str(input(f'Digite a quantidade de processos desejados: '))

        for i in range(n):
            indice = i+1
            tempo_chegada = int(input(f'Digite o tempo de chegada do processo: '))
            tempo_servico = int(input(f'Digite o tempo de serviço do processo: '))
            processos.append(Processo(indice, tempo_chegada, tempo_servico)) 
        return processos  

