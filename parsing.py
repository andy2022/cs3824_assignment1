## Implementation of brief parsing function for part 2

def parse(fname):
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