valor1 = 0
valor2 = 1
valor_informado = int(input('Digite o valor a verificar no Fibonacci: '))
pertence = 'Não Pertence'
while valor2 <= valor_informado :
    #verifiquei o valor 1 pois abrange caso a entrada seja 0.
    if(valor_informado == valor1 or valor_informado == valor2):
        pertence = 'Pertence'
    valor3 = valor1 + valor2
    valor1 = valor2
    valor2 = valor3

print(pertence)