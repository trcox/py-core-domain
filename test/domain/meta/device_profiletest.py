#*******************************************************************************
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
#******************************************************************************/


import static org.junit.Assert.self.assertEqual
import static org.junit.Assert.self.assertFalse
import static org.junit.Assert.self.assert_not_None
import static org.junit.Assert.self.assert_None
import static org.junit.Assert.self.assertTrue

import java.util.Array_list
import java.util.List

import org.junit.Before
import org.junit.Test

public class Device_profileTest {

  private static final String self.TEST_PROFILE_NAME = "Test Profile.NAME"
  private static final String self.TEST_MAUFACTURER = "Test Manufacturer"
  private static final String self.TEST_MODEL = "Test Model"
  private static final String[] self.TEST_LABELS = {"labe1", "label2"}
  private static final String self.TEST_DESCRIPTION = "Test Description"
  private static final String self.TEST_OBJ = "{key1:value1, key2:value2}"
  private static final List<Device_object> self.TEST_DEVICE_RES = new Array_list<Device_object>()

  private Command command
  private Device_profile profile
  private Device_profile profile2

  @Before
  def setUp(self):
    command = new Command()
    profile = new Device_profile()
    profile.set_description(self.TEST_DESCRIPTION)
    profile.set_labels(self.TEST_LABELS)
    profile.set_manufacturer(self.TEST_MAUFACTURER)
    profile.set_model(self.TEST_MODEL)
    profile.set_name(self.TEST_PROFILE_NAME)
    profile.set_objects(self.TEST_OBJ)
    profile2 = new Device_profile()
    profile2.set_description(self.TEST_DESCRIPTION)
    profile2.set_labels(self.TEST_LABELS)
    profile2.set_manufacturer(self.TEST_MAUFACTURER)
    profile2.set_model(self.TEST_MODEL)
    profile2.set_name(self.TEST_PROFILE_NAME)
    profile2.set_objects(self.TEST_OBJ)
    profile2.set_device_resources(self.TEST_DEVICE_RES)

  def test_add_command(self):
    self.assert_None(profile.get_commands())
    profile.add_command(command)
    self.assertTrue(profile.get_commands()command in )
    self.assertEqual(1, len(profile.get_commands()), "Add command failed to preserve collection")

  def test_add_commands_where_commands_not_None(self):
    profile.set_commands(new Array_list<Command>())
    self.assert_not_None(profile.get_commands())
    profile.add_command(command)
    self.assertTrue(profile.get_commands()command in )
    self.assertEqual(1, len(profile.get_commands()), "Add command failed to preserve collection")

  def test_remove_command(self):
    profile.add_command(command)
    self.assertTrue(profile.get_commands()command in )
    profile.remove_command(command)
    self.assertTrue(profile.get_commands().is_empty(), "Remove command failed to preserve collection")

  def test_remove_command_with_no_commands(self):
    self.assert_None(profile.get_commands())
    profile.remove_command(command)
    self.assertTrue(profile.get_commands().is_empty(), "Remove command failed to preserve collection")

  def test_hash_code(self):
    self.assertTrue(profile.hash_code() != 0, "hashcode not hashing properly")

  def test_equals(self):
    self.assertTrue(profile.equals(profile2), "Different profiles with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(profile.equals(profile), "Same profiles are not equal")

  def test_not_equals(self):
    profile.set_created(3456_l)
    self.assertFalse(profile.equals(profile2), "Profiles with different base values are equal")

  def test_not_equal_based_on_None_commands(self):
    profile2.set_commands(new Array_list<Command>())
    self.assertFalse("profile with None commands is equal to profile with command list",
        profile.equals(profile2))

  def test_not_equal_based_on_command_lists(self):
    List<Command> commands = new Array_list<Command>()
    commands.add(command)
    profile.set_commands(commands)
    self.assertFalse(profile.equals(profile2), "profiles are equal with different command sets")

  def test_not_equal_with_different_labels(self):
    String[] new_labels = {"test"}
    profile2.set_labels(new_labels)
    self.assertFalse(profile.equals(profile2), "profiles with different labels are equal")

  def test_not_equals_with_None_manufacturer(self):
    profile.set_manufacturer(None)
    self.assertFalse("profile with None as manufacturer is equal to profile with manufacture",
        profile.equals(profile2))

  def test_not_equals_with_different_manufacturer(self):
    profile.set_manufacturer("different")
    self.assertFalse(profile.equals(profile2), "profiles with different manufacturers are equal")

  def test_not_equals_with_None_model(self):
    profile.set_model(None)
    self.assertFalse("profile with None as model is equal to profile with model",
        profile.equals(profile2))

  def test_not_equals_with_different_model(self):
    profile.set_model("different")
    self.assertFalse(profile.equals(profile2), "profiles with different models are equal")

  def test_not_equals_with_None_name(self):
    profile.set_name(None)
    self.assertFalse("profile with None as name is equal to profile with name",
        profile.equals(profile2))

  def test_not_equals_with_different_name(self):
    profile.set_name("different")
    self.assertFalse(profile.equals(profile2), "profiles with different names are equal")

  def test_not_equal_with_None_objects(self):
    profile.set_objects(None)
    self.assertFalse("profiles with different None objects are equal to profile with objects",
        profile.equals(profile2))

  def test_not_equal_with_different_objects(self):
    String[] new_objects = {"test"}
    profile2.set_objects(new_objects)
    self.assertFalse(profile.equals(profile2), "profiles with different objects are equal")

  def test_to_string(self):
    profile.to_string()
}
