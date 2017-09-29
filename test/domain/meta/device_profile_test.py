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
from domain.meta import command
from domain.meta import device_profile


class DeviceProfileTest(unittest.TestCase):

    TEST_PROFILE_NAME = "Test Profile.NAME"
    TEST_MANUFACTURER = "Test Manufacturer"
    TEST_MODEL = "Test Model"
    TEST_LABELS = {"label1", "label2"}
    TEST_DESCRIPTION = "Test Description"
    TEST_OBJ = "{key1:value1, key2:value2}"
    TEST_DEVICE_RES = []

    def setUp(self):
        self.command = command.Command()
        self.profile1 = device_profile.DeviceProfile()
        self.profile1.description = self.TEST_DESCRIPTION
        self.profile1.labels = self.TEST_LABELS
        self.profile1.manufacturer = self.TEST_MANUFACTURER
        self.profile1.model = self.TEST_MODEL
        self.profile1.name = self.TEST_PROFILE_NAME
        self.profile1.objects = self.TEST_OBJ
        self.profile2 = device_profile.DeviceProfile()
        self.profile2.description = self.TEST_DESCRIPTION
        self.profile2.labels = self.TEST_LABELS
        self.profile2.manufacturer = self.TEST_MANUFACTURER
        self.profile2.model = self.TEST_MODEL
        self.profile2.name = self.TEST_PROFILE_NAME
        self.profile2.objects = self.TEST_OBJ
        self.profile2.deviceResources = self.TEST_DEVICE_RES

    def test_add_command(self):
        self.assertTrue(self.profile1.commands is None)
        self.profile1.add_command(self.command)
        self.assertTrue(self.command in self.profile1.commands)
        self.assertEqual(1, len(self.profile1.commands), "Add command failed to preserve collection")

    def test_add_commands_where_commands_not_None(self):
        self.profile1.commands = []
        self.assertTrue(self.profile1.commands is not None)
        self.profile1.add_command(self.command)
        self.assertTrue(self.command in self.profile1.commands)
        self.assertEqual(1, len(self.profile1.commands), "Add command failed to preserve collection")

    def test_remove_command(self):
        self.profile1.add_command(self.command)
        self.assertTrue(self.command in self.profile1.commands )
        self.profile1.remove_command(self.command)
        self.assertTrue(len(self.profile1.commands) == 0, "Remove command failed to preserve collection")

    def test_remove_command_with_no_commands(self):
        self.assertTrue(self.profile1.commands is None)
        self.profile1.remove_command(self.command)
        self.assertTrue(len(self.profile1.commands) == 0, "Remove command failed to preserve collection")

    def test_hash_code(self):
        self.assertTrue(self.profile1.__hash__() != 0, "hashcode not hashing properly")

    def test_equals(self):
        self.profile1.deviceResources = self.TEST_DEVICE_RES
        self.assertTrue(self.profile1 == self.profile2, "Different profiles with same values not equal")

    def test_equals_with_same(self):
        self.assertTrue(self.profile1 == self.profile1, "Same profiles are not equal")

    def test_not_equals(self):
        self.profile1.created = 3456
        self.assertFalse(self.profile1 == self.profile2, "Profiles with different base values are equal")

    def test_not_equal_based_on_None_commands(self):
        self.profile2.commands = []
        self.assertFalse(self.profile1 == self.profile2, "profile with None commands is equal to profile with command list")

    def test_not_equal_based_on_command_lists(self):
        commands = []
        commands.append(self.command)
        self.profile1.commands = commands
        self.assertFalse(self.profile1 == self.profile2, "profiles are equal with different command sets")

    def test_not_equal_with_different_labels(self):
        new_labels = ["test"]
        self.profile2.labels = new_labels
        self.assertFalse(self.profile1 == self.profile2, "profiles with different labels are equal")

    def test_not_equals_with_None_manufacturer(self):
        self.profile1.manufacturer = None
        self.assertFalse(self.profile1 == self.profile2, "profile with None as manufacturer is equal to profile with manufacturer")

    def test_not_equals_with_different_manufacturer(self):
        self.profile1.manufacturer = "different"
        self.assertFalse(self.profile1 == self.profile2, "profiles with different manufacturers are equal")

    def test_not_equals_with_None_model(self):
        self.profile1.model = None
        self.assertFalse(self.profile1 == self.profile2, "profile with None as model is equal to profile with model")

    def test_not_equals_with_different_model(self):
        self.profile1.model = "different"
        self.assertFalse(self.profile1 == self.profile2, "profiles with different models are equal")

    def test_not_equals_with_None_name(self):
        self.profile1.name = None
        self.assertFalse(self.profile1 == self.profile2, "profile with None as name is equal to profile with name")

    def test_not_equals_with_different_name(self):
        self.profile1.name = "different"
        self.assertFalse(self.profile1 == self.profile2, "profiles with different names are equal")

    def test_not_equal_with_None_objects(self):
        self.profile1.objects = None
        self.assertFalse(self.profile1 == self.profile2, "profiles with different None objects are equal to profile with objects")

    def test_not_equal_with_different_objects(self):
        new_objects = {"test"}
        self.profile2.objects = new_objects
        self.assertFalse(self.profile1 == self.profile2, "profiles with different objects are equal")

    def test_to_string(self):
        str(self.profile1)

if __name__ == "__main__":
    unittest.main()
