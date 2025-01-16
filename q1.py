def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    num = 1 - (q/p)**k
    den = 1 - (q/p)**N
    if den !=0:
        return num/den
    return k/N
def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if q>=p:
        return 0
    elif p>q:
        return 1 - (q/p)**k
    
def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if p==q:
        return k*(N-k)
    else:
        num = (1 - (q/p)**k)*N - k*(1-(q/p)**N)
        den = (p-q)*(1-(q/p)**N)
        return num/den

