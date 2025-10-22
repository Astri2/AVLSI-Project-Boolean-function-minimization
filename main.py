from step0 import getMinterms
from step1 import getprimeImplicants
from step2 import *
from step3 import essentialPrimesToBoolExpr

minterms, variableNames = getMinterms()
primeImplicants = getprimeImplicants(minterms)
primeImplicantChart = CreatePrimeImplicantChart(primeImplicants, minterms)
print("\n Prime Implicant Chart:", primeImplicantChart)
essentialPrimeImplicants = getEssentialPrimeImplicants(primeImplicantChart, minterms)
print("\n Essential Prime Implicant:", essentialPrimeImplicants)
print("\nFinal boolean expression:", essentialPrimesToBoolExpr(essentialPrimeImplicants, variableNames))