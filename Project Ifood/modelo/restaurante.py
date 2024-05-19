from modelo.avaliacao import Avaliacao

class Restaurante:
    # criando uma lista para adição dos restaurantes
    restaurantes = []

    # criando uma função para cada restaurante único
    # self indica que o nome, categoria, ativo vão ser apenas de um unico obj (referencia da instancia atual), porém podendo usar qualquer outro nome

    def __init__(self, nome, categoria):
    # quais são as caracteristicas da classe?
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        # adicionando restaurantes criados na lista 
        Restaurante.restaurantes.append(self)

    # função que exibe os atributos da classe em String
    # sem __str__ -> <__main__.Restaurante object at 0x00000241D5119CD0>
    # com __str__ -> Praça | Gourmet

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    # metodo próprio - criando por mim
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        # _ativo, significa que o atributo esta "protegido"
        # não deve ser modificado diretamente de fora da classe, terão que usar as propriedades
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <=nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        # caso não tenha avaliações retorna 0
        if not self._avaliacao:
            return '-'
        # soma para cada numero nas avaliações
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        # quantas avaliações tem 
        quant_notas = len(self._avaliacao)
        # divisao para calculo da media (exibe apenas 1 casa decimal)
        media = round(soma_notas/ quant_notas, 1)
        return media

# restaurante_praca = Restaurante('Praça', 'Gourmet')
# restaurante_praca.alternar_estado()
# restaurante_pizza = Restaurante('Pizza', 'Italiana')

# Restaurante.listar_restaurantes()

# print(vars(restaurante_praca))
# print(dir(restaurante_pizza))
# print(restaurante_praca)
