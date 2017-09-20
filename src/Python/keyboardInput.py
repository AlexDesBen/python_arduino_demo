#*-* coding: utf-8*-*
################################################################################
################################################################################
# Author : Alexandre Desilets-Benoit
# Name of module : keyboardInput
# Version : ???
# Description : function to validate input from keyboard and to shutdown all the
#               other sthreads and process
################################################################################
################################################################################

import sys

def Flaging(runFlag):
   PYTHON_VERSION = sys.version_info.major
   if PYTHON_VERSION == 2:
      Input = raw_input('\nType \'stop\' to stop\n\n')
   elif PYTHON_VERSION == 3:
      Input = input('\nType \'stop\' to stop\n\n')
   while Input.upper() != 'STOP':
      if PYTHON_VERSION == 2:
         Input = raw_input('\nType \'stop\' to stop\n\n')
      elif PYTHON_VERSION == 3:
         Input = input('\nType \'stop\' to stop\n\n')
   print("App stopped")
   runFlag.value = False
   return True
