print('--------------------------------')
#Pedimos ao usuário um valor em temperatura para colocarmos no armazenamento
Fahreinheit = int(input("Digite uma temperatura em Fahreinheit: "))
# Para converter esse número que o usuário colocou em Fahreinheit para Celsius,
# precisamos fazer um cálculo que converta Fahreinheit para Celsius
Celsius = (Fahreinheit - 32) * 5/9
# Para finalizar o código, teremos que atribuir os valores e colocar o resultado
print(f"O resultado final em Fahreinheit que é {Fahreinheit}° para Celsius é: {Celsius:.4}")
print('--------------------------------')