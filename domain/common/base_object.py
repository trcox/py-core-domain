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

import collections
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
        hash_value = None
        try:
            hash_value = hash(tuple(sorted(self.__dict__.items())))
        except TypeError:
            hash_value = self.__hash__helper__()
        return hash_value

    # Method for hashing unhashable attribute values
    def __hash__helper__(self):
        temp = self
        for item in list(self.__dict__):
            if not isinstance(getattr(self, item), collections.Hashable):
                for i, element in enumerate(getattr(temp, item)):
                    setattr(temp, "%s%s" % (item, i), element)
                setattr(temp, item, None)
        return temp

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def compare_to(self, other):
        if other.created > self.created:
            return 1
        return -1
