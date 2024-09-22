from random import randint
from fila import Fila
from processo import Processo

# Instruções para o usuário
# para as cores no terminal, checar: https://wiki.python.org.br/CoresNoTerminal
print('-'*100)
print('''\033[1m\033[32mOlá! Esse é um simulador de escalonamento de processos do tipo FIFO(First in, first out). 
Você pode acessar o nosso material caso ainda tenha dúvidas sobre FIFO!

Abaixo você poderá escolher quantos processos deseja simular. Leve em consideração que o
processo A é o primeiro a chegar, o B é o segundo, e assim sucessivamente.

Para uma melhor visualização, recomendamos que:
      - Utilize, no máximo, 5 processos
      - Cada processo tenha no máximo 9 unidades de tamanho
      
Se preferir, use a opção de gerar processos aleatoriamente :)\033[0;0m''')
print('-'*100)

while True:
    print('> Menu \n1) Inserir processos manualmente\n2) Gerar processos aleatoriamente')
    opcao = input('>> ')
    while opcao not in '12':
        print('\033[31mOpção invalida. Por favor, insira uma opção válida\033[0;0m')
        opcao = input('>> ')

    qtd_processos = int(input('Quantos processos deseja simular?(de 2 a 5 processos) '))
    while qtd_processos < 2 or qtd_processos > 5:
        print('\033[31mPor favor, insira a quantidade de processos dentro do intervalo indicado.\033[0;0m')
        qtd_processos = int(input('Quantos processos deseja simular?(de 2 a 5 processos) '))
    
    processos = Fila()

    if opcao == '1':
        for i in range(qtd_processos):
            tempo_servico = int(input(f'Insira o tempo de serviço do processo {chr(65+i)}: '))
            processos.enfileirar(tempo_servico)
        print(processos.dados())
    else:
        for i in range(qtd_processos):
            tempo_servico = randint(1, 9)
            processos.enfileirar(tempo_servico)
        print(processos.dados())

    lista_processos = processos.dados() # tempos de serviços recebidos em formato de lista

    # LÓGICA PARA MOSTRAR AO USUÁRIO OS PROCESSOS ESCALONADOS
    print('\nRESULTADO:\n')
    # A primeira linha representa o TEMPO
    for i in range(sum(lista_processos)):
        if i < 9:
            t = '0' + str(i + 1)
            print(f'{t:2}', end=' ')
        else:
            print(f'{i + 1:2}', end=' ')
    print()
    break
    # [X] usuário escolhe quantos processo vai querer OU gera processos aleatoriamente
    # [X] usuário digita os tamanhos dos processos OU os números são gerados

    # >>> COMO ORDENAR PELO TEMPO DE CHEGADA E, AO MESMO TEMPO, GUARDAR O NOME E O TEMPO DE SERVIÇO?

    #implementa-se a lógica para aparecer tudo na tela
    #pergunta se o usuário quer fazer outra simulação
    
