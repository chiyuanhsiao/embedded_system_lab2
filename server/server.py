import socket
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading

HOST = '192.168.187.193'# IP address
PORT = 8787 # Port to listen on (use ports > 1023)

LAST = 10 # show last LAST data
t = []
humi = []
pres = []
temp = []
gyro = [[] for i in range(3)]
acc = [[] for i in range(3)]
mag = [[] for i in range(3)]
color = [['r', 'g', 'b']]
dimension = ['X', 'Y', 'Z']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print("Starting server at: ", (HOST, PORT))
conn, addr = s.accept()

plt.ion()
fig = plt.figure(figsize = (10, 15))
ax = fig.subplots(4, 3)
while True:
    data = conn.recv(1024).decode('utf-8')
    print("Received from socket server:", data)
    try:
        obj = json.loads(data)

    except:
        print("warning: fail to load json")
    print(obj)

    t.append(obj["SAMPLE_NUM"])
    humi.append(obj["HUMIDITY"])
    temp.append(float(obj["TEMPERATURE"]))
    pres.append(float(obj["PRESSURE"]))
    t = t[-LAST:]
    humi = humi[-LAST:]
    temp = temp[-LAST:]
    pres = pres[-LAST:]
    for i in range(0, 3):
        gyro[i].append(float(obj['GYRO_XYZ'][i]))
        gyro[i] = gyro[i][-LAST:]
    for i in range(0, 3):
        mag[i].append(float(obj['MAGNETO_XYZ'][i]))
        mag[i] = mag[i][-LAST:]
    for i in range(0, 3):
        acc[i].append(float(obj['ACCELERO_XYZ'][i]))
        acc[i] = acc[i][-LAST:]
        

    
    print(humi)
    print(pres)
    print(temp)
    #ax.clear()
    for i in range (0, 4):
        for j in range (0, 3):
            ax[i,j].clear()
    for i in range (0, 3):
        ax[0,i].plot(t, list(gyro[i]), color[0][i] + '-o', label = 'GYRO' +
                     dimension[i])
        ax[0,i].set_title("Gyro " + dimension[i])
    for i in range (0, 3):
        ax[1,i].plot(t, list(mag[i]), color[0][i] + '--+')
        ax[1,i].set_title("Magneto " + dimension[i])
    for i in range (0, 3):
        ax[2,i].plot(t, list(acc[i]), color[0][i] + ':x')
        ax[2,i].set_title("Accelero " + dimension[i])

    ax[3,0].plot(t, humi, 'co-') 
    ax[3,0].set_title("Humidity")
    ax[3,0].set(xlabel = "Sample number", ylabel =  "%")
    ax[3,1].plot(t, temp, 'ko-')
    ax[3,1].set_title("Temperature")
    ax[3,1].set(xlabel = "Sample number", ylabel =  "degC")
    ax[3,2].plot(t, pres, 'mo-')
    ax[3,2].set_title("Pressure")
    ax[3,2].set(xlabel = "Sample number", ylabel = "mBar")
    plt.show()
    plt.tight_layout()
    plt.pause(0.001)
def GetDataAndPlot():
    plt.ion()
    fig, ax = plt.subplots()
    while True:
        data = conn.recv(1024).decode('utf-8')
        print("Received from socket server:", data)
        try:
            obj = json.loads(data)

        except:
            print("warning: fail to load json")
        print(obj)
        t.append(obj["SAMPLE_NUM"])
        gx.append(obj['GYRO_XYZ'][0])
        gy.append(obj['GYRO_XYZ'][1])
        gx = gx[-60:]
        gy = gy[-60:]
        t = t[-60:]
        
        #ax.clear()
        ax.plot(t, gx, 'r', label="GTRO_X")
        plt.title('GYRO data')
        plt.ylabel('Temperature (deg C)')
        plt.show()


def animate(i, t, gx, gy):
    print("animate")
    ax.clear()
    ax.plot(t, gx, 'r', label="GTRO_X")
    plt.title('GYRO data')
    plt.ylabel('Temperature (deg C)')
    plt.pause(0.0001)
    print("plot")
    print(gx, gy)


