import matplotlib.pyplot as plt

opcoes = {
    '1': "Restos Quadráticos Modulares",
    '1.1': "Ver calculo de resíduos quadráticos modulares",
    '2': "Visualizar pontos da Curva Elíptica",
    '2.2': "Ver calculo da equação elíptica",
    '3': "Ver gráfico de dispersão",
    '0': "Sair"
}

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
pontos = []

def restos_quadraticos(mod):
    """Retorna uma lista ordenada com os resíduos quadráticos módulo `mod`.

    A função calcula todos os valores (n*n) % mod para n em 0..mod-1,
    remove duplicatas e retorna a lista ordenada.
    """
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
    global eixo_x, eixo_y, pontos
    p = int(mod)
    # Limpa os eixos e pontos antes de adicionar novos
    eixo_x.clear()
    eixo_y.clear()
    pontos.clear()
    for x in range(p):
        resultado = (x**3 + a * x + b) % p
        for y in range(p):
            if (y * y) % p == resultado:
                eixo_x.append(x)
                eixo_y.append(y)
                pontos.append((x, y))
    return pontos

a = input("Entre com um número inteiro positivo para o coeficiente `a`: ")
b = input("Entre com um número inteiro positivo para o coeficiente `b`: ")
p = input("Entre com um número primo positivo para o módulo `p`: ")
while True:
    try:
        a = int(a)
        b = int(b)
        p = int(p)
        for opcao in opcoes:
            print(f"{opcao}: {opcoes[opcao]}")
        escolha = input("\nEscolha uma opção: ")
        if escolha == '1':
            residuos = restos_quadraticos(p)
            print(f"Resíduos quadráticos módulo {p}: {residuos}")
            print(f"Número total de resíduos quadráticos: {len(residuos)}")
            print("~" * 30)
        elif escolha == '1.1':
            for n in range(p):
                print(f"{n}² = {n * n} mod {p} = {(n * n) % p}")
                print("~" * 30)
            print("\n")
        elif escolha == '2':
            print(f"Pontos na curva elíptica y^2 = x^3 + {a}x + {b} mod {p}:")
            equacao_eliptica(a, b, p)
            for ponto in pontos:
                print(ponto)
            print("~" * 30)
            print(f"Número total de pontos: {len(pontos)}")
            print("\n")
        elif escolha == '2.2':
            for x in range(0, p):
                resultado = (x ** 3 + a * x + b)
                if resultado % p in restos_quadraticos(p):
                    print(f"x = {x} => y² = x³ + {a}*{x} + {b} = {resultado} mod {p} = {resultado % p} ✅ -> ({x}, {resultado % p})")
                else:
                    print(f"x = {x} => y² = x³ + {a}*{x} + {b} = {resultado} mod {p} = {resultado % p} ❌ -> não é resíduo quadrático")
                print("~" * 30)
            print("\n")
        elif escolha == '3':
            grafico_dispersao(eixo_x, eixo_y)
        elif escolha == '0':
            print("Saindo do programa.")
            break
    except ValueError:
        print("Por favor, insira valores inteiros válidos.")
        exit(1)
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        exit(0)