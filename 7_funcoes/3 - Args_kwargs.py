'''
Podemos combinar parametros obrigatorios com *args e kwargs.
Quando esses sao definidos(**args e **kwargs), o metodo recebe os valores como tuple e dict respectivamente.
'''
#! Exemplo:

def exibir_poema(data_extenso, *args, **kwargs):
    texto= "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("Quarta, 12 de novembro de 2025", "Zen of Pyhton", "Beautiful is better than ugly.",
             "Beautiful is better than ugly.", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
