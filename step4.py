# Convert Prime implicant into boolean expression

def primesToBoolExpr(primes, variableNames):
    # if the cover is empty, the function is 0
    if(len(primes) == 0): return "0 (no minterm)"

    cubes = []
    for prime in primes:
        # if a prime is composed of only hyphen, the function is always true, so 1
        if all(c == "-" for c in prime): return "1 (tautology)"

        cube = ""
        # for each prime, build a cube (conjonction of variables)
        for i, c in enumerate(prime):
            # discard hypens
            if(c == '-'): continue
            # replace 1s and 0s by their respective names and polarities
            elif(c == '1'): cube += variableNames[i]
            else: cube += variableNames[i] + "'"
        cubes.append(cube)

    # join all cubes with ORs
    return " + ".join(cubes)