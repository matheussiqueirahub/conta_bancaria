from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


def carregar_modulo():
    raiz = Path(__file__).resolve().parents[1]
    # Localiza o arquivo ignorando possíveis problemas de codificação no nome
    candidatos = list(raiz.glob("Program*Orientada-a-Objetos.py"))
    assert candidatos, "Arquivo de POO nao encontrado (pattern Program*Orientada-a-Objetos.py)"
    caminho = candidatos[0]
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
    out = capsys.readouterr().out.strip()
    assert out.startswith("Ve") and out.endswith("em movimento."), out


def test_movimentar_carro(capsys):
    m = carregar_modulo()
    v = m.Carro()
    v.movimentar()
    out = capsys.readouterr().out.strip()
    assert out.startswith("Carro") and out.endswith("dirigindo."), out


def test_movimentar_moto(capsys):
    m = carregar_modulo()
    v = m.Moto()
    v.movimentar()
    out = capsys.readouterr().out.strip()
    assert out.startswith("Moto") and out.endswith("acelerando."), out
