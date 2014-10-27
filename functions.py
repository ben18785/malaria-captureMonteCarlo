from IBM_functions import basic
import random as random
import numpy as np
import matplotlib.pyplot as plt

# A function which puts male and female mosquitoes at random swarms and houses respectively throughout the domain
def initialise(aArea,numMaleMosquitoes,numFemaleMosquitoes,vPInParameters,vPMoveParameters,cPDie):

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

        aMaleMosquitoList.append(basic.maleMosquito(aSwarmList[cRandSwarm],aPInMale,aPMoveMale,cPDie))

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

        aFemaleMosquitoList.append(basic.femaleMosquito(aHouseList[cRandHouse],aPInFemale,aPMoveFemale,cPDie))


        # Move the mosquito inside in relation to its probability PIn
        cRandInsideHouse= random.random()
        if cRandInsideHouse < aFemaleMosquitoList[-1].getPIn():
            aFemaleMosquitoList[-1].moveInside()

        cNumFemaleMosquitoes-=1

# A function which allows the mosquitoes to move around probabilistically
def evolveSystem(aArea,cDays,vReleaseParameters,vPInParameters,vPMoveParameters,aPDie,vSampleParameters):

    cNumberMaleReleases = vReleaseParameters[0]
    cReleaseMaleStartTime = vReleaseParameters[1]
    cReleaseMaleTimeGap = vReleaseParameters[2]
    cReleaseMaleMosquitoNumber = vReleaseParameters[3]
    cNumberFemaleReleases = vReleaseParameters[4]
    cReleaseFemaleStartTime = vReleaseParameters[5]
    cReleaseFemaleTimeGap = vReleaseParameters[6]
    cReleaseFemaleMosquitoNumber = vReleaseParameters[7]
    cIntroductionNew = vReleaseParameters[8]
    vReleaseMaleTimes = releaseTimeGenerator(cNumberMaleReleases,cReleaseMaleStartTime,cReleaseMaleTimeGap)
    vReleaseFemaleTimes = releaseTimeGenerator(cNumberFemaleReleases,cReleaseFemaleStartTime,cReleaseFemaleTimeGap)

    cMaleReleaseIndexCounter = 0
    cFemaleReleaseIndexCounter = 0
    fig = plt.figure()
    for t in range(0,cDays):
        print(t)
        # # print(aArea.getNumMosquitoes())
        # print(sum(aArea.getNumListMarkedTotalFemales()))

        vMale = aArea.getMaleMosquitoList()
        vFemale = aArea.getFemaleMosquitoList()

        MoveAndInsideMosquitoes(vMale,aArea,1,vPInParameters,vPMoveParameters,aPDie)
        MoveAndInsideMosquitoes(vFemale,aArea,0,vPInParameters,vPMoveParameters,aPDie)

        vFemales = aArea.getNumListInsideFemales()
        vMales = aArea.getNumListInsideMales()

        cMaleReleaseIndexCounter += releaseMosquitoes(t,vReleaseMaleTimes,cMaleReleaseIndexCounter,cReleaseMaleMosquitoNumber,1,aArea,cIntroductionNew,vPInParameters,vPMoveParameters,aPDie)
        cFemaleReleaseIndexCounter += releaseMosquitoes(t,vReleaseFemaleTimes,cFemaleReleaseIndexCounter,cReleaseFemaleMosquitoNumber,0,aArea,cIntroductionNew,vPInParameters,vPMoveParameters,aPDie)

        cSampleMaleTime = vSampleParameters[0]
        cSampleFemaleTime = vSampleParameters[1]
        if t == cSampleMaleTime:
            print("Sampling males")
            [cCountMarked,cCountUnmarked] = sampleTargets(aArea,1,vSampleParameters)
            print(cCountMarked,cCountUnmarked)
            print(lincolnEstimate(cCountMarked,cCountUnmarked,cReleaseMaleMosquitoNumber))
        if t == cSampleFemaleTime:
            print("Sampling females")
            [cCountMarked,cCountUnmarked] = sampleTargets(aArea,0,vSampleParameters)
            print(cCountMarked,cCountUnmarked)
            print(lincolnEstimate(cCountMarked,cCountUnmarked,cReleaseMaleMosquitoNumber))

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


def MoveAndInsideMosquitoes(vMosquitoList,aArea,cSex,vPInParameters,vPMoveParameters,aPDie):
    k = 1
    cNumMoved = 0
    for mosquitoes in vMosquitoList:

        # First see whether or not mosquito dies
        cRandDie = random.random()
        if cRandDie < mosquitoes.getPDie():
            mosquitoes.die(aArea,vPInParameters,vPMoveParameters,aPDie)

        else: # If not dead move
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

def releaseMosquitoes(t,vReleaseTimes,cReleaseIndexCounter,cReleaseMosquitoNumber,cSex,aArea,cIntroductionNew,vPInParameters,vPMoveParameters,aPDie):

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
    if cIntroductionNew == 0:
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

    else: # Just release that number of marked mosquitoes into a random target location
        cRandTargetIndex = random.randint(0,cLenTargets-1)
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

        for i in range(0,cReleaseMosquitoNumber):
            if cSex == 1:
                if cPInHeterogeneityIndicator == 0:
                    aPIn = cPInMaleAll
                else:
                    aPIn = random.betavariate(cPInMaleBetaA,cPInMaleBetaB)
                if cPMoveHeterogeneityIndicator == 0:
                    aPMove = cPMoveMaleAll
                else:
                    aPMove = random.betavariate(cPMoveMaleBetaA,cPMoveMaleBetaB)
                aMosquito = basic.maleMosquito(vTargets[cRandTargetIndex],aPIn,aPMove,aPDie)
                aMosquito.mark()
            else:
                if cPInHeterogeneityIndicator == 0:
                    aPIn = cPInFemaleAll
                else:
                    aPIn = random.betavariate(cPInFemaleBetaA,cPInFemaleBetaB)
                if cPMoveHeterogeneityIndicator == 0:
                    aPMove = cPMoveFemaleAll
                else:
                    aPMove = random.betavariate(cPMoveFemaleBetaA,cPMoveFemaleBetaB)
                aMosquito = basic.femaleMosquito(vTargets[cRandTargetIndex],aPIn,aPMove,aPDie)
                aMosquito.mark()

    return 1

def sampleTargets(aArea,cSex,vSampleParameters):

    if cSex == 0: # Females - assume we know the location of all houses
        vTargetsSampled = aArea.getHouseList()
    else:
        cKnownSwarmsPercentage = vSampleParameters[2]
        vTargets = aArea.getSwarmList()

        # Assume that only a random fraction of male swarms are known
        cNumSwarms = len(vTargets)
        vTargetsShuffled = random.sample(vTargets,cNumSwarms)
        cNumKnownSwarms = int(cKnownSwarmsPercentage*cNumSwarms)
        vTargetsKnown = vTargetsShuffled[0:cNumKnownSwarms]
        vTargetsSampled = vTargetsKnown

    cDailyNumTargetsSampled = vSampleParameters[3]
    vTargetsSampled = vTargetsSampled[0:cDailyNumTargetsSampled]

    cCountMarked = 0
    cCountUnmarked = 0
    for targets in vTargetsSampled:
        cCountMarked += targets.getNumMarkedInside()
        cCountUnmarked += targets.getNumUnmarkedInside()

    return [cCountMarked,cCountUnmarked]

def lincolnEstimate(cCountMarked,cCountUnmarked,cNumReleased):
    if cCountMarked == 0:
        print("No marked mosquitoes found")
        return -1

    cCountTotal = cCountMarked + cCountUnmarked
    return cNumReleased*(cCountTotal/cCountMarked)
