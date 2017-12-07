import numpy as np
import random

class Fictitious(object):
	
	def __init__(self, matrix, belief):
		self.m = matrix.astype(float)
		self.b = belief.astype(float)
		self.s = 0

	def get_score(self):
		return self.s

	def get_belief(self):
		return self.b

	def get_normalized_belief(self):
		return self.b/np.sum(self.b)

	def update(self, e_a, e_b):
		self.b[e_b] += 1
		self.s += self.m[e_a,e_b]
		return

	def calc_exp_util(self, e):
		return np.sum(self.m[e,:]*(self.b/np.sum(self.b)))

	def get_strategy(self):
		max_exp = -999999999
		best_s = -1
		for s in xrange(len(self.m[:,0])):
			exp_util = self.calc_exp_util(s)
			if exp_util > max_exp:
				max_exp = exp_util
				best_s = s

		return best_s

	def get_random_strategy(self):
		return random.randint(0,len(self.m[:,0])-1)

	def get_bad_friend_strategy(self, player):
		min_exp = 999999999
		best_s = -1
		for s in xrange(len(self.m[:,0])):
			min_op = np.sum(player.m[:,s]*(self.b/np.sum(self.b)))
			if min_op < min_exp:
				min_exp = min_op
				best_s = s
		return best_s

	def get_good_friend_strategy(self, player):
		max_exp = -999999999
		best_s = -1
		for s in xrange(len(self.m[:,0])):
			max_op = np.sum(player.m[:,s]*(self.b/np.sum(self.b)))
			if max_op > max_exp:
				max_exp = max_op
				best_s = s
		return best_s