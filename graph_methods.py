## Methods for reading data files and creating graphs
## Uses package networkx

import networkx

def add_edges(mygraph, fname):
    '''
    Reads the specified edges text file and adds all edges to the specified graph.
    mygraph: Graph to which edges will be added (MultiDiGraph)
    fname: Input file to read
    '''
    f = open(fname, "r")
    firstline = f.readline() # Read first line
    assert(firstline[:5] == "#tail") # Check that correct table is being read

    for line in f:
        arr = line.split()
        assert(len(arr) == 8) # For edge files, arr length is 8

        # Special conditions based on edge type (arr[5])
        if arr[5] == "physical":
            # Add two edges - head-to-tail and tail-to-head
            mygraph.add_edge(arr[1], arr[0], weight = int(arr[2])) # head to tail
            mygraph.add_edge(arr[0], arr[1], weight = int(arr[2])) # tail to head
        else:
            mygraph.add_edge(arr[0], arr[1], weight = int(arr[2])) # head to tail
    # End of loop

    f.close()