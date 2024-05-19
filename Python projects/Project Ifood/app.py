from modelo.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('PH', 10)
restaurante_praca.receber_avaliacao('Kleber', 3)
restaurante_praca.receber_avaliacao('Lucas', 7)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()