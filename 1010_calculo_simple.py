cod1,cant1,pre1 = map(float, input().split())
cod2,cant2,pre2 = map(float, input().split())

vat= (cant1*pre1)+(cant2*pre2)

print(f"VALOR A PAGAR: R$ {vat:.2f}")