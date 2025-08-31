"""
Classe ContaBancaria com encapsulamento de saldo e operações básicas.

Uso rápido:
    conta = ContaBancaria("Fulano", 100.0)
    conta.depositar(50)
    ok = conta.sacar(30)
    conta.exibir_saldo()  # Saída: "Saldo atual de Fulano: R$ 120.00"
"""

from __future__ import annotations


class ContaBancaria:
    """Modelo simples de conta bancária com encapsulamento do saldo.

    - _titular: nome do titular da conta (privado por convenção)
    - _saldo: saldo atual da conta (privado por convenção)
    """

    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        if not isinstance(titular, str) or not titular.strip():
            raise ValueError("Titular deve ser um nome não vazio.")
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")
        self._titular: str = titular.strip()
        self._saldo: float = float(saldo_inicial)

    @property
    def titular(self) -> str:
        """Retorna o nome do titular (somente leitura)."""
        return self._titular

    @property
    def saldo(self) -> float:
        """Retorna o saldo atual (somente leitura)."""
        return self._saldo

    def depositar(self, valor: float) -> None:
        """Adiciona um valor positivo ao saldo."""
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser positivo.")
        self._saldo += float(valor)

    def sacar(self, valor: float) -> bool:
        """Saca um valor, caso haja saldo suficiente. Retorna True se o saque foi realizado."""
        if valor <= 0:
            raise ValueError("Valor do saque deve ser positivo.")
        if valor > self._saldo:
            return False
        self._saldo -= float(valor)
        return True

    def exibir_saldo(self) -> None:
        """Exibe o saldo atual da conta."""
        print(f"Saldo atual de {self._titular}: R$ {self._saldo:.2f}")


__all__ = ["ContaBancaria"]

