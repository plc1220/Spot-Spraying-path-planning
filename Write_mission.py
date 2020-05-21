import pandas as pd
from math import sqrt

def waypoint (gps_points,instanceName):

    # Get user input
    print('Get home location')
    lat = input("Enter Latitude: ")
    long = input("Enter Longitude: ")
    alt = input("Enter Alt:")
    print ('\nGet Mission Parameters')
    hgt = input("Enter Mission Height:")
    spraytime = input('Enter Spray Time:')
    flow = input('Enter flow rate (%): ')

    flow1 = 1100 + (int(flow)*8)

    # Further process dataframe
    first = gps_points["x"][0],gps_points["y"][0]
    last = gps_points["x"].iloc[-1],gps_points["y"].iloc[-1]
    print (first)
    print (last)

    distance1 = sqrt((first[0]-float(lat))**2+(first[1]-float(long))**2)
    distance2 = sqrt((last[0]-float(lat))**2+(last[1]-float(long))**2)

    print(distance2)
    print(distance1)
    print(gps_points)
    
    if distance2 < distance1:
        gps_points = gps_points.iloc[::-1]
    print(gps_points)
    lat_list = gps_points["x"].tolist()
    lon_list = gps_points["y"].tolist()
    alt_list = gps_points["z"].tolist()
    
    # Function to write mission file with cooordinates

    def mission_writing():
        x = 3*i+1
        y = 3*i+2
        z = 3*i+3
        file.write ('\n'+str(x)+'\t0\t3\t16\t1\t0\t0\t0\t'+str(lat_list[i])+'\t'+str(lon_list[i])+'\t'+str((alt_list[i]-float(alt))+int(hgt))+'\t1\n'#
                    +str(y)+'\t0\t10\t184\t9\t'+str(int(flow1))+'\t1\t'#
                    +str((int(spraytime)*2))+'\t0\t0\t0\t1')
        file.write ('\n'+str(z)+'\t0\t10\t93\t'+str(spraytime)+'\t0\t0\t0\t0\t0\t0\t1')

    # Write
    file = open("dataset/%s/%s_mission.txt"%(instanceName,instanceName),"w")
    file.write ('QGC WPL 110\n0	1	0	16	0	0	0	0\t'+str(lat)+'\t'+str(long)+'\t'+str(alt)+'\t1')

    nrows = len(gps_points)

    for i in range(nrows):
        mission_writing()
    print('Mission written as dataset/%s/%s_mission.txt'%(instanceName,instanceName))
    file.close()

    return spraytime, flow
    
if __name__ == '__main__':
    
    Name = input("\nEnter the coordinates file you would like to generate mission from: ")
    dirName = "dataset/%s/%s.csv" % (Name, Name)
    gps_points = pd.read_csv(dirName, sep=",", usecols =["no","x","y","z"])
    print(gps_points)
    
    lat_list = gps_points["x"].tolist()
    lon_list = gps_points["y"].tolist()
    alt_list = gps_points["z"].tolist()
    
    waypoint(gps_points,Name)


