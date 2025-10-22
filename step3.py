# Convert Prime implicant into boolean expression

def essentialPrimesToBoolExpr(essentialPrimes: list[str], variableNames: list[str]):
    conjonctions: list[str] = []
    for prime in essentialPrimes:
        conj: str = ""
        for i, c in enumerate(prime):
            if(c == '-'): continue
            elif(c == '1'): conj += variableNames[i]
            else: conj += variableNames[i] + "'"
        conjonctions.append(conj)
    return " + ".join(conjonctions)