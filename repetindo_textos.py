def repetir_texto(): #----> Função para repetir uma string
    texto = input("Digite uma string: "+ "\n") #----> Solicitação da entrada da string
    numero = int(input("Digite um número inteiro: ")) #----> Solicitação da entrada do número inteiro
    resultado = texto * numero #----> Multiplicação da string pelo número inteiro
    print(resultado) #----> Exibição do resultado

if __name__ == "__main__": #----> Condição para execução da função
    repetir_texto() #----> Chamada da função