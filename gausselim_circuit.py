from numpy import array,empty,copy,dot,linalg

A = array([[ 0,  0, 9 ],
           [6,0,0],
           [ 1,1,  -1 ]], float)
v = array([ -12, 6, 0 ],float)
N = len(v)
B=copy(A)
u=copy(v)

#A = array([[ 6,  0,  0 ],
#            [ 0,  0, 9 ],
#            [ 1, 1,  -1 ]], float)
#v = array([ -6, 12, 0 ],float)
#N = len(v)

# Gaussian elimination
for m in range(N):
	largest=A[m,m]
	for i in range (m+1,N):
		if abs(A[i,m]) > largest:
			largest=abs(A[i,m])
			pivot=i
	for i in range(0,N):
		A[m,i],A[pivot,i]=A[pivot,i],A[m,i]
	v[m],v[pivot]=v[pivot],v[m]
	print(pivot)
for m in range(N):
 	div = A[m,m]
 	A[m,:] /= div
 	v[m] /= div
 	for i in range(m+1,N):
  		mult = A[i,m]
		v[i] -= mult*v[m]
		A[i,:] -= mult*A[m,:]
  		
  		
x = empty(N,float)
for m in range(N-1,-1,-1):
   x[m] = v[m]
   for i in range(m+1,N):
   	x[m] -= A[m,i]*x[i]
 
print(x)
print(linalg.solve(B,u))
#dg swaps before invert
#copy