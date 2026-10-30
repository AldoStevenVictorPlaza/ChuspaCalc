import pytest

from escuadra.modulos.matematicas.financiera import (
    calcular_interes_compuesto,
    calcular_valor_futuro,
    calcular_valor_presente,
)


def test_calcular_valor_futuro():
    resultado = calcular_valor_futuro(1000, 0.1, 2)

    assert resultado == pytest.approx(1210.0)


def test_calcular_valor_presente():
    resultado = calcular_valor_presente(1210, 0.1, 2)

    assert resultado == pytest.approx(1000.0)


def test_calcular_interes_compuesto():
    resultado = calcular_interes_compuesto(1000, 0.1, 2)

    assert resultado == pytest.approx(210.0)


def test_valor_futuro_con_periodos_cero():
    resultado = calcular_valor_futuro(1000, 0.1, 0)

    assert resultado == pytest.approx(1000.0)


def test_interes_compuesto_con_tasa_cero():
    resultado = calcular_interes_compuesto(1000, 0, 2)

    assert resultado == pytest.approx(0.0)
