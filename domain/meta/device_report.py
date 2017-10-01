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


class DeviceReport(base_object.BaseObject):

    def __init__(self, name=None, device=None, event=None, expected=None, created=None,
                 modified=None, origin=None):
        super(DeviceReport, self).__init__(created, modified, origin)
        # non-database identifier for a device report - must be unique
        self.name = name
        # associated device name - should be a valid and unique device name
        self.device = device
        # associated schedule event name - should be a valid and unique schedule event name
        self.event = event
        # array of value descriptor names describing the types of data captured in the reports
        self.expected = expected

    def __str__(self):
        return "DeviceReport [name=%s, device=%s, event=%s, expected=%s, to_string()=%s]" \
                     % (self.name, self.device, self.event, self.expected,
                        super(DeviceReport).__init__())

    def __hash__(self):
        temp = self
        if temp.expected is not None:
            for i, expected in enumerate(self.expected):
                setattr(temp, "expected%s" % i, expected)
            temp.expected = None
        return super(DeviceReport, temp).__hash__()
