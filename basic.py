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

class area:
    def __init__(self,U,numHouses,numSwarms):
        for i in range(0,numHouses):
            pass