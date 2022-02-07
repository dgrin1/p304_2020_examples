import math as math

def sin(x):
	sum_old = 0.002
	sum_s = 0
	for n in range(51):
		if float(abs(sum_s - sum_old)) < 10e-15:
			break
		else:
			s = float((x**(2*n + 1))*(((-1)**n))/(math.factorial(2*n + 1)))
			sum_old = sum_s
			sum_s += s

	return sum_s

def cos(x):
	relation = sin(x+(2*math.pi))
	return relation

def tan(x):
	fraction = sin(x)/cos(x)
	return fraction

def cosecant(x):
	reciprocal_sine = 1/sin(x)
	return reciprocal_sine


def secant(x):
	reciprocal_cosine = 1/cos(x)
	return reciprocal_cosine


def cotangent(x):
	reciprocal_tangent = 1/tan(x)
	return reciprocal_tangent

print(sin(math.pi/4), cos(math.pi/4), tan(math.pi/4))

