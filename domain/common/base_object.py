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

import time

class BaseObject(object):
 
  def __init__(self, created, modified, origin):
    initialization_time = time.time()
    self.created = created if created is not None else initialization_time
    self.modified = modified if modified is not None else initialization_time
    self.origin = origin if origin is not None else initialization_time
    
  @property
  def created(self):
    return self.__created
    
  @created.setter
  def created(self, created):
    self.__created = created
    
  @property
  def modified(self):
    return self.__modified
    
  @modified.setter
  def modified(self, modified):
    self.__modified = modified
    
  @property
  def origin(self):
    return self.__origin
    
  @origin.setter
  def origin(self, origin):
    self.__origin = origin
 
  def __str__(self):
    return "BaseObject [created=%s, modified=%s, origin=%s]" % (self.created, self.modified, self.origin)
    
  def __eq__(self, other):
    if type(other) is type(self):
        return self.__dict__ == other.__dict__
    return False

  def __ne__(self, other):
    return not self == other
    
  def __hash__(self):
    return hash(tuple(sorted(self.__dict__.items())))
  
  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, 
      sort_keys=True, indent=4)
      
  def compareTo(self, input):
    if(input.created > self.created):
      return 1
    else:
      return -1