#Conversor de Temperatura
temp = input("Converter em Celsius ou Fahrenheit (C/F)")
x = 0
if temp == 'C':
    c = int(input("Quantos graus em Fahrenheit?: "))
    calc = 1.8 * c + 32
    print(f"{c}  Celsius em Fahrenheit é: {calc}")
else:
    f = int(input("Quantos graus em Celsius?: "))
    calc = (f - 32) / 1.8
    print(f"{f} Fahrenheit em Celsius é {calc}")