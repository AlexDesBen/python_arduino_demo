#*-* coding: utf-8*-*
################################################################################
################################################################################
#Author : 
#Date : 
#Company : ProximityHCI
#Name of module : 
#Version : 
#Description : 
################################################################################
################################################################################

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class CarStatus(Label):
   pass
class TapSide(Label):
   pass
#class ButtonSide(Button):
#   def OnClick(self):
#      BMWApp.get_running_app().TapCallBack(self.text)

class CarApp(App):
   def CarCallBack(self,statusCar):
      car = self.get_running_app().root.ids['statusCar']
      if statusCar == 'Static':
         car.text = 'Static'
      else:
         car.text = 'Moving'
   def TapCallBack(self,statusTap):
      left = self.get_running_app().root.ids['Left']
      right = self.get_running_app().root.ids['Right']
      if statusTap == 'Left':
         left.color = (1,1,1,1)
         right.color = (1,1,1,0.1)
      elif statusTap == 'Right':
         left.color = (1,1,1,0.1)
         right.color = (1,1,1,1)
      else:
         left.color = (1,1,1,0.1)
         right.color = (1,1,1,0.1)

if __name__ == '__main__':
    CarApp().run()












