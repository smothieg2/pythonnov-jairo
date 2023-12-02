valor = int(input())

billete100 = billete50 = billete20 = billete10 = billete5 = billete2 = billete1 = 0

billete100 = valor // 100
valor %= 100

billete50 = valor // 50
valor %= 50

billete20 = valor // 20
valor %= 20

billete10 = valor // 10
valor %= 10

billete5 = valor // 5
valor %= 5

billete2 = valor // 2
valor %= 2

billete1 = valor

print(valor)
print("{} nota(s) de R$ 100,00".format(billete100))
print("{} nota(s) de R$ 50,00".format(billete50))
print("{} nota(s) de R$ 20,00".format(billete20))
print("{} nota(s) de R$ 10,00".format(billete10))
print("{} nota(s) de R$ 5,00".format(billete5))
print("{} nota(s) de R$ 2,00".format(billete2))
print("{} nota(s) de R$ 1,00".format(billete1))