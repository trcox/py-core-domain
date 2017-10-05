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
from domain.meta import device_service
from domain.meta import operating_state
from domain.meta import protocol


class ServiceTest(unittest.TestCase):

    TEST_SERVICE_NAME = "test service"
    TEST_OP = operating_state.OperatingState.ENABLED
    TEST_lastConnected = 1000000
    TEST_lastReported = 1000000
    TEST_LABELS = ["MODBUS", "TEMP"]
    TEST_ADDR_NAME = "TEST_ADDR.NAME"
    TEST_PROTOCOL = protocol.Protocol.HTTP
    TEST_ADDRESS = "localhost"
    TEST_PORT = 48089
    TEST_PATH = "/api/v1/device"

    def setUp(self):
        address1 = addressable.Addressable(self.TEST_ADDR_NAME, self.TEST_PROTOCOL,
                                           self.TEST_ADDRESS, self.TEST_PATH, self.TEST_PORT)
        # must use DeviceService since Service is abstract
        self.service1 = device_service.DeviceService()
        self.service1.name = self.TEST_SERVICE_NAME
        self.service1.lastConnected = self.TEST_lastConnected
        self.service1.lastReported = self.TEST_lastReported
        self.service1.operatingState = self.TEST_OP
        self.service1.labels = self.TEST_LABELS
        self.service1.addressable = address1
        self.service2 = device_service.DeviceService()
        self.service2 = device_service.DeviceService()
        self.service2.name = self.TEST_SERVICE_NAME
        self.service2.lastConnected = self.TEST_lastConnected
        self.service2.lastReported = self.TEST_lastReported
        self.service2.operatingState = self.TEST_OP
        self.service2.labels = self.TEST_LABELS
        self.service2.addressable = address1

    def test_equals(self):
        self.assertTrue(self.service1 == self.service2,
                        "Different service with same values not equal")

    def test_equals_same(self):
        self.assertTrue(self.service1 == self.service1, "Same service are not equal")

    def test_not_equals(self):
        self.service1.created = 3456
        self.assertFalse(self.service1 == self.service2,
                         "Services with different base values are equal")

    def test_equal_diff_name(self):
        self.service2.name = "foo"
        self.assertFalse(self.service1 == self.service2,
                         "Services with different names values are equal")

    def test_equal_diff_op_state(self):
        self.service2.operatingState = operating_state.OperatingState.DISABLED
        self.assertFalse(self.service1 == self.service2,
                         "Services with different op state values are equal")

    def test_equal_diff_addressable(self):
        address2 = addressable.Addressable(self.TEST_PROTOCOL, self.TEST_ADDRESS, self.TEST_PATH,
                                           self.TEST_PORT, "foo")
        self.service2.addressable = address2
        self.assertFalse(self.service1 == self.service2,
                         "Services with different addressable are equal")

    def test_equal_diff_last_connected(self):
        self.service2.lastConnected = 5678
        self.assertFalse(self.service1 == self.service2,
                         "Services with different last connected values are equal")

    def test_equal_diff_last_reported(self):
        self.service2.lastReported = 5678
        self.assertFalse(self.service1 == self.service2,
                         "Services with different last reported values are equal")

    def test_equals_diff_labels(self):
        new_labels = ["newlabel"]
        self.service2.labels = new_labels
        self.assertFalse(self.service1 == self.service2,
                         "Services with different labels seen as equal")

    def test_hash_code(self):
        self.assertTrue(self.service1.__hash__() != 0, "hashcode not hashing properly")

if __name__ == "__main__":
    unittest.main()
