class Produto:
	def __init__(self, nome: str, preco: float, quantidade: int = 0):
		self.nome = str(nome)
		self.preco = float(preco)
		self.quantidade = int(quantidade)

	def atualizar_preco(self, novo_preco: float):
		self.preco = float(novo_preco)

	def aplicar_desconto(self, percentual: float):
		fator = 1 - (float(percentual) / 100.0)
		self.preco *= fator

	def aumentar_quantidade(self, delta: int):
		self.quantidade += int(delta)

	@property
	def valor_estoque(self) -> float:
		return self.preco * self.quantidade

	def __repr__(self):
		return f"Produto(nome='{self.nome}', preco={self.preco:.2f}, quantidade={self.quantidade})"

if __name__ == '__main__':
	# Exemplo de uso
	p = Produto('Caneta', 2.5, 100)
	print('Inicial:', p)
	p.aplicar_desconto(10)
	print('Após 10% de desconto:', p)
	p.atualizar_preco(3.0)
	p.aumentar_quantidade(50)
	print('Atualizado:', p)
	print(f'Valor do estoque: R$ {p.valor_estoque:.2f}')
