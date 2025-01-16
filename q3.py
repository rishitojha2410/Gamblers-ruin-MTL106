
import numpy as np #type: ignore



def game_duration(p, q, k, t, W):
    """
    Return the expected number of rounds the gambler will play before quitting.

    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    t : int, t < k, the gambler will quit if she reaches t
    W : int, the threshold on maximum wealth the gambler can reach
    
    """

    num_states = W +2
    transition_matrix = np.zeros((num_states, num_states))
    transition_matrix[0][0] = 1        
    for i in range(num_states):
        if i > 0:                
            transition_matrix[i, i-1] = q
        if i < num_states - 1 and i>0:   
            transition_matrix[i, i+1] = p

        
    transition_matrix[-1, -2] = 1
        
        

    b = np.ones((num_states-1,1))

      
    A = np.eye(num_states-1) - transition_matrix[1:num_states+1,1:num_states+1]
    F_matrix = np.linalg.inv(A)
    expected_time = F_matrix@b
        
        
        
    
    return (k-t)*expected_time[0,0]



print(game_duration(0.5,0.5,201,200,1))