"""
Exemplo simples de POO em Python com herança e sobrescrita de métodos.

Classes:
- Veiculo: classe base com o método movimentar().
- Carro: subclasse que sobrescreve movimentar() para mensagem específica.
- Moto: subclasse que sobrescreve movimentar() para mensagem específica.
"""

from __future__ import annotations


class Veiculo:
    """Classe base que representa um veículo genérico."""

    def movimentar(self) -> None:
        """Indica que o veículo está em movimento."""
        print("Veículo está em movimento.")


class Carro(Veiculo):
    """Representa um carro, especialização de Veiculo."""

    def movimentar(self) -> None:
        """Indica que o carro está dirigindo."""
        print("Carro está dirigindo.")


class Moto(Veiculo):
    """Representa uma moto, especialização de Veiculo."""

    def movimentar(self) -> None:
        """Indica que a moto está acelerando."""
        print("Moto está acelerando.")


if __name__ == "__main__":
    # Demonstração simples de polimorfismo:
    frota: list[Veiculo] = [Veiculo(), Carro(), Moto()]
    for v in frota:
        v.movimentar()
