from IBM_functions import basic
import matplotlib.pyplot as plt
from IBM_functions import functions

#PIn parameters

cPInHeterogeneityIndicator = 1 # Whether to allow individual heterogeneity in PIn
cPInMaleAll = 0.5 # If no heterogeneity, this parameter will hold for all male mosquitoes
cPInMaleBetaA = 1 # Beta function parameter 1 if heterogeneity, males
cPInMaleBetaB = 3 # Beta function parameter 2 if heterogeneity, males
cPInFemaleAll = 0.5
cPInFemaleBetaA = 3 # Beta function parameter 1 if heterogeneity, females
cPInFemaleBetaB = 1 # Beta function parameter 2 if heterogeneity, females
vPInParameters = [cPInHeterogeneityIndicator,cPInMaleAll,cPInMaleBetaA,cPInMaleBetaB,cPInFemaleAll,cPInFemaleBetaA,cPInFemaleBetaB]

# PMove parameters
cPMoveHeterogeneityIndicator = 0 # Whether to allow individual heterogeneity in PMove
cPMoveMaleAll = 0.5 # If no heterogeneity, this parameter will hold for all male mosquitoes
cPMoveMaleBetaA = 1 # Beta function parameter 1 if heterogeneity, males
cPMoveMaleBetaB = 1 # Beta function parameter 2 if heterogeneity, males
cPMoveFemaleAll = 0.5
cPMoveFemaleBetaA = 1 # Beta function parameter 1 if heterogeneity, females
cPMoveFemaleBetaB = 1 # Beta function parameter 2 if heterogeneity, females
vPMoveParameters = [cPMoveHeterogeneityIndicator,cPMoveMaleAll,cPMoveMaleAll,cPMoveMaleBetaA,cPMoveMaleBetaB,cPMoveFemaleAll,cPMoveFemaleBetaA,cPMoveFemaleBetaB]

# Initialise area
cNumHouses = 100
cNumSwarms = 100
cSize = 1500
cNumMaleMosquitoes = 1000
cNumFemaleMosquitoes = 1000
aArea = basic.area(cSize,cNumHouses,cNumSwarms)
functions.initialise(aArea,cNumMaleMosquitoes,cNumFemaleMosquitoes,vPInParameters,vPMoveParameters)
vFemales = aArea.getNumListInsideFemales()
vMales = aArea.getNumListInsideMales()


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(aArea.getHouseLocations()[:,0],aArea.getHouseLocations()[:,1],s=5*vFemales,c='b',label='houses')
ax1.scatter(aArea.getSwarmLocations()[:,0],aArea.getSwarmLocations()[:,1],s=5*vMales,c='r',label = 'swarms')
plt.legend(loc='upper left')
plt.show()









