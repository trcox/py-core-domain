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

# pylint: disable=C0103


class Schedule(base_object.BaseObject):

    # TODO - make protected after changes to test package
    DATETIME_FORMATS = ["yyyy_mMdd'T'HHmmss"]

    def __init__(self, name=None, start=None, end=None, frequency=None, cron=None, runOnce=False,
                 created=None, modified=None, origin=None):
        super(Schedule, self).__init__(created, modified, origin)
        # non-database identifier for a schedule- must be unique
        self.name = name
        # Start time in ISO 8601 format YYYYMMDD'T'HHmmss
        # @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyymmdd'T'HHmmss")
        self.start = start
        # End time in ISO 8601 format YYYYMMDD'T'HHmmss
        # @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyymmdd'T'HHmmss")
        self.end = end
        # how frequently should the event occur
        self.frequency = frequency
        # cron styled regular expression indicating how often the action under schedule should
        # occur. Use either runOnce, frequency or cron and not all.
        self.cron = cron
        # boolean indicating that this schedules runs one time - at the time indicated by the start
        self.runOnce = runOnce

    def __str__(self):
        return ("Schedule [name=%s, start=%s, end=%s, frequency=%s, cron=%s, runOnce=%s,"
                " to_string()=%s]") \
                % (self.name, self.start, self.end, self.frequency, self.cron, self.runOnce,
                   super(Schedule, self).__str__())
