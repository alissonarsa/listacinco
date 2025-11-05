import random
import string
import time

def quicksort(arr):
	if len(arr) <= 1:
		return arr[:]
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

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

def gerar_nomes(n=10000):
	nomes = []
	for i in range(n):
		tam = random.randint(5, 12)
		nome = ''.join(random.choices(string.ascii_lowercase, k=tam)).capitalize()
		nomes.append(nome)
	return nomes

def medir(func, dados):
	t0 = time.perf_counter()
	func(dados)
	t1 = time.perf_counter()
	return t1 - t0

if __name__ == '__main__':
	nomes = gerar_nomes(10000)
	# para garantir igualdade de entradas
	nomes_qs = list(nomes)
	nomes_ms = list(nomes)

	t_qs = medir(quicksort, nomes_qs)
	print(f'QuickSort (10.000 nomes): {t_qs:.4f} s')

	t_ms = medir(mergesort, nomes_ms)
	print(f'MergeSort (10.000 nomes): {t_ms:.4f} s')

	print('\nObservação: implementações recursivas podem variar em desempenho conforme a forma dos dados e limites de recursão.')
