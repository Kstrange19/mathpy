def algoritmo_euclides(a, b):
    """Retorna o máximo divisor comum (MDC) de a e b usando o Algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a

def algoritmo_euclides_estendido(a, b):
    """Retorna o MDC de a e b, e os coeficientes x e y tais que ar + bs = MDC(a, b)."""
    if a == 0:
        return b, 0, 1
    else:
        mdc, r1, s1 = algoritmo_euclides_estendido(b % a, a)
        r = s1 - (b // a) * r1
        s = r1
        return mdc, r, s