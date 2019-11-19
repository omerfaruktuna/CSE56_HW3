import pandas as pd
import numpy as np
print('Libraries installed')

input_data = pd.read_csv("blender-efficiency.csv") 
#input_data = pd.read_csv("blender-efficiency.csv",header=None) 

#print(input_data.head())

a = input_data.values.tolist()
#print(a)
a_np = np.array(a)
#print(a_np)

# A_NEW = A[start_index_row : stop_index_row, start_index_columnn : stop_index_column)]

#x_np = a_np[:,:4]
#y_np = a_np[:,4:5]

x_np = a_np[:,:-1]
y_np = a_np[:,-1]


#print(x_np)
#print(y_np)

#print(x_np.shape)
#print(y_np.shape)


part1 = np.linalg.inv(x_np.transpose().dot(x_np))
part2 = part1.dot(x_np.transpose())
w = part2.dot(y_np)

print('W is :')
print(w)

tmp_list=[]

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

print('Estimated Blending efficiency is: ')
print(w.transpose().dot(z))

#w = (X T X) −1 X T r
