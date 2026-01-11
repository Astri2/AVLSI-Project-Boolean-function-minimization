from step0 import getMinterms
from step1 import getprimeImplicants
from step2 import *
from step3 import essentialPrimesToBoolExpr

res0 = getMinterms()
if(res0 == None): exit(1)
minterms, variableNames = res0

primeImplicants = getprimeImplicants(minterms)

primeImplicantChart = CreatePrimeImplicantChart(primeImplicants, minterms)
print("\nPrime Implicant Chart:", primeImplicantChart)

essentialPrimeImplicants = getEssentialPrimeImplicants(primeImplicantChart, minterms)
print("\nEssential Prime Implicant:", essentialPrimeImplicants)

finalExpression = essentialPrimesToBoolExpr(essentialPrimeImplicants, variableNames)
print("\nFinal boolean expression:", finalExpression)