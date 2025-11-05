import random
import string
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

class Aluno:
	def __init__(self, nome, notas):
		self.nome = str(nome)
		self.notas = [float(n) for n in notas]

	@property
	def media(self):
		return sum(self.notas) / len(self.notas) if self.notas else 0.0

	def __repr__(self):
		return f"Aluno(nome='{self.nome}', media={self.media:.2f})"

def quicksort_alunos(alunos, reverse=False):
	if len(alunos) <= 1:
		return alunos[:]
	pivot = alunos[len(alunos) // 2].media
	left = [a for a in alunos if a.media < pivot]
	middle = [a for a in alunos if a.media == pivot]
	right = [a for a in alunos if a.media > pivot]
	if reverse:
		return quicksort_alunos(right, reverse=True) + middle + quicksort_alunos(left, reverse=True)
	else:
		return quicksort_alunos(left, reverse=False) + middle + quicksort_alunos(right, reverse=False)

def gerar_produtos(n):
	produtos = []
	for i in range(n):
		produtos.append({'nome': f'P{i+1}', 'preco': random.uniform(1, 10000), 'quantidade': random.randint(0, 100)})
	return produtos

def gerar_nomes(n):
	nomes = []
	for i in range(n):
		tam = random.randint(5, 12)
		nomes.append(''.join(random.choices(string.ascii_lowercase, k=tam)).capitalize())
	return nomes

def gerar_alunos(n):
	alunos = []
	for i in range(n):
		notas = [random.uniform(0, 10) for _ in range(4)]
		alunos.append(Aluno(f'Aluno {i+1}', notas))
	return alunos

def medir_tempo(func, *args, **kwargs):
	t0 = time.perf_counter()
	res = func(*args, **kwargs)
	t1 = time.perf_counter()
	return (t1 - t0), res

def gerar_relatorio(caminho='relatorio.txt'):
	rel = []

	# tamanhos escolhidos
	n_produtos = 1000
	n_nomes = 10000
	n_alunos = 2000

	produtos = gerar_produtos(n_produtos)
	nomes = gerar_nomes(n_nomes)
	alunos = gerar_alunos(n_alunos)

	# Bubble vs Insertion (produtos)
	t_bubble, _ = medir_tempo(lambda l: bubble_sort(l, key=lambda x: x['preco']), copy.deepcopy(produtos))
	t_insertion, _ = medir_tempo(lambda l: insertion_sort(l, key=lambda x: x['preco']), copy.deepcopy(produtos))
	rel.append(('Bubble Sort (produtos, n=%d)' % n_produtos, t_bubble))
	rel.append(('Insertion Sort (produtos, n=%d)' % n_produtos, t_insertion))

	# QuickSort vs MergeSort (nomes)
	t_qs, _ = medir_tempo(quicksort, list(nomes))
	t_ms, _ = medir_tempo(mergesort, list(nomes))
	rel.append(('QuickSort (nomes, n=%d)' % n_nomes, t_qs))
	rel.append(('MergeSort (nomes, n=%d)' % n_nomes, t_ms))

	# QuickSort para Aluno por média (decrescente)
	t_qs_alunos, _ = medir_tempo(lambda l: quicksort_alunos(l, reverse=True), list(alunos))
	rel.append(('QuickSort Alunos por media (n=%d)' % n_alunos, t_qs_alunos))

	# grava relatorio
	with open(caminho, 'w', encoding='utf-8') as f:
		f.write('Relatório de tempos de execução\n')
		f.write('================================\n')
		for nome, t in rel:
			f.write(f"{nome}: {t:.6f} s\n")

	return rel

if __name__ == '__main__':
	print('Gerando relatório (pode demorar alguns segundos/minutos dependendo do tamanho)...')
	rel = gerar_relatorio()
	for nome, t in rel:
		print(f'{nome}: {t:.6f} s')
	print("\nRelatório salvo em 'relatorio.txt'")
