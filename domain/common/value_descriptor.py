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

class ValueDescriptor(DescribedObject):

  def __init__(self, name=None, min=None, max=None, type=None, uomLabel=None, defaultValue=None, formatting=None, 
      labels=None, description=None, created=None, modified=None, origin=None):
    super(ValueDescriptor, self).__init__(description, created, modified, origin)
    self.name = name
    self.min = min
    self.max = max
    self.type = type
    self.uomLabel = uomLabel
    self.defaultValue = defaultValue
    self.formatting = formatting
    self.labels = labels
    
  @property
  def name(self):
    return self.__name
    
  @name.setter
  def name(self, name):
    self.__name = name
    
  @property
  def min(self):
    return self.__min
    
  @min.setter
  def min(self, min):
    self.__min = min
    
  @property
  def max(self):
    return self.__max
    
  @max.setter
  def max(self, max):
    self.__max = max
        
  @property
  def type(self):
    return self.__type
    
  @type.setter
  def type(self, type):
    self.__type = type
    
  @property
  def uomLabel(self):
    return self.__uomLabel
    
  @uomLabel.setter
  def uomLabel(self, uomLabel):
    self.__uomLabel = uomLabel
        
  @property
  def defaultValue(self):
    return self.__defaultValue
    
  @defaultValue.setter
  def defaultValue(self, defaultValue):
    self.__defaultValue = defaultValue
    
  @property
  def formatting(self):
    return self.__formatting
    
  @formatting.setter
  def formatting(self, formatting):
    self.__formatting = formatting
        
  @property
  def labels(self):
    return self.__labels
    
  @labels.setter
  def labels(self, labels):
    self.__labels = labels
    
  def getNames(valueDescriptors):
    names = []
    for valueDescriptor in valueDescriptors:
      names.append(valueDescriptor.name)
    return names
    
  def __str__(self):
    return "ValueDescriptor [name=%s, min=%s, max=%s, type=%s, uomLabel=%s, defaultValue=%s, formatting=%s, labels=%s]" \
        % (self.name, self.min, self.max, self.type, self.uomLabel, self.defaultValue, self.formatting, self.labels)
    
  def __hash__(self):
    temp = self
    for i, label in enumerate(self.labels):
      setattr(temp, "label%s" % i, label)
    temp.labels = None
    return super(ValueDescriptor, temp).__hash__()