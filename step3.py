def getUncoveredMinterms(essential, chart, minterms):
    covered = [False] * len(minterms)

    for imp in essential:
        row = chart[imp]
        for i, v in enumerate(row):
            if v == "1":
                covered[i] = True

    return [i for i, c in enumerate(covered) if not c]

def selectAdditionalImplicants(chart, uncovered, essentials):
    selected = []
    for imp, row in chart.items():
        if imp in essentials:
            continue
        count = sum(1 for i in uncovered if row[i] == "1")
        if count > 0:
            selected.append((count, imp))

    if not selected:
        return []

    selected.sort(reverse=True)
    return [selected[0][1]]