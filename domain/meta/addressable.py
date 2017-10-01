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

from domain.common import base_object, http_method


class Addressable(base_object.BaseObject):

    def __init__(self, name, protocol, address, port, publisher=None,
                 user=None, password=None, topic=None, path=None, method=None,
                 created=None, modified=None, origin=None):
        super(Addressable, self).__init__(created, modified, origin)
        # unique name and identifier of the addressable
        self.name = name
        # protocol used using the addressable
        self.protocol = protocol
        # address (in either tcp or http format) of the addressable
        self.address = address
        # port on the address for the addressable
        self.port = port
        # for MQTT or other message bus addressables
        self.publisher = publisher
        # user id for authentication to addressable
        self.user = user
        # password for the user for authentication to addressable
        self.password = password
        # topic for MQTT message bus addressables or routing token for REST calls
        self.topic = topic
        # for callbacks
        self.path = path
        # HTTP method used with the addressable (default is POST)
        self.method = method if method is not None else http_method.HTTPMethod.POST

    def get_base_url(self):
        return "%s://%s:%s" % (self.protocol.name, self.address, self.port)

    # TODO - is this method used anywhere? If so, it does not appear to be setup correctly and makes
    # no sense. Remove if found to not be used
    # @deprecated removed if not used and if it is used, make sure it returns the right information
    def get_url(self):
        builder = self.get_base_url()
        if self.publisher is None and self.topic is not None:
            builder += "%s/" % (self.topic)
        builder += self.path
        return builder

    def __str__(self):
        return ("Addressable [name=%s, protocol=%s, address=%s, port=%s, path=%s, publisher=%s,"
                " user=%s, password=%s, topic=%s, to_string()=%s]") \
                % (self.name, self.protocol.name, self.address, self.port, self.path,
                   self.publisher, self.user, self.password, self.topic,
                   super(Addressable, self).__str__())
