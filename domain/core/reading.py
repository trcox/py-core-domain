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

class Reading(BaseObject):
 
  def __init__(self, value=None, name=None, device=None, pushed=None, created=None, modified=None, origin=None):
    super(Reading, self).__init__(created, modified, origin)
    self.pushed = pushed
    self.name = name
    self.value = value
    self.device = device
    
  @property
  def name(self):
    return self.__name
    
  @name.setter
  def name(self, name):
    self.__name = name
  
  @property
  def pushed(self):
    return self.__pushed
    
  @pushed.setter
  def pushed(self, pushed):
    self.__pushed = pushed
  
  @property
  def value(self):
    return self.__value
    
  @value.setter
  def value(self, value):
    self.__value = value
    
  @property
  def device(self):
    return self.__device
    
  @device.setter
  def device(self, device):
    self.__device = device
 
  def __str__(self):
    return "Reading [pushed=%s, name= %s, value=%s, device=%s]" % (self.pushed, self.name, self.value, self.device)