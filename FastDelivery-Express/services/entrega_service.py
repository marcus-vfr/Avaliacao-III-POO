from modelos.entrega import (
    EntregaComum,
    EntregaExpressa,
    EntregaPremium
)


class EntregaService:
    """
    Responsável pela criação dos tipos de entrega.
    """

    @staticmethod
    def criar_entrega(tipo, distancia):

        tipo = tipo.lower()

        if tipo == "comum":
            return EntregaComum(distancia)

        elif tipo == "expressa":
            return EntregaExpressa(distancia)

        elif tipo == "premium":
            return EntregaPremium(distancia)

        raise ValueError("Tipo de entrega inválido.")
