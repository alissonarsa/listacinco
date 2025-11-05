import random

def bubble_sort(lista, key=lambda x: x):
	n = len(lista)
	# ordena in-place
	for i in range(n):
		trocou = False
		for j in range(0, n - 1 - i):
			if key(lista[j]) > key(lista[j + 1]):
				lista[j], lista[j + 1] = lista[j + 1], lista[j]
				trocou = True
		if not trocou:
			break

def gerar_produtos(n=20):
	produtos = []
	for i in range(n):
		produtos.append({
			'nome': f'Produto {i+1}',
			'preco': round(random.uniform(1, 1000), 2),
			'quantidade': random.randint(0, 100)
		})
	return produtos

if __name__ == '__main__':
	produtos = gerar_produtos(20)
	print('Antes:')
	for p in produtos[:10]:
		print(p)

	bubble_sort(produtos, key=lambda x: x['preco'])

	print('\nDepois (ordenado por preco ascendente):')
	for p in produtos[:10]:
		print(p)