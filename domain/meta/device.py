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

from domain.common import DescribedObject
from .asset import Asset

class Device(DescribedObject, Asset):

  # TODO - someday have a naming service for all types (Device, Service,
  # Profile, Addressable, ValueDescriptor, etc.). This naming service makes
  # sure the name is unique - potentially even across EdgeX instances in a
  # cluster - and can even generate a name with some help from the
  # originating service. Need to look into how Docker provides names to
  # containers and use a similar approach.
  
  def __init__(self, adminState=None, operatingState=None, description=None, name=None, lastConnected=None, lastReported=None, Addressable=None, 
      labels=None, location=None, service=None, profile=None, created=None, modified=None, origin=None):
    super(Device, self).__init__(created=created, modified=modified, origin=origin)
    self.adminState = adminState
    self.operatingState = operatingState
    self.description = description
    self.name = name
    self.lastConnected = lastConnected
    self.lastReported = lastReported
    self.Addressable = Addressable
    self.labels = labels
    self.location = location
    self.service = service
    self.profile = profile
    
  # administrative state - either locked or unlocked (as reported by devices
  # or device services)
  @property
  def adminState(self):
    return self.__adminState
    
  @adminState.setter
  def adminState(self):
   self.__adminState = adminState
  
  # operational state - either enabled or disabled (set by humans or systems)
  @property
  def operatingState(self):
    return self.__operatingState
    
  @operatingState.setter
  def operatingState(self):
   self.__operatingState = operatingState
    
  @property
  def description(self):
    return self.__description
    
  @description.setter
  def description(self):
   self.__description = description
  
  # non-database identifier for a device - must be unique
  @property
  def name(self):
    return self.__name
    
  @name.setter
  def name(self):
   self.__name = name
    
  # time in milliseconds that the device last provided any feedback or
  # responded to any request
  @property
  def lastConnected(self):
    return self.__lastConnected
    
  @lastConnected.setter
  def lastConnected(self):
   self.__lastConnected = lastConnected

  # time in milliseconds that the device last reported data to the core
  @property
  def lastReported(self):
    return self.__lastReported
    
  @lastReported.setter
  def lastReported(self):
   self.__lastReported = lastReported

  # address (MQTT topic, HTTP address, serial bus, etc.) for the device
  @property
  def addressable(self):
    return self.__addressable
    
  @addressable.setter
  def addressable(self):
   self.__addressable = addressable
    
  # tags or other labels applied to the device for search or other
  # identification needs
  @property
  def labels(self):
    return self.__labels

  @labels.setter
  def labels(self, labels):
    self.__labels = labels
    
  # device service specific location information (such as a lat-long)
  @property
  def location(self):
    return self.__location

  @location.setter
  def location(self, location):
    self.__location = location
    
  # owning device service (each device can have only one owning service)
  @property
  def service(self):
    return self.__service

  @service.setter
  def service(self, service):
    self.__service = service
    
  # associated device profile that describes the device
  @property
  def profile(self):
    return self.__profile

  @profile.setter
  def profile(self, profile):
    self.__profile = profile
  
  def __str__(self):
    return "Device [name=%s, adminState=%s, operatingState=%s, addressable=%s, lastConnected=%s, lastReported=%s, labels=%s, location=%s, service=%s, profile=%s]" \
        % (self.name, self.adminState, self.operatingState, self.Addressable, self.lastConnected, self.lastReported, self.labels, self.location, self.service, self.profile)