import matplotlib.pyplot as plt

def grafico_dispersao(eixo_x, eixo_y):
    """Plota um gráfico de dispersão dos pontos fornecidos nos eixos x e y."""
    plt.scatter(eixo_x, eixo_y)
    plt.title(f"Gráfico de Dispersão com {len(pontos)} pontos")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.xticks(range(0, max(eixo_x)+1, 1))
    plt.yticks(range(0, max(eixo_y)+1, 1))
    plt.gcf().set_size_inches(12, 10)
    plt.grid(True)
    plt.show()

# Funções utilitárias para resíduos quadráticos modulares e curvas elípticas

RQ = []
eixo_x = []
eixo_y = []

def restos_quadraticos(mod):
    """Retorna uma lista ordenada com os resíduos quadráticos módulo `mod`.

    A função calcula todos os valores (n*n) % mod para n em 0..mod-1,
    remove duplicatas e retorna a lista ordenada.
    """
    global RQ
    m = int(mod)
    if m <= 0:
        return []
    # usar um set para garantir unicidade, depois ordenar
    residuos = { (n * n) % m for n in range(m) }
    RQ = sorted(residuos)
    return RQ

def eh_residuo(n, mod):
    """Retorna True se n é um resíduo quadrático módulo mod."""
    m = int(mod)
    if m <= 0:
        return False
    r = int(n) % m
    return r in restos_quadraticos(m)

def inverso_modular(a, mod):
    """Retorna o inverso multiplicativo de a módulo mod, ou None se não existir."""
    m = int(mod)
    a = int(a) % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def equacao_eliptica(a, b, mod):
    """Retorna os pontos (x, y) que satisfazem a equação elíptica y² = x³ + ax + b mod p."""
    pontos = []
    p = int(mod)
    for x in range(p):
        resultado = (x**3 + a * x + b) % p
        for y in range(p):
            if (y * y) % p == resultado:
                eixo_x.append(x)
                eixo_y.append(y)
                pontos.append((x, y))
    return pontos

while True:
    a = input("Entre com um número inteiro positivo para o coeficiente `a` (ou 'sair' para terminar): ")
    if a.lower() == 'sair':
        break
    b = input("Entre com um número inteiro positivo para o coeficiente `b` (ou 'sair' para terminar): ")
    if b.lower() == 'sair':
        break
    p = input("Entre com um número primo positivo para o módulo `p` (ou 'sair' para terminar): ")
    if p.lower() == 'sair':
        break
    try:
        a = int(a)
        b = int(b)
        p = int(p)
        pontos = equacao_eliptica(a, b, p)
        print(f"Pontos na curva elíptica y^2 = x^3 + {a}x + {b} mod {p}:")
        for ponto in pontos:
            print(ponto)
        print(f"Número total de pontos: {len(pontos)}")
        grafico_dispersao(eixo_x, eixo_y)
    except ValueError:
        print("Por favor, insira valores inteiros válidos.")