## Implementation of brief parsing function for part 2

def parse(fname):
    '''
    Reads through specified ranked-edges data file and stores results in
    dict structure. The key is the rank, and the value is a list containing all
    edges stored as tuples. Returns the generated dict.
    fname: Name of input file to read
    '''
    d = {}
    f = open(fname, "r")
    firstline = f.readline()
    assert(firstline[:5] == "#tail") # Check that correct table is being read

    for line in f:
        arr = line.split()
        assert(len(arr) == 3) # Verify that only 3 items available in arr
        rank = int(arr[2]) # Cast 3rd entry as integer

        # Generate tuple
        edge = (arr[0], arr[1])

        # If rank already exists as key, append tuple to existing list
        if rank in d.keys():
            d[rank].append(edge)
        # Otherwise, add edge to new list
        else:
            d[rank] = [edge]

    f.close()

    return d


# Alternate implementation involving list - not intended for use
def parse2(fname):
    '''
    Reads through specified ranked-edges data file and store each row
    as a tuple. Returns a list with all rows entered as tuples.
    '''
    l = list()
    f = open(fname, "r")
    firstline = f.readline()
    assert(firstline[:5] == "#tail") # Check that correct table is being read

    for line in f:
        arr = line.split()
        assert(len(arr) == 3) # Verify that only 3 items available in arr

        # Create tuple, append to list
        entry = (arr[0], arr[1], int(arr[2]))
        l.append(entry)

    f.close()

    return l