import random

def insertion_sort(lista, key=lambda x: x):
	# ordena in-place
	for i in range(1, len(lista)):
		atual = lista[i]
		j = i - 1
		while j >= 0 and key(lista[j]) > key(atual):
			lista[j + 1] = lista[j]
			j -= 1
		lista[j + 1] = atual

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

	insertion_sort(produtos, key=lambda x: x['preco'])

	print('\nDepois (ordenado por preco ascendente):')
	for p in produtos[:10]:
		print(p)
