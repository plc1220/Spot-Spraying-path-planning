import math
from statistics import mean
def distance_calculator(latlist, lonlist):
    distance = []
    for i in range(len(latlist)-1):
        dlat = latlist[i+1] - latlist[i]
        dlong = lonlist[i+1] - lonlist[i]
        d= math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5
        distance.append(d)

    total_distance = round(sum(distance),2)
    mean_distance = round(mean(distance),2)
    return total_distance, mean_distance, distance

def time_calculator(distance,a,vf,sp):
    time = []
    for i in range(len(distance)):
        t1 = vf/a
        s1 = 0.5*a*(t1**2)
        t2 = (distance[i]-s1)/vf
        t = (t1+t2+float(sp))*(1.1)
        time.append(t)

    total_time = math.ceil(sum(time)/60)
    average_time = round(mean(time),2)
    return total_time, average_time, time

def weight_calculator(Wi,number,spray):
    weight=[]
    for i in range(len(number)):
        w = 20+(Wi)-(i*spray/1000)
        weight.append(w)
    return weight,w-20,round((Wi-(w-20)),2)
if __name__ == '__main__':
    from ReadCSV import read

    clist = read()[0]
    xlist = []
    ylist = []
    for i in range(len(clist)):
        x = clist[i][1]
        y = clist[i][2]
        xlist.append(x)
        ylist.append(y)

    d_data = distance_calculator(xlist,ylist)
    print("Total distance:"+str(d_data[0])+' m'+"\nAverage distance:"+#
          str(d_data[1])+' m')

    t_data = time_calculator(d_data[2],1,3,2)
    print( "Total time taken:"+str(t_data[0])+' min'+"\nAverage Time:"+#
           str(t_data[1])+' s')
    w_data = weight_calculator(10,clist,150)
    print("Recommend pesticide for this flight:"+str(w_data[2])+' litre')

