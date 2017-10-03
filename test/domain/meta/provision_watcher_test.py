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
from domain.meta import device_profile
from domain.meta import device_service
from domain.meta import operating_state
from domain.meta import provision_watcher


class ProvisionWatcherTest(unittest.TestCase):

    TEST_NAME = "test pw"

    def setUp(self):
        ids = {}
        ids["z"] = "y"
        profile = device_profile.DeviceProfile()
        service = device_service.DeviceService()
        self.watcher1 = provision_watcher.ProvisionWatcher(self.TEST_NAME)
        self.watcher1.identifiers = ids
        self.watcher1.profile = profile
        self.watcher1.service = service
        self.watcher1.operating_state = operating_state.OperatingState.ENABLED
        self.watcher2 = provision_watcher.ProvisionWatcher(self.TEST_NAME)
        self.watcher2.identifiers = ids
        self.watcher2.profile = profile
        self.watcher2.service = service
        self.watcher2.operating_state = operating_state.OperatingState.ENABLED


    def test_add_no_identifier_starting(self):
        self.watcher1.identifiers = None
        self.watcher1.add_identifier("a", "b")
        self.assertEqual("b", self.watcher1.identifiers["a"],
                         "Provision_watcher identifiers not added correctly")

    def test_add_identifier(self):
        self.watcher1.add_identifier("a", "b")
        self.assertEqual("b", self.watcher1.identifiers["a"],
                         "Provision_watcher identifiers not added correctly")

    def test_remove_no_identifier(self):
        self.watcher1.identifiers = None
        self.watcher1.remove_identifier("z")
        self.assertEqual({}, self.watcher1.identifiers,
                         "Provision_watcher remove identifier not working properly")

    def test_remove_identifier(self):
        self.watcher1.remove_identifier("z")
        self.assertEqual({}, self.watcher1.identifiers,
                         "Provision_watcher remove identifier not working properly")

    def test_equals(self):
        self.assertTrue(self.watcher1 == self.watcher2,
                        "Different watchers with same values not equal")

    def test_equals_same(self):
        self.assertTrue(self.watcher1 == self.watcher1, "Same watcher are not equal")

    def test_not_equals(self):
        self.watcher2.created = 3456
        self.assertFalse(self.watcher1 == self.watcher2,
                         "Watchers with different base values are equal")

    def test_equal_diff_name(self):
        self.watcher2.name = "foo"
        self.assertFalse(self.watcher1 == self.watcher2,
                         "Watchers with different names values are equal")

    def test_equal_diff_identifiers(self):
        ids = {}
        ids["a"] = "b"
        self.watcher2.identifiers = ids
        self.assertFalse(self.watcher1 == self.watcher2,
                         "Watchers with different identifier values are equal")

    def test_equal_diff_profiles(self):
        profile = device_profile.DeviceProfile()
        profile.name = "foo"
        self.watcher2.profile = profile
        self.assertFalse(self.watcher1 == self.watcher2,
                         "Watchers with different profiles are equal")

    def test_equal_diff_services(self):
        service = device_service.DeviceService()
        service.name = "foo"
        self.watcher2.service = service
        self.assertFalse(self.watcher1 == self.watcher2,
                         "Watchers with different services are equal")

    def test_equal_diff_op_state(self):
        self.watcher2.operating_state = operating_state.OperatingState.DISABLED
        self.assertFalse(self.watcher1 == self.watcher2,
                         "Watchers with different op states are equal")

    def test_hash_code(self):
        self.assertTrue(self.watcher1.__hash__() != 0, "hashcode not hashing properly")

    def test_to_string(self):
        str(self.watcher1)

if __name__ == "__main__":
    unittest.main()
