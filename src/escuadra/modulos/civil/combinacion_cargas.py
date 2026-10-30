"""
Modulo para combinacion de cargas vivas y muertas en ingenieria civil.

Este calculo es educativo y simplificado.
No reemplaza la normativa estructural local vigente.
"""


def _validar_cargas(carga_muerta: float, carga_viva: float) -> None:
    """
    Valida que las cargas suministradas no sean negativas.

    Raises:
        ValueError: si la carga muerta o la carga viva es negativa.
    """
    if carga_muerta < 0:
        raise ValueError("La carga muerta no puede ser negativa.")
    if carga_viva < 0:
        raise ValueError("La carga viva no puede ser negativa.")


def combinar_cargas_lrfd(
    carga_muerta: float,
    carga_viva: float,
    factor_muerta: float = 1.2,
    factor_viva: float = 1.6,
) -> float:
    """
    Calcula la carga ultima de diseno mediante factores LRFD.

    Formula:
        U = factor_muerta * carga_muerta + factor_viva * carga_viva

    Args:
        carga_muerta: carga permanente o muerta.
        carga_viva: carga variable o viva.
        factor_muerta: factor aplicado a carga muerta.
        factor_viva: factor aplicado a carga viva.

    Returns:
        Carga ultima combinada.

    Raises:
        ValueError: si la carga muerta o la carga viva es negativa.
    """
    _validar_cargas(carga_muerta, carga_viva)
    return factor_muerta * carga_muerta + factor_viva * carga_viva


def combinar_cargas_asd(carga_muerta: float, carga_viva: float) -> float:
    """
    Calcula la carga de servicio combinada mediante el metodo ASD.

    Formula:
        S = carga_muerta + carga_viva

    Args:
        carga_muerta: carga permanente o muerta.
        carga_viva: carga variable o viva.

    Returns:
        Carga combinada de servicio.

    Raises:
        ValueError: si la carga muerta o la carga viva es negativa.
    """
    _validar_cargas(carga_muerta, carga_viva)
    return carga_muerta + carga_viva
