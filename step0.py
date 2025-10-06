from sys import stderr

def __toBin(n: int, size: int) -> str:
    # convert to bin and remove 0b prefix
    b: str = bin(n)[2:]
    # add 0 to the left to always get the same len
    b = "0" * max(0, size - len(b)) + b
    return b

def __generateVariableNames(nbVariables: int) -> list[str]:
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
        if(values[i] not in "10-"):
            print("Error: Value must be '1', '0' or '-'", file=stderr)
            return None
        
    return nbVariables, values

def __extractMinterms(nbVariables: int, values: list[str] ):
    max_m_len = len(str(len(values)-1))

    minterms: list[str] = []
    print("Minterms:")
    for num, val in enumerate(values):
        if(val == "0"): continue

        if(val == "1"): print(f" m{num:<{max_m_len}} : ", end="")
        elif(val == "-"): print(f"(m{num:<{max_m_len}}): ", end="")
        minterms.append(__toBin(num, nbVariables))
        print(minterms[-1])

    print('[\"', end="")
    print(*minterms, sep="\", \"", end="")
    print('\"]', end="")

    return minterms

def getMinterms():
    res = __fillTruthTable()
    if(res == None): return None
    
    nbVariables, values = res
    minterms = __extractMinterms(nbVariables, values)
    return minterms