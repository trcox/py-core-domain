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
from .get import Get
from .put import Put

class Command(BaseObject):

  def __init__(self, name=None, get=None, put=None, created=None, modified=None, origin=None):
    super(Command, self).__init__(created, modified, origin)
    self.name = name
    self.get = get
    self.put = put

  # command name which should be unique on a profile but not necessarily
  # unique for all -profiles
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name

  # get command details
  @property
  def get(self):
    return self.__get

  @get.setter
  def get(self, get):
    if (get is not None and not isinstance(get, Get)):
      raise TypeError("Command get must be of type Get")
    self.__get = get

  # put command details
  @property
  def put(self):
    return self.__put

  @put.setter
  def put(self, put):
    if (put is not None and not isinstance(put, Put)):
      raise TypeError("Command put must be of type Put")
    self.__put = put

  def __str__(self):
    return "Command [name=%s, get=%s, put=%s, to_string=%s]" % (self.name, self.get, self.put, super(Command, self).__str__())

  def associated_value_descriptors(self):
    associated_value_descriptor = []
    if (self.get is not None):
      associated_value_descriptor.extend(self.get.all_associated_value_descriptors())
    if (self.put is not None):
      associated_value_descriptor.extend(self.put.all_associated_value_descriptors())
    return associated_value_descriptor