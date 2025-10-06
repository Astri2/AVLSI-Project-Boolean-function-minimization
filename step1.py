# implementation of the McCluskey Algorithm
# Step 1
# https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm

def mergeMinterms(minterm1: str, minterm2: str) -> str:
    mergedMinterm = ""
    for i in range(len(minterm1)):
        # If the bits vary then replace it with a dash, otherwise the bit remains in the merged minterm.
        if(minterm1[i] != minterm2[i]):
            mergedMinterm += "-"
        else: mergedMinterm += minterm1[i]
    return mergedMinterm

    # TODO better inline
    # mergedMinterm = "".join([(c1 if c1 == c2 else '-') for c1, c2 in zip(minterm1, minterm2)])

def checkDashesAlign(minterm1: str, minterm2: str)-> bool:
    for i in range(len(minterm1)):
        # If one minterm has dashes and the other does not then the minterms cannot be merged. 
        # TODO: does this make sense ?
        if minterm1[i] != '-' and minterm2[i] == '-': 
            return False
    return True

def checkMintermDifference(minterm1: str, minterm2: str) -> bool:
    # minterm1 and minterm2 are strings representing all of the currently found prime implicants and merged 
    # minterms. Examples include '01--' and '10-0' m1, m2 ← integer representation of minterm1 and minterm2 with the dashes removed, these are replaced with 0
    m1: int = int(minterm1.replace('-', '0'), 2)
    m2: int = int(minterm2.replace('-', '0'), 2)
    res: int = m1 ^ m2
    return res != 0 and (res & (res - 1)) == 0

def getprimeImplicants(minterms: list[str]) -> list[str]:
    """Computes the prime implicants from a list of minterms.
    Each minterm is of the form "1001, "1010", etc and can be represented with a string
    # TODO: does not take "Groups" into account

    Args:
        minterms (list[str]): list of minterms to merge recursively to get prime Implicants

    Returns:
        list[str]: The prime Implicants
    """
    
    primeImplicants: list[str] = list()
    merges: list[bool] = [False] * len(minterms)
    numberOfMerges: int = 0
    mergedMinterm: str = ""
    minterm1: str = ""
    minterm2: str = ""

    for i in range(len(minterms)):
        for c in range(i+1, len(minterms)):
            minterm1: str = minterms[i]
            minterm2: str = minterms[c]
            # Checking that two minterms can be merged
            if(checkDashesAlign(minterm1, minterm2)) and checkMintermDifference(minterm1, minterm2):
                mergedMinterm: str = mergeMinterms(minterm1, minterm2)
                # TODO set instead of list ?
                if(mergedMinterm not in primeImplicants):
                    primeImplicants.append(mergedMinterm)
                numberOfMerges += 1
                merges[i] = True
                merges[c] = True
    
    # Filtering all minterms that have not been merged as they are prime implicants. Also removing duplicates
    for j in range(len(minterms)):
        if(not merges[j] and minterms[j] not in primeImplicants):
            primeImplicants.append(minterms[j])

    # if no merges have taken place then all of the prime implicants have been found so return, otherwise
    # keep merging the minterms.
    if(numberOfMerges == 0):
        return primeImplicants
    else: return getprimeImplicants(primeImplicants)

if __name__ == "__main__":
    l = ["0100", "1000", "1001", "1010", "1100", "1011", "1110", "1111"]
    print(getprimeImplicants(l))