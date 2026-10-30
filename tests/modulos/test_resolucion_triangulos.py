"""
Tests unitarios para las funciones del módulo resolucion_triangulos,
verificando la resolución de triángulos a partir de sus tres lados o de
un lado y dos ángulos, así como el manejo de datos inválidos.
"""

import pytest

from escuadra.modulos.geometria.resolucion_triangulos import (
    resolver_triangulo_lado_angulo,
    resolver_triangulo_lados,
)


def test_resolver_triangulo_lados_3_4_5():
    # El triángulo 3-4-5 es rectángulo: ángulos 36.87°, 53.13° y 90°
    angulos = resolver_triangulo_lados(3, 4, 5)
    assert angulos == pytest.approx((36.87, 53.13, 90.0), abs=0.01)


def test_resolver_triangulo_lados_equilatero():
    # Un triángulo equilátero tiene tres ángulos de 60°
    angulos = resolver_triangulo_lados(2, 2, 2)
    assert angulos == pytest.approx((60.0, 60.0, 60.0))


def test_resolver_triangulo_lados_desigualdad_triangular_lanza_error():
    # 1 + 2 no supera a 10, así que no se puede formar un triángulo
    with pytest.raises(ValueError):
        resolver_triangulo_lados(1, 2, 10)


def test_resolver_triangulo_lados_con_lado_cero_lanza_error():
    # Los lados deben ser mayores a cero
    with pytest.raises(ValueError):
        resolver_triangulo_lados(0, 1, 1)


def test_resolver_triangulo_lado_angulo_10_30_60():
    # Con a=10, A=30° y B=60° se obtiene b≈17.32, c=20 y C=90°
    b, c, angulo_c = resolver_triangulo_lado_angulo(10, 30, 60)
    assert b == pytest.approx(17.32, abs=0.01)
    assert c == pytest.approx(20.0)
    assert angulo_c == 90


def test_resolver_triangulo_lado_angulo_con_lado_cero_lanza_error():
    # El lado debe ser mayor a cero
    with pytest.raises(ValueError):
        resolver_triangulo_lado_angulo(0, 30, 60)


def test_resolver_triangulo_lado_angulo_con_suma_180_lanza_error():
    # Dos ángulos que suman 180° no dejan ángulo para el tercer vértice
    with pytest.raises(ValueError):
        resolver_triangulo_lado_angulo(10, 100, 80)
