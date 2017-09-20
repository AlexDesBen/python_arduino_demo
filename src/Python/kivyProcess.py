#*-* coding: utf-8*-*
################################################################################
################################################################################
#Author : Alexandre Desilets-Benoit
#Name of module : KivyProcess
#Version : ???
#Description : objects and classes to create interactiv GUI
################################################################################
################################################################################

import multiprocessing as mp
import threading
import time

from dataStructure import *
from CarApp import *


class UIProcessPassive(mp.Process):
   def __init__(self,runFlag,newEvent):
      mp.Process.__init__(self)
      self.runFlag = runFlag
      self.newEvent = newEvent
   def run(self):
      time.sleep(5)
      while self.runFlag.value:
         if self.newEvent.value == True:
            print("cancel eventtrigger")
            self.newEvent.value = False

class UIProcess(mp.Process):
   def __init__(self,buf,size,nbr,runFlag,eventFlag,validEventFlag,eventID,CarFlag,RightFlag,LeftFlag,analysisFlag,newEvent):
      mp.Process.__init__(self)
      self.data = dataStructure(buf,size,nbr,eventFlag,validEventFlag,analysisFlag)
      self.runFlag = runFlag
      self.eventFlag = eventFlag
      self.validEventFlag = validEventFlag
      self.eventID = eventID
      self.NAME = 'patate'
      self.Right = None
      self.Left = None
      self.app = CarApp()
      self.CarFlag = CarFlag
      self.RightFlag = RightFlag
      self.LeftFlag = LeftFlag
      self.analysisFlag = analysisFlag
      self.newEvent = newEvent
   def run(self):
      print('launched UI process')
      threadDisplay = threading.Thread(target = Displaying,args = (self.runFlag,self.CarFlag,self.LeftFlag,self.RightFlag,self.newEvent,self.app))
      threadDisplay.daemon = True
      threadDisplay.start()
      self.app.run()
      threadDisplay.join()

def Displaying(runFlag,CarFlag,LeftFlag,RightFlag,newEvent,App):
   time.sleep(5)
   print('launched UI process')
   while runFlag.value != True:
      print("UIthread waiting")
      time.sleep(1)
   while runFlag.value:
      if newEvent.value:
         if CarFlag.value:
            App.CarCallBack('Running')
         else:
            App.CarCallBack('Static')
         if RightFlag.value:
            print("UIthread set to right")
            App.TapCallBack('Right')
         elif LeftFlag.value:
            print("UIthread set to right")
            App.TapCallBack('Left')
         else:
            print("UIthread set to wtf")
            App.TapCallBack('else')
         newEvent.value = False
   return True

