import re


palavras_positivas = ['bom', 'excelente', 'feliz']
palavras_negativas = ['ruim', 'péssimo', 'triste']

# Lista de feedbacks reais (exemplo maior)
feedbacks = [
    "O atendimento foi excelente e estou muito feliz com o resultado!",
    "Péssimo serviço, o atraso foi horrível e me deixou muito triste.",
    "O produto é bom, mas a entrega foi ruim.",
    "Experiência incrível, nota dez, tudo muito bom!",
    "Fiquei triste com a qualidade, achei péssimo."
]

# Variáveis para métricas gerais
total_positivos = 0
total_negativos = 0

for texto in feedbacks:
    qtd_p = len(re.findall(r'\b(?:%s)\b' % '|'.join(palavras_positivas), texto, flags=re.IGNORECASE))
    qtd_n = len(re.findall(r'\b(?:%s)\b' % '|'.join(palavras_negativas), texto, flags=re.IGNORECASE))
    
    if qtd_p > qtd_n: total_positivos += 1
    elif qtd_n > qtd_p: total_negativos += 1

# Métrica em "Tempo Real"
print(f"--- Dashboard de Sentimentos ---")
print(f"Total de feedbacks analisados: {len(feedbacks)}")
print(f"Satisfação dos Clientes: {(total_positivos/len(feedbacks))*100}%")

qtd_positiva = len(re.findall(r'\b(?:%s)\b' % '|'.join(palavras_positivas), texto, flags=re.IGNORECASE))
qtd_negativa = len(re.findall(r'\b(?:%s)\b' % '|'.join(palavras_negativas), texto, flags=re.IGNORECASE))

Conta a quantidade de palavras positivas e negativas que a regex vai procurar no texto

sentimento='Neutro'
if qtd_positiva > qtd_negativa:
  sentimento='Positivo'
elif qtd_negativa > qtd_positiva:
   sentimento='Negativo'

# Se uma frase tem 5 palavras positivas e 0 negativas, a confiança é alta.
# Se tem 5 positivas e 4 negativas, a confiança é baixa.
total_palavras = qtd_p + qtd_n
if total_palavras > 0:
    confianca = (abs(qtd_p - qtd_n) / total_palavras) * 100
    print(f"Confiança da análise: {confianca:.2f}%")

print(f'O sentimento sobre o atendimento foi: {sentimento}')

import matplotlib.pyplot as plt

# Dados para o gráfico
categorias = ['Positivas', 'Negativas']
valores = [qtd_positiva, qtd_negativa]
cores = ['#2ecc71', '#e74c3c'] # Verde e Vermelho

plt.figure(figsize=(8, 5))
plt.bar(categorias, valores, color=cores)
plt.title(f'Análise de Sentimento: {sentimento}')
plt.ylabel('Quantidade de Palavras')
plt.show()