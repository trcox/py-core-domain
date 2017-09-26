#*******************************************************************************
# Copyright 2016-2017 Dell Inself.c1.
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

import unittest

from domain.meta import Command, Get, Put, Response

class CommandTest(unittest.TestCase):

  TEST_NAME = "test_command_name"
  TEST_PATH = "/api/v1/device/{device_id}/temp"
  TEST_CODE = "200"
  TEST_DESCRIPTION = "ok"
  TEST_EXPECTED_VALUE1 = "temperature"
  TEST_EXPECTED_VALUE2 = "humidity"
  TEST_PARAM1 = "Temperature"
  TEST_PARAM2 = "Humidity"

  def setUp(self):
    expected = []
    expected.append(self.TEST_EXPECTED_VALUE1)
    expected.append(self.TEST_EXPECTED_VALUE2)
    r = Response(self.TEST_CODE, self.TEST_DESCRIPTION, expected)
    self.c1 = Command()
    self.c1.name = self.TEST_NAME
    g = Get()
    g.path = self.TEST_PATH
    g.add_response(r)
    self.c1.get = g
    p = Put()
    p.path = self.TEST_PATH
    params = []
    params.append(self.TEST_PARAM1)
    params.append(self.TEST_PARAM2)
    p.parameterNames = params
    self.c1.put = p
    self.c2 = Command()
    self.c2.name = self.TEST_NAME
    self.c2.get = g
    self.c2.put = p

  def test_associated_value_descriptors_with_get_and_put(self):
    vds = self.c1.associated_value_descriptors()
    self.assertTrue(self.TEST_PARAM1 in vds, "Command does not have put param value descriptors")
    self.assertTrue(self.TEST_PARAM2 in vds, "Command does not have put param value descriptors")
    self.assertTrue(self.TEST_EXPECTED_VALUE1 in vds, "Command does not have expected get value descriptors")
    self.assertTrue(self.TEST_EXPECTED_VALUE2 in vds, "Command does not have expected get value descriptors")

  def test_associated_value_descriptors_with_no_get_no_put(self):
    self.c1.put = None
    self.c1.get = None
    vds = []
    self.assertEqual(self.c1.associated_value_descriptors(), vds, "Command should not have value descriptors with no gets or puts")

  def test_associated_value_descriptors_with_no_get(self):
    self.c1.get = None
    vds = self.c1.associated_value_descriptors()
    self.assertTrue(self.TEST_PARAM1 in vds, "Command does not have put param value descriptors")
    self.assertTrue(self.TEST_PARAM2 in vds, "Command does not have put param value descriptors")

  def test_associated_value_descriptors_with_no_put(self):
    self.c1.put = None
    vds = self.c1.associated_value_descriptors()
    self.assertTrue(self.TEST_EXPECTED_VALUE1 in vds, "Command does not have expected get value descriptors")
    self.assertTrue(self.TEST_EXPECTED_VALUE2 in vds, "Command does not have expected get value descriptors")

  def test_equals(self):
    self.assertTrue(self.c1 == self.c2, "Different command with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(self.c1 == self.c1, "Same commands are not equal")

  def test_not_equals(self):
    self.c1.created = 3456
    self.assertFalse(self.c1 == self.c2, "Commands with different base values are equal")

  def test_equal_with_different_name(self):
    self.c2.name = "foo"
    self.assertFalse(self.c1 == self.c2, "Commands with different names values are equal")

  def test_equal_with_different_gets(self):
    self.c2.get = None
    self.assertFalse(self.c1 == self.c2, "Commands with different get values are equal")

  def test_equal_with_different_puts(self):
    self.c2.put = None
    self.assertFalse(self.c1 == self.c2, "Commands with different put values are equal")

  def test_hash_code(self):
    self.assertTrue(self.c1.__hash__() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    str(self.c1)

if __name__ == "__main__":
  unittest.main()
