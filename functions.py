from IBM_functions import basic
import random as random
import numpy as np
import matplotlib.pyplot as plt

# A function which puts male and female mosquitoes at random swarms and houses respectively throughout the domain
def initialise(aArea,numMaleMosquitoes,numFemaleMosquitoes,vPInParameters,vPMoveParameters):

    # Get PIn parameters
    cPInHeterogeneityIndicator = vPInParameters[0]
    cPInMaleAll = vPInParameters[1]
    cPInMaleBetaA = vPInParameters[2]
    cPInMaleBetaB = vPInParameters[3]
    cPInFemaleAll = vPInParameters[4]
    cPInFemaleBetaA = vPInParameters[5]
    cPInFemaleBetaB = vPInParameters[6]

    # Get the PMove parameters
    cPMoveHeterogeneityIndicator = vPMoveParameters[0]
    cPMoveMaleAll = vPMoveParameters[1]
    cPMoveMaleBetaA = vPMoveParameters[2]
    cPMoveMaleBetaB = vPMoveParameters[3]
    cPMoveFemaleAll = vPMoveParameters[4]
    cPMoveFemaleBetaA = vPMoveParameters[5]
    cPMoveFemaleBetaB = vPMoveParameters[6]

    # First sort males
    cNumMaleMosquitoes = numMaleMosquitoes
    cNumSwarms= aArea.getNumSwarms()
    vSwarmSequence = range(0,cNumSwarms)
    aSwarmList = aArea.getSwarmGroup().getTargetList()
    aMaleMosquitoList = []

   # Put male mosquitoes in
    while cNumMaleMosquitoes > 0:
        cRandSwarm = random.choice(vSwarmSequence)
        if cPInHeterogeneityIndicator == 0 and cPMoveHeterogeneityIndicator == 0:
            aPInMale = cPInMaleAll
            aPMoveMale = cPMoveMaleAll
        elif cPInHeterogeneityIndicator == 0:
            aPInMale = cPInMaleAll
            aPMoveMale = random.betavariate(cPMoveMaleBetaA,cPMoveMaleBetaB)
        elif cPMoveHeterogeneityIndicator == 0:
            aPInMale = random.betavariate(cPInMaleBetaA,cPInMaleBetaB)
            aPMoveMale = cPMoveMaleAll
        else:
            aPInMale = random.betavariate(cPInMaleBetaA,cPInMaleBetaB)
            aPMoveMale = random.betavariate(cPMoveMaleBetaA,cPMoveMaleBetaB)

        aMaleMosquitoList.append(basic.maleMosquito(aSwarmList[cRandSwarm],aPInMale,aPMoveMale))

        # Move the mosquito inside in relation to probability
        c_randInsideSwarm = random.random()
        if c_randInsideSwarm < aMaleMosquitoList[-1].getPIn():
            aMaleMosquitoList[-1].moveInside()

        cNumMaleMosquitoes-=1

    # Now sort females
    cNumFemaleMosquitoes = numFemaleMosquitoes
    cNumHouses = aArea.getNumHouses()
    vHouseSequence = range(0,cNumHouses)
    aHouseList = aArea.getHouseGroup().getTargetList()
    aFemaleMosquitoList = []

    # Put female mosquitoes in
    while cNumFemaleMosquitoes > 0:
        cRandHouse = random.choice(vHouseSequence)
        if cPInHeterogeneityIndicator == 0 and cPMoveHeterogeneityIndicator == 0:
            aPInFemale = cPInFemaleAll
            aPMoveFemale = cPMoveFemaleAll
        elif cPInHeterogeneityIndicator == 0:
            aPInFemale = cPInFemaleAll
            aPMoveFemale = random.betavariate(cPMoveFemaleBetaA,cPMoveFemaleBetaB)
        elif cPMoveHeterogeneityIndicator == 0:
            aPInFemale = random.betavariate(cPInFemaleBetaA,cPInFemaleBetaB)
            aPMoveFemale = cPMoveFemaleAll
        else:
            aPInFemale = random.betavariate(cPInFemaleBetaA,cPInFemaleBetaB)
            aPMoveFemale = random.betavariate(cPMoveFemaleBetaA,cPMoveFemaleBetaB)

        aFemaleMosquitoList.append(basic.femaleMosquito(aHouseList[cRandHouse],aPInFemale,aPMoveFemale))


        # Move the mosquito inside in relation to its probability PIn
        cRandInsideHouse= random.random()
        if cRandInsideHouse < aFemaleMosquitoList[-1].getPIn():
            aFemaleMosquitoList[-1].moveInside()

        cNumFemaleMosquitoes-=1

# A function which allows the mosquitoes to move around probabilistically
def evolveSystem(aArea,cDays,vReleaseParameters):

    cNumberMaleReleases = vReleaseParameters[0]
    cReleaseMaleStartTime = vReleaseParameters[1]
    cReleaseMaleTimeGap = vReleaseParameters[2]
    cReleaseMaleMosquitoNumber = vReleaseParameters[3]
    cNumberFemaleReleases = vReleaseParameters[4]
    cReleaseFemaleStartTime = vReleaseParameters[5]
    cReleaseFemaleTimeGap = vReleaseParameters[6]
    cReleaseFemaleMosquitoNumber = vReleaseParameters[7]
    vReleaseMaleTimes = releaseTimeGenerator(cNumberMaleReleases,cReleaseMaleStartTime,cReleaseMaleTimeGap)
    vReleaseFemaleTimes = releaseTimeGenerator(cNumberFemaleReleases,cReleaseFemaleStartTime,cReleaseFemaleTimeGap)

    cMaleReleaseIndexCounter = 0
    cFemaleReleaseIndexCounter = 0
    fig = plt.figure()
    for t in range(0,cDays):
        print(t)
        # print(aArea.getNumMosquitoes())
        print(sum(aArea.getNumListMarkedTotalFemales()))
        print(sum(aArea.getNumListMarkedTotalMales()))
        vMale = aArea.getMaleMosquitoList()
        vFemale = aArea.getFemaleMosquitoList()

        MoveAndInsideMosquitoes(vMale,aArea,1)
        MoveAndInsideMosquitoes(vFemale,aArea,0)

        vFemales = aArea.getNumListInsideFemales()
        vMales = aArea.getNumListInsideMales()

        cMaleReleaseIndexCounter += releaseMosquitoes(t,vReleaseMaleTimes,cMaleReleaseIndexCounter,cReleaseMaleMosquitoNumber,1,aArea)
        cFemaleReleaseIndexCounter += releaseMosquitoes(t,vReleaseFemaleTimes,cFemaleReleaseIndexCounter,cReleaseFemaleMosquitoNumber,0,aArea)

        vColourMales = aArea.getMarkedIndicatorMales()
        vColourFemales = aArea.getMarkedIndicatorFemales()

        ax1 = fig.add_subplot(211)
        ax1.scatter(aArea.getHouseLocations()[:,0],aArea.getHouseLocations()[:,1],s=5*vFemales,c=vColourFemales,label='houses')
        plt.legend(loc='upper left')
        ax1.hold(False)

        ax2 = fig.add_subplot(212)
        ax2.scatter(aArea.getSwarmLocations()[:,0],aArea.getSwarmLocations()[:,1],s=5*vMales,c=vColourMales,label = 'swarms',vmin=0,vmax = 1)
        ax2.hold(False)
        plt.legend(loc='upper left')
        plt.draw()


        fig.show()


def MoveAndInsideMosquitoes(vMosquitoList,aArea,cSex):
    k = 1
    cNumMoved = 0
    for mosquitoes in vMosquitoList:
        # Whether or not not move mosquito
        cMoveRand = random.random()
        if cMoveRand < mosquitoes.getPMove():
            moveMosquito(mosquitoes,aArea,cSex)
            cNumMoved += 1
        # Whether or not to move the mosquito inside
        cInRand = random.random()
        if cInRand < mosquitoes.getPIn():
            mosquitoes.moveInside()
        else:
            mosquitoes.moveOutside()
    return cNumMoved

def moveMosquito(mosquitoes,aArea,cSex):

    # Get a list of all relevant targets
    if cSex == 1:
        vTargetList = list(aArea.getSwarmList())
    else:
        vTargetList = list(aArea.getHouseList())

    # Remove the current target from this list
    vTargetList.remove(mosquitoes.getTarget())
    vMovePropensities = []
    aLocation = mosquitoes.getLocation()
    for targets in vTargetList:
        bLocation = targets.getLocation()
        vMovePropensities.append(1/squareDistance(aLocation,bLocation))

    # Normalise the propensities
    vMovePropensities = np.array(vMovePropensities)/sum(vMovePropensities)

    # Select a target at random
    targetSwitch = 0
    cNumTargets = len(vMovePropensities)
    while targetSwitch == 0:
        cTargetRandIndex = random.randint(0,cNumTargets-1)
        cTargetRand = random.random()

        if cTargetRand < vMovePropensities[cTargetRandIndex]:
            mosquitoes.move(vTargetList[cTargetRandIndex])
            targetSwitch = 1


def squareDistance(aLocation,bLocation):
    return (aLocation[0]-bLocation[0])**2 + (aLocation[1]-bLocation[1])**2

def releaseTimeGenerator(cNumReleases,cReleaseStartTime,cReleaseTimeGap):
    vReleaseTimes = []
    cReleaseTimeTemp = cReleaseStartTime
    for i in range(0,cNumReleases):
        vReleaseTimes.append(cReleaseTimeTemp)
        cReleaseTimeTemp += cReleaseTimeGap
    return vReleaseTimes

def releaseMosquitoes(t,vReleaseTimes,cReleaseIndexCounter,cReleaseMosquitoNumber,cSex,aArea):

    # If not a release time just return 0
    if t > vReleaseTimes[-1]:
        return 0
    if t != vReleaseTimes[cReleaseIndexCounter]:
        return 0

    if cSex == 1:
        vTargets = aArea.getSwarmList()
    else:
        vTargets = aArea.getHouseList()
    cLenTargets = len(vTargets)

    # Find a target that has a sufficient number of mosquitoes
    switchRelease = 0
    while switchRelease == 0:
        cRandTargetIndex = random.randint(0,cLenTargets-1)
        if vTargets[cRandTargetIndex].getNumUnmarkedInside() > cReleaseMosquitoNumber:
            vUnmarkedInsideMosquitoList = vTargets[cRandTargetIndex].getUnmarkedMosquitoInsideList()
            switchRelease = 1

    # Only want to release the correct number, no more
    vUnmarkedInsideMosquitoList = vUnmarkedInsideMosquitoList[0:cReleaseMosquitoNumber]
    for mosquitoes in vUnmarkedInsideMosquitoList:
        mosquitoes.mark()
    return 1