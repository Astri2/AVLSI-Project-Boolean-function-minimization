from sys import stderr

def __toBin(n: int, size: int) -> str:
    # convert to bin and remove 0b prefix
    b: str = bin(n)[2:]
    # add 0 to the left to always get the same len
    b = "0" * max(0, size - len(b)) + b
    return b

def __generateVariableNames(nbVariables: int) -> list[str]:
    # iterate trough all letters. Add numbers if needed
    if(nbVariables <= 26):
        return [chr(97+i) for i in range(nbVariables)]
    else:
        return [chr(97 + i%26) + str((i // 26)+1) for i in range(nbVariables)]

def __fillTruthTable():
    nbVariables_s: str = input("Number of variables: ")
    if(not nbVariables_s.isnumeric()):
        print("Error: Variable count must be numeric", file=stderr)
        return None
    
    nbVariables = int(nbVariables_s)
    if(nbVariables < 1): 
        print("Error: Variable count can't be less than 1", file=stderr)
        return None
    
    variableNames: list[str] = __generateVariableNames(nbVariables)
    
    ValSep = " " * len(variableNames[0])
    max_m: int = 2**nbVariables
    max_m_len = len(str(max_m-1))
    values: list[str] = [''] * max_m

    print("For each truth table line, please enter the result value (True: 1, False: 0, Don't care: -)")
    print(" " * max_m_len + "  | ", end ="")
    print(*variableNames, end= " |\n")
    for i in range(max_m):
        print(f"m{i:<{max_m_len}} | ", end="")
        print(*__toBin(i, nbVariables), sep=ValSep, end=" | ")
        values[i] = input()
        if(not values[i] or values[i] not in "10-"):
            print("Error: Value must be '1', '0' or '-'", file=stderr)
            return None
        
    return nbVariables, values, variableNames

def __extractMinterms(nbVariables: int, values: list[str] ):
    max_m_len = len(str(len(values)-1))

    minterms: list[str] = []
    dontcare: list[str] = []
    print("Minterms:")
    for num, val in enumerate(values):
        if(val == "0"): continue

        m = __toBin(num, nbVariables)
        
        if(val == "1"): 
            print(f" m{num:<{max_m_len}} : ", end="")
            minterms.append(m)
        elif(val == "-"): 
            print(f"(m{num:<{max_m_len}}): ", end="")
            dontcare.append(m)

        print(m)

    # At this point we could already stop the algorithm for specific cases
    # However we want to check that the algorithm can withstand those cases so we commented the checks
    """
    if(len(minterms) == 0):
        if(len(dontcare) == 0):
            print("Antilogy Detected. The solution is f=0. Stopping here")
        else:
            print("Only don't care minterm detected. Choosing f=0. Stopping here")
        exit(0)
    elif(len(minterms) == len(values)):
        print("Tautology Detected. The solution is f=1. Stopping here")
        exit(0)
    """
    
    return minterms, dontcare

def getMinterms():
    res = __fillTruthTable()
    if(res == None): return None
    
    nbVariables, values, variableNames = res
    minterms, dontcare = __extractMinterms(nbVariables, values)
    return minterms, dontcare, variableNames