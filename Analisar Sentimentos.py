
def analisar_sentimento(comentario):
    # Lista de palavras positivas, negativas e neutras
    palavras_positivas = ["bom", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    palavras_negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    palavras_neutras = ["mas", "deixou", "apesar", "embora"]

    palavras = comentario.lower().split()

    contador_positivas = sum(palavra in palavras_positivas for palavra in palavras)
    contador_negativas = sum(palavra in palavras_negativas for palavra in palavras)
    contador_neutras = sum(palavra in palavras_neutras for palavra in palavras)

    if contador_positivas > contador_negativas:
        sentimento = "Positivo"
    elif contador_negativas > contador_positivas:
        sentimento = "Negativo"
    else:
        sentimento = "Neutro"

    return sentimento

comentario = input("Insira seu comentário: ")

sentimento = analisar_sentimento(comentario)
print("Sentimento:", sentimento)
