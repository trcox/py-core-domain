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


class DeviceObject(object):

  def __init__(self, name=None, tag=None, description=None, properties=None, attributes=None):
    self.name = name
    self.tag = tag
    self.description = description
    self.properties = properties
    self.attributes = attributes
  
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name
    
  @property
  def tag(self):
    return self.__tag

  @tag.setter
  def tag(self, tag):
    self.__tag = tag
    
  @property
  def description(self):
    return self.__description

  @description.setter
  def description(self, description):
    self.__description = description
    
  @property
  def properties(self):
    return self.__properties

  @properties.setter
  def properties(self, properties):
    self.__properties = properties
    
  @property
  def attributes(self):
    return self.__attributes

  @attributes.setter
  def attributes(self, attributes):
    self.__attributes = attributes

  def __str__(self):
    return "DeviceObject [name=%s, tag=%s, description=%s, properties=%s, attributes=%s]" \
        % (self.name, self.tag, self.description, self.properties, self.attributes)
