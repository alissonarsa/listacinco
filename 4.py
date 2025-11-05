import random
import time
import copy

def bubble_sort(lista, key=lambda x: x):
	n = len(lista)
	for i in range(n):
		trocou = False
		for j in range(0, n - 1 - i):
			if key(lista[j]) > key(lista[j + 1]):
				lista[j], lista[j + 1] = lista[j + 1], lista[j]
				trocou = True
		if not trocou:
			break

def insertion_sort(lista, key=lambda x: x):
	for i in range(1, len(lista)):
		atual = lista[i]
		j = i - 1
		while j >= 0 and key(lista[j]) > key(atual):
			lista[j + 1] = lista[j]
			j -= 1
		lista[j + 1] = atual

def gerar_produtos(n=1000):
	produtos = []
	for i in range(n):
		produtos.append({
			'nome': f'Produto {i+1}',
			'preco': random.uniform(1, 10000),
			'quantidade': random.randint(0, 100)
		})
	return produtos

def medir(func, dados, key=lambda x: x):
	copia = copy.deepcopy(dados)
	t0 = time.perf_counter()
	func(copia, key=key)
	t1 = time.perf_counter()
	return t1 - t0

if __name__ == '__main__':
	produtos = gerar_produtos(1000)

	t_bubble = medir(bubble_sort, produtos, key=lambda x: x['preco'])
	print(f'Bubble Sort (1000 produtos): {t_bubble:.4f} s')

	t_insertion = medir(insertion_sort, produtos, key=lambda x: x['preco'])
	print(f'Insertion Sort (1000 produtos): {t_insertion:.4f} s')

	print('\nObservação: tempos podem variar conforme máquina e carga do sistema.')