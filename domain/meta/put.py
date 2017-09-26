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

from .action import Action

class Put(Action):

  def __init__(self, parameterNames=None, path=None, responses=None):
    super(Put, self).__init__(path, responses)
    self.parameterNames = parameterNames

  # ValueDescriptor names indicating the type and shape of the parameter
  # value
  @property
  def parameterNames(self):
    if (self.__parameterNames is None):
      self.__parameterNames = []
    return self.__parameterNames

  @parameterNames.setter
  def parameterNames(self, parameterNames):
    self.__parameterNames = parameterNames

  def add_parameterName(self, param):
    if (self.parameterNames is None):
      self.parameterNames = []
    self.parameterNames.append(param)

  def remove_parameter_name(self, param):
    if (self.parameterNames is not None and param in self.parameterNames):
      self.parameterNames.remove(param)

  def __str__(self):
    return "Put [parameterNames=%s]" % (self.parameterNames)

  def all_associated_value_descriptors(self):
    assoc_value_descriptors = super(Put, self).all_associated_value_descriptors()
    assoc_value_descriptors.extend(self.parameterNames)
    return assoc_value_descriptors
