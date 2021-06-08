# a = "J'ai une classe de " + 30 + " élèves"
# J'ai une classe de 30 élèves
a = "J'ai une classe de " + str(30) + " élèves"

# b = 10 + " + " + int("5") + " est égal à " + 15
# 10 + 5 est égal à 15
b = str(10) + " + " + "5" + " est égal à " + str(15)

# c = 10 + "5"
# 15
c = 10 + int("5")

# d = "L'addition de 10 + 5 est égal à " + 10 + 5
# l'addition de 10 + 5 est égal à 15
d = "L'addition de 10 + 5 est égal à " + str(10 + 5)

print(a)
print(b)
print(c)
print(d)