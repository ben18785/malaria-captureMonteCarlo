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
    def __init__(self,a_target,sex):
        self.target = a_target
        self.sex = sex
        self.marked = False
        self.inside = 0
        a_target.addOutsideMosquito(self)

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
            print "Error: have tried to move a mosquito that is not outside to the inside"

    def moveOutside(self):
        if self.inside == 1:
            self.target.addOutsideMosquito(self)
            self.target.removeInsideMosquito(self)
            self.inside = 0
        else:
            print "Error: have tried to move a mosquito that is not inside to the outside"

    def labelInside(self):
        self.inside = 1

    def labelOutside(self):
        self.inside = 0

class maleMosquito(mosquito):
    def __init__(self,a_swarmTarget):
        mosquito.__init__(self,a_swarmTarget,"male")

class femaleMosquito(mosquito):
    def __init__(self,a_houseTarget):
        mosquito.__init__(self,a_houseTarget,"female")

class location:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getLocation(self):
        return [self.x,self.y]

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

    def getLocation(self):
        l_location = []
        for item in self.targetList:
            l_location.append(item.getLocation())
        return l_location

    def getNumListMosquitoes(self):
        l_mos = []
        for targets in self.targetList:
            l_mos.append(targets.getNumberMosquitoes())
        return np.array(l_mos)

    def addTarget(self,a_target):
        self.targetList.append(a_target)

    def removeTarget(self,a_target):
        self.targetList.remove(a_target)



class area:
    def __init__(self,U,numHouses,numSwarms):
        self.numHouses = numHouses
        self.numSwarms = numSwarms
        self.houseGroup = groupTarget()
        self.swarmGroup = groupTarget()
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


    def getHouseGroup(self):
        return self.houseGroup

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

    def getNumListFemales(self):
        return self.houseGroup.getNumListMosquitoes()

