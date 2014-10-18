from IBM_functions import basic
import matplotlib.pyplot as plt

a_loc = basic.location(2,1)
b_loc = basic.location(3,1)
a_house = basic.houseTarget(a_loc)
a_swarm = basic.swarmTarget(b_loc)
b_swarm = basic.swarmTarget(a_loc)

a_mosquito = basic.maleMosquito(a_swarm)
b_mosquito = basic.femaleMosquito(a_house)
c_mosquito = basic.maleMosquito(a_swarm)

print a_swarm.getMarkedInside()
a_mosquito.moveInside()
c_mosquito.moveInside()
a_swarm.getInsideMosquitoGroup().mark()
print a_swarm.getMarkedInside()


a_mosquito.move(b_swarm)
print b_swarm.getMarkedOutside()

a_area = basic.area(1500,100,100)
v_xh = []
v_yh = []
v_xs = []
v_ys = []

a_houseGroup = a_area.getHouseGroup()
a_houseList = a_houseGroup.getTargetList()
a_swarmGroup = a_area.getSwarmGroup()
a_swarmList = a_swarmGroup.getTargetList()
for i in range(0,100):
    v_xh.append(a_houseList[i].getLocation()[0])
    v_yh.append(a_houseList[i].getLocation()[1])
    v_xs.append(a_swarmList[i].getLocation()[0])
    v_ys.append(a_swarmList[i].getLocation()[1])

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(v_xh,v_yh,c='b',label='houses')
ax1.scatter(v_xs,v_ys,c='r',label = 'swarms')
plt.legend(loc='upper left');
plt.show()

