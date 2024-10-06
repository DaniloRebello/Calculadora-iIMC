print ("Seja bem vindo!")
print()
print("Vamos descobrir como anda seu estado Nutricional!")
nome =  input (" Qual o seu nome? ")
peso = float(input("Qual é o seu peso? "))
altura = float(input("E a sua Altura? "))
print()

imc = peso / (altura * altura)

print("olá ", nome, "!", "seu peso é de ", peso, "kg", " e a sua altura ", altura, "m")
print()
print (f"O seu resultado é de IMC: {imc:.2f}, kg/m.")
print()

if imc < 18.5:
    print("Seu IMC está abaixo do normal.")
elif 18.5 <= imc <= 24.9:
    print("Seu peso está normal. Parabéns!")
elif 25 <= imc <= 29.9:
    print("Você está com sobrepeso. Cuide mais da sua saúde!")
else:   
    print("Você está com obesidade. Procure ajuda profissional")
  


       