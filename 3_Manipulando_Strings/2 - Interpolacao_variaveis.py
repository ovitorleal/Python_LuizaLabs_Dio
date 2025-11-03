# Em pyhton temos 3 formas de interpolar variaveis em strings:
#     1- Usando %; pouco usado apos python 3.0;
#     2- Usando o metodo .format();
#     3- Usando f-strings . o mais recomendado.

#Ex. Obsoleto (%):
nome = "Vitor"
idade = 35
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Tenho %d anos, trabalho como %s e uso a linguagem %s para desenvolver meus projetos." % (nome, idade, profissao, linguagem))


#Método .format():
print ("Olá, me chamo {}. Tenho {} anos, trabalho como {} e uso a linguagem {} para desenvolver meus projetos.".format(nome, idade, profissao, linguagem))

#outra opção (ainda .format()) -> Entre chaves temos que colocar o indice da variavel (lembrando que é ZERO based index)
print ("Olá, me chamo {3}. Tenho {2} anos, trabalho como {1} e uso a linguagem {0} para desenvolver meus projetos.".format(linguagem, profissao, idade, nome))

#ainda .format() -> Podemos nomear os parametros dentro das chaves
print ("Olá, me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e uso a linguagem {linguagem} para desenvolver meus projetos.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#outra opção é criar um dicionario e usar o ** para desempacotar os valores
pessoa = {
    "nome": "Vitor",
    "idade": 35,
    "profissao": "Programador",
    "linguagem": "Python"
}
print ("Olá, me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e uso a linguagem {linguagem} para desenvolver meus projetos.".format(**pessoa))

#f-strings (recomendado):
print (f"Olá, me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e uso a linguagem {linguagem} para desenvolver meus projetos.")

#usando f-strigs para formatar numeros

PI = 3.141592653589793
print(f"Valor de PI: {PI: .2f}")  # Limitando o numero de casas decimais para 2
print(f"Valor de PI: {PI: 10.2f}") #Colocando espaço antes do resultado
