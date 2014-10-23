from IBM_functions import basic
import random as random

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
def evolveSystem(aArea):

    # Work with males


    # Work with females
    vFemale = aArea.getFemaleMosquitoList()
    for females in vFemale:
        pass



