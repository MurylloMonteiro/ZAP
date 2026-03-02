def soma(numer1, numer2):
    return numer1 + numer2

def sub(numer1, numer2):
    return numer1 - numer2

def mult(numer1, numer2):
    return numer1 * numer2

def div(numer1, numer2):
    return numer1 / numer2

while True:
    num1 = int(input("Digite o primeiro numero : "))
    num2 = int(input("Digite o segundo  numero : "))
    
    esc = int(input("""
    Escolha : 
        Soma 1
        Sub  2
        mult 3
        div  4          
    :"""))

    if esc == 1: 
        print(soma(num1, num2))
    elif esc == 2:
        print(sub(num1, num2))
    elif esc == 3:
        print(mult(num1, num2))
    elif esc == 4: 
        print(div(num1, num2))





    

