#*******************************************************************************
# Copyright 2017 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
#
# @microservice: py-core-domain library
# @author: Tyler Cox, Dell
# @version: 1.0.0
#*******************************************************************************

from domain.common import BaseObject

class Event(BaseObject):
 
  def __init__(self, device=None, readings=None, pushed=None, created=None, modified=None, origin=None):
    super(Event, self).__init__(created, modified, origin)
    self.pushed = pushed
    self.readings = readings
    self.device = device
    
  @property
  def device(self):
    return self.__device
    
  @device.setter
  def device(self, device):
    self.__device = device
    self.updateReadingsDevice()
  
  @property
  def pushed(self):
    return self.__pushed
    
  @pushed.setter
  def pushed(self, pushed):
    self.__pushed = pushed
  
  @property
  def readings(self):
    return self.__readings
    
  @readings.setter
  def readings(self, readings):
    self.__readings = readings
    if (self.__readings is not None):
      for r in self.__readings:
        if hasattr(self, '__device'):
          r.device = self.device
    
  def addReading(self, reading):
    if self.readings is None:
      self.readings = []
    reading.device = self.device
    self.readings.append(reading)

  def addReadings(self, readings):
    if self.readings is None:
      self.readings = []
    for r in readings:
      r.device = self.device
    self.readings.extend(readings)
    
  def removeReading(self, reading):
    if self.readings is None:
      self.readings = []
    if reading not in self.readings:
      return False
    return self.readings.remove(reading)
    
  def markPushed(self, pushed):
    self.pushed = pushed
    for reading in self.readings:
      reading.pushed = pushed
      
  def updateReadingsDevice(self):
    if (self.readings is not None) and (len(self.readings) > 0):
      for reading in self.readings:
        reading.device = self.device
 
  def __str__(self):
    return "Event [pushed=%s, device= %s, readings=%s, toString()=%s]" % (self.pushed, self.device, self.readings, super(Event, self).__str__())