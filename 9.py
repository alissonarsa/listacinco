import random

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
	# ordena por média; reverse=True para decrescente
	if len(alunos) <= 1:
		return alunos[:]
	pivot = alunos[len(alunos) // 2].media
	left = [a for a in alunos if a.media < pivot]
	middle = [a for a in alunos if a.media == pivot]
	right = [a for a in alunos if a.media > pivot]
	if reverse:
		# decrescente: right, middle, left
		return quicksort_alunos(right, reverse=True) + middle + quicksort_alunos(left, reverse=True)
	else:
		return quicksort_alunos(left, reverse=False) + middle + quicksort_alunos(right, reverse=False)

def gerar_alunos(n=20):
	nomes = [f'Aluno {i+1}' for i in range(n)]
	alunos = []
	for nome in nomes:
		notas = [random.uniform(0, 10) for _ in range(4)]
		alunos.append(Aluno(nome, notas))
	return alunos

if __name__ == '__main__':
	alunos = gerar_alunos(20)
	print('Antes:')
	print(alunos)

	ordenados = quicksort_alunos(alunos, reverse=True)
	print('\nDepois (ordenado por média decrescente):')
	print(ordenados)
