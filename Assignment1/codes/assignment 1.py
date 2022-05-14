from numpy import *
import numpy as np

'''
we have to find matrix X
X=(B^(2))-(4B)
'''

B= matrix('1,1;8,3')
C= matrix('4,0;0,4')
p=np.dot(B,B)
r=np.dot(C,B)
X=p-r
print(X)

'''
we have to find matrix Y
(X)(Y)=(Z)
'''
X=p-r
Z= matrix('5;50')
c=np.linalg.inv(X)
Y=c*Z
print(Y)
#  [[5 0]
#X= [0 5]]
#  [[a]
#Y= [b]]
#a=1  b=10
