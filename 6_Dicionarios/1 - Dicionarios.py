'''
Um dicionario é um conjunto não-ordenado de pares CHAVE:VALOR.
Chaves sao unica em um dada instacia do dicionário. Dicionarios sao delimitados por chaves{};
Contem um lista de pares (chave:valor) separada por virgulas
'''
#! Exemplos:

pessoa = {"nome": "Vitor", "idade":35}

pessoa = dict(nome="Vitor", idade=28)

pessoa["telefone"] = "981006080"

print(pessoa)

# * Acessando os dados:

dados = {"nome": "Vitor", "idade":35, "telefone":"981006080"}

dados ["nome"]
print(dados["nome"])
dados ["idade"]
print(dados["idade"])
dados["telefone"]
print(dados["telefone"])

dados["nome"] = "Maria"
print(dados["nome"])
dados["idade"] = 18
print(dados["idade"])
dados["telefone"] = 999999999
print(dados["telefone"])

print(dados) #{'nome': 'Maria', 'idade': 18, 'telefone': 999999999} #! mudou os dados

# * Dicionarios aninhados
'''Dicionarios pode armazenar qualquer tipo de objeto Python como valor,
desde que a chave para esse valor seja um objeto imutavel (string e numeros)
'''

contatos = {
    "vitor@gmail.com": {"nome": "Vitor", "telefone": "3333-2221"},
    "juliana@gmail.com": {"nome": "Juliana", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}

print(contatos["juliana@gmail.com"]["telefone"])

#Pode iterar um dict

for chave in contatos:
    print(chave, contatos[chave])
    
for chave, valor in contatos.items(): #.items() retorna uma lista de tuplas
    print(chave,valor)
