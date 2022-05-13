#Given four position vectors A,B,C and D with coordinates (4,5,1),(0,-1,-1),(3,9,4) and (-4,4,4) respectively.
#need to prove the above position vectors are coplanar.
#the above position vectors are coplanar if scalar triple product of vectors AB,AC and AD is zero
#vector AB=(B-A)=(0-4,-1-5,-1-1)=(-4,-6,-2)
#vector AC=(C-A)=(3-4,9-5,4-1)=(-1,4,3)
#vector AD=(D-A)=(-4-4,4-5,4-1)=(-8,-1,3)

#Scalar triple product of the vectors AB,AC,AD is determinant of the matrix 
#[[-4 -6 -2]
# [-1  4  3]
# [-8 -1  3]]
#now we need to show the determinant of the above matrix is 0
import numpy as np
#creating a 3*3 numpy matrix
n_array = np.array([[-4,-6,-2],[-1,4,3],[-8,-1,3]])
#calculating the determinant of the above matrix
det = np.linalg.det(n_array)
print(int(det))
#the determinant value is 0 and
#Hence as the condition for coplanar vectors is satisfied, the given four position vectors are coplanar
