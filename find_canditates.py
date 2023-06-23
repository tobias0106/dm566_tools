def find_candidates(v):
    """
    Find all candidates for the next level of the tree for the Apriori algorithm.
    """
    candidates = []
    length = len(v[0])-1
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if v[i][:-1] == v[j][:-1]:
                candidates.append(v[i] + v[j][-1])
    return candidates


mads = ['ABE', 'ABH', 'AEH', 'AFI', 'BDE', 'BEH', 'BET', 'CGI', 'DEH', 'DEI', 'DFI', 'DOI', 'EFH', 'ECI', 'EHI']

mcq_2022 = ['AB', 'AC', 'AE', 'AF', 'BC', 'BF', 'CE', 'CF', 'EF']

candidates = find_candidates(mcq_2022)
print(candidates)

