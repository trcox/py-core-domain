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
# @author: Jim White, Dell
# @version: 1.0.0
# ******************************************************************************/

import unittest
from domain.meta import device_report


class DeviceReportTest(unittest.TestCase):

    TEST_RPT_NAME = "Test Report.NAME"
    TEST_DEVICE = "Test device"
    TEST_EVENT = "Test event"
    TEST_EXPECTED = ["value_descriptor1", "value_descriptor2"]

    def setUp(self):
        self.device_report1 = device_report.DeviceReport(self.TEST_RPT_NAME, self.TEST_DEVICE,
                                                         self.TEST_EVENT, self.TEST_EXPECTED)
        self.device_report2 = device_report.DeviceReport(self.TEST_RPT_NAME, self.TEST_DEVICE,
                                                         self.TEST_EVENT, self.TEST_EXPECTED)

    def test_equals(self):
        self.assertTrue(self.device_report1 == self.device_report2,
                        "Different reports with same values not equal")

    def test_equals_same(self):
        self.assertTrue(self.device_report1 == self.device_report1,
                        "Same reports are not equal")

    def test_not_equals(self):
        self.device_report1.created = 3456
        self.assertFalse(self.device_report1 == self.device_report2,
                         "Reports with different base values are equal")

    def test_equal_different_name(self):
        self.device_report2.name = "foo"
        self.assertFalse(self.device_report1 == self.device_report2,
                         "Reports with different names values are equal")

    def test_equal_different_devices(self):
        self.device_report2.device = "foo"
        self.assertFalse(self.device_report1 == self.device_report2,
                         "Reports with different devices values are equal")

    def test_equal_different_events(self):
        self.device_report2.event = "foo"
        self.assertFalse(self.device_report1 == self.device_report2,
                         "Reports with different events values are equal")

    def test_equal_different_expected(self):
        self.device_report2.expected = "foo"
        self.assertFalse(self.device_report1 == self.device_report2,
                         "Reports with different expected values are equal")

    def test_hash_code(self):
        self.assertTrue(self.device_report1.__hash__() != 0, "hashcode not hashing properly")

    def test_to_string(self):
        str(self.device_report1)

if __name__ == "__main__":
    unittest.main()
