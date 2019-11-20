import pandas as pd
import numpy as np

input_data = pd.read_csv("blender-efficiency.csv") 
#input_data = pd.read_csv("blender-efficiency.csv",header=None) 

#print(input_data.head())

a = input_data.values.tolist()
#print(a)
aa_np = np.array(a)

length = aa_np.shape[0]
#print(length)

zz = np.ones((length,1))

a_np = np.append(zz, aa_np, axis=1)
#print(a_np)

# A_NEW = A[start_index_row : stop_index_row, start_index_columnn : stop_index_column)]

#x_np = a_np[:,:4]
#y_np = a_np[:,4:5]

x_np = a_np[:,:-1]
y_np = a_np[:,-1]

#y_np = yy_np.transpose()
#print(yy_np.shape)
print("X is :\n")
print(x_np)
print("\n")
print("R is :\n")
print(y_np)
print("\n")

"""
print(x_np.shape)
print("\n")
print(y_np.shape)
print("\n")
"""

part1 = np.linalg.inv(x_np.transpose().dot(x_np))
part2 = part1.dot(x_np.transpose())
w = part2.dot(y_np)

print('W is calculated as\n:')
print(w)

print('\nLearning Completed...')

tmp_list=[]

tmp_list.append(1.0)

input_number    = float(input("\nEnter Particle Size: "))

tmp_list.append(input_number)

input_number    = float(input("\nEnter Mixer Diameter: "))

tmp_list.append(input_number)

input_number    = float(input("\nEnter Mixer Rotation: "))

tmp_list.append(input_number)

input_number    = float(input("\nEnter Blending Time: "))

tmp_list.append(input_number)

z = np.array(tmp_list)

#z = np.array([2 ,4, 200, 60])

print('\nEstimated Blending efficiency is: ')
#print(w.transpose().dot(z))
#print("\n")
print(z.dot(w))

#w = (X T X) −1 X T r
