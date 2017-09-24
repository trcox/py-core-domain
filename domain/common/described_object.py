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

class DescribedObject(BaseObject):

  def __init__(self, description=None, created=None, modified=None, origin=None):
    super(DescribedObject, self).__init__(created, modified, origin)
    self.description = description
    
  @property
  def description(self):
    return self.__description
    
  @description.setter
  def description(self, description):
    self.__description = description
    
  def __str__(self):
    return "DescribedObject [description=%s, toString()=%s]" % (self.description, super(DescribedObject, self).__str__())
    
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