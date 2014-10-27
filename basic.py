import random as random
import numpy as np


class groupMosquitoes:
    def __init__(self,a_target):
        self.mosquitoList = []
        self.target = a_target

    def getMosquitoesMark(self):
        c_len = len(self.mosquitoList)
        c_marked = 0
        for mos in self.mosquitoList:
            if mos.getMark():
                c_marked+=1
        c_unmarked = c_len-c_marked
        return [c_marked,c_unmarked]

    def getUnmarkedMosquitoesList(self):
        cLen = len(self.mosquitoList)
        vUnmarkedMosquitoList = []
        for mosquitoes in self.mosquitoList:
            if not mosquitoes.getMark():
                vUnmarkedMosquitoList.append(mosquitoes)
        return vUnmarkedMosquitoList

    def getMarkedMosquitoesList(self):
        cLen = len(self.mosquitoList)
        vMarkedMosquitoList = []
        for mosquitoes in self.mosquitoList:
            if mosquitoes.getMark():
                vMarkedMosquitoList.append(mosquitoes)
        return vMarkedMosquitoList

    def getNumberInGroup(self):
        return len(self.mosquitoList)

    def getGroupList(self):
        return self.mosquitoList

    def mark(self):
        for mos in self.mosquitoList:
            mos.mark()

    def addMosquito(self,a_mosquito):
        self.mosquitoList.append(a_mosquito)

    def removeMosquito(self,a_mosquito):
        self.mosquitoList.remove(a_mosquito)

class mosquito:
    def __init__(self,aTarget,asex,aPIn,aPMove,aPDie):
        self.target = aTarget
        self.sex = asex
        self.marked = False
        self.inside = 0
        self.PIn = aPIn
        self.pMove = aPMove
        self.pDie = aPDie
        aTarget.addOutsideMosquito(self)

    def getPDie(self):
        return self.pDie

    def getPIn(self):
        return self.PIn

    def getPMove(self):
        return self.pMove

    def getSex(self):
        return self.sex

    def getLocation(self):
        return self.target.getLocation()

    def getMark(self):
        return self.marked

    def getTarget(self):
        return self.target

    def getInside(self):
        return self.inside

    def move(self,new_target):
        if self.inside == 1:
            self.target.removeInsideMosquito(self)
        elif self.inside == 0:
            self.target.removeOutsideMosquito(self)
        self.target = new_target
        new_target.addOutsideMosquito(self)


    def mark(self):
        self.marked = True

    def moveInside(self):
        if self.inside == 0:
            self.target.addInsideMosquito(self)
            self.target.removeOutsideMosquito(self)
            self.inside = 1
        else:
            # Do not need to do anything since mosquito is already inside
            pass

    def moveOutside(self):
        if self.inside == 1:
            self.target.addOutsideMosquito(self)
            self.target.removeInsideMosquito(self)
            self.inside = 0
        else:
            pass

    def labelInside(self):
        self.inside = 1

    def labelOutside(self):
        self.inside = 0

    def die(self,aArea,vPInParameters,vPMoveParameters,aPDie):
        # Remove the mosquito from the target
        if self.inside == 1:
            self.target.removeInsideMosquito(self)
        else:
            self.target.removeOutsideMosquito(self)

        # Select a random target for the mosquito and create it
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

        if self.getSex()=="male":
            vTargets = aArea.getSwarmList()
            if cPInHeterogeneityIndicator == 0:
                aPIn = cPInMaleAll
            else:
                aPIn = random.betavariate(cPInMaleBetaA,cPInMaleBetaB)
            if cPMoveHeterogeneityIndicator == 0:
                aPMove = cPMoveMaleAll
            else:
                aPMove = random.betavariate(cPMoveMaleBetaA,cPMoveMaleBetaB)
        else:
            vTargets = aArea.getHouseList()
            if cPInHeterogeneityIndicator == 0:
                aPIn = cPInFemaleAll
            else:
                aPIn = random.betavariate(cPInFemaleBetaA,cPInFemaleBetaB)
            if cPMoveHeterogeneityIndicator == 0:
                aPMove = cPMoveFemaleAll
            else:
                aPMove = random.betavariate(cPMoveFemaleBetaA,cPMoveFemaleBetaB)

        CRandIndex = random.randint(0,len(vTargets)-1)
        aMosquito = mosquito(vTargets[CRandIndex],self.getSex(),aPIn,aPMove,aPDie)

        # Move new mosquito inside with probability
        cRandIn = random.random()
        if cRandIn < aPIn:
            aMosquito.moveInside()


class maleMosquito(mosquito):
    def __init__(self,a_swarmTarget,aPIn,aPMove,aPDie):
        mosquito.__init__(self,a_swarmTarget,"male",aPIn,aPMove,aPDie)

class femaleMosquito(mosquito):
    def __init__(self,a_houseTarget,aPIn,aPMove,aPDie):
        mosquito.__init__(self,a_houseTarget,"female",aPIn,aPMove,aPDie)

class location:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getLocation(self):
        return [self.x,self.y]

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class target:
    def __init__(self,a_location,type):
        self.location = a_location
        self.type = type
        self.insideMosquitoes = groupMosquitoes(self)
        self.outsideMosquitoes = groupMosquitoes(self)

    def getType(self):
        return self.type

    def getLocation(self):
        return self.location.getLocation()

    def getNumMarkedInside(self):
        return self.getMarkedInside()[0]

    def getMarkedInsideIndicator(self):
        if self.getNumMarkedInside() > 0:
            return 1
        else:
            return 0

    def getNumMarkedOutside(self):
        return self.getMarkedOutside()[0]

    def getNumMarkedTotal(self):
        return self.getNumMarkedInside() + self.getNumMarkedOutside()

    def getNumUnmarkedInside(self):
        return self.getMarkedInside()[1]

    def getUnmarkedMosquitoInsideList(self):
        return self.insideMosquitoes.getUnmarkedMosquitoesList()

    def getMarkedMosquitoInsideList(self):
        return self.insideMosquitoes.getMarkedMosquitoesList()

    def getMarkedInside(self):
        return self.insideMosquitoes.getMosquitoesMark()

    def getMarkedOutside(self):
        return self.outsideMosquitoes.getMosquitoesMark()

    def getNumberMosquitoes(self):
        totalMosquitoes = self.insideMosquitoes.getNumberInGroup() + self.outsideMosquitoes.getNumberInGroup()
        return totalMosquitoes

    def getNumberInside(self):
        return self.insideMosquitoes.getNumberInGroup()

    def getNumberOutside(self):
        return self.outsideMosquitoes.getNumberInGroup()

    def getInsideMosquitoGroup(self):
        return self.insideMosquitoes

    def getOutsideMosquitoGroup(self):
        return self.outsideMosquitoes

    def getMosquitoList(self):
        vMosquitoList = []
        vMosquitoList.append(self.getInsideMosquitoGroup().getGroupList())
        vMosquitoList.append(self.getOutsideMosquitoGroup().getGroupList())
        vMosquitoList = [item for sublist in vMosquitoList for item in sublist]
        return vMosquitoList


    def addInsideMosquitoes(self,a_group):
        c_len = a_group.getNumberInGroup()
        c_male = 0
        for mos in a_group.getGroupList():
            if mos.getSex() == "male":
                c_male +=1
        c_female = c_len - c_male
        if self.type == "house":
            if c_male > 0:
                print "Error: have tried to add a group comprising at least one male mosquito to a house"
            else:
                self.insideMosquitoes.append(a_group)
        elif self.type == "swarm":
            if c_female > 0:
                print "Error: have tried to add a group comprising at least one female mosquito to a swarm"
            else:
                self.insideMosquitoes.append(a_group)
        for mos in a_group.getGroupList():
            mos.labelInside()


    def addOutsideMosquitoes(self,a_group):
        c_len = a_group.getNumberInGroup()
        c_male = 0
        for mos in a_group.getGroupList():
            if mos.getSex() == "male":
                c_male +=1
        c_female = c_len - c_male
        if self.type == "house":
            if c_male > 0:
                print "Error: have tried to add a group comprising at least one male mosquito to a house"
            else:
                self.outsideMosquitoes.append(a_group)
        elif self.type == "swarm":
            if c_female > 0:
                print "Error: have tried to add a group comprising at least one female mosquito to a swarm"
            else:
                self.outsideMosquitoes.append(a_group)
        for mos in a_group.getGroupList():
            mos.labelOutside()


    def addInsideMosquito(self,a_mosquito):
        if self.type == "house":
            if a_mosquito.getSex() == "female":
                self.insideMosquitoes.addMosquito(a_mosquito)
                a_mosquito.labelInside()
            else:
                print "Error: A male mosquito have tried to add a male mosquito to a house!"
        elif self.type == "swarm":
            if a_mosquito.getSex() == "male":
                self.insideMosquitoes.addMosquito(a_mosquito)
                a_mosquito.labelInside()
            else:
                print "Error: A female mosquito have tried to add a male mosquito to a swarm!"

    def addOutsideMosquito(self,a_mosquito):
        if self.type == "house":
            if a_mosquito.getSex() == "female":
                self.outsideMosquitoes.addMosquito(a_mosquito)
                a_mosquito.labelOutside()
            else:
                print "Error: A male mosquito have tried to add a male mosquito to a house!"
        elif self.type == "swarm":
            if a_mosquito.getSex() == "male":
                self.outsideMosquitoes.addMosquito(a_mosquito)
                a_mosquito.labelOutside()
            else:
                print "Error: A female mosquito have tried to add a male mosquito to a swarm!"

    def removeInsideMosquito(self,a_mosquito):
        self.insideMosquitoes.removeMosquito(a_mosquito)

    def removeOutsideMosquito(self,a_mosquito):
        self.outsideMosquitoes.removeMosquito(a_mosquito)

class houseTarget(target):
    def __init__(self,a_location):
        target.__init__(self,a_location,"house")

class swarmTarget(target):
    def __init__(self,a_location):
        target.__init__(self,a_location,"swarm")

class releaseTarget(target):
    def __init__(self,a_location):
        target.__init__(self,a_location,"releasePoint")

class groupTarget:
    def __init__(self):
        self.targetList = []

    def getTargetList(self):
        return self.targetList

    def getNumTarget(self):
        return len(self.targetList)

    def getMosquitoList(self):
        vTargets = self.targetList
        vMosquitoList = []
        for targets in vTargets:
            vMosquitoList.append(targets.getMosquitoList())
        vMosquitoList = [item for sublist in vMosquitoList for item in sublist]
        return vMosquitoList


    def getLocation(self):
        l_location = []
        for item in self.targetList:
            l_location.append(item.getLocation())
        return l_location

    def getNumListMosquitoes(self):
        lMos = []
        for targets in self.targetList:
            lMos.append(targets.getNumberMosquitoes())
        return np.array(lMos)

    def getNumListMarkedInsideMosquitoes(self):
        lMos = []
        for targets in self.targetList:
            lMos.append(targets.getNumMarkedInside())
        return np.array(lMos)

    def getListMarkedInsideIndicator(self):
        lMos = []
        for targets in self.targetList:
            lMos.append(targets.getMarkedInsideIndicator())
        return np.array(lMos)

    def getNumListMarkedTotalMosquitoes(self):
        lMos = []
        for targets in self.targetList:
            lMos.append(targets.getNumMarkedTotal())
        return np.array(lMos)

    def getNumListInsideMosquitoes(self):
        lMos = []
        for targets in self.targetList:
            lMos.append(targets.getNumberInside())
        return np.array(lMos)

    def addTarget(self,a_target):
        self.targetList.append(a_target)

    def removeTarget(self,a_target):
        self.targetList.remove(a_target)

class area:
    def __init__(self,U,numHouses,numSwarms,vCovarianceParameters):

        self.houseGroup = groupTarget()
        self.swarmGroup = groupTarget()
        cCovarianceIndicator = vCovarianceParameters[0]

        if cCovarianceIndicator == 0:
            for i in range(0,numHouses):
                rand_x = U*random.random()
                rand_y = U*random.random()
                loc_a = location(rand_x,rand_y)
                self.houseGroup.addTarget(houseTarget(loc_a))
            for i in range(0,numSwarms):
                rand_x = U*random.random()
                rand_y = U*random.random()
                loc_a = location(rand_x,rand_y)
                self.swarmGroup.addTarget(swarmTarget(loc_a))
        else:
            cNumDisturbances = vCovarianceParameters[1]
            cSwarmsPerDisturbance = vCovarianceParameters[2]
            cHousesPerDisturbance = vCovarianceParameters[3]
            aGroupDisturbance = groupDisturbances()
            for i in range(0,cNumDisturbances):
                aDisturbance = disturbance(U)
                for j in range(0,cSwarmsPerDisturbance):
                    aDisturbance.addSwarm(U,vCovarianceParameters)
                for j in range(0,cHousesPerDisturbance):
                    aDisturbance.addHouse(U,vCovarianceParameters)
                aGroupDisturbance.addDisturbance(aDisturbance)
            self.swarmGroup = aGroupDisturbance.getGroupSwarms()
            self.houseGroup = aGroupDisturbance.getGroupHouses()

        self.numHouses = self.houseGroup.getNumTarget()
        self.numSwarms = self.swarmGroup.getNumTarget()



    def getHouseGroup(self):
        return self.houseGroup

    def getHouseList(self):
        return self.houseGroup.getTargetList()

    def getSwarmList(self):
        return self.swarmGroup.getTargetList()

    def getFemaleMosquitoList(self):
        aHouseGroup = self.houseGroup
        vMosquitoList = aHouseGroup.getMosquitoList()
        return vMosquitoList

    def getMaleMosquitoList(self):
        aSwarmGroup = self.swarmGroup
        vMosquitoList = aSwarmGroup.getMosquitoList()
        return vMosquitoList

    def getSwarmGroup(self):
        return self.swarmGroup

    def getHouseLocations(self):
        return np.array(self.houseGroup.getLocation())

    def getSwarmLocations(self):
        return np.array(self.swarmGroup.getLocation())

    def getNumHouses(self):
        return self.numHouses

    def getNumSwarms(self):
        return self.numSwarms

    def getNumMales(self):
        c_maleCount = 0
        for swarms in self.swarmGroup.getTargetList():
            c_maleCount += swarms.getNumberMosquitoes()

        return c_maleCount

    def getNumFemales(self):
        c_femaleCount = 0
        for houses in self.houseGroup.getTargetList():
            c_femaleCount += houses.getNumberMosquitoes()

        return c_femaleCount

    def getNumMosquitoes(self):
        c_total = self.getNumMales()+self.getNumFemales()
        return c_total

    def getNumMalesInside(self):
        c_maleInsideCount = 0
        for swarms in self.swarmGroup.getTargetList():
            c_maleInsideCount += swarms.getNumberInside()

        return c_maleInsideCount

    def getNumFemalesInside(self):
        c_femaleInsideCount = 0
        for houses in self.houseGroup.getTargetList():
            c_femaleInsideCount += houses.getNumberInside()

        return c_femaleInsideCount

    def getNumMalesOutside(self):
        c_MalesOutsideCount = self.getNumMales()-self.getNumMalesInside()
        return c_MalesOutsideCount

    def getNumFemalesOutside(self):
        c_femalesOutsideCount = self.getNumFemales()-self.getNumFemalesInside()
        return c_femalesOutsideCount

    def getNumListMales(self):
        return self.swarmGroup.getNumListMosquitoes()

    def getNumListMarkedInsideMales(self):
        return self.swarmGroup.getNumListMarkedInsideMosquitoes()

    def getNumListMarkedInsideFemales(self):
        return self.houseGroup.getNumListMarkedInsideMosquitoes()

    def getNumListMarkedTotalMales(self):
        return self.swarmGroup.getNumListMarkedTotalMosquitoes()

    def getNumListMarkedTotalFemales(self):
        return self.houseGroup.getNumListMarkedTotalMosquitoes()

    def getNumMarkedFemalesTotal(self):
        return sum(self.getNumListMarkedTotalFemales())

    def getNumMarkedMosquitoesTotal(self):
        return self.getNumListMarkedTotalMales() + self.getNumMarkedFemalesTotal()

    # Returns a vector of indicator variables, where 1 indicates the presence of a marked individual inside that target
    def getMarkedIndicatorMales(self):
        return self.swarmGroup.getListMarkedInsideIndicator()

    # Returns a vector of indicator variables, where 1 indicates the presence of a marked individual inside that target
    def getMarkedIndicatorFemales(self):
        return self.houseGroup.getListMarkedInsideIndicator()

    def getNumListInsideMales(self):
        return self.swarmGroup.getNumListInsideMosquitoes()

    def getNumListFemales(self):
        return self.houseGroup.getNumListMosquitoes()

    def getNumListInsideFemales(self):
        return self.houseGroup.getNumListInsideMosquitoes()

class disturbance:
    def __init__(self,aSize):
        cRandX = aSize*random.random()
        cRandY = aSize*random.random()
        self.location = location(cRandX,cRandY)
        self.houses = []
        self.swarms = []
        self.x = self.location.getX()
        self.y = self.location.getY()

    def addSwarm(self,aSize,vCovarianceParameters):
        cSigmaKernelSwarms = vCovarianceParameters[4]
        aXIncrement = random.normalvariate(0,cSigmaKernelSwarms)
        aYIncrement = random.normalvariate(0,cSigmaKernelSwarms)
        cRandX = self.x + aXIncrement
        cRandY = self.y + aYIncrement

        # Make sure not outside box
        if cRandX > aSize:
            cRandX = aSize - (cRandX - aSize)
        elif cRandX < 0:
            cRandX = -cRandX
        if cRandY > aSize:
            cRandY = aSize - (cRandY - aSize)
        elif cRandY < 0:
            cRandY = -cRandY

        aLocation = location(cRandX,cRandY)
        aSwarm = swarmTarget(aLocation)
        self.swarms.append(aSwarm)

    def addHouse(self,aSize,vCovarianceParameters):
        cSigmaKernelHouses = vCovarianceParameters[5]
        aXIncrement = random.normalvariate(0,cSigmaKernelHouses)
        aYIncrement = random.normalvariate(0,cSigmaKernelHouses)
        cRandX = self.x + aXIncrement
        cRandY = self.y + aYIncrement

        # Make sure not outside box
        if cRandX > aSize:
            cRandX = aSize - (cRandX - aSize)
        elif cRandX < 0:
            cRandX = -cRandX
        if cRandY > aSize:
            cRandY = aSize - (cRandY - aSize)
        elif cRandY < 0:
            cRandY = -cRandY

        aLocation = location(cRandX,cRandY)
        aHouse = houseTarget(aLocation)
        self.houses.append(aHouse)

    def getVSwarms(self):
        return self.swarms

    def getVHouses(self):
        return self.houses

    def getSwarmGroup(self):
        aSwarmGroupTarget = groupTarget()
        for swarms in self.swarms:
            aSwarmGroupTarget.addTarget(swarms)
        return aSwarmGroupTarget

    def getHouseGroup(self):
        aHouseGroupTarget = groupTarget()
        for houses in self.houses:
            aHouseGroupTarget.addTarget(houses)
        return aHouseGroupTarget

class groupDisturbances:
    def __init__(self):
        self.vDisturbances = []

    def addDisturbance(self,aDisturbance):
        self.vDisturbances.append(aDisturbance)

    def getVSwarms(self):
        vSwarms = []
        for disturbances in self.vDisturbances:
            vSwarms.append(disturbances.getVSwarms())
        vSwarms = [item for sublist in vSwarms for item in sublist]
        return vSwarms

    def getVHouses(self):
        vHouses = []
        for disturbances in self.vDisturbances:
            vHouses.append(disturbances.getVHouses())
        vHouses = [item for sublist in vHouses for item in sublist]
        return vHouses

    def getGroupSwarms(self):
        vSwarms = self.getVSwarms()
        aGroupSwarms = groupTarget()
        for swarms in vSwarms:
            aGroupSwarms.addTarget(swarms)
        return aGroupSwarms

    def getGroupHouses(self):
        vHouses = self.getVHouses()
        aGroupHouses = groupTarget()
        for houses in vHouses:
            aGroupHouses.addTarget(houses)
        return aGroupHouses