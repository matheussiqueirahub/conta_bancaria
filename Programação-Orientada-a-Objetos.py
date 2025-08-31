from __future__ import annotations
from abc import ABC, abstractmethod


class Veiculo(ABC):
    """Classe base abstrata para veículos."""

    @abstractmethod
    def movimentar(self) -> None:
        """Ação de movimento a ser implementada pelas subclasses."""
        raise NotImplementedError


class VeiculoGenerico(Veiculo):
    """Implementação genérica que apenas indica movimento."""

    def movimentar(self) -> None:
        print("Veículo está em movimento.")


class Carro(Veiculo):
    """Representa um Carro."""

    def movimentar(self) -> None:
        print("Carro está dirigindo.")


class Moto(Veiculo):
    """Representa uma Moto."""

    def movimentar(self) -> None:
        print("Moto está acelerando.")


if __name__ == "__main__":
    # Demonstração de polimorfismo com veículos
    veiculos: list[Veiculo] = [VeiculoGenerico(), Carro(), Moto()]
    for v in veiculos:
        v.movimentar()

    # Demonstração simples de ContaBancaria
    from conta_bancaria import ContaBancaria

    conta = ContaBancaria("Ana", 100.0)
    conta.depositar(50)
    conta.sacar(30)
    conta.exibir_saldo()

