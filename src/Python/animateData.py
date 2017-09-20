#*-* coding: utf-8*-*
################################################################################
################################################################################
#Author : Alexandre Desilets-Benoit
#Name of module : animateData
#Version : ???
#Description : functions the feed in matplotlib.animate function
################################################################################
################################################################################

import numpy as np
import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import platform as cpu
import ctypes
import sys

from ArduinoAcquisition import *
from dataStructure import *


def plotAnimation(lengthOfArray,dataMainIn,runFlagIn,six1 = True,six2 = True,diff = True):
   global runFlag, dataMain
   global line0, line1, line2, line3, line4, line5, line6, line7, line8, line9
   global line10, line11, line12, line13, line14, line15, line16, line17, line18, line19
   global ax1, ax2
   runFlag = runFlagIn
   dataMain = dataMainIn
   #Insert ploting here
   fig = plt.figure('raw data as a function of time',facecolor='white',figsize=(9,6))
   ax1 = plt.subplot(1,2,1)
   ax1.set_title('acceleration')
   ax1.set_xlabel('index')
   ax1.set_ylabel('int16')
   ax1.set_ylim(-32000,32000)
   if six1:
      line0, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[0],'r.')
      line1, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[1],'b.')
      line2, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[2],'g.')
   if six2:
      line3, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[3],'rx')
      line4, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[4],'bx')
      line5, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[5],'gx')
   if diff:
      line6, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[6],'r')
      line7, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[7],'b')
      line8, = ax1.plot(np.arange(0,lengthOfArray),dataMain.acceleration[8],'g')
   line18, = ax1.plot(np.arange(0,lengthOfArray),dataMain.diffAcceleration,'k')
   ax2 = plt.subplot(1,2,2)
   ax2.set_title('rotation')
   ax2.set_xlabel('index')
   ax2.set_ylabel('int16')
   ax2.set_ylim(-5000,5000)
   if six1:
      line9, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[0],'r.')
      line10, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[1],'b.')
      line11, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[2],'g.')
   if six2:
      line12, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[3],'rx')
      line13, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[4],'bx')
      line14, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[5],'gx')
   if diff:
      line15, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[6],'r')
      line16, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[7],'b')
      line17, = ax2.plot(np.arange(0,lengthOfArray),dataMain.rotation[8],'g')
   line19, = ax2.plot(np.arange(0,lengthOfArray),dataMain.diffRotation,'k')
   if six1:
      ani1 = animation.FuncAnimation(fig, update1, data_gen1, interval=10)
      ani2 = animation.FuncAnimation(fig, update2, data_gen2, interval=10)
      ani3 = animation.FuncAnimation(fig, update3, data_gen3, interval=10)
      ani10 = animation.FuncAnimation(fig, update10, data_gen10, interval=10)
      ani11 = animation.FuncAnimation(fig, update11, data_gen11, interval=10)
      ani12 = animation.FuncAnimation(fig, update12, data_gen12, interval=10)
   if six2:
      ani4 = animation.FuncAnimation(fig, update4, data_gen4, interval=10)
      ani5 = animation.FuncAnimation(fig, update5, data_gen5, interval=10)
      ani6 = animation.FuncAnimation(fig, update6, data_gen6, interval=10)
      ani13 = animation.FuncAnimation(fig, update13, data_gen13, interval=10)
      ani14 = animation.FuncAnimation(fig, update14, data_gen14, interval=10)
      ani15 = animation.FuncAnimation(fig, update15, data_gen15, interval=10)
   if diff:
      ani7 = animation.FuncAnimation(fig, update7, data_gen7, interval=10)
      ani8 = animation.FuncAnimation(fig, update8, data_gen8, interval=10)
      ani9 = animation.FuncAnimation(fig, update9, data_gen9, interval=10)
      ani16 = animation.FuncAnimation(fig, update16, data_gen16, interval=10)
      ani17 = animation.FuncAnimation(fig, update17, data_gen17, interval=10)
      ani18 = animation.FuncAnimation(fig, update18, data_gen18, interval=10)
   ani19 = animation.FuncAnimation(fig, update19, data_gen19, interval=10)
   ani20 = animation.FuncAnimation(fig, update20, data_gen20, interval=10)
   plt.show()

def update1(data):
   global line0
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line0.set_ydata(data)
      #ax1.set_ylim(-32000,32000)
      return line0,
   else:
      return None
def update2(data):
   global line1
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line1.set_ydata(data)
      return line1,
   else:
      return None
def update3(data):
   global line2
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line2.set_ydata(data)
      return line2,
   else:
      return None
def update4(data):
   global line3
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line3.set_ydata(data)
      return line3,
   else:
      return None
def update5(data):
   global line4
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line4.set_ydata(data)
      return line4,
   else:
      return None
def update6(data):
   global line5
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line5.set_ydata(data)
      return line5,
   else:
      return None
def update7(data):
   global line6
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line6.set_ydata(data)
      return line6,
   else:
      return None
def update8(data):
   global line7
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line7.set_ydata(data)
      return line7,
   else:
      return None
def update9(data):
   global line8
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line8.set_ydata(data)
      return line8,
   else:
      return None
def update10(data):
   global line9
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line9.set_ydata(data)
      #ax2.set_ylim(-2000,2000)
      return line9,
   else:
      return None
def update11(data):
   global line10
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line10.set_ydata(data)
      return line10,
   else:
      return None
def update12(data):
   global line11
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line11.set_ydata(data)
      return line11,
   else:
      return None
def update13(data):
   global line12
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line12.set_ydata(data)
      return line12,
   else:
      return None
def update14(data):
   global line13
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line13.set_ydata(data)
      return line13,
   else:
      return None
def update15(data):
   global line14
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line14.set_ydata(data)
      return line14,
   else:
      return None
def update16(data):
   global line15
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line15.set_ydata(data)
      return line15,
   else:
      return None
def update17(data):
   global line16
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line16.set_ydata(data)
      return line16,
   else:
      return None
def update18(data):
   global line17
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line17.set_ydata(data)
      return line17,
   else:
      return None
def update19(data):
   global line18
   global ax1
   if (type(data) == np.ndarray) or data != None:
      line18.set_ydata(data)
      return line18,
   else:
      return None
def update20(data):
   global line19
   global ax2
   if (type(data) == np.ndarray) or data != None:
      line19.set_ydata(data)
      return line19,
   else:
      return None
################################################################################
def Get_data1():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[0,:]
   else:
      pass
def Get_data2():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[1,:]
   else:
      pass
def Get_data3():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[2,:]
   else:
      pass
def Get_data4():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[3,:]
   else:
      pass
def Get_data5():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[4,:]
   else:
      pass
def Get_data6():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[5,:]
   else:
      pass
def Get_data7():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[6,:]
   else:
      pass
def Get_data8():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[7,:]
   else:
      pass
def Get_data9():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.acceleration[8,:]
   else:
      pass
def Get_data10():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[0,:]
   else:
      pass
def Get_data11():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[1,:]
   else:
      pass
def Get_data12():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[2,:]
   else:
      pass
def Get_data13():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[3,:]
   else:
      pass
def Get_data14():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[4,:]
   else:
      pass
def Get_data15():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[5,:]
   else:
      pass
def Get_data16():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[6,:]
   else:
      pass
def Get_data17():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[7,:]
   else:
      pass
def Get_data18():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.rotation[8,:]
   else:
      pass
def Get_data19():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.diffAcceleration
   else:
      pass
def Get_data20():
   global dataMain
   global runFlag
   if runFlag.value != False:
      return dataMain.diffRotation
   else:
      pass
################################################################################
def data_gen1():
   while True: yield Get_data1()
def data_gen2():
   while True: yield Get_data2()
def data_gen3():
   while True: yield Get_data3()
def data_gen4():
   while True: yield Get_data4()
def data_gen5():
   while True: yield Get_data5()
def data_gen6():
   while True: yield Get_data6()
def data_gen7():
   while True: yield Get_data7()
def data_gen8():
   while True: yield Get_data8()
def data_gen9():
   while True: yield Get_data9()
def data_gen10():
   while True: yield Get_data10()
def data_gen11():
   while True: yield Get_data11()
def data_gen12():
   while True: yield Get_data12()
def data_gen13():
   while True: yield Get_data13()
def data_gen14():
   while True: yield Get_data14()
def data_gen15():
   while True: yield Get_data15()
def data_gen16():
   while True: yield Get_data16()
def data_gen17():
   while True: yield Get_data17()
def data_gen18():
   while True: yield Get_data18()
def data_gen19():
   while True: yield Get_data19()
def data_gen20():
   while True: yield Get_data20()

