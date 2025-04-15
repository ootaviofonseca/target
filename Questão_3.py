import json
def media(dados):
    
    return sum(dados) / len(dados) if dados else 0

def diasAcimaDaMedia(dados, media):
    return sum(1 for valor in dados if valor > media)

def maiorFaturamento(dados):
    return max(dados) if dados else 0

def menorFaturamento(dados):
    return min(dados) if dados else 0

# Carregar os dados do arquivo JSON
with open('dadosfaturamento.json', 'r') as f:
    dados = json.load(f)

# Filtrar apenas os dias com faturamento > 0
faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]


menor = menorFaturamento(faturamentos)
maior = maiorFaturamento(faturamentos)
mediaTotal = media(faturamentos) 
acima_media = diasAcimaDaMedia(faturamentos, mediaTotal)

# Resultados
print("Menor faturamento:", menor)
print("Maior faturamento:", maior)
print("Dias com faturamento acima da média:", acima_media)
