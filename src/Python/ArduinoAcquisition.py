#*-* coding: utf-8*-*
################################################################################
################################################################################
# Author : Alexandre Desilets-Benoit
# Name of module : ArduinoAcquisition
# Version : ???
# Description : module to connect to arduino and request values fro the 2 six 
#               axis sensors as fast as possible
################################################################################
################################################################################

import numpy as np
import serial as sr
import multiprocessing as mp
import platform as cpu
import sys
import time
import binascii
from dataStructure import *

PYTHON_VERSION = sys.version_info.major
if 'Ubuntu-16.04' in cpu.platform():
   isRPi = False
else:
   isRPi = True
   import RPi.GPIO as GPIO

class ArduinoFunc():
   def __init__(self,port,baudrate,delais,dataPointer):
      self.port = port
      self.baudrate = baudrate
      self.delais = delais
      self.Connection = False
      self.data = dataPointer
      self.PYTHON_VERSION = sys.version_info.major
      test = 0
      try:
         print("Trying to connect to %s"%self.port)
         self.arduino = sr.Serial(self.port,self.baudrate,timeout = 5,write_timeout=1)
         print("Connected to port %s"%self.port)
         self.Connection = True
         print("Emptying arduino cash")
         self.arduino.write(b'z')
         print('wait 5 seconds')
         time.sleep(5)
         print('done sleeping')
         test = self.arduino.readline()
         test = test.decode(encoding='UTF-8')
         test = test.replace('\n','').replace('\r','')
         while test != 'k':
            print('empty arduino cache')
            self.arduino.write(b'z')
            test = self.arduino.readline()
            test = test.decode(encoding='UTF-8')
            test = test.replace('\n','').replace('\r','')
         print("Emptied arduino cash\n")
      except:
         print("1 error in connecting to port %s"%self.port)
   def readBuffer(self):
      self.arduino.write(b'd')
      temp = self.arduino.readline()
      temp = temp.decode(encoding='UTF-8')
      temp = temp.replace('\n','').replace('\r','')
      self.data.AddData(temp)
   def readBinaryBuffer2(self):
      self.arduino.write(b'b')
      tempBin = []
      for i in range(24):
         tempBin.append(self.arduino.read()[0])
      tempOut = []
      for i in range(12):
         temp1 = binascii.b2a_hex(tempBin[2*i])
         temp2 = binascii.b2a_hex(tempBin[2*i+1])
         temp1 = format(int(temp1,16)*(2**8),'0>16b')
         temp2 = format(int(temp2,16),'0>16b')
         temp = int(str(int(temp1)+int(temp2)),2)
         tempOut.append(temp)
         if tempOut[i] >= 2**15:
            tempOut[i] = tempOut[i] - 2**16
      self.data.AddData(tempOut)
   def readBinaryBuffer3(self):
      self.arduino.write(b'b')
      tempBin = []
      for i in range(24):
         tempBin.append(self.arduino.read()[0])
      tempOut = []
      for i in range(12):
         tempOut.append((tempBin[2*i]<<8)+tempBin[2*i+1])
         if tempOut[i] >= 2**15:
            tempOut[i] = tempOut[i] - 2**16
      self.data.AddData(tempOut)
   def closeSerial(self):
      self.Connection = False
      self.arduino.close()

class AcquisitionProcess(mp.Process):
   def __init__(self,buf,size,nbr,runFlag,eventFlag,validEventFlag,CarFlag,RightFlag,LeftFlag,analysisFlag):
      mp.Process.__init__(self)
      self.data = dataStructure(buf,size,nbr,eventFlag,validEventFlag,analysisFlag)
      self.runFlag = runFlag
      self.eventFlag = eventFlag
      self.validEventFlag = validEventFlag
      self.CarFlag = CarFlag
      self.RightFlag = RightFlag
      self.LeftFlag = LeftFlag
      self.analysisFlag = analysisFlag
   def run(self):
      print('launched process for gathering data')
      # Connect arduino to CPU
      arduino = ArduinoFunc('/dev/ttyACM0',115200,0.005,self.data)
      if arduino.Connection:
         self.runFlag.value = True
         T0 = time.time()
         i = 1
         while self.runFlag.value:
            T1 = time.time()
            if i%10000 == 0:
               print('%4i time : %6.3f'%(i,((T1-T0)*1000)/i))
            if arduino.PYTHON_VERSION == 2:
               arduino.readBinaryBuffer2()
            elif arduino.PYTHON_VERSION == 3:
               arduino.readBinaryBuffer3()
            i+=1
         # Close connection at the end of script
         arduino.closeSerial()
         print("Arduino connection closed")
      else:
         print('Arduino never connected')
         self.runFlag.value = True
         i = 1
         time.sleep(5)

