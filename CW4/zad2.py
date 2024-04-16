from zad1 import calcParams
slope, intercept = calcParams()


def predict_unemployment(year):
    return slope * year + intercept


target_unemployment_rate = 12
year = 2000

while predict_unemployment(year) < target_unemployment_rate:
    year += 1

print(f"Procent bezrobotnych przekroczy 12% w roku {year}.")
