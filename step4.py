# Convert Prime implicant into boolean expression

def primesToBoolExpr(primes, variableNames):

    if(len(primes) == 0): return "0 (no minterm)"

    cubes = []
    for prime in primes:
        if all(c == "-" for c in prime): return "1 (tautology)"

        cube = ""
        for i, c in enumerate(prime):
            if(c == '-'): continue
            elif(c == '1'): cube += variableNames[i]
            else: cube += variableNames[i] + "'"
        cubes.append(cube)
    return " + ".join(cubes)