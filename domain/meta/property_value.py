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

import ast

# pylint: disable=C0103


class PropertyValue(object):

    def __init__(self, type=None, readWrite=None, minimum=None, maximum=None, defaultValue=None,
                 size=None, precision=None, word=None, LSB=None, mask=None, shift=None, scale=None,
                 offset=None, base=None, assertion=None, signed=True):
        # ValueDescriptor Type of property after transformations
        self.type = type

        # ReadWrite Permissions set for this property
        self.readWrite = readWrite

        # Minimum value that can be get/set from this property
        self.minimum = minimum

        # Maximum value that can be get/set from this property
        self.maximum = maximum

        # Default value set to this property if no argument is passed
        self.defaultValue = defaultValue

        # Size of this property in its type
        # (i.e. bytes for numeric types, characters for string types)
        self.size = size

        # Required precision of the property
        self.precision = precision

        # Word size of property used for endianness
        self.word = word if word is not None else "2"

        # Endianness setting for a property
        self.LSB = LSB

        # Mask to be applied prior to get/set of property
        self.mask = mask if mask is not None else "0x00"

        # Shift to be applied after masking, prior to get/set of property
        self.shift = shift if shift is not None else "0"

        # Multiplicative factor to be applied after shifting, prior to get/set of property
        self.scale = scale if scale is not None else "1.0"

        # Additive factor to be applied after multiplying, prior to get/set of property
        self.offset = offset if offset is not None else "0.0"

        # Base for property to be applied to, leave 0 for no power operation
        # (i.e. base ^ property: 2 ^ 10)
        self.base = base if base is not None else "0"

        # Required value of the property, set for checking error state.
        # Failing an assertion condition will mark the device with an error state
        self.assertion = assertion

        # Treat the property as a signed or unsigned value
        self.signed = signed

    def to_big_integer(self, string_value):
        if self.mask[:2] == "0x":
            return int(string_value, 0)
        return float(string_value)

    # replaces Java shift() method
    def parse_shift(self):
        return int(self.shift, 0)

    # replaces Java scale() method
    def parse_scale(self):
        return float(int(self.scale, 0))

    # replaces Java offset() method
    def parse_offset(self):
        return float(int(self.offset, 0))

    # replaces Java LSB() method
    def parse_lsb(self):
        return ast.literal_eval(self.LSB)

    # replaces Java base() method
    def parse_base(self):
        return int(self.base)

    # replaces Java assertion() method
    def parse_assertion(self):
        if self.assertion is None:
            return None
        return int(self.assertion, 0)

    # replaces Java word() method
    def parse_word(self):
        return int(self.word)

    # replaces Java precision() method
    def parse_precision(self):
        return float(self.precision)

    def __str__(self):
        return ("PropertyValue[readWrite:%s, minimum:%s, maximum:%s, defaultValue:%s, size:%s,"
                " precision:%s, word:%s, LSB:%s, mask:%s, shift:%s, scale:%s, offset:%s, base:%s,"
                " assertion:%s, signed:%s]") % \
                (self.readWrite, self.minimum, self.maximum, self.defaultValue, self.size,
                 self.precision, self.word, self.LSB, self.mask, self.shift, self.scale,
                 self.offset, self.base, self.assertion, self.signed)
