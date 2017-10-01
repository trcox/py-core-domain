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
from domain.meta import response as response_module


class Action(object):

    def __init__(self, path=None, responses=None):
        # path used by service for action on a device or sensor
        self.path = path
        # responses from get or put request to service
        self.responses = responses

    #*
    #* Add a response to the responses and initialize the list if None.
    #*
    #* @param response Response object to add.
    #*
    def add_response(self, response):
        if self.responses is None:
            self.responses = []
        if not isinstance(response, response_module.Response):
            raise TypeError("Action response must be of type Response")
        self.responses.append(response)

    #*
    #* Remove the Response from the responses list
    #*
    #* @param response Response object to remove
    #*
    def remove_response(self, response):
        if self.responses is None:
            self.responses = []
        if response in self.responses:
            self.responses.remove(response)

    #*
    #* Convenience method to return a list of all expected values from all the associated responses.
    #*
    #* @return List of expected value string names
    #*
    def all_expected_values(self):
        if self.responses is None:
            return []
        return sum([r.expectedValues for r in self.responses], [])

    #*
    #* Convenience method to return the names of all associated value descriptor names. For Get this
    #* is just expected value names. For Put, this is expected value names plus parameter names.
    #*
    #* @return list of associated value descriptors
    #*
    def all_associated_value_descriptors(self):
        return self.all_expected_values()

    def __str__(self):
        return "Action [path=%s, responses=%s]" % (self.path, [str(r) for r in self.responses])

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
