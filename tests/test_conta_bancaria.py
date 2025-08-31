from __future__ import annotations

import pytest

from conta_bancaria import ContaBancaria


def test_init_valid_e_props():
    c = ContaBancaria(" Ana ", 100.0)
    assert c.titular == "Ana"
    assert c.saldo == 100.0


def test_init_invalido():
    with pytest.raises(ValueError):
        ContaBancaria("", 0)
    with pytest.raises(ValueError):
        ContaBancaria("Fulano", -1)


def test_deposito_e_saque_basico(capsys):
    c = ContaBancaria("Fulano", 100.0)
    c.depositar(50)
    assert c.saldo == 150.0
    assert c.sacar(30) is True
    assert c.saldo == 120.0
    c.exibir_saldo()
    saida = capsys.readouterr().out.strip()
    assert saida == "Saldo atual de Fulano: R$ 120.00"


def test_deposito_invalido():
    c = ContaBancaria("Fulano")
    for valor in (0, -10):
        with pytest.raises(ValueError):
            c.depositar(valor)


def test_saque_invalido_ou_insuficiente():
    c = ContaBancaria("Fulano", 10)
    for valor in (0, -5):
        with pytest.raises(ValueError):
            c.sacar(valor)
    assert c.sacar(20) is False  # saldo insuficiente
    assert c.saldo == 10

