# Random-Weakly-Connected-DAG
Create a random weakly-connected Directed Acyclic Simple Graph on n nodes and m edges. Much like how an Erdos-Renyi graph can be created in a G(n, m) form, where n represents the number of nodes and m the number of edges, this algorithm assembles a simple weakly-connected Directed Acyclic Graph in much the same way.

This algorithm takes advantage of two properties of Directed Acyclic Graphs and of weakly-connected graphs respectively.

1. Directed Acyclic Graphs have a topological ordering. Since Directed Acyclic Graphs can be topologically sorted so that no node i connects to a node j where i > j, then only the upper triangle
of an adjacency matrix will have connections.

2. Weakly Connected Graphs have a minimal spanning tree.

--- ---

The algorithm then consists of 3 steps. 

1. Create a random spanning tree of a complete graph of n vertices using a random walk.

2. Direct the random tree so that each edge only connects from an i to a j such i < j.

3. Randomly add edges to the upper triangle randomly until the total number of edges is equal to m.
