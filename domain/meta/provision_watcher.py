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
from domain.meta import operating_state


class ProvisionWatcher(base_object.BaseObject):

    def __init__(self, name=None, profile=None, identifiers=None, service=None,
                 operatingState=operating_state.OperatingState.ENABLED, created=None,
                 modified=None, origin=None):
        super(ProvisionWatcher, self).__init__(created, modified, origin)
        # unique name and identifier of the addressable
        self.name = name
        # device profile that should be applied to the devices available at the
        # identifier addresses
        self.profile = profile
        # set of key value pairs that identify type of of address (MAC, HTTP,...) and address
        # to watch for (00-05-1_b-A1-99-99, 10.0.0.1,...)
        self.identifiers = identifiers if identifiers is not None else {}
        # device service that owns the watcher
        self.service = service
        # operational state - either enabled or disabled
        self.operatingState = operatingState

    @property
    def identifiers(self):
        if self.__identifiers is None:
            self.__identifiers = {}
        return self.__identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        self.__identifiers = identifiers

    def add_identifier(self, key, value):
        if self.identifiers is None:
            self.identifiers = {}
        self.identifiers[key] = value

    def remove_identifier(self, key):
        if self.identifiers is not None and key in self.identifiers:
            del self.identifiers[key]

    def __str__(self):
        return ("ProvisionWatcher [name=%s identifiers=%s, service=%s, profile=%s,"
                " operatingState=%s]") \
                % (self.name, self.identifiers, self.service, self.profile, self.operatingState)

    def __hash__(self):
        temp = self
        if temp.identifiers is not None:
            for key, value in self.identifiers.items():
                setattr(temp, "key%s" % key, value)
            temp.identifiers = None
        return super(ProvisionWatcher, temp).__hash__()
