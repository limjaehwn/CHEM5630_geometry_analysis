#!/usr/bin/env python
# coding: utf-8

# In[36]:


# This is the geometry analysis project.
#Wwe are going to determine theis distance between bonded atoms for Angstrom
# Input: water.xyz file
import numpy
import os

path = 'water.xyz'

file_location = os.path.abspath(path)

#print(file_location)

xyz_file = numpy.genfromtxt(fname = file_location, skip_header = 2, dtype = 'unicode')

symbols = xyz_file[:,0]

print(symbols)

coordinates_string = xyz_file[:,1:]

coordinates = coordinates_string.astype(numpy.float)

#print(coordinates_string)

#print(coordinates_float)

num_atoms = len(symbols)

#print(num_atoms)

for num1 in range (0,num_atoms):
    for num2 in range(0,num_atoms):
        #print(num1, num2)
        x_distance = coordinates[num1,0] - coordinates[num2,0]
        y_distance = coordinates[num1,1] - coordinates[num2,1]
        z_distance = coordinates[num1,2] - coordinates[num2,2]
        bond_length_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
        print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')
