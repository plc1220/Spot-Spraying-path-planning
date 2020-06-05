import matplotlib.cm as cmx
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d

def scatter3d(x,y,z, cs, colorsMap='jet'):
    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection='3d')
    ax1.plot3D(x,y,z,'--g')
    X = [x[0],x[-1]]
    Y = [y[0],y[-1]]
    Z = [z[0],z[-1]]
    ax1.scatter3D(X,Y,Z, s = 60, c='r',marker='s',cmap='magma')
    ax1.scatter3D(x,y,z,c=z,cmap='hsv')
    plt.show()

if __name__ == '__main__':
    
    Name = input("\nEnter the coordinates file you would like to generate mission from: ")
    dirName = "dataset/%s/%s.csv" % (Name, Name)
    gps_points = pd.read_csv(dirName, sep=",", usecols =["no","x","y","z"])
    
    y = gps_points["y"].tolist()
    x = gps_points["x"].tolist()
    z = gps_points["z"].tolist()
    
    scatter3d(x,y,z,[0.0,1.0])