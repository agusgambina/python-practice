import numpy as np

def create_array_of_10_zeros():
  return np.zeros(10)

def create_an_array_of_10_ones():
  return np.ones(10)

def create_an_array_of_10_fives():
  return np.ones(10) * 5

def create_an_array_of_the_integers_from_10_to_50():
  return np.arange(10, 51)

def create_an_array_of_all_the_even_integers_from_10_to_50():
  return np.arange(10, 51, 2)

def create_a_3x3_matrix_with_values_ranging_from_0_to_8():
  return np.arange(9).reshape(3,3)

def create_a_3x3_identity_matrix():
  return np.eye(3)

def generate_a_random_number_between_0_and_1():
  return np.random.rand(1)


def generate_an_array_of_25_random_numbers_sampled_from_a_standard_normal_distribution():
  return np.random.normal(25)

def create_the_following_matrix():
  return np.linspace(0.01, 1, 100).reshape(10, 10)
  # return np.arange(1, 101).reshape(10, 10)/100
  

def create_an_array_of_20_linearly_spaced_points_between_0_and_1():
  return np.linspace(0, 1, 20)

def replicate_1(matrix):
  return matrix[2:, 1:]

def replicate_2(matrix):
  return matrix[3,4]

def replicate_3(matrix):
  return matrix[:3,1:2]

def replicate_4(matrix):
  return matrix[4]

def replicate_5(matrix):
  return matrix[3:]

def mat_sum(matrix):
  return np.sum(matrix)

def mat_deviation(matrix):
  return np.std(matrix)

def sum_of_all_columns(matrix):
  return matrix.sum(axis=0)