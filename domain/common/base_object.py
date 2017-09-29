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

import json


class BaseObject(object):

    def __init__(self, created=None, modified=None, origin=None):
        self.created = created
        self.modified = modified
        self.origin = origin

    def __str__(self):
        return "BaseObject [created=%s, modified=%s, origin=%s]" \
            % (self.created, self.modified, self.origin)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def compare_to(self, other):
        if other.created > self.created:
            return 1
        return -1
