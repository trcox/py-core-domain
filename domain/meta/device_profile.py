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

from domain.common import described_object
from domain.meta import command as comm


class DeviceProfile(described_object.DescribedObject):

  def __init__(self, name=None, manufacturer=None, model=None, labels=None, deviceResources=None, resources=None,
      commands=None, description=None, created=None, modified=None, origin=None):
    super(DeviceProfile, self).__init__(description, created, modified, origin)
    self.name = name
    self.manufacturer = manufacturer
    self.model = model
    self.labels = labels
    self.deviceResources = deviceResources
    self.resources = resources
    self.commands = commands
    
  # non-database identifier for a device profile must be unique  
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name
    
  # manufacture of the device
  @property
  def manufacturer(self):
    return self.__manufacturer

  @manufacturer.setter
  def manufacturer(self, manufacturer):
    self.__manufacturer = manufacturer
  
  # model of the device  
  @property
  def model(self):
    return self.__model

  @model.setter
  def model(self, model):
    self.__model = model
  
  # tag or label used by services to identify or search for groups of
  # profiles
  @property
  def labels(self):
    return self.__labels

  @labels.setter
  def labels(self, labels):
    self.__labels = labels

  # device service used JSON data that is required to communicate with
  # devices of this profile type
  @property
  def deviceResources(self):
    return self.__deviceResources

  @deviceResources.setter
  def deviceResources(self, deviceResources):
    self.__deviceResources = deviceResources

  # device service used object actions that are optionally used to map
  # commands to objects of devices of this profile type
  @property
  def resources(self):
    return self.__resources

  @resources.setter
  def resources(self, resources):
    self.__resources = resources

  # list of commands to get/put information from the associated devices of
  # this profile type
  @property
  def commands(self):
    return self.__commands

  @commands.setter
  def commands(self, commands):
    self.__commands = commands

  def add_command(self, command):
    if (self.commands is None):
      self.commands = []
    if not isinstance(command, comm.Command):
      raise TypeError("DeviceProfile command must be of type Command")
    self.commands.append(command)

  def remove_command(self, command):
    if (self.commands is None):
      self.commands = []
    if command not in self.commands:
      return False
    return self.commands.remove(command)

  def compare_property_lists(this_list, other_list):
    if (this_list is None):
      if (other_list is not None):
        return False
    else:
      if (other_list is None):
        return False
      if (len(this_list) != len(other_list)):
        return False
      i = 0
      for object in this_list:
        if (not object == other_list.get(i)):
          return False
        i += 1
    return True

  def __str__(self):
    return "DeviceProfile [name=%s, manufacturer=%s, model=%s, labels=%s, deviceResources=%s, commands=%s, resources=%s]" \
        % (self.name, self.manufacturer, self.model, self.labels, self.deviceResources, self.commands, self.resources)

  def __hash__(self):
    temp = self
    if temp.labels is not None:
      for i, label in enumerate(self.labels):
        setattr(temp, "label%s" % i, label)
      temp.labels = None
    if temp.commands is not None:
      for i, command in enumerate(self.commands):
        setattr(temp, "command%s" % i, command)
      temp.commands = None
    return super(DeviceProfile, temp).__hash__()