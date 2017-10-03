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
from domain.meta import addressable
from domain.meta import admin_state
from domain.meta import device
from domain.meta import device_profile
from domain.meta import device_service
from domain.meta import operating_state
from domain.meta import protocol

class DeviceTest(unittest.TestCase):


    TEST_NAME = "TEST_DEVICE.NAME"
    TEST_DESCRIPTION = "TEST_DESCRIPTION"
    TEST_ADMIN = admin_state.AdminState.UNLOCKED
    TEST_OP = operating_state.OperatingState.ENABLED
    TEST_LAST_CONNECTED = 1000000
    TEST_LAST_REPORTED = 1000000
    TEST_LABELS = ["MODBUS", "TEMP"]
    TEST_LOCATION = "{40lat;45long}"

    def setUp(self):
        self.device1 = device.Device()
        self.device1.adminState = self.TEST_ADMIN
        self.device1.description = self.TEST_DESCRIPTION
        self.device1.labels = self.TEST_LABELS
        self.device1.last_connected = self.TEST_LAST_CONNECTED
        self.device1.last_reported = self.TEST_LAST_REPORTED
        self.device1.location = self.TEST_LOCATION
        self.device1.name = self.TEST_NAME
        self.device1.operating_state = self.TEST_OP
        self.device1.addressable = addressable.Addressable("z", protocol.Protocol.HTTP,
                                                           "b", "c", 0)
        self.device1.service = device_service.DeviceService()
        self.device1.service.name = "foo"
        self.device1.profile = device_profile.DeviceProfile()
        self.device1.profile.name = "boo"
        self.device2 = device.Device()
        self.device2.adminState = self.TEST_ADMIN
        self.device2.description = self.TEST_DESCRIPTION
        self.device2.labels = self.TEST_LABELS
        self.device2.last_connected = self.TEST_LAST_CONNECTED
        self.device2.last_reported = self.TEST_LAST_REPORTED
        self.device2.location = self.TEST_LOCATION
        self.device2.name = self.TEST_NAME
        self.device2.operating_state = self.TEST_OP
        self.device2.addressable = addressable.Addressable("z", protocol.Protocol.HTTP,
                                                           "b", "c", 0)
        self.device2.service = device_service.DeviceService()
        self.device2.service.name = "foo"
        self.device2.profile = device_profile.DeviceProfile()
        self.device2.profile.name = "boo"

    def test_equals(self):
        self.assertTrue(self.device1 == self.device2,
                        "Different devices with same values not equal")

    def test_equals_same(self):
        self.assertTrue(self.device1 == self.device1, "Same devices are not equal")

    def test_not_equals(self):
        self.device1.created = 3456
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different base values are equal")

    def test_equal_diff_name(self):
        self.device2.name = "foo"
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different names values are equal")

    def test_equal_diff_admin_state(self):
        self.device2.adminState = admin_state.AdminState.LOCKED
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different admin states values are equal")

    def test_equal_diff_op_state(self):
        self.device2.operating_state = operating_state.OperatingState.DISABLED
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different op states values are equal")

    def test_equals_both_addressable_no(self):
        self.device1.addressable = None
        self.device2.addressable = None
        self.assertTrue(self.device1 == self.device2,
                        "Devices with None addressables are not equal")

    def test_equal_an_addressable(self):
        self.device1.addressable = None
        self.assertFalse(self.device1 == self.device2,
                         "Devices with no addressable are equal to device with an addressable")

    def test_equal_diff_addressable(self):
        self.device1.addressable = addressable.Addressable("a", protocol.Protocol.HTTP,
                                                           "b", "c", 0)
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different addressables are equal")

    def test_equal_diff_last_connected(self):
        self.device2.last_connected = 5678
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different last connected values are equal")

    def test_equal_diff_last_reported(self):
        self.device2.last_reported = 5678
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different last reported values are equal")

    def test_equals_diff_labels(self):
        new_labels = ["newlabel"]
        self.device2.labels = new_labels
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different labels seen as equal")

    def test_equal_diff_location(self):
        self.device2.location = "foobar"
        self.assertFalse(self.device1 == self.device2,
                         "Devices with different location values are equal")

    def test_equals_both_services_no(self):
        self.device1.service = None
        self.device2.service = None
        self.assertTrue(self.device1 == self.device2,
                        "Devices with None as services are not equal")

    def test_equals_one_non_no_service(self):
        self.device1.service = None
        self.assertFalse(self.device1 == self.device2,
                         "Devices with None service are equal to device with non None service")

    def test_equal_diff_services(self):
        self.device1.service = device_service.DeviceService()
        self.device1.service.name = "boo"
        self.assertFalse(self.device1 == self.device2, "Devices with different services are equal")

    def test_equals_both_no_profiles(self):
        self.device1.profile = None
        self.device2.profile = None
        self.assertTrue(self.device1 == self.device2, "Devices with None profiles are not equal")

    def test_equals_one_non_no_profile(self):
        self.device1.profile = None
        self.assertFalse(self.device1 == self.device2,
                         "Devices with None profile are equal to device with non None profile")

    def test_equal_diff_profiles(self):
        self.device2.profile.name = "foo"
        self.assertFalse(self.device1 == self.device2, "Devices with different profiles are equal")

    def test_hash_code(self):
        self.assertTrue(self.device1.__hash__() != 0, "hashcode not hashing properly")

    def test_to_string(self):
        str(self.device1)

if __name__ == "__main__":
    unittest.main()
