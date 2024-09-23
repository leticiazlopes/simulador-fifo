class Processo:

    def __init__(self, nome, tempo_chegada, tempo_servico):
        self.nome = nome
        self.tempo_chegada = tempo_chegada
        self.tempo_servico = tempo_servico 
        self.tempo_restante = tempo_servico 
        self.momento_do_termino = 0 # é inicializado aqui e calculado na simulação
        self.momento_de_inicio = 0 # é inicializado aqui e calculado na simulação

def adicionar_processos():
        processos = []
        
        n = input(f'Digite a quantidade de processos desejados: ')
        while not n.isnumeric(): # se 'n' não for numérico
             print('\033[31mO valor inserido é inválido. Por favor, digite um número inteiro.\033[0;0m')
             n = input(f'Digite a quantidade de processos desejados: ')

        for i in range(int(n)):
            nome = str(chr(65+i))
            #IMPLEMENTAR VALIDACAO
            tempo_chegada = input(f'Digite o tempo de chegada do processo {nome}: ')
            while not tempo_chegada.isnumeric() and tempo_chegada > '0':
                print('\033[31mO valor inserido é inválido. Por favor, digite um tempo de chegada válido\033[0;0m')
                tempo_chegada = input(f'Digite o tempo de chegada do processo {nome}: ')
            tempo_chegada = int(tempo_chegada)


            tempo_servico = input(f'Digite o tempo de serviço do processo {nome}: ')
            while not tempo_servico.isnumeric() and tempo_servico > '0':
                print('\033[31mO valor inserido é inválido. Por favor, digite um tempo de chegada válido\033[0;0m')
                tempo_servico = input(f'Digite o tempo de chegada do processo {nome}: ')
            tempo_servico = int(tempo_servico)
            
            processos.append(Processo(nome, tempo_chegada, tempo_servico)) 

        return processos  

