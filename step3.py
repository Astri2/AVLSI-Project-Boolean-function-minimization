def getUncoveredMinterms(currentImplicants, chart, minterms):
    covered = [False] * len(minterms)

    # for each minterm, check that it is covered by the current implicants
    for imp in currentImplicants:
        row = chart[imp]
        for i, v in enumerate(row):
            if v == "1":
                covered[i] = True
    
    # return the indices of the uncovered minterms
    return [i for i, c in enumerate(covered) if not c]

def selectAdditionalImplicant(chart, uncovered, currentImplicants):
    selected = []
    
    # for each non selected implicant
    for imp, row in chart.items():
        if imp in currentImplicants:
            continue

        # count the number of uncovered minterm the implicant could cover if selected
        count = sum(1 for i in uncovered if row[i] == "1")
        if count > 0:
            selected.append((count, imp))

    if not selected:
        return []

    # selected the implicant covering the most minterms
    selected.sort(reverse=True)
    return [selected[0][1]]

def completeCover(essentialPrimeImplicants, primeImplicantChart, minterms):
    
    finalCover = essentialPrimeImplicants
    
    # while not all minterms are covered
    while True:
        # retrieve the uncovered minterms indices
        uncovered = getUncoveredMinterms(finalCover, primeImplicantChart, minterms)
        if(len(uncovered) == 0): return finalCover
        
        # add an implicant that covers as many uncovered minterms as possible
        additional = selectAdditionalImplicant(primeImplicantChart, uncovered, finalCover)
        if(len(additional) == 0):
            print("No additional implicant found")
            return finalCover
        
        finalCover += additional