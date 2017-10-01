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

from domain.common import base_object


class Command(base_object.BaseObject):

    def __init__(self, name=None, get=None, put=None, created=None, modified=None, origin=None):
        super(Command, self).__init__(created, modified, origin)
        # command name which should be unique on a profile but not necessarily
        # unique for all profiles
        self.name = name
        # get command details
        self.get = get
        # gut command details
        self.put = put

    def __str__(self):
        return "Command [name=%s, get=%s, put=%s, to_string=%s]" % (self.name, self.get, self.put,
                                                                    super(Command, self).__str__())

    def associated_value_descriptors(self):
        associated_value_descriptor = []
        if self.get is not None:
            associated_value_descriptor.extend(self.get.all_associated_value_descriptors())
        if self.put is not None:
            associated_value_descriptor.extend(self.put.all_associated_value_descriptors())
        return associated_value_descriptor
