#A estrutura condicional permite que o desvio de fluxo de controle quando determinadas expressões logicas atendidas.

##IF -> para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar o if.
#O comando ira testar a expressão logica, e em caso de retorno verdadeiro as ações do bloco do if serão executadas.
#Exemplo:
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque...")
    
if saldo < saque:
    print ("Saldo insuficiente!")
    
    
##IF/ELSE -> para criar uma estrutura condicional composta por dois desvios, podemos utilizar o if/else.
#Como sabemos se a expressao logica testada no if for verdadeira, entao o bloco de código do if sera executado.
#Caso contrario o bloco de codigo do else sera executado.
#Exemplo:
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque...")
else:
    print ("Saldo insuficiente!")

#ELIF -> Em alguns cenarios queremos mais de 2 desvios, para isso utilizamos ELIF.
#O elif é composto por uma nova expressao logica, que sera testada e caso retorne verdadeiro, o bloco de codigo do elif sera executado.
#Nao existe numero maximo de elifs que podemos utilizar, Mas é bom evitar estruturas condicionais muito grandes pois aumentam a complexidade do codigo.
#Exemplo:
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato \n"))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))

elif opcao == 2:
    print("Exibindo extrato...")

else:
    SystemExit("Opção inválida!")
    

        
        
