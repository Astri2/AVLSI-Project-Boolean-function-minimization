import re

def CreatePrimeImplicantChart(primeImplicants, minterms):
    primeImplicantChart = {}
    # iterate through each implicant
    for i in range(len(primeImplicants)):
        primeImplicant = primeImplicants[i]
        primeImplicantChart[primeImplicant]=''
        # for each minterm, check it is covered by the current implicant
        for j in range(len(minterms)):
            # replace '-' by a regex matching both 0 and 1
            primeImplicant_RE = re.sub("-", "[01]", primeImplicant)
            if re.fullmatch(primeImplicant_RE, minterms[j]):
                primeImplicantChart[primeImplicant]+="1"
            else:
                primeImplicantChart[primeImplicant]+="0"

    return primeImplicantChart
   
def getEssentialPrimeImplicants(primeImplicantChart, minterms):

    essentialPrimeImplicants = set()
    mintermCoverages = list(primeImplicantChart.values())
    keys = list(primeImplicantChart.keys())
    num_minterms = len(minterms)

    # for each minterm
    for i in range(num_minterms):
        c = [m[i] for m in mintermCoverages]
        count_one = 0
        idx_one = 0
        # check how many implicant cover it
        for j in range(len(c)):
            if c[j] == "1":
                count_one += 1
                if(count_one > 1):
                    break
                else:
                    idx_one = j
        # if there is exactly one, then this implicant is essential
        if count_one == 1:
            essentialPrimeImplicants.add(keys[idx_one])
    
    return list(essentialPrimeImplicants)