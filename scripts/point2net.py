import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import spatial
import networkx as nx
import sys

if __name__ == "__main__":

    POINTFILE = sys.argv[1]
    OUTPUTFILE = sys.argv[2]

    df = pd.read_csv(POINTFILE, sep="\t")
    
    N = df.shape[0]
    M = (N - 1) / 2 * 3.2  # number of edges to be placed
    D = np.zeros((N, N))
    
    D = spatial.distance.squareform(spatial.distance.pdist(df))
    
    d = np.sqrt(np.sum(D, axis=1))
    D = np.diag(1 / d) @ D @ np.diag(1 / d)
    S = np.random.power(3, (N,))
    
    dif = 1e30
    P_ = []
    for l in np.logspace(1, 5):
        P = np.outer(S, S) * np.exp(-l * np.power(D, 1))
        P[P > 1] = 1
        np.fill_diagonal(P, 0)
        EM = np.sum(P) / 2
        d = np.abs(EM - M)
        if d < dif:
            dif = d
            P_ = P
        print(l)
    
    P = P_
    Arand = np.array(np.random.random((N, N)) <= P).astype(int)
    
    G = nx.from_numpy_array(Arand)
    
    pos = {}
    r, c = np.nonzero(np.triu(Arand))
    for i in range(N):
        pos[i] = np.array([df.iloc[i, 0], -df.iloc[i, 1]])
    
    for node, (x, y) in pos.items():
        G.node[node]["x"] = float(x)
        G.node[node]["y"] = float(y)
    nx.write_graphml(G, OUTPUTFILE)
    #nx.draw_networkx(G, pos=pos, with_labels=False, node_size=S * 10)
    #plt.axis("off")

    #fig.savefig(OUTPUTFILE, bbox_inches = "tight", dpi = 300)
