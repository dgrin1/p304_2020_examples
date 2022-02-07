#syntax function defintion
def fac(n):
#going to start at some initial value and keep multiplying by bigger number

	i=1
	val=i
# go up to some highest value of i which is n
#stopping criterion
	while i<=n:
#at each value multiply by one higher number
		val*=i
#increment the counter
		i+=1
	return val
