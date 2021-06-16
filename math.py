#add
def add(x,y):
    return x+y
#sub
def subtract(x,y):
    return x-y  	#master
#mul
def multiply(x,y):
    return x*y		#bug456
#divide
def divide(x,y):
    if x<0:
	return NEGATIVE_PARAM_ERROR	#master
    if y==0:
	return DIVIDE_0_ERROR	#bug789
    else:
	return x/y

def square(x):
	pass