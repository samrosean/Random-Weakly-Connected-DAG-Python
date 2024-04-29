'''
Create a random weakly-connected Directed Acyclic Simple Graph on n nodes and m edges
Samuel Rosean - samuelrosean@einsteinmed.edu

Input:
    N - number of nodes
    m - number of total edges

Output:
    matrix - numpy adjacency matrix of resulting graph
            

Much like how a Erdos-Renyi graph can be created in a G(n, m) form, where n represents the number of nodes and m the numebr of edges of the final graph, 
this algorithm assembles a weakly connnected Directed Acyclic Graph in much the same way.

This algorithm takes advantage of two properties of Directed Acyclic Graphs and of weakly-connected graphs respectively.

1. Directed Acyclic Graphs have a topological ordering. Since Directed Acyclic Graphs can be topologically sorted so that no node i connects to a node j where i > j, then only the upper triangle
of an adjacency matrix will have connections.

2. Weakly Connected Graphs have a minimal spanning tree.

--- ---

The algorithm then consists of 3 steps. 

1. Create a random spanning tree of a complete graph of n vertices using a random walk. (https://www.cs.cmu.edu/~15859n/RelatedWork/RandomTrees-Wilson.pdf

2. Direct the random tree so that each edge only connects from an i to a j such i < j.

3. Randomly add edges to the upper triangle through a poison process until the total number of edges is equal to m.

'''

def randomDAG(size = 10, connections = 20)

    ## since a DAG can only have connections in the upper right traingle, this creates an upper limit on the amount of edges which it can have.
    if connections > ((size*(size-1))/2):
        print("Too many connections to create a DAG")
        
    ## since every weakly connected graph has at least a minimal spanning tree, and since a tree graph has n-1 edges, this creates a lower bound on the amount of edges a DAG can have.
    elif connections < size - 1:
        print("Not enough connections to make a weakly-connected graph on the given number of vertices.")
        print("For a graph of size " + str(size) + " there must be at least " + str(size - 1) + " connections for a minimal weakly-connected graph.")
    else:
        
        #create a list of nodes yet to be reached (we start at node 0)
        unReached = list(range(1,size))
        ## create array to store the edges 
        minimalEdges = []

        ## set current node (starts at 0)
        currentLocation = 0
        ## random walk until you have reached every node, if you reach a new node, the edge that got you there will be part of the random tree
        while len(unReached) > 0:
            lookIndex = random.randint(0,size-1)
            while lookIndex == currentLocation:
                lookIndex = random.randint(0,size-1)
            if lookIndex in unReached:
                minimalEdges.append((currentLocation, lookIndex))
                unReached.remove(lookIndex)
            currentLocation = lookIndex

        ## create a matrix to put new edges in, orient all edges so they go from i to j such tha i < j
        matrix = np.empty((size, size))
        matrix.fill(0)
        for item in minimalEdges:
            if item[0] > item[1]:
                matrix[item[1]][item[0]] = 1
            else:
                matrix[item[0]][item[1]] = 1
    
        
        i = 0
        ## add all the remaining connections needed randomly (must fall in the upper triangle)
        while i < connections - (size - 1):
            index = random.randint(0,size-2)
            index2 = random.randint(index+1,size-1)
            if (matrix[index][index2] == 0):
                matrix[index][index2] = 1
                i+=1
    
        return(matrix)