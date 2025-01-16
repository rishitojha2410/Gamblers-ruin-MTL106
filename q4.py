import numpy as np #type:ignore
def stationary_distribution(p, q, r, N):
    """
    Return a list of size N+1 containing the stationary distribution of the Markov chain.
    
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    
    """
    pi = [0]*(N+1)
    pi[0] = 1 #assign a random value
    pi[1] = (1-r[0])*pi[0]/q[1]
    for i in range(2,N+1):
        if q[i]!=0:
            pi[i] = (pi[i-1]*(1-r[i-1]) - pi[i-2]*p[i-2])/q[i]
    l = sum(pi)
    pi_normalised = [float(i/l) for i in pi]
    return pi_normalised

def expected_wealth(p, q, r, N):
    """
    Return the expected wealth of the gambler in the long run.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    """
    l = stationary_distribution(p,q,r,N)
    e_w = 0
    for i in range(len(l)):
        e_w += i*l[i]
    return e_w
    
def expected_time(p, q, r, N, a, b):
    """
    Return the expected time for the price to reach b starting from a.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    a : int, the starting price
    b : int, the target price
    """
    one_matrix = [[1]]*(N+1)
    pi = [stationary_distribution(p,q,r,N)]
    pi_one = np.dot(one_matrix,pi)
    P_matrix = np.zeros((N+1,N+1))
    
    P_matrix[0][0] = r[0]
    P_matrix[0][1] = p[0]
    
    
    I_array = np.eye(N+1)
    for i in range(1,N):
        P_matrix[i][i] = r[i]
        P_matrix[i][i-1] = q[i]
        P_matrix[i][i+1] = p[i]
    P_matrix[N][N] = r[N]
    P_matrix[N][N-1] = q[N]
    Z_inv = I_array - P_matrix + pi_one
    Z_matrix = np.linalg.inv(Z_inv)
    pi_b = pi[0][b]
    Z_bb = Z_matrix[b,b]
    Z_ab = Z_matrix[a,b]
    return float((Z_bb-Z_ab)/pi_b)

  
