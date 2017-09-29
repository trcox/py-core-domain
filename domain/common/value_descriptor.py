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

# pylint: disable=C0103


class ValueDescriptor(described_object.DescribedObject):

    def __init__(self, name=None, min=None, max=None, type=None, uomLabel=None, defaultValue=None,
                 formatting=None, labels=None, description=None, created=None, modified=None,
                 origin=None):
        super(ValueDescriptor, self).__init__(description, created, modified, origin)
        self.name = name
        self.min = min
        self.max = max
        self.type = type
        self.uomLabel = uomLabel
        self.defaultValue = defaultValue
        self.formatting = formatting
        self.labels = labels

    @staticmethod
    def get_names(value_descriptors: list):
        names = []
        for value_descriptor in value_descriptors:
            names.append(value_descriptor.name)
        return names

    def __str__(self):
        return ("ValueDescriptor [name=%s, min=%s, max=%s, type=%s, uomLabel=%s, defaultValue=%s,"
                "formatting=%s, labels=%s]") \
                % (self.name, self.min, self.max, self.type, self.uomLabel, self.defaultValue,
                   self.formatting, self.labels)

    def __hash__(self):
        temp = self
        if temp.labels is not None:
            for i, label in enumerate(self.labels):
                setattr(temp, "label%s" % i, label)
            temp.labels = None
        return super(ValueDescriptor, temp).__hash__()
