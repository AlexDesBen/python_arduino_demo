#*-* coding: utf-8*-*
################################################################################
################################################################################
# Author : Alexandre Desilets-Benoit
# Name of module : dataStructure
# Version : ???
# Description : object to transform c-type buffer to a numpy array in each 
#               process
################################################################################
################################################################################

import numpy as np

class dataStructure():
   def __init__(self,buf,size,nbr,eventFlag,validEventFlag,analysisFlag):
      self.i = 0
      self.lengthOfArray = size
      self.data = np.frombuffer(buf.get_obj())
      self.data = self.data.reshape(nbr,size)
      self.acceleration = self.data[0:10]
      self.rotation = self.data[10:20]
      self.diffAcceleration = self.data[9]
      self.diffRotation = self.data[19]
      self.eventFlag = eventFlag
      self.validEventFlag = validEventFlag
      self.analysisFlag = analysisFlag
      self.counter = 0
      self.sign = 0
   def AddData(self,dataString):
      self.i+=1
      if type(dataString) == str:
         data = dataString.replace('\n','').replace('\r','')
         data = data.split(',')
      else:
         data = dataString
      tempacc = np.array([data[0],data[1],data[2],
         data[6],data[7],data[8],
         data[0]-data[6],data[1]-data[7],
         data[2]-data[8],
         np.linalg.norm([data[0],data[1],data[2]]) - np.linalg.norm([data[6],data[7],data[8]])])
      # offset measured statistically is (-20,-50,-220) between both sensors
      tempgyro = np.array([data[3],data[4],data[5],
         data[9],data[10],data[11],
         data[3]-data[9]+20,data[4]-data[10]+50,
         data[5]-data[11]+220,
         140+np.linalg.norm([data[3],data[4],data[5]]) - np.linalg.norm([data[9],data[10],data[11]])])
      for i in range(0,self.lengthOfArray-1):
         self.data[:,i] = self.data[:,i+1]
      self.acceleration[:,-1] = tempacc
      self.rotation[:,-1] = tempgyro
   def getData(self):
      temp = []
      for lines in self.data:
         for element in lines:
            temp.append(element)
      return temp

