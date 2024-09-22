
class Processo:

    def __init__(self, nome, tempo_chegada, tempo_servico):
        self.nome = nome
        self.tempo_chegada = tempo_chegada
        self.tempo_servico = tempo_servico 
        self.tempo_restante = tempo_servico 
        self.momento_do_termino = 0
        self.momento_de_inicio = 0 




def adicionar_processos():
        processos = []
        #IMPLEMENTAR VALIDACAO
        n = int(input(f'Digite a quantidade de processos desejados: '))

        for i in range(n):
            nome = str(chr(65+i))
            #IMPLEMENTAR VALIDACAO
            tempo_chegada = int(input(f'Digite o tempo de chegada do processo {nome}: '))
            tempo_servico = int(input(f'Digite o tempo de serviço do processo {nome}: '))
            processos.append(Processo(nome, tempo_chegada, tempo_servico)) 

        return processos  

