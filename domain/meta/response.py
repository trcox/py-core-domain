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

class Response(object):

  def __init__(self, code=None, description=None, expectedValues=None):
    self.code = code
    self.description = description
    self.expectedValues = expectedValues

  # status code provided with the response (usually an HTTP status code for
  # REST calls)
  @property
  def code(self):
    return self.__code

  @code.setter
  def code(self, code):
    self.__code = code

  # information about response - error description or good response
  # information
  @property
  def description(self):
    return self.__description

  @description.setter
  def description(self, description):
    self.__description = description

  # value descriptors indicating the values returned as part of the response.
  @property
  def expectedValues(self):
    if self.__expectedValues is None:
      self.__expectedValues = []
    return self.__expectedValues

  @expectedValues.setter
  def expectedValues(self, expectedValues):
    self.__expectedValues = expectedValues

  def add_expected_value(self, expectedValue):
    if (self.expectedValues is None):
      self.expectedValues = []
    self.expectedValues.append(expectedValue)

  def remove_expected_value(self, expectedValue):
    if (self.expectedValues is None):
      self.expectedValues = []
    if expectedValue not in self.expectedValues:
      return False
    return self.expectedValues.remove(expectedValue)

  def __str__(self):
    return "Response [code=%s, description=%s, expectedValues=%s]" % (self.code, self.description, self.expectedValues)

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
      sort_keys=True, indent=4)