class Fila:

    def __init__(self):
        self._dados = []

    def enfileirar(self, elemento):
        self._dados.append(elemento)

    def desenfileirar(self):
        return self._dados.pop(0)
   
    def imprimir(self):
        print(self._dados)
       
    def dados(self) -> list:
        lista_dados = self._dados
        return lista_dados
    