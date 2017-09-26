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

class Asset(object):

  @property
  def adminState(self):
    raise NotImplementedError()
    
  @adminState.setter
  def adminState(self, adminState):
    raise NotImplementedError()
    
  @property
  def operatingState(self):
    raise NotImplementedError()
    
  @operatingState.setter
  def operatingState(self, operatingState):
    raise NotImplementedError()
    
  @property
  def description(self):
    raise NotImplementedError()
    
  @description.setter
  def description(self, description):
    raise NotImplementedError()
    
  @property
  def name(self):
    raise NotImplementedError()
    
  @name.setter
  def name(self, name):
    raise NotImplementedError()
    
  @property
  def lastConnected(self):
    raise NotImplementedError()
    
  @lastConnected.setter
  def lastConnected(self, lastConnected):
    raise NotImplementedError()
    
  @property
  def lastReported(self):
    raise NotImplementedError()
    
  @lastReported.setter
  def lastReported(self, lastReported):
    raise NotImplementedError()
    
  @property
  def addressable(self):
    raise NotImplementedError()
    
  @addressable.setter
  def addressable(self, addressable):
    raise NotImplementedError()
