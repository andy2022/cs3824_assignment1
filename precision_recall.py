## Function to compute data for generating precision-recall curve

def generate(ranked_edges, g):
    '''
    For each rank in the ranked-edges file, check if all edges appear in the
    corresponding graph structure (provided as parameter).
    ranked_edges: dict containing all edges split up by rank
    g: corresponding graph structure from part 1
    '''
    true_positives = 0
    current_edge = 0
    #precision = [0] * (len(ranked_edges)*100)
    #recall = [0] * (len(ranked_edges)*100)
    precision = []
    recall = []

    for rank in [i for i in ranked_edges.keys() if len(ranked_edges[i]) > 0]:

        # Iterate through list of all edges in this rank
        for edge in ranked_edges[rank]:

            # If current edge exists in graph, increment true positives
            if g.has_edge(*edge):
                true_positives += 1
            current_edge += 1 # Increment current edge number

            # Calculate precision and recall for this edge
            precision.append(true_positives / current_edge)
            recall.append(true_positives / g.number_of_edges())

    return precision, recall