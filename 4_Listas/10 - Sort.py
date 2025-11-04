# ordena a lista

linguagens = ["python", "js", "c", "java","csharp" ]

linguagens.sort() #=> ordena alfabeticamente

linguagens.sort(reverse=True) # => ordem de tras pra frente alfabeticamente falando

linguagens.sort(key=lambda x: len(x)) #=> por tamanho crescente da palavra

linguagens.sort(key=lambda x: len(x), reverse=True) #=> por tamanho decrescente da palavra

