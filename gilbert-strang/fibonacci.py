import time

def fast_fibonacci(n):
    """Application of eigenvalues and eigenvectors for fast fibonacci algorithm.
    It's much slower than cached recursive algorithm and more importantly the 
    result is not accurate.

    Args:
        n (int): The nth fibonacci number to be calculated

    Returns:
        int: The nth fibonacci number
    """
    lambda1 = (1 + 5**.5)/2
    # lambda1 = 1.618033988749895 
    # lambda1 = 1.618034
    print(f'lambda1 = {lambda1}')
    lambda2 = (1-5**.5)/2
    # lambda2 = -0.6180339887498949
    # lambda2 = -0.618034
    print(f'lambda2 = {lambda2}')
    c1 = lambda1 ** n
    # print(f'c1 = {c1}')
    c2 = lambda2 ** n
    # print(f'c2 = {c2}')

    return round((c1 -c2) /(lambda1 - lambda2))

start_time = time.time()
print(fast_fibonacci(800))
end_time = time.time()
print(f'Time elapsed: {end_time - start_time} seconds')