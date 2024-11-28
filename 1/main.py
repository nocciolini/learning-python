number = float(input("Digite o numero: "))
sqrt = float(number ** 0.5)

if sqrt.is_integer():
    print("É um quadrado perfeito:", number)
else:
    print("Não é um quadrado perfeito:", number)
