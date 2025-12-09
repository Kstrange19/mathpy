import matplotlib.pyplot as plt
import sys
import os

# Obtém o caminho da pasta onde o main.py está, e sobe um nível (para a pasta MATEPY)
caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(caminho_raiz)

from utils.funcs import algoritmo_euclides_estendido

opcoes = {
    '1': "Restos Quadráticos Modulares",
    '~ 1.1': "Ver calculo de resíduos quadráticos modulares",
    '2': "Visualizar pontos da Curva Elíptica",
    '~ 2.2': "Ver calculo da equação elíptica",
    '3': "Ver gráfico de dispersão",
    '4': "Checar singularidade",
    '5': "Checar isomorfismo",
    '6': "Calcular J-invariante",
    '7': "Calcular discriminante",
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
discriminante = lambda a, b, m: -16 * (4 * a**3 + 27 * b**2) % m
j_invariante = lambda a, b, m: (-1728 * (4 * a ** 3) * inverso_modular(a, b, m) % m) if discriminante(a, b) != 0 else "Indefinido."

def restos_quadraticos(m):
    """Retorna uma lista ordenada com os resíduos quadráticos módulo `mod`.

    A função calcula todos os valores (n*n) % mod para n em 0..mod-1,
    remove duplicatas e retorna a lista ordenada.
    """
    m = int(m)
    if m <= 0:
        return []
    # usar um set para garantir unicidade, depois ordenar
    residuos = { (n * n) % m for n in range(m) }
    RQ = sorted(residuos)
    return RQ

def eh_residuo(n, m):
    """Retorna True se n é um resíduo quadrático módulo mod."""
    m = int(m)
    if m <= 0:
        return False
    r = int(n) % m
    return r in restos_quadraticos(m)

def inverso_modular(a, b, m):
    """Retorna o inverso multiplicativo de a módulo mod, ou None se não existir."""
    a = int(a) % m
    b = int(b) % m
    m = int(m)
    d = discriminante(a, b)
    if d == 0:
        return None
    mdc, r, s = algoritmo_euclides_estendido(d, m)
    if mdc != 1:
        return None
    else:
        return r % m

def equacao_eliptica(a, b, m):
    """Retorna os pontos (x, y) que satisfazem a equação elíptica y² = x³ + ax + b mod p."""
    global eixo_x, eixo_y, pontos
    m = int(m)
    # Limpa os eixos e pontos antes de adicionar novos
    eixo_x.clear()
    eixo_y.clear()
    pontos.clear()
    for x in range(m):
        resultado = (x**3 + a * x + b) % m
        for y in range(m):
            if (y * y) % m == resultado:
                eixo_x.append(x)
                eixo_y.append(y)
                pontos.append((x, y))
    return pontos

def checar_singularidade(a, b, m):
    """Verifica se a curva elíptica é singular."""
    m = int(m)
    discriminante(a, b, m)
    return discriminante == 0

def checar_isomorfismo(a1, b1, a2, b2, m):
    """Verifica se duas curvas elípticas são isomorfas."""
    m = int(m)
    j1 = j_invariante(a1, b1, m)
    j2 = j_invariante(a2, b2, m)
    if j1 == j2:
        print(f"J-invariante da primeira curva: {j1}")
        print(f"J-invariante da segunda curva: {j2}")
        return True
    else:
        print(f"J-invariante da primeira curva: {j1}")
        print(f"J-invariante da segunda curva: {j2}")
        return False

a = input("Entre com um número inteiro positivo para o coeficiente `a`: ")
b = input("Entre com um número inteiro positivo para o coeficiente `b`: ")
m = input("Entre com um número primo positivo para o módulo `m`: ")
while True:
    try:
        a = int(a)
        b = int(b)
        m = int(m)
        for opcao in opcoes:
            print(f"{opcao}: {opcoes[opcao]}")
        escolha = input("\nEscolha uma opção: ")
        if escolha == '1':
            residuos = restos_quadraticos(m)
            print(f"Resíduos quadráticos módulo {m}: {residuos}")
            print(f"Número total de resíduos quadráticos: {len(residuos)}")
            print("~" * 30)
        elif escolha == '1.1':
            for n in range(m):
                print(f"{n}² = {n * n} mod {m} = {(n * n) % m}")
                print("~" * 30)
            print("\n")
        elif escolha == '2':
            print(f"Pontos na curva elíptica y^2 = x^3 + {a}x + {b} mod {m}:")
            equacao_eliptica(a, b, m)
            for ponto in pontos:
                print(ponto)
            print("~" * 30)
            print(f"Número total de pontos: {len(pontos)}")
            print("\n")
        elif escolha == '2.2':
            for x in range(0, m):
                resultado = (x ** 3 + a * x + b)
                if resultado % m in restos_quadraticos(m):
                    print(f"x = {x} => y² = x³ + {a}*{x} + {b} = {resultado} mod {m} = {resultado % m} ✅ -> ({x}, {resultado % m}) é um ponto da curva")
                else:
                    print(f"x = {x} => y² = x³ + {a}*{x} + {b} = {resultado} mod {m} = {resultado % m} ❌ -> não é resíduo quadrático")
                print("~" * 30)
            print("\n")
        elif escolha == '3':
            grafico_dispersao(eixo_x, eixo_y)
        elif escolha == '4':
            if checar_singularidade(a, b, m):
                print("A curva elíptica é singular.")
            else:
                print("A curva elíptica não é singular.")
            print("~" * 30)
        elif escolha == '5':
            a2 = int(input("Entre com o coeficiente `a` da segunda curva: "))
            b2 = int(input("Entre com o coeficiente `b` da segunda curva: "))
            checar_isomorfismo(a, b, a2, b2, m)
            print("~" * 30)
        elif escolha == '6':
            j = j_invariante(a, b, m)
            print(f"J-invariante da curva elíptica y² = x³ + {a}x + {b} mod {m} é: {j}")
            print("~" * 30)
        elif escolha == '7':
            d = discriminante(a, b, m)
            print(f"O discriminante da curva elíptica y² = x³ + {a}x + {b} mod {m} é: {d}")
            print("~" * 30)
        elif escolha == '0':
            print("Saindo do programa.")
            break
    except ValueError:
        print("Por favor, insira valores inteiros válidos.")
        exit(1)
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        exit(0)