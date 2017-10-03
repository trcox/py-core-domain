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
from domain.meta import admin_state
from domain.meta import device_service


class DeviceServiceTest(unittest.TestCase):

    def setUp(self):
        self.service1 = device_service.DeviceService()
        self.service1.adminState = admin_state.AdminState.UNLOCKED
        self.service2 = device_service.DeviceService()
        self.service2.adminState = admin_state.AdminState.UNLOCKED

    def test_equals(self):
        self.assertTrue(self.service1 == self.service2,
                        "Different services with same values not equal")

    def test_equals_same(self):
        self.assertTrue(self.service1 == self.service1, "Same services are not equal")

    def test_not_equals(self):
        self.service1.created = 3456
        self.assertFalse(self.service1 == self.service2,
                         "services with different base values are equal")

    def test_equal_diff_admin_state(self):
        self.service2.adminState = admin_state.AdminState.LOCKED
        self.assertFalse(self.service1 == self.service2,
                         "Services with different admin state values are equal")

    def test_hash_code(self):
        self.assertTrue(self.service1.__hash__() != 0, "hashcode not hashing properly")

    def test_to_string(self):
        str(self.service1)

if __name__ == "__main__":
    unittest.main()
