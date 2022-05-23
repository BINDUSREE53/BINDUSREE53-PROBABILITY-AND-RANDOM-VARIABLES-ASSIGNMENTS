import math

m= 0.02
x=0.028
y=0.97

only_twice=math.comb(50,2)*pow(m,2)*pow(x,2)*pow(y,48)
only_once=math.comb(50,1)*pow(m,1)*pow(x,1)*pow(y,49)
zero=math.comb(50,0)*pow(m,0)*pow(x,0)*pow(y,50)
required_probability=1-only_twice-only_once-zero
print(required_probability)
