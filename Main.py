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
cPMoveMaleBetaA = 1 # Beta function parameter 1 if heterogeneity, males
cPMoveMaleBetaB = 1 # Beta function parameter 2 if heterogeneity, males
cPMoveFemaleAll = 0.5
cPMoveFemaleBetaA = 1 # Beta function parameter 1 if heterogeneity, females
cPMoveFemaleBetaB = 1 # Beta function parameter 2 if heterogeneity, females
vPMoveParameters = [cPMoveHeterogeneityIndicator,cPMoveMaleAll,cPMoveMaleBetaA,cPMoveMaleBetaB,cPMoveFemaleAll,cPMoveFemaleBetaA,cPMoveFemaleBetaB]

# Dying
cPDie = 0.1

# Initialise area
cDays = 100
cNumHouses = 50
cNumSwarms = 50
cSize = 1500
cNumMaleMosquitoes = 5000
cNumFemaleMosquitoes = 5000

# Covariance in houses/swarms
cCovarianceIndicator = 1
cNumDisturbances = 4
cSwarmsPerDisturbance = int(cNumHouses/cNumDisturbances)
cHousesPerDisturbance = int(cNumSwarms/cNumDisturbances)
cSigmaKernelHouses = 100
cSigmaKernelSwarms = 100
vCovarianceParameters = [cCovarianceIndicator,cNumDisturbances,cSwarmsPerDisturbance,cHousesPerDisturbance,cSigmaKernelSwarms,cSigmaKernelHouses]

aArea = basic.area(cSize,cNumHouses,cNumSwarms,vCovarianceParameters)
functions.initialise(aArea,cNumMaleMosquitoes,cNumFemaleMosquitoes,vPInParameters,vPMoveParameters,cPDie)


# Released mosquitoes
cNumberMaleReleases = 1 # Single release -> 1, multiple -> #
cReleaseMaleStartTime = 1
cReleaseMaleTimeGap = 2
cReleaseMaleMosquitoNumber = 500
cNumberFemaleReleases = 1 # Single release -> 1, multiple -> #
cReleaseFemaleStartTime = 1
cReleaseFemaleTimeGap = 2
cReleaseFemaleMosquitoNumber = 500
cIntroductionNew = 1 # Whether or not to introduce new mosquitoes to system
vReleaseParameters = [cNumberMaleReleases,cReleaseMaleStartTime,cReleaseMaleTimeGap,cReleaseMaleMosquitoNumber,cNumberFemaleReleases,cReleaseFemaleStartTime,cReleaseFemaleTimeGap,cReleaseFemaleMosquitoNumber,cIntroductionNew]

# Sampling parameters
cSampleMaleTime = 3
cSampleFemaleTime = 3
cKnownSwarmsPercentage = 0.5
cDailyNumTargetsSampled = 50
vSampleParameters = [cSampleMaleTime,cSampleFemaleTime,cKnownSwarmsPercentage,cDailyNumTargetsSampled]

# Evolve system
functions.evolveSystem(aArea,cDays,vReleaseParameters,vPInParameters,vPMoveParameters,cPDie,vSampleParameters)






