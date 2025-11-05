import random
import string

def quicksort(arr):
	if len(arr) <= 1:
		return arr[:]
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

def gerar_nomes(n=20):
	nomes = []
	for i in range(n):
		tam = random.randint(4, 10)
		nome = ''.join(random.choices(string.ascii_lowercase, k=tam)).capitalize()
		nomes.append(nome)
	return nomes

if __name__ == '__main__':
	nomes = gerar_nomes(20)
	print('Antes:')
	print(nomes)

	ordenados = quicksort(nomes)
	print('\nDepois (ordem alfabética):')
	print(ordenados)