class Formatador:
    """
    Classe responsável por formatações.
    """

    @staticmethod
    def formatar_moeda(valor):
        return f"R$ {valor:.2f}"

    @staticmethod
    def linha():
        print("-" * 50)

    @staticmethod
    def titulo(texto):
        Formatador.linha()
        print(texto.upper())
        Formatador.linha()
