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

    t2 = True
    if t2:
        goto .L0
    else:
        goto .L1

    label .L0
    print("Codigo si es Verdadero.")
    goto .Salto

    label .L1
    print("Codigo si es Falso.")


    label .Salto
principal()

