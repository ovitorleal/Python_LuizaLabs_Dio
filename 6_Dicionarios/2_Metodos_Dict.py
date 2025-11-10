# ! Metodo .clear()
#!Exemplo

contatos = {
    "vitor@gmail.com": {"nome": "Vitor", "telefone": "3333-2221"},
    "juliana@gmail.com": {"nome": "Juliana", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}
contatos.clear()
print(contatos)

# ! Metodo .copy()

contatos = {
    "vitor@gmail.com": {"nome": "Vitor", "telefone": "3333-2221"},
    "juliana@gmail.com": {"nome": "Juliana", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}

copia = contatos.copy()
copia ["vitor@gmail.com"] = {"nome":"Vitinho"}

print(contatos["vitor@gmail.com"])
print(copia["vitor@gmail.com"])

#! .fromkeys()

contatos.fromkeys(["nome","telefone"])
print(dict())
contatos.fromkeys(["nome","telefone"], "vazio")
print(dict())

#! .get()
contatos = {
"vitor@gmail.com": {"nome": "Vitor", "telefone": "3333-2221"}
}
resultado = contatos["chave"] #Key
print(resultado)
resultado = contatos.get("chave") #None
print(resultado)
resultado = contatos.get("chave", {}) #{}
print(resultado)
resultado = contatos.get("vitor@gmail.com", {}) #{"vitor@gmail.com": {"nome": "Vitor", "telefone": "3333-2221"}}
print(resultado)

#! .keys()
contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}
contatos.keys() # dict_keys(['guilherme@gmail.com'])

#! .pop()
contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}
contatos.pop("guilherme@gmail.com") # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme@gmail.com", {}) # {}

#! popitem()
contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}
contatos.popitem() # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})contatos.popitem() # KeyError

#! setdefault()
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}
contato.setdefault("nome", "Giovanna") # "Guilherme"contato # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contato.setdefault("idade", "28") # 28


#! .values()
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    }
contatos.values() 
''''dict_values([
    {'nome': 'Guilherme', 'telefone': '3333-2221'}, 
    {'nome': 'Giovanna', 'telefone': '3443-2121'}, 
    {'nome': 'Chappie', 'telefone': '3344-9871'}, 
    {'nome': 'Melaine', 'telefone': '3333-7766'}])'''
    
#! in
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},}

resultado = "guilherme@gmail.com" in contatos # True
print(resultado)
resultado = "megui@gmail.com"in contatos # False
print(resultado)
resultado = "idade"in contatos["guilherme@gmail.com"] # False
print(resultado)
resultado = "telefone"in contatos["giovanna@gmail.com"] # True
print(resultado)

#! del
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    }
del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]
print(contatos )
''' {'guilherme@gmail.com': {'nome': 'Guilherme'}, 
'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 
'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}'''