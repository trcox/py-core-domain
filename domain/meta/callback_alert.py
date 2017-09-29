# *******************************************************************************
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
# *******************************************************************************

from .action_type import ActionType

 # Class used to signal what device has been changed and what type of action was accomplished on it
 # in metadata.
 
 
class CallbackAlert(object):

  def __init__(self, type, id):
    self.type = type
    self.id = id

  @property
  def type(self):
    return self.__type

  @type.setter
  def type(self, type):
    if not isinstance(type, ActionType):
      raise TypeError("CallbackAlert type must be of type ActionType")
    self.__type = type
    
  # id of the device
  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, id):
    self.__id = id