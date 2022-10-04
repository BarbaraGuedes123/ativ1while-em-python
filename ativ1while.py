soma=int
x=int

x=int(input("Digite um número(0-SAIR): "))
soma=0

while x != 0:
     soma= soma + x
     x= int(input("Digite um número(0-SAiR): "))
     print("A soma vale: ", soma)
