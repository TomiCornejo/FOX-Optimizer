import numpy as np

def iterarFOX(Max_iter,it,dim, X, Best_pos):
    X = np.array(X)
    Best_pos = np.array(Best_pos)
    
    c1 = 0.18  # range of c1 is [0, 0.18]
    c2 = 0.82  # range of c2 is [0.19, 1]
    
    MinT = 0
    Jump = 0

    a = 2 * (1 - (it / Max_iter))

    for i in range(X.shape[0]):
        r = np.random.rand()
        p = np.random.rand()

        if r >= 0.5:    
            Time_S_T = np.random.rand(dim)
            Sp_S = Best_pos / Time_S_T
            Dist_S_T = Sp_S * Time_S_T
            Dist_Fox_Prey = 0.5 * Dist_S_T
            tt = np.sum(Time_S_T) / dim
            t = tt / 2
            Jump = 0.5 * 9.81 * t**2
            
            if p > 0.18:
                X[i, :] = Dist_Fox_Prey * Jump * c1
            elif p <= 0.18:
                X[i, :] = Dist_Fox_Prey * Jump * c2
            
            if MinT > tt: MinT = tt
        elif r < 0.5:
            X[i, :] = Best_pos + np.random.randn(dim) * (MinT * a)
    return X