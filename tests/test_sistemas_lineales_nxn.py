"""
Tests unitarios para la función resolver_sistema del módulo
sistemas_lineales_nxn, verificando la resolución de sistemas, el manejo
de matrices singulares y del pivoteo, y que los datos de entrada no se
modifiquen.
"""

import pytest

from escuadra.math.sistemas_lineales_nxn import resolver_sistema


def test_resolver_sistema_2x2():
    solucion = resolver_sistema([[2, 1], [1, 3]], [3, 5])

    assert solucion == pytest.approx([0.8, 1.4])


def test_resolver_sistema_3x3_con_solucion_conocida():
    A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b = [1, 1, 6]

    solucion = resolver_sistema(A, b)

    assert solucion == pytest.approx([1, 2, 3])


def test_resolver_sistema_singular_devuelve_none():
    assert resolver_sistema([[1, 2], [2, 4]], [3, 6]) is None


def test_resolver_sistema_que_requiere_pivoteo():
    solucion = resolver_sistema([[0, 2], [1, 1]], [4, 3])

    assert solucion == pytest.approx([1, 2])


def test_resolver_sistema_no_modifica_las_entradas():
    A = [[2, 1], [1, 3]]
    b = [3, 5]

    resolver_sistema(A, b)

    assert A == [[2, 1], [1, 3]]
    assert b == [3, 5]
