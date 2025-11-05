import random

def gerar_produtos(n=50):
	produtos = []
	for i in range(n):
		produtos.append({
			'nome': f'Produto {i+1}',
			'preco': round(random.uniform(1, 10000), 2),
			'quantidade': random.randint(0, 200)
		})
	return produtos

def ranking_mais_caros(produtos, top_n=10):
	# usa sort estável do Python para eficiência
	ordenados = sorted(produtos, key=lambda x: x['preco'], reverse=True)
	return ordenados[:top_n]

if __name__ == '__main__':
	produtos = gerar_produtos(50)
	top = ranking_mais_caros(produtos, top_n=10)
	print('Top 10 produtos mais caros:')
	for i, p in enumerate(top, 1):
		print(f"{i:2d}. {p['nome']:12} - R$ {p['preco']:9.2f} (qtd: {p['quantidade']})")
