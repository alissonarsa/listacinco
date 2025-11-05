import random
import string

def mergesort(arr):
	if len(arr) <= 1:
		return arr[:]
	mid = len(arr) // 2
	left = mergesort(arr[:mid])
	right = mergesort(arr[mid:])
	return _merge(left, right)

def _merge(a, b):
	i = j = 0
	out = []
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			out.append(a[i])
			i += 1
		else:
			out.append(b[j])
			j += 1
	out.extend(a[i:])
	out.extend(b[j:])
	return out

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

	ordenados = mergesort(nomes)
	print('\nDepois (ordem alfabética por MergeSort):')
	print(ordenados)