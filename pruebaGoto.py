from goto import with_goto

@with_goto  # Decorador necesario.
def llamada():
    print("IMPRIMIR ESTO")
llamada()

@with_goto  # Decorador necesario.
def principal():

    # t - temporales
    # a - parametros
    # v1 - retornos

    t0 = 15 + 6
    t1 = t0 * 2

    if t1 > 1:
        goto .L0
    else:
        goto .L1

    label .L0
    print("Codigo si es Verdadero.")
    llamada()
    goto .Salto

    label .L1
    print("Codigo si es Falso.")

    label .Salto
principal()

