# -*- coding: utf-8 -*-

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


def Plot(data, file_name):
	color = ['blue', 'darkorange']
	print len(data)
	print len(data[0,:])
	x = np.linspace(1, len(data)+1)
	for j in range(len(data[0,:])):
		fig = plt.plot(data[:,j], label="Jogador"+str(j+1), color=color[j], lw=2.0)

	plt.title('Shapley')
	plt.xlabel(u'Número de interações')
	plt.ylabel(u'Crença do jogador escolher A')

	leg = plt.legend(loc='best', ncol=1)
	leg.get_frame().set_alpha(0.5)

	plt.savefig("figures/"+str(file_name)+".png",bbox_inches='tight',dpi=1000)	
	plt.show()


def Plot2(data, file_name):
	color = ['darkviolet', 'blue', 'red', 'darkorange', 'forestgreen']
	print len(data)
	print len(data[:,0])
	x = np.linspace(1, len(data[0])+1)
	for i in range(len(data)):
		fig = plt.plot(data[i,:], label=u"Crença "+str(10**i), color=color[i], lw=2.0)

	plt.title('Dilema dos prisioneiros')
	plt.xlabel(u'Número de interações')
	plt.ylabel(u'Crença do jogador escolher A')

	leg = plt.legend(loc='best', ncol=1)
	leg.get_frame().set_alpha(0.5)

	plt.savefig("figures/"+str(file_name)+"3.png",bbox_inches='tight',dpi=1000)	
	plt.show()


def main2():
	file_name = "games/prisioner"
	matrix_a, matrix_b = ReadData(file_name, " ")

	n_iter = 10000

	matrix = []
	for p in range(5):
		belief_a = np.array([10**p,0])
		belief_b = np.array([10**p,0])

		player_a = fic.Fictitious(matrix_a, belief_a)
		player_b = fic.Fictitious(matrix_b, belief_b)

		data = []
		for i in xrange(n_iter):
			a_s = player_a.get_strategy()
			b_s = player_b.get_strategy()
			player_a.update(a_s, b_s)
			player_b.update(b_s, a_s)
			data.append(player_a.get_normalized_belief()[0])

		matrix.append(data)

	Plot2(np.array(matrix), file_name)


def main():
	file_name = "games/shapley"
	matrix_a, matrix_b = ReadData(file_name, " ")

	n_iter = 10000

	belief_a = np.array([1,0,0])
	belief_b = np.array([1,0,0])

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

	Plot(np.array(data), file_name)

if __name__ == "__main__":
	main()
