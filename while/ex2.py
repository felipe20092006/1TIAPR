num = int(input("Digite um numero par: "))
while num % 2 != 0:
    print("Numero invalido!")
    num = int(input("Digite um numero par: "))
print(f"Obrigado! {num} é um numero par!")