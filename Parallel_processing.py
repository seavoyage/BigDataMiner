#Simple Parallel Processing

from IPython.parallel import Client
rc = Client()
v = rc.load_balanced_view()

@v.parallel(block=True)
def f(x): return 2*x

result = f.map(range(10))
print("Using a parallel function: ", result)

               
# $ ipcluster start -n 4
