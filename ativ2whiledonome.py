sexo: str
nome: str

nome=input("Digite um nome: ")
sexo=input("digite seu sexo: ")

while (sexo != "M") and (sexo != "m"):
      nome=input("digite seu nome: ")
      sexo=input("digite seu sexo: ")
      print("Seu sexo é: ",sexo)