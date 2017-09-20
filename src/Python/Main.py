#*-* coding: utf-8*-*
################################################################################
################################################################################
# Author : Alexandre Desilets-Benoit
# Name of module : Main.py
# Version : ???
# Description : Main script to gather data from arduino with 2 six axis sensors
#               and display it on the screen real-time
################################################################################
################################################################################

import numpy as np
import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import subprocess
import threading
import time
import serial as sr
import multiprocessing as mp
import platform as cpu
import ctypes
import sys
import binascii
from sklearn import svm

from CarApp import *
from ArduinoAcquisition import *
from dataStructure import *
from animateData import *
from kivyProcess import *
from keyboardInput import *

#OUTPUT_METHOD = 'KIVY'
OUTPUT_METHOD = 'MPL'
PYTHON_VERSION = sys.version_info.major
OS_PLATFORM = cpu.platform()

if 'Ubuntu-16.04' in OS_PLATFORM:
   isRPi = False
else:
   import RPi.GPIO as GPIO
   isRPi = True

if __name__ == "__main__":
   lengthOfArray = 32
   size = 20
   dataMP = mp.Array(ctypes.c_long,[0 for i in range(lengthOfArray*size)])
   runFlag = mp.Value(ctypes.c_bool,False)
   eventFlag = mp.Value(ctypes.c_bool,False)
   validEventFlag = mp.Value(ctypes.c_bool,False)
   analysisFlag = mp.Value(ctypes.c_bool,False)
   eventID = mp.Value(ctypes.c_int,0)
   CarFlag = mp.Value(ctypes.c_bool,False)
   LeftFlag = mp.Value(ctypes.c_bool,False)
   RightFlag = mp.Value(ctypes.c_bool,False)
   newEvent = mp.Value(ctypes.c_bool,False)

   dataMain = dataStructure(dataMP,lengthOfArray,size,eventFlag,validEventFlag,analysisFlag)
   
   processLock = mp.Lock()
   process = []
   if OUTPUT_METHOD == 'KIVY':
      process.append(UIProcess(dataMP,lengthOfArray,size,runFlag,eventFlag,validEventFlag,eventID,CarFlag,RightFlag,LeftFlag,analysisFlag,newEvent))
   else:
      process.append(UIProcessPassive(runFlag,newEvent))
   process.append(AcquisitionProcess(dataMP,lengthOfArray,size,runFlag,eventFlag,validEventFlag,CarFlag,RightFlag,LeftFlag,analysisFlag))
   for p in process:
      p.start()

   time.sleep(5)
   threadFlag = threading.Thread(target = Flaging,args = (runFlag,))
   threadFlag.daemon = True
   threadFlag.start()
   
   if OUTPUT_METHOD == 'KIVY':
      print('KIVY')
   elif OUTPUT_METHOD == 'MPL':
      plotAnimation(lengthOfArray,dataMain,runFlag,six1 = False,six2 = False,diff = False)
   
   for p in process:
      p.join()
   threadFlag.join()

