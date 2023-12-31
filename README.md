# Análise de Outliers em Dados de Temperatura e Umidade

Este script Python utiliza a biblioteca pandas para realizar uma análise de outliers em conjuntos de dados de temperatura e umidade. Ele calcula os quartis, o IQR (Intervalo Interquartil) e, com base nesses valores, identifica os valores que são considerados outliers.

## Dados de Exemplo

```python
import pandas as pd

temperatura = [71, 69, 80, 83, 70, 65, 64, 72, 75, 68, 81, 85, 72, 75]
humidade = [91, 70, 90, 86, 96, 70, 65, 90, 70, 80, 75, 85, 95, 80]

```

Os dados de exemplo são fornecidos para as variáveis 'temperatura' e 'humidade', que contêm listas de números representando as leituras de temperatura e umidade, respectivamente.

## Função `get_outliers`

A função `get_outliers(dados)` é definida para identificar e retornar os outliers em um conjunto de dados. Os passos para identificar os outliers são os seguintes:

1. Converte a lista em um objeto Series do pandas.
2. Calcula os quartis (Q1 e Q3) e o IQR (Intervalo Interquartil).
3. Calcula os limites inferior e superior utilizando a fórmula correta: `limite_inferior = 1.5 * IQR - Q1` e `limite_superior = 1.5 * IQR + Q3`.
4. Identifica os outliers usando a condição `dados_series < limite_inferior) | (dados_series > limite_superior)`.
5. Retorna os valores identificados como outliers.

```python
def get_outliers(dados):
    # Converte a lista em um objeto Series do pandas
    dados_series = pd.Series(dados)

    # Calcula os quartis
    Q1 = dados_series.quantile(0.25)
    Q3 = dados_series.quantile(0.75)

    # Calcula o IQR
    IQR = Q3 - Q1

    # Calcula os limites inferior e superior
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = 1.5 * IQR + Q3

    # Identifica os outliers
    outliers = (dados_series < limite_inferior) | (dados_series > limite_superior)

    outliers_valores = dados_series[outliers]
    return outliers_valores
```

## Identificação dos Outliers

Após definir a função `get_outliers`, os outliers são identificados para as variáveis 'temperatura' e 'humidade' chamando a função `get_outliers(dados)` para cada conjunto de dados.

```python
# Chama a função para calcular os outliers
print("Outliers de humidade:", get_outliers(humidade))
print("Outliers de temperatura:", get_outliers(temperatura))
```


## Resultado
O script retornou que não existem outliers nos dados fornecidos.

Segue um print do retorno do script no console.

![Alt text](image.png)