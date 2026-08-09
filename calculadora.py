def soma (a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao (a, b):
    return a*b
def divisao (a, b):
    if b == 0:
       return "erro:divisao por zero"
    return a / b

    print ("===CALCULADORA===")
num1=float(input("digite o primeiro numero"))
num2=float (input("digite o segundo numero"))
print("1 soma")
print ("2 subtracao")
print ("3 multiplicacao")
print ("4 divisao")
opcao=input("escolha uma operacao:")
if opcao =="1":
    print("resultado:",soma(num1,num2))
elif opcao=="2":
     print("resultado:",subtracao(num1,num2))
elif opcao=="3":
    print("resultado:",multiplicacao(num1,num2))
elif opcao == "4":
     print("resultado:",divisao(num1,num2))
else:
    print("opcao invalida")
