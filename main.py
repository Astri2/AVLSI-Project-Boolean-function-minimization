from step0 import getMinterms
from step1 import getprimeImplicants
from step2 import *

params = getMinterms()
primeImplicants = getprimeImplicants(params)
primeImplicantChart = CreatePrimeImplicantChart(primeImplicants, params)
print("\n Prime Implicant Chart:", primeImplicantChart)
print("\n Essential Prime Implicant:", getEssentialPrimeImplicants(primeImplicantChart, params))