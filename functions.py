from IBM_functions import basic
import random as random

# A function which puts male and female mosquitoes at random swarms and houses respectively throughout the domain
def initialise(a_area,numMaleMosquitoes,pMaleInsideSwarm,numFemaleMosquitoes,pFemaleInsideSwarm):

    # First sort males
    c_numMaleMosquitoes = numMaleMosquitoes
    c_numSwarms= a_area.getNumSwarms()
    v_swarmSequence = range(0,c_numSwarms)
    a_swarmList = a_area.getSwarmGroup().getTargetList()
    a_maleMosquitoList = []

   # Put male mosquitoes in
    while c_numMaleMosquitoes > 0:
        c_randSwarm = random.choice(v_swarmSequence)
        a_maleMosquitoList.append(basic.maleMosquito(a_swarmList[c_randSwarm]))

        # Move the mosquito inside in relation to probability
        c_randInsideSwarm = random.random()
        if c_randInsideSwarm < pMaleInsideSwarm:
            a_maleMosquitoList[-1].moveInside()

        c_numMaleMosquitoes-=1

    # Now sort females
    c_numFemaleMosquitoes = numFemaleMosquitoes
    c_numHouses = a_area.getNumHouses()
    v_houseSequence = range(0,c_numHouses)
    a_houseList = a_area.getHouseGroup().getTargetList()
    a_femaleMosquitoList = []

    # Put female mosquitoes in
    while c_numFemaleMosquitoes > 0:
        c_randSwarm = random.choice(v_houseSequence)
        a_femaleMosquitoList.append(basic.femaleMosquito(a_houseList[c_randSwarm]))

        # Move the mosquito inside in relation to probability
        c_randInsideSwarm = random.random()
        if c_randInsideSwarm < pFemaleInsideSwarm:
            a_femaleMosquitoList[-1].moveInside()

        c_numFemaleMosquitoes-=1




