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


class ScheduleEvent(base_object.BaseObject):

    def __init__(self, name=None, addressable=None, parameters=None, schedule=None,
                 service=None, created=None, modified=None, origin=None):
        super(ScheduleEvent, self).__init__(created, modified, origin)
        # non-database identifier for a schedule event - must be unique
        self.name = name
        # address (MQTT topic, HTTP address, serial bus, etc.) for the action (can be empty)
        self.addressable = addressable
        # json body for parameters
        self.parameters = parameters
        # name to associated owning schedule
        self.schedule = schedule
        # service associated with this event
        self.service = service

    def __str__(self):
        return ("ScheduleEvent [name=%s, addressable=%s, parameters=%s, service=%s, schedule=%s,"
                " to_string()=%s]") \
                % (self.name, self.addressable, self.parameters, self.service, self.schedule,
                   super(ScheduleEvent, self).__str__())
