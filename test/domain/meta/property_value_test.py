# *******************************************************************************
# Copyright 2016-2017 Dell Inc.
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
# @microservice: core-domain library
# @author: Tyler Cox, Dell
# @version: 1.0.0
# ******************************************************************************/

import unittest
from domain.meta import property_value


class PropertyValueTest(unittest.TestCase):

    def setUp(self):
        self.pvalue1 = property_value.PropertyValue()

    def test_to_big_integer(self):
        self.pvalue1.mask = "0x00"
        self.assertEqual(self.pvalue1.to_big_integer("0x01"), 1,
                         "Property Value convert to big int not working properly")

    def test_to_big_integer_odd_mask(self):
        self.pvalue1.mask = "foo"
        self.assertEqual(self.pvalue1.to_big_integer("10"), 10,
                         "Property Value convert to big int not working properly")

    def test_shift(self):
        self.pvalue1.shift = "0x08"
        self.assertEqual(self.pvalue1.parse_shift(), 8.0,
                         "Property Value shift not working properly")

    def test_shift_no_mask(self):
        self.pvalue1.shift = "10"
        self.assertEqual(self.pvalue1.parse_shift(), 10.0,
                         "Property Value shift not working properly")

    def test_scale(self):
        self.pvalue1.scale = "0x08"
        self.assertEqual(self.pvalue1.parse_scale(), 8.0,
                         "Property Value scale not working properly")

    def test_scalet_no_mask(self):
        self.pvalue1.scale = "10"
        self.assertEqual(self.pvalue1.parse_scale(), 10.0,
                         "Property Value scale not working properly")

    def test_offset(self):
        self.pvalue1.offset = "0x08"
        self.assertEqual(self.pvalue1.parse_offset(), 8.0,
                         "Property Value offset not working properly")

    def test_off_no_mask(self):
        self.pvalue1.offset = "10"
        self.assertEqual(self.pvalue1.parse_offset(), 10.0,
                         "Property Value offset not working properly")

    def test_self_assertion(self):
        self.pvalue1.assertion = "0x01"
        self.pvalue1.mask = "foo"
        self.assertEqual(self.pvalue1.parse_assertion(), 1,
                         "Property Value self.assertion not working properly")

    def test_self_assertion_no(self):
        self.pvalue1.assertion = None
        self.assertEqual(self.pvalue1.parse_assertion(), None,
                         "Property Value self.assertion not working properly")

    def test_self_assertion_no_mask(self):
        self.pvalue1.assertion = "10"
        self.pvalue1.mask = "foo"
        self.assertEqual(self.pvalue1.parse_assertion(), 10,
                         "Property Value self.assertion not working properly")

    def test_to_string(self):
        str(self.pvalue1)

if __name__ == "__main__":
    unittest.main()
