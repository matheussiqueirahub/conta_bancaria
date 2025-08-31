from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


def carregar_modulo():
    raiz = Path(__file__).resolve().parents[1]
    caminho = raiz / "Programação-Orientada-a-Objetos.py"
    assert caminho.exists(), f"Arquivo não encontrado: {caminho}"
    spec = importlib.util.spec_from_file_location("poo_veiculos", caminho)
    assert spec and spec.loader
    modulo = importlib.util.module_from_spec(spec)
    sys.modules["poo_veiculos"] = modulo
    spec.loader.exec_module(modulo)  # type: ignore[attr-defined]
    return modulo


def test_veiculo_abstrato():
    m = carregar_modulo()
    with pytest.raises(TypeError):
        m.Veiculo()  # type: ignore[call-arg]


def test_movimentar_generico(capsys):
    m = carregar_modulo()
    v = m.VeiculoGenerico()
    v.movimentar()
    assert capsys.readouterr().out.strip() == "Veículo está em movimento."


def test_movimentar_carro(capsys):
    m = carregar_modulo()
    v = m.Carro()
    v.movimentar()
    assert capsys.readouterr().out.strip() == "Carro está dirigindo."


def test_movimentar_moto(capsys):
    m = carregar_modulo()
    v = m.Moto()
    v.movimentar()
    assert capsys.readouterr().out.strip() == "Moto está acelerando."

