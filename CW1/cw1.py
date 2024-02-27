import numpy as np

# Załaduj dane
data = np.loadtxt('D:\Szkoła\Semestr 6\SI\CW1\dane\\australian.txt')
np.set_printoptions(suppress=True)
typ = open("D:\Szkoła\Semestr 6\SI\CW1\dane\\australian-type.txt", "r")
typy = []
for x in typ:
    typy.append(x[-2])
typy.append('nd')
typ.close()

# a) wypisujemy istniejące w systemie symbole klas decyzyjnych
symb_klas = np.unique(data[:, -1])
print("Symbole klas: ", symb_klas)

# b) wielkości klas decyzyjnych (liczby obiektów w klasach)
wielk_klas = data.shape[0]
print("Wielkość klas: ", wielk_klas)

# c) minimalne i maksymalne wartości poszczególnych atrybutów(dotyczy atrybutównumerycznych)
i = 0
for col in data.T:
    if typy[i] == 'n':
        print("Atrybut ", i + 1, " Min: ", np.min(col), " Max: ", np.max(col))
    i += 1

# d) dla każdego atrybutu wypisujemy liczbę różnych dostępnych wartości
i = 0
for col in data.T:
    print("Atrybut ", i + 1, " Liczba różnych wartości: ", len(np.unique(col)))
    i += 1


# e) dla każdego atrybutu wypisujemy listę wszystkich różnych dostępnych wartości
i = 0
for col in data.T:
    print("Atrybut ", i + 1, " Różne wartości: ", np.unique(col))
    i += 1

# f) odchylenie standardowe dla poszczególnych atrybutów w całym systemie i w klasach decyzyjnych
# (dotyczy atrybutów numerycznych)
i = 0
for col in data.T:
    print("Odchylenie standardowe dla atrybutu ", i + 1, " w całym systemie: ", np.std(col))
    i += 1
