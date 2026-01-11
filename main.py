from step0 import getMinterms
from step1 import getprimeImplicants
from step2 import CreatePrimeImplicantChart, getEssentialPrimeImplicants
from step3 import completeCover
from step4 import essentialPrimesToBoolExpr

res0 = getMinterms()
if(res0 == None): exit(1)
minterms, dontcare, variableNames = res0

primeImplicants = getprimeImplicants(minterms + dontcare)
print("\nPrime Implicants:", primeImplicants)

primeImplicantChart = CreatePrimeImplicantChart(primeImplicants, minterms)
print("\nPrime Implicant Chart:", primeImplicantChart)

essentialPrimeImplicants = getEssentialPrimeImplicants(primeImplicantChart, minterms)
print("\nEssential Prime Implicant:", essentialPrimeImplicants)

FinalCover = completeCover(essentialPrimeImplicants, primeImplicantChart, minterms)
print("\nFinal Implicant cover:", FinalCover)

finalExpression = essentialPrimesToBoolExpr(FinalCover, variableNames)
print("\nFinal boolean expression:", finalExpression)