a=float(input())  
c=input()

c=c.lower()

if c=="ao quadrado":
    print(a**2)
    quit()
                            #int() para o computador entender que é um número
b=float(input())


if c=="*":
    print(a*b)

elif c=="/":                         #else:"caso não seja asterisco, faça outra coisa"
    print(a/b)   

elif c=="+":  
    print(a+b)
                                     
elif c=="-":
    print(a-b)

elif c=="elevado":
    print(a**b)
