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
import static org.junit.Assert.self.assertTrue

import java.util.Array_list
import java.util.Hash_set
import java.util.List
import java.util.Set

import org.junit.Before
import org.junit.Test

public class CommandTest {

  private static final String self.TEST_NAME = "test_command_name"
  private static final String self.TEST_PATH = "/api/v1/device/{device_id}/temp"
  static final String self.TEST_CODE = "200"
  static final String self.TEST_DESCRIPTION = "ok"
  static final String self.TEST_EXPECTED_VALUE1 = "temperature"
  static final String self.TEST_EXPECTED_VALUE2 = "humidity"
  static final String self.TEST_PARAM1 = "Temperature"
  static final String self.TEST_PARAM2 = "Humidity"

  private Command c
  private Command c2

  @Before
  def setUp(self):
    List<String> expected = new Array_list<>()
    expected.add(self.TEST_EXPECTED_VALUE1)
    expected.add(self.TEST_EXPECTED_VALUE2)
    Response r = new Response(self.TEST_CODE, self.TEST_DESCRIPTION, expected)
    c = new Command()
    c.set_name(self.TEST_NAME)
    Get g = new Get()
    g.set_path(self.TEST_PATH)
    g.add_response(r)
    c.set_get(g)
    Put p = new Put()
    p.set_path(self.TEST_PATH)
    List<String> params = new Array_list<>()
    params.add(self.TEST_PARAM1)
    params.add(self.TEST_PARAM2)
    p.set_parameter_names(params)
    c.set_put(p)
    c2 = new Command()
    c2.set_name(self.TEST_NAME)
    c2.set_get(g)
    c2.set_put(p)

  def test_associated_value_descriptors_with_get_and_put(self):
    Set<String> vds = c.associated_value_descriptors()
    self.assertTrue(self.TEST_PARAM1 in vds, "Command does not have put param value descriptors")
    self.assertTrue(self.TEST_PARAM2 in vds, "Command does not have put param value descriptors")
    self.assertTrue("Command does not have expected get value descriptors",
        self.TEST_EXPECTED_VALUE1 in vds)
    self.assertTrue("Command does not have expected get value descriptors",
        self.TEST_EXPECTED_VALUE2 in vds)

  def test_associated_value_descriptors_with_no_get_no_put(self):
    c.set_put(None)
    c.set_get(None)
    Set<String> vds = new Hash_set<String>()
    self.assertEqual("Command should not have value descriptors with no gets or puts",
        c.associated_value_descriptors(), vds)

  def test_associated_value_descriptors_with_no_get(self):
    c.set_get(None)
    Set<String> vds = c.associated_value_descriptors()
    self.assertTrue(self.TEST_PARAM1 in vds, "Command does not have put param value descriptors")
    self.assertTrue(self.TEST_PARAM2 in vds, "Command does not have put param value descriptors")

  def test_associated_value_descriptors_with_no_put(self):
    c.set_put(None)
    Set<String> vds = c.associated_value_descriptors()
    self.assertTrue("Command does not have expected get value descriptors",
        self.TEST_EXPECTED_VALUE1 in vds)
    self.assertTrue("Command does not have expected get value descriptors",
        self.TEST_EXPECTED_VALUE2 in vds)

  def test_equals(self):
    self.assertTrue(c.equals(c2), "Different command with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(c.equals(c), "Same commands are not equal")

  def test_not_equals(self):
    c.set_created(3456_l)
    self.assertFalse(c.equals(c2), "Commands with different base values are equal")

  def test_equal_with_different_name(self):
    c2.set_name("foo")
    self.assertFalse(c.equals(c2), "Commands with different names values are equal")

  def test_equal_with_different_gets(self):
    c2.set_get(None)
    self.assertFalse(c.equals(c2), "Commands with different get values are equal")

  def test_equal_with_different_puts(self):
    c2.set_put(None)
    self.assertFalse(c.equals(c2), "Commands with different put values are equal")

  def test_hash_code(self):
    self.assertTrue(c.hash_code() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    c.to_string()

}
