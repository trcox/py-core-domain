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


class ResourceOperation(object):

    def __init__(self, operation=None, object=None, property=None, parameter=None, mappings=None,
                 index=None):
        self.operation = operation
        self.object = object
        self.property = property if property is not None else "value"
        self.parameter = parameter if parameter is not None else object
        self.mappings = mappings
        self.index = index if index is not None else "1"

    def __str__(self):
        return ("ResourceOperation [operation=%s, object=%s, property=%s, parameter=%s,"
                " mappings=%s, index=%s]") \
               % (self.operation, self.object, self.property, self.parameter, self.mappings,
                  self.index)
