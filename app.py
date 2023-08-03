import pandas as pd

temperatura = [71, 69, 80, 83, 70, 65, 64, 72, 75, 68, 81, 85, 72, 75]
humidade = [91, 70, 90, 86, 96, 70, 65, 90, 70, 80, 75, 85, 95, 80]


# Função para calcular os outliers
def get_outliers(dados):
    print("-----------------------------------")
    # Converte a lista em um objeto Series do pandas
    dados_series = pd.Series(dados)

    # Calcula os quartis
    Q1 = dados_series.quantile(0.25)
    Q3 = dados_series.quantile(0.75)

    print("Q1:", Q1)
    print("Q3:", Q3)

    # Calcula o IQR
    IQR = Q3 - Q1

    print("IQR:", IQR)

    # Calcula os limites inferior e superior
    limite_inferior = 1.5 * IQR - Q1
    limite_superior = 1.5 * IQR + Q3

    print("Limite inferior:", limite_inferior)
    print("Limite superior:", limite_superior)

    # Identifica os outliers
    outliers = (dados_series < limite_inferior) | (dados_series > limite_superior)

    outliers_valores = dados_series[outliers]
    return outliers_valores


# Chama a função para calcular os outliers
print("Outliers de humidade:", get_outliers(humidade))
print("Outliers de temperatura:", get_outliers(temperatura))
