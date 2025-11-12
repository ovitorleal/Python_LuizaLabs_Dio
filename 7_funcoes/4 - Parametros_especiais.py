'''
Por padrao, argumentos podem ser passados para uma função Python
tanto por posição quanto explicitamente pelo nome.
Para uma melhor legibilidade e desempenho, faz sentido
restringir a maneira pelo qual argumentos possam ser passados,
assim um desenvolvedor precisa apenas olhar para a definição da funçao para determinar se os itens sao passados 
POR POSIÇÃO, POR POSIÇÃO E NOME, OU POR NOME.
'''

#! Exemplo Position only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
    
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #* VALIDO

criar_carro(modelo="Palio", ano=1999, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina") #*INVALIDO
    


#! Exemplo Keyword only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
    
criar_carro(modelo="Palio", ano=1999, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina") #*VALIDO

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #* INVALIDO


#! Exemplo Keyword and Positional

def criar_carro(*, modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
    


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #* VALIDO

criar_carro(modelo="Palio", ano=1999, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina") #*INVALIDO