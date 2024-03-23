def seq_fibonacci(n):
    fibonacci = [0, 1]
    while fibonacci[-1] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def verifica_numero_fibonacci(numero):
    fibonacci = seq_fibonacci(numero)
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero_informado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
print(verifica_numero_fibonacci(numero_informado))

def inverte_string(string):
    tamanho = len(string)
    string_invertida = ""
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

entrada = input("Digite uma string para inverter: ")
print("String original:", entrada)
print("String invertida:", inverte_string(entrada))