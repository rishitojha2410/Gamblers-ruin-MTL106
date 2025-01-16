import numpy as np #type: ignore
"""
Use the following function to convert the decimal fraction of k/N into it's binary representation
using k_prec number of bits after the decimal point. You may assume that the expansion of 
k/N terminates before k_prec bits after the decimal point.
"""
def decimalToBinary(num, k_prec) : 
  
    binary = ""  
    Integral = int(num)    
    fractional = num - Integral 
   
    while (Integral) :       
        rem = Integral % 2
        binary += str(rem);  
        Integral //= 2

    binary = binary[ : : -1]  
    binary += '.'

    while (k_prec) : 
        fractional *= 2
        fract_bit = int(fractional)  
  
        if (fract_bit == 1) :  
            fractional -= fract_bit  
            binary += '1'       
        else : 
            binary += '0'
        k_prec -= 1
        
    return binary 

def win_probability(p, q, k, N):
    """
    Return the probability of winning while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    

    #transition probability matrix
    P = np.zeros((N + 1, N + 1))

    
    for i in range(1, N):
        if i < N / 2:
            P[i, 2 * i] = p
            P[i, 0] = q
        else:
            P[i, N] = p
            P[i, 2 * i - N] = q

    # Absorbing states
    
    P[0, 0] = 1  
    P[N, N] = 1  
    
    Q = P[1:N, 1:N] #transition matrix between transient states
    R = P[1:N, [0, N]] 
    I = np.eye(N - 1) #identity matrix of size (N+1)*(N+1)
    F = np.linalg.inv(I - Q) #fundamental matrix
    B = np.dot(F,R)
    
    win_prob = B[k-1, 1]  # Probability of winning from initial wealth k

    return win_prob



def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if k==0 or k==N:
        duration=0
    else:
        P = np.zeros((N+1,N+1))
        for i in range(1,N):
            if i<N/2:
                P[i,2*i] = p
                P[i,0] = q
            else:
                P[i,N] = p
                P[i,2*i-N] = q
        P[0,0] = 1
        P[N,N] = 1
        Q = P[1:N,1:N] #N-1 transient states
        I = np.eye(N-1)
        F = np.linalg.inv(I-Q) #fundamental matrix
        ones = np.ones((N-1,1))
        t = np.dot(F,ones) #gives expected duration for each transient state
        duration = t[k-1,0]
    return duration


