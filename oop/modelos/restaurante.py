from .avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
 
    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._cardapio = []
        self._avaliacoes = []
        self._ativo = True
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(19)} | {'Categoria'.ljust(19)} | {'Avaliações'.ljust(19)} | {'Status'.ljust(19)} ")
        for restaurante in cls.restaurantes:
            status = "Aberto" if restaurante._ativo else "Fechado"
            print(f'{restaurante._nome.ljust(19)} | {restaurante._categoria.ljust(19)} | {str(restaurante.media_avaliacao).ljust(19)} | {status.ljust(19)}')

    def receber_avaliacao(self, nome, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(nome, nota)
            self._avaliacoes.append(avaliacao)

    @property        #codigo 100 feito por mycael
    def media_avaliacao(self):
        soma = 0
        for avaliacao in self._avaliacoes:
            soma += avaliacao._nota

        try:
            media = soma / len(self._avaliacoes)
            return round(media, 1)
        except ZeroDivisionError:
            return '-'

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f'Cardapio do restaurante: {self._nome}')

        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                print(f'{i}. Prato: {item._nome} | R$ {item._preco:.2f} | {item._descricao}')
            else:
                print(f'{i}. Bebida: {item._nome} | R$ {item._preco:.2f} | {item._tamanho}')