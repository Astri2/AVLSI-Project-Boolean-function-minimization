# Convert Prime implicant into boolean expression

def essentialPrimesToBoolExpr(essentialPrimes, variableNames):

    if(len(essentialPrimes) == 0): return "Antilogy: no boolean expression is valid"

    cubes = []
    for prime in essentialPrimes:
        if all(c == "-" for c in prime): return "Tautology: any boolean expression is valid"

        cube = ""
        for i, c in enumerate(prime):
            if(c == '-'): continue
            elif(c == '1'): cube += variableNames[i]
            else: cube += variableNames[i] + "'"
        cubes.append(cube)
    return " + ".join(cubes)