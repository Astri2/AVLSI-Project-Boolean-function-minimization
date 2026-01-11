import re

def CreatePrimeImplicantChart(primeImplicants, minterms):
    #primeImplicantChart = {primeImplicant: '' for primeImplicant in primeImplicants}
    primeImplicantChart = {}
    for i in range(len(primeImplicants)):
        primeImplicant = primeImplicants[i]
        primeImplicantChart[primeImplicant]=''
        for j in range(len(minterms)):
            primeImplicant_RE = re.sub("-", "[01]", primeImplicant)
            if re.fullmatch(primeImplicant_RE, minterms[j]):
                primeImplicantChart[primeImplicant]+="1"
            else:
                primeImplicantChart[primeImplicant]+="0"

    return primeImplicantChart
   
def getEssentialPrimeImplicants(primeImplicantChart, minterms):

    for implicant, cov in primeImplicantChart.items():
        if "0" not in cov: return [implicant]

    essentialPrimeImplicants = []
    mintermCoverages = list(primeImplicantChart.values())
    keys = list(primeImplicantChart.keys())
    num_minterms = len(minterms)

    for i in range(num_minterms):
        c = [m[i] for m in mintermCoverages]
        count_one = 0
        idx_one = 0
        for j in range(len(c)):
            if c[j] == "1":
                count_one += 1
                if(count_one > 1):
                    break
                else:
                    idx_one = j
            
        if count_one == 1:
            essentialPrimeImplicants.append(keys[idx_one])
    
    return essentialPrimeImplicants