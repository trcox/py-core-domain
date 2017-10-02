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

from domain.common import described_object
from domain.meta import asset


class Service(described_object.DescribedObject, asset.Asset):

    def __init__(self, name=None, lastConnected=None, lastReported=None, operatingState=None,
                 labels=None, addressable=None, destination=None, description=None, created=None,
                 modified=None, origin=None):
        described_object.DescribedObject.__init__(self, description, created, modified, origin)
        asset.Asset.__init__(self, operatingState=operatingState, description=description,
                             name=name, lastConnected=lastConnected, lastReported=lastReported,
                             addressable=addressable, adminState=None)
        self.labels = labels
        self.destination = destination
