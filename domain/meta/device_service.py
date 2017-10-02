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

from domain.meta import service


class DeviceService(service.Service):

    def __init__(self, name=None, lastConnected=None, lastReported=None, operatingState=None,
                 labels=None, addressable=None, adminState=None, destination=None,
                 description=None, created=None, modified=None, origin=None):
        super(DeviceService, self).__init__(operatingState, description, name,
                                            lastConnected, lastReported, addressable, destination,
                                            created, modified, origin)
        self.adminState = adminState

    def __str__(self):
        return "DeviceService [adminState=%s, operatingState=%s, addressable=%s]" \
            % (self.adminState, self.operatingState, self.addressable)
