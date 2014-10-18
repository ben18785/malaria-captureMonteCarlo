from IBM_functions import basic
import matplotlib.pyplot as plt
from IBM_functions import functions


a_area = basic.area(1500,100,100)
functions.initialise(a_area,1000,0.4,1000,0.6)
v_females = a_area.getNumListFemales()
v_males = a_area.getNumListMales()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(a_area.getHouseLocations()[:,0],a_area.getHouseLocations()[:,1],s=5*v_females,c='b',label='houses')
ax1.scatter(a_area.getSwarmLocations()[:,0],a_area.getSwarmLocations()[:,1],s=5*v_males,c='r',label = 'swarms')
plt.legend(loc='upper left')
plt.show()






