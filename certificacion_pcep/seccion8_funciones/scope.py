variable_global: int = 3


def suma(primer_numero: int, segundo_numero: int) -> int:
    return primer_numero + segundo_numero


def funcion_con_variable_local() -> None:
    variable_local: int = 3
    print(variable_local)
