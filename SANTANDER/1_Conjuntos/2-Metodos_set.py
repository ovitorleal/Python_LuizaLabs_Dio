# {}.union

conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_a.union(conjunto_b) #{1,2,3,4}

# {}.intersection

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.intersection(conjunto_b) #{2,3}

#{}.difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b) #{1}
conjunto_b.difference(conjunto_a) #{4}

#{}.symetric_difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) #{1,4}

#{}.issubset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b) #True 
conjunto_b.issubset(conjunto_a) #False

#{}.issuperset => contrario de issubset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b) #False
conjunto_b.issubset(conjunto_a) #True 

#{}.isdisjoint => não há intersection

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) #True
conjunto_a.issubset(conjunto_c) #False

#{}.add

sorteio = {1,23}

sorteio.add(25) #{1,23,25}
sorteio.add(42) #{1,23,25,42}
sorteio.add(25) #{1,23,25,42} => só adiciona o que nao existe, por isso nao entreou outro 25


#{}.discard

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros) #{1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros.discard(1)
numeros.discard(45)
print(numeros) #{2,3,2,4,5,5,6,7,8,9,0}


#{}.pop

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros) #{1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros.pop() #0
numeros.pop() #1
print(numeros) #{2,3,2,4,5,5,6,7,8,9,0}



#{}.remove

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros) #{1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros.remove(0) #0
print(numeros) #{1,2,3,2,4,5,5,6,7,8,9}