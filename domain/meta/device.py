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

# pylint: disable=C0103


class Device(described_object.DescribedObject, asset.Asset):

    # TODO - someday have a naming service for all types (Device, Service,
    # Profile, Addressable, ValueDescriptor, etc.). This naming service makes
    # sure the name is unique - potentially even across EdgeX instances in a
    # cluster - and can even generate a name with some help from the
    # originating service. Need to look into how Docker provides names to
    # containers and use a similar approach.

    def __init__(self, adminState=None, operatingState=None, description=None, name=None,
                 lastConnected=None, lastReported=None, addressable=None, labels=None,
                 location=None, service=None, profile=None, created=None, modified=None,
                 origin=None):
        super(Device, self).__init__(created=created, modified=modified, origin=origin)
        # administrative state - either locked or unlocked (as reported by devices
        # or device services)
        self.adminState = adminState
        # operational state - either enabled or disabled (set by humans or systems)
        self.operatingState = operatingState
        self.description = description
        # non-database identifier for a device - must be unique
        self.name = name
        # time in milliseconds that the device last provided any feedback or
        # responded to any request
        self.lastConnected = lastConnected
        # time in milliseconds that the device last reported data to the core
        self.lastReported = lastReported
        # address (MQTT topic, HTTP address, serial bus, etc.) for the device
        self.addressable = addressable
        # tags or other labels applied to the device for search or other
        # identification needs
        self.labels = labels
        # device service specific location information (such as a lat-long)
        self.location = location
        # owning device service (each device can have only one owning service)
        self.service = service
        # associated device profile that describes the device
        self.profile = profile

    def __str__(self):
        return ("Device [name=%s, adminState=%s, operatingState=%s, addressable=%s,"
                " lastConnected=%s, lastReported=%s, labels=%s, location=%s, service=%s,"
                " profile=%s]") \
                % (self.name, self.adminState, self.operatingState, self.addressable,
                   self.lastConnected, self.lastReported, self.labels, self.location,
                   self.service, self.profile)
