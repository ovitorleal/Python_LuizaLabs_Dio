#IF ANINHADO -> Pode criar estruturas condicionais aninhadas, basta adicionar estruturas if/elif/else dentro do bloco de codigo de estruturas if/elif/else.
#Exemplo:
conta_normal = True
conta_universitaria = False
saldo = 2000.0
saque = 1500
cheque_especial = 450

if conta_normal:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente para saque!")
        
elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para saque!")
        
else:
    print("Tipo de conta inválida!")
    
    
##IF TERNARIO -> Permite escrever uma condição em uma unica linha. Ele é composto por tres partes: retorno caso a expressao seja verdadeira, a segunda parte
#é a expressao logica e a terceira parte é o retorno caso a expressao nao seja atendida.
#Exemplo:
status = "Sucesso" if saldo>= saque else "Falha"
print (f"{status} ao realizar o saque!")
