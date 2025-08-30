from collections import Counter

def contar_frequencias(numeros, ordenar_por="valor", decrescente=False):
    """
    ordenar_por:
      - "valor"       -> ordena pelos próprios números (default)
      - "frequencia"  -> ordena pela contagem
      - "aparicao"    -> mantém a ordem do primeiro aparecimento na lista
    decrescente:
      - True  -> ordem decrescente
      - False -> ordem crescente (default)
    """
    freq = Counter(numeros)
    print(f"Total de números: {len(numeros)}")

    if ordenar_por == "valor":
        for n in sorted(freq.keys(), reverse=decrescente):
            qtd = freq[n]
            print(f"Número {n}: {qtd} {'vez' if qtd == 1 else 'vezes'}")

    elif ordenar_por == "frequencia":
        if decrescente:
            # mais frequentes primeiro; em empate, menor número primeiro
            pares = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        else:
            # menos frequentes primeiro; em empate, menor número primeiro
            pares = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        for n, qtd in pares:
            print(f"Número {n}: {qtd} {'vez' if qtd == 1 else 'vezes'}")

    elif ordenar_por == "aparicao":
        vistos = dict.fromkeys(numeros)  # preserva a ordem do primeiro aparecimento
        for n in vistos.keys():
            qtd = freq[n]
            print(f"Número {n}: {qtd} {'vez' if qtd == 1 else 'vezes'}")

    else:
        raise ValueError("Parâmetro 'ordenar_por' deve ser 'valor', 'frequencia' ou 'aparicao'.")

# ===================== EXEMPLO DE USO =====================
numeros = [84, 68, 33, 53, 47, 73, 68, 63, 73, 77, 40,
           74, 71, 81, 91, 65, 55, 57, 45, 85, 88,
           59, 80, 41, 50, 53, 65, 76, 85, 73, 60,
           67, 51, 78, 56, 94, 35, 45, 55, 64, 74,
           65, 94, 76, 48, 39, 69, 89, 98, 43, 54]

# Somente números da lista, em ordem numérica crescente:
contar_frequencias(numeros, ordenar_por="valor", decrescente=False)

# Outras opções:
# contar_frequencias(numeros, ordenar_por="frequencia", decrescente=True)   # mais frequentes primeiro
# contar_frequencias(numeros, ordenar_por="aparicao")                        # na ordem em que aparecem
