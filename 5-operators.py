num1 = int(input("Digite o primeiro número\n"))
num2 = int(input("Digite o segundo número\n"))

# Aritmeticos  (3 % 2 = 1 | 4 ao quadrado = 4 * 4)
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Resto da divisão de {num1} por {num2} é {mod}")
print(f"Potência do número {num1} por {num2} é {exp}")
print(f"A soma de {num1} por {num2} é {sum}")
print(f"A subtração de {num1} por {num2} é {sub}")
print(f"A divisão de {num1} por {num2} é {div}")
print(f"A multiplicação de {num1} por {num2} é {mult}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 = num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"O números {num1} e {num2} são iguais? {equal}")
print(f"O números {num1} e {num2} são maiores ou iguais? {bigger_equal}")   

# Atribuíção    
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1