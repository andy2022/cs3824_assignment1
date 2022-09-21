## Function to compute data for generating precision-recall curve

def func(ranked_edges, g):
    '''
    For each rank in the ranked-edges file, check if all edges appear in the
    corresponding graph structure (provided as parameter).
    ranked_edges: dict containing all edges split up by rank
    g: corresponding graph structure from part 1
    '''
    true_positives = 0
    total_edges = 0 # Maintain count of total edges in ranked-edges file
    precision = [0] * (list(ranked_edges)[-1]+1)
    recall = [0] * (list(ranked_edges)[-1]+1)

    for rank in ranked_edges.keys():

        # Iterate through list of all edges in this rank
        for edge in ranked_edges[rank]:

            # If current edge exists in graph, increment true positives
            if g.has_edge(*edge):
                true_positives += 1
            total_edges += 1

        # Calculate precision and recall for this rank
        precision[rank] = true_positives / rank
        recall[rank] = true_positives / list(ranked_edges)[-1]

    return precision, recall