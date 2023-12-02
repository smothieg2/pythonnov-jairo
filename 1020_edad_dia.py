edad_en_dias = int(input())

anios = edad_en_dias // 365
meses = (edad_en_dias % 365) // 30
dias = (edad_en_dias % 365) % 30

print("{} ano(s)".format(anios))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))