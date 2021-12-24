ida = input('Digite a string: ')
volta = ''
contador = len(ida)-1
while contador >= 0:
    volta += ida[contador]
    contador -= 1
print(volta)

