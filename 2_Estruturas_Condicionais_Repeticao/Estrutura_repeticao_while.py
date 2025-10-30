#O while é usado para repetir um bloco de codigo varias vezes. Faz sentido usar while quando sabemos o numero exato de vezes que nosso bloco 
#de codigo deve ser executado
#Exemplo de while:
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair\n:"))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por usar nosso sistema bancario!")