num_1 = int(input("Digite o primeiro número: ")) #----> Receber o primeiro número
num_2 = int(input("Digite o segundo número: ")) #----> Receber o segundo número

operacao = input("Digite a operação desejada (+, -, *, /): ") #----> Receber a operação desejada

if operacao == '+':
    resultado = num_1 + num_2 #----> Soma dos números
elif operacao == '-':
    resultado = num_1 - num_2 #----> Subtração dos números
elif operacao == '*':
    resultado = num_1 * num_2 #----> Multiplicação dos números
elif operacao == '/':
    if num_2 != 0:
        resultado = num_1 / num_2 #----> Divisão dos números
    else:
        resultado = "Erro: Divisão por zero" #----> Tratamento de divisão por zero
else:
    resultado = "Operação inválida" #----> Operação inválida

print("O resultado é: ", resultado) #----> Exibição do resultado