from IBM_functions import basic
import matplotlib.pyplot as plt
from IBM_functions import functions

#PIn parameters

cPInHeterogeneityIndicator = 1 # Whether to allow individual heterogeneity in PIn
cPInMaleAll = 0.5 # If no heterogeneity, this parameter will hold for all male mosquitoes
cPInMaleBetaA = 1 # Beta function parameter 1 if heterogeneity, males
cPInMaleBetaB = 1 # Beta function parameter 2 if heterogeneity, males
cPInFemaleAll = 0.5
cPInFemaleBetaA = 1 # Beta function parameter 1 if heterogeneity, females
cPInFemaleBetaB = 1 # Beta function parameter 2 if heterogeneity, females
vPInParameters = [cPInHeterogeneityIndicator,cPInMaleAll,cPInMaleBetaA,cPInMaleBetaB,cPInFemaleAll,cPInFemaleBetaA,cPInFemaleBetaB]

# PMove parameters
cPMoveHeterogeneityIndicator = 1 # Whether to allow individual heterogeneity in PMove
cPMoveMaleAll = 0.5 # If no heterogeneity, this parameter will hold for all male mosquitoes
cPMoveMaleBetaA = 10 # Beta function parameter 1 if heterogeneity, males
cPMoveMaleBetaB = 1 # Beta function parameter 2 if heterogeneity, males
cPMoveFemaleAll = 0.5
cPMoveFemaleBetaA = 10 # Beta function parameter 1 if heterogeneity, females
cPMoveFemaleBetaB = 1 # Beta function parameter 2 if heterogeneity, females
vPMoveParameters = [cPMoveHeterogeneityIndicator,cPMoveMaleAll,cPMoveMaleBetaA,cPMoveMaleBetaB,cPMoveFemaleAll,cPMoveFemaleBetaA,cPMoveFemaleBetaB]

# Initialise area
cDays = 100
cNumHouses = 50
cNumSwarms = 50
cSize = 1500
cNumMaleMosquitoes = 2000
cNumFemaleMosquitoes = 2000

# Covariance in houses/swarms
cCovarianceIndicator = 1
cNumDisturbances = 2
cSwarmsPerDisturbance = int(cNumHouses/cNumDisturbances)
cHousesPerDisturbance = int(cNumSwarms/cNumDisturbances)
cSigmaKernelHouses = 500
cSigmaKernelSwarms = 500
vCovarianceParameters = [cCovarianceIndicator,cNumDisturbances,cSwarmsPerDisturbance,cHousesPerDisturbance,cSigmaKernelSwarms,cSigmaKernelHouses]

aArea = basic.area(cSize,cNumHouses,cNumSwarms,vCovarianceParameters)
functions.initialise(aArea,cNumMaleMosquitoes,cNumFemaleMosquitoes,vPInParameters,vPMoveParameters)


# Released mosquitoes
cNumberMaleReleases = 2 # Single release -> 1, multiple -> #
cReleaseMaleStartTime = 1
cReleaseMaleTimeGap = 2
cReleaseMaleMosquitoNumber = 20
cNumberFemaleReleases = 1 # Single release -> 1, multiple -> #
cReleaseFemaleStartTime = 1
cReleaseFemaleTimeGap = 2
cReleaseFemaleMosquitoNumber = 20
vReleaseParameters = [cNumberMaleReleases,cReleaseMaleStartTime,cReleaseMaleTimeGap,cReleaseMaleMosquitoNumber,cNumberFemaleReleases,cReleaseFemaleStartTime,cReleaseFemaleTimeGap,cReleaseFemaleMosquitoNumber]

# Sampling parameters
cSampleMaleTime = 30
cSampleFemaleTime = 30

# Evolve system
functions.evolveSystem(aArea,cDays,vReleaseParameters)






