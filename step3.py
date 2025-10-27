# Convert Prime implicant into boolean expression

def essentialPrimesToBoolExpr(essentialPrimes: list[str], variableNames: list[str]):

    if(not essentialPrimes): return "Antilogy: no boolean expression is valid"

    conjonctions: list[str] = []
    for prime in essentialPrimes:
        if all(c == "-" for c in prime): return "Tautology: any boolean expression is valid"

        conj: str = ""
        for i, c in enumerate(prime):
            if(c == '-'): continue
            elif(c == '1'): conj += variableNames[i]
            else: conj += variableNames[i] + "'"
        conjonctions.append(conj)
    return " + ".join(conjonctions)