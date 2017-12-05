import numpy as np
import fictitious as fic
import matplotlib.pyplot as plt
import csv


def ReadData (dataset, char_del):
	matrix = []
	with open(dataset, "r") as f:
		file = csv.reader(f, delimiter=char_del)
		for row in file:
			matrix.append(row)
	f.close()
	n_row = len(matrix)/2
	return np.array(matrix[0:n_row], dtype=int), np.array(matrix[n_row:], dtype=int)


def Plot(data):
	print len(data)
	print len(data[0,:])
	x = np.linspace(1, len(data)+1)
	for j in range(len(data[0,:])):
		fig = plt.plot(data[:,j], label="Jogador"+str(j+1))

	plt.title('Jogo potencial')
	plt.xlabel('Numero de interacoes')
	plt.ylabel('Crenca do jogador escolher A')

	leg = plt.legend(loc='best', ncol=1)
	leg.get_frame().set_alpha(0.5)

	plt.savefig("image.png",bbox_inches='tight',dpi=1000)	
	plt.show()


def main():
	
	file_name = "potential"
	matrix_a, matrix_b = ReadData(file_name, " ")
	print matrix_a
	print matrix_b

	#matrix_a = np.array([[5,4],[3,6]])
	#matrix_b = np.array([[0,-2],[1,2]])
	n_iter = 100

	belief_a = np.array([3,8])
	belief_b = np.array([1,10])

	player_a = fic.Fictitious(matrix_a, belief_a)
	player_b = fic.Fictitious(matrix_b, belief_b)

	data = []
	for i in xrange(n_iter):
		a_s = player_a.get_strategy()
		b_s = player_b.get_strategy()
		player_a.update(a_s, b_s)
		player_b.update(b_s, a_s)
		data.append([player_a.get_normalized_belief()[0], player_b.get_normalized_belief()[0]])

	print player_a.get_score()
	print player_b.get_score()

	print player_a.get_normalized_belief()
	print player_b.get_normalized_belief()

	Plot(np.array(data))

if __name__ == "__main__":
	main()
